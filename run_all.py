"""Orquestador de scrapers de WATCHDOG.

Ejecuta los scrapers (todos o un subconjunto) escribiendo en data/public/.
NO hace publish ni health (eso son pasos separados del pipeline). Lo usa el
workflow horario y tambien sirve para correr localmente.

Uso:
    python run_all.py [all|sec|congress|polymarket]

- all        -> todos los scrapers
- sec        -> sec_insider + sec_13f
- congress   -> congress
- polymarket -> polymarket_leaderboard
"""

from __future__ import annotations

import sys
import time

from scrapers import congress, polymarket_leaderboard, sec_13f, sec_insider

# Mapa de grupo -> lista de (nombre, funcion run).
GROUPS = {
    "congress": [("congress", congress.run)],
    "sec": [("sec_insider", sec_insider.run), ("sec_13f", sec_13f.run)],
    "polymarket": [("polymarket_leaderboard", polymarket_leaderboard.run)],
}


def _selected(dataset: str) -> list:
    """Devuelve la lista de runners segun el dataset pedido."""
    if dataset == "all":
        out = []
        for g in ("congress", "sec", "polymarket"):
            out.extend(GROUPS[g])
        return out
    if dataset in GROUPS:
        return GROUPS[dataset]
    raise SystemExit(f"dataset desconocido: {dataset} (usa all|sec|congress|polymarket)")


def main(dataset: str = "all") -> int:
    """Lanza los scrapers seleccionados. Devuelve 0 si todos OK, 1 si alguno fallo."""
    runners = _selected(dataset)
    failed: list[str] = []
    for name, fn in runners:
        t0 = time.time()
        print(f"\n========== {name} ==========")
        try:
            fn()
            print(f"[{name}] OK en {time.time() - t0:.1f}s")
        except Exception as e:
            failed.append(name)
            print(f"[{name}] FALLO: {e}")
    if failed:
        print(f"\nFallaron: {failed}")
        return 1
    print("\nTodos OK")
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    sys.exit(main(arg))
