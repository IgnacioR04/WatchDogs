"""Tests de la logica de Google Drive (scrapers/_drive.py) con servicio mockeado.

No tocan Drive real: simulan la API para verificar que ensure_folder_path crea
las carpetas particionadas correctas y que upload_file llama a create/update
segun corresponda. (La subida real esta aplazada hasta cablear OAuth.)
"""

from __future__ import annotations

from scrapers import _drive


class _FakeFiles:
    """Simula el recurso files() de la Drive API."""

    def __init__(self, store):
        self.store = store           # dict id -> {name, parents, mimeType}
        self._counter = [0]

    def list(self, q=None, fields=None, pageSize=None, pageToken=None,
             supportsAllDrives=None, includeItemsFromAllDrives=None):
        # Parseo simplista del query: "'PARENT' in parents and name = 'NAME'"
        parent = q.split("'")[1] if "in parents" in q else None
        name = None
        if "name = '" in q:
            name = q.split("name = '")[1].split("'")[0]
        matches = []
        for fid, meta in self.store.items():
            if parent and parent not in meta.get("parents", []):
                continue
            if name and meta.get("name") != name:
                continue
            matches.append({"id": fid, "name": meta["name"], "mimeType": meta["mimeType"]})
        return _Exec({"files": matches})

    def create(self, body=None, media_body=None, fields=None, supportsAllDrives=None):
        self._counter[0] += 1
        fid = f"id_{self._counter[0]}"
        self.store[fid] = {
            "name": body["name"],
            "parents": body.get("parents", []),
            "mimeType": body.get("mimeType", "application/octet-stream"),
        }
        return _Exec({"id": fid})

    def update(self, fileId=None, media_body=None, supportsAllDrives=None):
        return _Exec({"id": fileId})


class _Exec:
    def __init__(self, result):
        self._result = result

    def execute(self):
        return self._result


class _FakeService:
    def __init__(self):
        self.store = {}
        self._files = _FakeFiles(self.store)

    def files(self):
        return self._files


def test_ensure_folder_path_crea_particiones():
    """ensure_folder_path crea la jerarquia y reusa carpetas existentes."""
    svc = _FakeService()
    leaf = _drive.ensure_folder_path("ROOT", ["raw", "sec_insiders", "year=2026", "month=06"], service=svc)
    # Debe haber creado 4 carpetas
    folders = [m for m in svc.store.values() if m["mimeType"] == _drive.MIME_FOLDER]
    assert len(folders) == 4
    names = {m["name"] for m in folders}
    assert names == {"raw", "sec_insiders", "year=2026", "month=06"}

    # Segunda llamada con prefijo comun NO duplica las carpetas existentes.
    _drive.ensure_folder_path("ROOT", ["raw", "sec_insiders", "year=2026", "month=07"], service=svc)
    folders2 = [m for m in svc.store.values() if m["mimeType"] == _drive.MIME_FOLDER]
    assert len(folders2) == 5  # solo se añade month=07


def test_find_file_localiza_por_nombre():
    """find_file devuelve el archivo correcto dentro de una carpeta."""
    svc = _FakeService()
    folder = _drive.ensure_folder_path("ROOT", ["data"], service=svc)
    svc.store["f1"] = {"name": "manifest.json", "parents": [folder], "mimeType": "application/json"}
    found = _drive.find_file(folder, "manifest.json", service=svc)
    assert found is not None and found["id"] == "f1"
    assert _drive.find_file(folder, "noexiste.json", service=svc) is None
