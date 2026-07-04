"""Tests minimos de la Fase G (construccion de cartera)."""

from __future__ import annotations

import pandas as pd

from portfolio.constraints import get_profile
from portfolio.optimizer import cap_weights, equal_weight, inverse_vol


def test_equal_weight_suma_uno():
    w = equal_weight(["A", "B", "C", "D"])
    assert abs(sum(w.values()) - 1.0) < 1e-6
    assert all(abs(v - 0.25) < 1e-6 for v in w.values())


def test_equal_weight_vacio():
    assert equal_weight([]) == {}


def test_inverse_vol_menos_peso_al_mas_volatil():
    # B es 3x mas volatil que A -> debe pesar menos.
    df = pd.DataFrame({
        "A": [0.01, -0.01, 0.01, -0.01, 0.01],
        "B": [0.03, -0.03, 0.03, -0.03, 0.03],
    })
    w = inverse_vol(["A", "B"], df)
    assert abs(sum(w.values()) - 1.0) < 1e-6
    assert w["A"] > w["B"]


def test_inverse_vol_ticker_sin_datos_recibe_peso_neutro():
    df = pd.DataFrame({"A": [0.01, -0.01, 0.01, -0.01]})
    w = inverse_vol(["A", "Z"], df)  # Z no tiene columna
    assert set(w.keys()) == {"A", "Z"}
    assert abs(sum(w.values()) - 1.0) < 1e-6


def test_cap_weights_respeta_maximo():
    w = {"A": 0.5, "B": 0.3, "C": 0.2}
    capped = cap_weights(w, 0.40)  # 0.40*3=1.2 >= 1.0 -> factible
    assert all(v <= 0.40 + 1e-6 for v in capped.values())
    assert abs(sum(capped.values()) - 1.0) < 1e-3


def test_cap_weights_infactible_reparte_al_cap():
    # cap*n < total: imposible mantener la suma, se reparte todo al cap.
    w = {"A": 0.5, "B": 0.3, "C": 0.2}
    capped = cap_weights(w, 0.30)  # 0.30*3=0.90 < 1.0
    assert all(abs(v - 0.30) < 1e-6 for v in capped.values())


def test_cap_weights_sin_exceso_no_cambia():
    w = {"A": 0.4, "B": 0.35, "C": 0.25}
    capped = cap_weights(w, 0.50)
    assert capped == {t: round(v, 4) for t, v in w.items()}


def test_perfiles_core_suma_coherente():
    for name in ("conservador", "moderado", "agresivo"):
        p = get_profile(name)
        assert abs(p.core_fraction + p.satellite_fraction - 1.0) < 1e-6
        assert 0 < p.max_equity <= 1.0
        assert p.core_weights, "el core no puede estar vacio"


def test_get_profile_default_moderado():
    assert get_profile("inexistente").name == "moderado"
