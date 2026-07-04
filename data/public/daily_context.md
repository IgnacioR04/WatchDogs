# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-04T13:43:40+00:00 · ventana señales 2026-06-04 → 2026-07-04_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen → cartera propuesta → señales → mercado → calidad → instrucciones. Responde segun la seccion 6.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  → **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.15)
- Tendencia: `bull` (SPY vs MA200: 8.14%)
- Credito: `tight` (HY spread 2.75)
- Tipos: `flat` (curva 10y-2y 0.35)
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque |
|--------|-----:|--------|
| SPY | 12.0% | core |
| QQQ | 12.0% | core |
| TLT | 12.0% | core |
| GLD | 9.3% | core |
| HUBB | 6.7% | satellite |
| IEF | 6.2% | core |
| BBSI | 5.5% | satellite |
| LPLA | 5.3% | satellite |
| GH | 3.4% | satellite |
| NXDR | 3.1% | satellite |
| SMCI | 2.5% | satellite |
| CRWV | 2.0% | satellite |
| CIFR | 1.7% | satellite |
| FEAM | 1.7% | satellite |
| STEM | 1.5% | satellite |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.0%
- VaR 95% 1d: 1.5% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -11.9%
- Beta vs SPY: 0.881 · posiciones efectivas: 14.3 · HHI: 0.07

**Por que estos satellite (señales WATCHDOG):**

- **BBSI** · score 979.2 · 14 señales · fuentes: corporate_insider
- **SMCI** · score 837.3 · 12 señales · fuentes: corporate_insider
- **GH** · score 829.2 · 12 señales · fuentes: corporate_insider
- **FEAM** · score 819.6 · 12 señales · fuentes: corporate_insider
- **CIFR** · score 716.8 · 10 señales · fuentes: corporate_insider
- **CRWV** · score 616.2 · 9 señales · fuentes: corporate_insider
- **STEM** · score 347.5 · 5 señales · fuentes: corporate_insider
- **LPLA** · score 346.4 · 6 señales · fuentes: congress
- **NXDR** · score 336.5 · 5 señales · fuentes: corporate_insider
- **HUBB** · score 296.1 · 5 señales · fuentes: congress

## 3. Mejores señales de smart money (compra, 30d)

| Ticker | Score | Fuente | Actor | Cluster | Flags |
|--------|------:|--------|-------|--------:|-------|
| HTO | 75.4 | corporate_insider | ATLAS Infrastructure P |  | - |
| IBM | 74.6 | corporate_insider | Robinson Anne |  | - |
| IBM | 74.6 | corporate_insider | Robinson Anne |  | - |
| MAZE | 74.3 | corporate_insider | Bernstein Harold |  | - |
| TTEC | 73.3 | corporate_insider | BROWN CHRISTOPHER (JOH |  | - |
| BETR | 72.1 | corporate_insider | Advani Loveen |  | - |
| BBSI | 72.1 | corporate_insider | Harris Anthony J |  | - |
| BBSI | 72.1 | corporate_insider | Harris Anthony J |  | - |
| BBSI | 72.1 | corporate_insider | Harris Anthony J |  | - |
| BBSI | 72.1 | corporate_insider | Harris Anthony J |  | - |
| BBSI | 72.1 | corporate_insider | Harris Anthony J |  | - |
| SMCI | 72.1 | corporate_insider | WEIGAND DAVID E |  | - |

> Cluster = nº de insiders distintos comprando el mismo ticker (señal de conviccion). Flags = avisos de calidad de la señal.

## 4. Snapshot de mercado y macro

**Precios (ret 1d / 5d / 20d):**

- SPY: 744.78 (-0.13% / 1.43% / -1.0%)
- QQQ: 712.6 (-1.73% / -0.53% / -4.14%)
- IWM: 297.58 (-0.58% / -0.44% / 3.69%)
- TLT: 85.51 (-0.01% / -1.74% / 0.6%)
- IEF: 94.12 (0.1% / -0.38% / 0.46%)
- GLD: 378.13 (2.03% / 2.35% / -7.29%)
- ^VIX: 16.15 (-2.65% / -14.51% / 0.56%)
- BTC-USD: 62542.48 (-0.0% / 4.0% / -4.82%)

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.17 (Δ1m 0.12)
- Treasury 10Y yield: 4.48 (Δ1m 0.01)
- Curva 10Y-2Y: 0.35 (Δ1m -0.06)
- Fed Funds Rate: 3.63 (Δ1m -1.5)
- High yield spread (OAS): 2.75 (Δ1m 0.0)

## 5. Calidad de los datos

- Estado global: `ok`
- Congreso/13F tienen retraso legal de hasta ~45 dias.
- Senate no disponible en vivo (portal eFD bloqueado); House si.

## 6. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: solo puedes usar tickers ya presentes en la cartera candidata: `BBSI, CIFR, CRWV, FEAM, GH, GLD, HUBB, IEF, LPLA, NXDR, QQQ, SMCI, SPY, STEM, TLT`. No inventes tickers nuevos ni uses ninguno sin datos de precio.
2. **Presupuesto de riesgo**: la suma de todos los pesos ≤ **90.0%** (el resto es cash). Estamos en regimen `risk_on`.
3. **Peso maximo por posicion**: ≤ **12.0%**.
4. **Sin apalancamiento y sin cortos**: todos los pesos ≥ 0, suma ≤ 1.
5. **Justifica cada cambio** con una razon concreta basada en los datos de este briefing (señal, regimen, riesgo). Nada de datos externos.

### Que quiero de ti

- Un veredicto: aceptar la cartera tal cual (`accept`) o ajustarla (`adjust`).
- Si ajustas: la lista de cambios (subir/bajar/quitar/añadir peso) con su razon.
- Una tesis breve (2-4 frases) y los riesgos clave.
- Tu nivel de confianza (0 a 1).

### Formato de respuesta OBLIGATORIO

Responde **solo con este JSON** (sin texto alrededor), para que el codigo lo pueda validar:

```json
{
  "verdict": "accept | adjust",
  "adjustments": [
    {"ticker": "XXX", "action": "increase|decrease|remove|add",
     "target_weight": 0.05, "reason": "..."}
  ],
  "final_weights": {"SPY": 0.12, "QQQ": 0.10, "...": 0.0},
  "thesis": "...",
  "key_risks": ["...", "..."],
  "confidence": 0.0
}
```

- `final_weights` debe contener la cartera COMPLETA que propones (la que el codigo validara). Si tu veredicto es `accept`, copia los pesos de la seccion 2.
- Si no propones cambios, `adjustments` puede ir vacio.

**Recuerda**: esto no es asesoramiento financiero; solo hipotesis sobre datos publicos con retraso legal. Cuantifica la incertidumbre, no afirmes certezas.
