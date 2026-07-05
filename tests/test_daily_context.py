"""Test minimo del briefing diario para el LLM (Fase H)."""

from __future__ import annotations

from pipelines.build_daily_context import build


def test_briefing_tiene_las_siete_secciones():
    md = build()
    assert isinstance(md, str) and md
    for header in (
        "## 1. Regimen de mercado",
        "## 2. Cartera CANDIDATA",
        "## 3. Señales de smart money",
        "## 4. Snapshot de mercado",
        "## 5. Noticias y contexto del mundo",
        "## 6. Calidad de los datos",
        "## 7. Instrucciones para ti",
    ):
        assert header in md, f"falta seccion: {header}"


def test_briefing_incluye_restricciones_duras_y_formato_json():
    md = build()
    assert "Restricciones DURAS" in md
    assert "Universo permitido" in md
    assert "Presupuesto de riesgo" in md
    assert "final_weights" in md  # esquema de respuesta obligatorio
    assert "```json" in md


def test_briefing_universo_incluye_senales():
    """El universo permitido debe mencionar las señales (no solo la candidata),
    coherente con el system prompt y con validate_llm_output."""
    md = build()
    assert "o de las señales" in md
