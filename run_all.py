"""Script de utilidad: ejecuta los 4 scrapers en serie.

Util para correr todo localmente (los workflows del CI corren cada uno por
separado por temas de cron y permisos). No es invocado por nadie automatico.
"""

from __future__ import annotations

import sys
import time

from scrapers import congress, polymarket, sec_13f, sec_insider


def main() -> int:
    """Lanza los 4 scrapers, devuelve 0 si todos OK, 1 si alguno fallo."""
    runners = [
        ("congress", congress.run),
        ("sec_insider", sec_insider.run),
        ("sec_13f", sec_13f.run),
        ("polymarket", polymarket.run),
    ]
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
    sys.exit(main())
