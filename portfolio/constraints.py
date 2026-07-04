"""Perfiles y restricciones de cartera (Fase G v3).

Define la politica core-satellite por perfil de riesgo. El CORE es la base
estable (indices, bonos, oro); el SATELLITE son las apuestas de las señales
WATCHDOG. El resto es cash. La exposicion total nunca supera ni el cap del
perfil ni el presupuesto de riesgo del regimen.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Profile:
    """Perfil de riesgo: como repartir entre core, satellite y cash."""
    name: str
    core_fraction: float              # del capital en riesgo, cuanto va a core
    satellite_fraction: float         # cuanto va a satellite (core+sat = 1)
    max_equity: float                 # exposicion total maxima (cap del perfil)
    max_position: float               # peso maximo de una posicion
    max_satellite_positions: int      # cuantas apuestas satellite como mucho
    core_weights: dict[str, float] = field(default_factory=dict)  # composicion normalizada del core


# Composiciones de core por perfil (se normalizan). Mas bonos/oro = mas defensivo.
_CORE_CONS = {"SPY": 0.25, "QQQ": 0.10, "TLT": 0.30, "IEF": 0.15, "GLD": 0.20}
_CORE_MOD = {"SPY": 0.35, "QQQ": 0.20, "TLT": 0.20, "IEF": 0.10, "GLD": 0.15}
_CORE_AGR = {"SPY": 0.35, "QQQ": 0.30, "TLT": 0.10, "IEF": 0.05, "GLD": 0.20 - 0.10}  # 0.10

PROFILES: dict[str, Profile] = {
    "conservador": Profile(
        name="conservador", core_fraction=0.80, satellite_fraction=0.20,
        max_equity=0.60, max_position=0.08, max_satellite_positions=6,
        core_weights=_CORE_CONS),
    "moderado": Profile(
        name="moderado", core_fraction=0.65, satellite_fraction=0.35,
        max_equity=0.85, max_position=0.12, max_satellite_positions=10,
        core_weights=_CORE_MOD),
    "agresivo": Profile(
        name="agresivo", core_fraction=0.50, satellite_fraction=0.50,
        max_equity=1.00, max_position=0.15, max_satellite_positions=14,
        core_weights=_CORE_AGR),
}


def get_profile(name: str) -> Profile:
    """Devuelve el perfil por nombre (default moderado)."""
    return PROFILES.get(name, PROFILES["moderado"])
