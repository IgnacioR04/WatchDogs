"""Test minimo del briefing diario para el LLM (Fase H)."""

from __future__ import annotations

from pipelines.build_daily_context import build


def test_briefing_tiene_las_seis_secciones():
    md = build()
    assert isinstance(md, str) and md
    for header in (
        "## 1. Regimen de mercado",
        "## 2. Cartera CANDIDATA",
        "## 3. Mejores señales",
        "## 4. Snapshot de mercado",
        "## 5. Calidad de los datos",
        "## 6. Instrucciones para ti",
    ):
        assert header in md, f"falta seccion: {header}"


def test_briefing_incluye_restricciones_duras_y_formato_json():
    md = build()
    assert "Restricciones DURAS" in md
    assert "Universo permitido" in md
    assert "Presupuesto de riesgo" in md
    assert "final_weights" in md  # esquema de respuesta obligatorio
    assert "```json" in md
