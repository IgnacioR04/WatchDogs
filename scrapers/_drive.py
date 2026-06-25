"""Cliente de Google Drive (data lake historico). [PENDIENTE DE OAUTH]

IMPORTANTE - limitacion conocida (2026-06-25):
Las service accounts NO tienen cuota de almacenamiento propia y NO pueden
subir archivos a un Drive personal (Gmail). Pueden autenticarse, listar y
crear carpetas, pero al subir un fichero falla con 'storageQuotaExceeded'.
Las soluciones de Google (Shared Drives, domain-wide delegation) requieren
Google Workspace de pago.

Para una cuenta personal de 100GB la via correcta es OAuth de usuario con
refresh token (los archivos los posee el usuario, que si tiene cuota). Este
modulo ya soporta lectura/listado con service account; la subida real espera
a cablear OAuth. Por ahora el historico profundo esta APLAZADO (la capa
publica de 30 dias se genera directamente de los scrapers).

Autenticacion (cuando se reactive):
- En CI: GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON_B64 (base64 del JSON) o, con OAuth,
  GOOGLE_OAUTH_* + refresh token.
- En local: GOOGLE_DRIVE_SA_FILE (ruta al JSON sin codificar).

La carpeta raiz del historico es GOOGLE_DRIVE_ROOT_FOLDER_ID.

Funciones principales:
- get_service(): construye el cliente Drive autenticado.
- ensure_folder_path(root_id, parts): crea (si no existen) carpetas anidadas.
- upload_file(local_path, folder_id, filename): sube un archivo.
- download_file(file_id, local_path): descarga un archivo por id.
- list_files(folder_id, query): lista archivos de una carpeta.
- find_file(folder_id, name): busca un archivo por nombre exacto.
"""

from __future__ import annotations

import base64
import io
import json
import os
from pathlib import Path
from typing import Any

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# Scope: acceso a Drive limitado a lo que se comparte con la service account.
SCOPES = ["https://www.googleapis.com/auth/drive"]
MIME_FOLDER = "application/vnd.google-apps.folder"

ROOT_FOLDER_ID = os.environ.get("GOOGLE_DRIVE_ROOT_FOLDER_ID", "")


def _load_credentials() -> service_account.Credentials:
    """Carga las credenciales de la service account.

    Prioridad:
    1. GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON_B64 (base64 del JSON) -> CI.
    2. GOOGLE_DRIVE_SA_FILE (ruta a JSON sin codificar) -> local.
    Lanza RuntimeError si no hay ninguna disponible.
    """
    b64 = os.environ.get("GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON_B64")
    if b64:
        info = json.loads(base64.b64decode(b64).decode("utf-8"))
        return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)

    sa_file = os.environ.get("GOOGLE_DRIVE_SA_FILE")
    if sa_file and Path(sa_file).exists():
        return service_account.Credentials.from_service_account_file(sa_file, scopes=SCOPES)

    raise RuntimeError(
        "Sin credenciales de Drive. Define GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON_B64 "
        "(CI) o GOOGLE_DRIVE_SA_FILE (local)."
    )


_service_cache = None


def get_service():
    """Devuelve el cliente Drive autenticado (cacheado entre llamadas)."""
    global _service_cache
    if _service_cache is None:
        creds = _load_credentials()
        _service_cache = build("drive", "v3", credentials=creds, cache_discovery=False)
    return _service_cache


def find_file(folder_id: str, name: str, service=None) -> dict[str, Any] | None:
    """Busca un archivo/carpeta por nombre exacto dentro de una carpeta.

    Devuelve el primer match {id, name, mimeType} o None.
    """
    service = service or get_service()
    safe = name.replace("'", "\\'")
    q = f"'{folder_id}' in parents and name = '{safe}' and trashed = false"
    resp = service.files().list(
        q=q, fields="files(id, name, mimeType)", pageSize=10,
        supportsAllDrives=True, includeItemsFromAllDrives=True,
    ).execute()
    files = resp.get("files", [])
    return files[0] if files else None


def list_files(folder_id: str, query: str | None = None, service=None) -> list[dict[str, Any]]:
    """Lista archivos de una carpeta. `query` añade condiciones extra (sintaxis Drive).

    Devuelve lista de {id, name, mimeType, modifiedTime, size}.
    """
    service = service or get_service()
    q = f"'{folder_id}' in parents and trashed = false"
    if query:
        q += f" and ({query})"
    out: list[dict[str, Any]] = []
    page_token = None
    while True:
        resp = service.files().list(
            q=q,
            fields="nextPageToken, files(id, name, mimeType, modifiedTime, size)",
            pageSize=1000, pageToken=page_token,
            supportsAllDrives=True, includeItemsFromAllDrives=True,
        ).execute()
        out.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return out


def _create_folder(name: str, parent_id: str, service=None) -> str:
    """Crea una carpeta dentro de parent_id y devuelve su id."""
    service = service or get_service()
    meta = {"name": name, "mimeType": MIME_FOLDER, "parents": [parent_id]}
    f = service.files().create(body=meta, fields="id", supportsAllDrives=True).execute()
    return f["id"]


def ensure_folder_path(root_id: str, parts: list[str], service=None) -> str:
    """Garantiza que exista la ruta de carpetas `parts` bajo root_id.

    Crea las carpetas que falten y devuelve el id de la ultima (hoja).
    Ejemplo: ensure_folder_path(root, ['raw', 'sec_insiders', 'year=2026']).
    """
    service = service or get_service()
    current = root_id
    for part in parts:
        existing = find_file(current, part, service=service)
        if existing and existing.get("mimeType") == MIME_FOLDER:
            current = existing["id"]
        else:
            current = _create_folder(part, current, service=service)
    return current


def upload_file(
    local_path: str | Path,
    folder_id: str,
    filename: str | None = None,
    *,
    mime_type: str = "application/octet-stream",
    overwrite: bool = False,
    service=None,
) -> str:
    """Sube un archivo local a una carpeta de Drive. Devuelve el file id.

    Si overwrite=True y ya existe un archivo con ese nombre, actualiza su
    contenido en vez de crear uno nuevo (util para manifests/indices).
    """
    service = service or get_service()
    local_path = Path(local_path)
    name = filename or local_path.name
    media = MediaFileUpload(str(local_path), mimetype=mime_type, resumable=False)

    if overwrite:
        existing = find_file(folder_id, name, service=service)
        if existing:
            f = service.files().update(
                fileId=existing["id"], media_body=media, supportsAllDrives=True,
            ).execute()
            return existing["id"]

    meta = {"name": name, "parents": [folder_id]}
    f = service.files().create(
        body=meta, media_body=media, fields="id", supportsAllDrives=True,
    ).execute()
    return f["id"]


def download_file(file_id: str, local_path: str | Path, service=None) -> Path:
    """Descarga un archivo de Drive por id a una ruta local. Devuelve la ruta."""
    service = service or get_service()
    local_path = Path(local_path)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    request = service.files().get_media(fileId=file_id, supportsAllDrives=True)
    with io.FileIO(str(local_path), "wb") as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
    return local_path


def download_json(file_id: str, service=None) -> Any:
    """Descarga y parsea un JSON de Drive directamente a objeto Python."""
    service = service or get_service()
    request = service.files().get_media(fileId=file_id, supportsAllDrives=True)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return json.loads(buf.getvalue().decode("utf-8"))


def whoami(service=None) -> str:
    """Devuelve el email de la service account autenticada (para diagnostico)."""
    service = service or get_service()
    about = service.about().get(fields="user(emailAddress)").execute()
    return about.get("user", {}).get("emailAddress", "?")
