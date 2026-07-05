# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-05T08:33:27+00:00 · ventana señales 2026-06-05 → 2026-07-05_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen → cartera propuesta → señales → mercado → calidad → instrucciones. Responde segun la seccion 6.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  → **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.15)
- Tendencia: `bull` (SPY vs MA200: 8.14%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque |
|--------|-----:|--------|
| SPY | 12.0% | core |
| QQQ | 11.4% | core |
| TLT | 11.4% | core |
| GLD | 8.6% | core |
| BBSI | 6.8% | satellite |
| IEF | 5.7% | core |
| KEQU | 4.4% | satellite |
| GH | 4.1% | satellite |
| NXDR | 4.0% | satellite |
| SMCI | 2.8% | satellite |
| CRWV | 2.5% | satellite |
| CIFR | 2.2% | satellite |
| FEAM | 2.1% | satellite |
| INDP | 1.2% | satellite |
| ADTX | 0.7% | satellite |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.7%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.8%
- Max drawdown historico: -14.4%
- Beta vs SPY: 0.858 · posiciones efectivas: 15.7 · HHI: 0.0636

**Por que estos satellite (señales WATCHDOG):**

- **BBSI** · score 844.0 · 14 señales · fuentes: corporate_insider
- **SMCI** · score 725.4 · 12 señales · fuentes: corporate_insider
- **GH** · score 715.2 · 12 señales · fuentes: corporate_insider
- **FEAM** · score 708.0 · 12 señales · fuentes: corporate_insider
- **CIFR** · score 629.0 · 10 señales · fuentes: corporate_insider
- **CRWV** · score 542.8 · 9 señales · fuentes: corporate_insider
- **NXDR** · score 297.0 · 5 señales · fuentes: corporate_insider
- **ADTX** · score 280.5 · 4 señales · fuentes: large_holder
- **INDP** · score 276.0 · 4 señales · fuentes: large_holder
- **KEQU** · score 253.0 · 4 señales · fuentes: corporate_insider, large_holder

## 3. Mejores señales de smart money (compra, 30d)

| Ticker | Score | Fuente | Actor | Cluster | Flags |
|--------|------:|--------|-------|--------:|-------|
| APPN | 71.8 | large_holder | Lead Edge Capital Mana |  | - |
| KEQU | 71.8 | large_holder | Minerva Advisors LLC |  | - |
| INTC | 70.7 | congress | Nancy Pelosi |  | - |
| CTM | 70.5 | corporate_insider | Ives Glen R | 4 | cluster_buy,small_amount |
| NINE | 70.5 | large_holder | Algebris Investments ( |  | - |
| ALMR | 70.5 | large_holder | SHERPA HEALTHCARE FUND |  | - |
| PSBD | 70.5 | large_holder | Alaris Master Fund LP |  | - |
| SUNE | 70.5 | large_holder | JANE STREET GROUP, LLC |  | - |
| MSGM | 70.5 | large_holder | Red Oak Partners, LLC |  | - |
| ZBAO | 70.5 | large_holder | Ningbo Pangu Chuangfu  |  | - |
| ADTX | 70.5 | large_holder | Castillo Christopher |  | - |
| ADTX | 70.5 | large_holder | Castillo Christopher |  | - |

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
- BTC-USD: 62935.89 (0.63% / 4.65% / -4.22%)

**Macro (valor · cambio 1m):**


## 5. Calidad de los datos

- Estado global: `ok`
- Congreso/13F tienen retraso legal de hasta ~45 dias.
- Senate no disponible en vivo (portal eFD bloqueado); House si.

## 6. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: solo puedes usar tickers ya presentes en la cartera candidata: `ADTX, BBSI, CIFR, CRWV, FEAM, GH, GLD, IEF, INDP, KEQU, NXDR, QQQ, SMCI, SPY, TLT`. No inventes tickers nuevos ni uses ninguno sin datos de precio.
2. **Presupuesto de riesgo**: la suma de todos los pesos ≤ **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
