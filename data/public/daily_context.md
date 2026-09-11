# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-11T00:27:07+00:00 · ventana señales 2026-08-12 -> 2026-09-11_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.84)
- Tendencia: `bull` (SPY 762.4 · MA50 758.02 · MA200 710.95 · dist MA200: 7.24%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.39)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 762.4 | -0.46% | 0.08% | -1.06% |
| QQQ | 12.0% | core | 716.31 | -0.29% | 1.23% | -0.3% |
| TLT | 12.0% | core | 81.73 | -0.57% | -0.17% | -0.18% |
| CSQ | 10.2% | satellite | 20.6 | -1.2% | -1.39% | -0.66% |
| GLD | 9.3% | core | 403.35 | 0.91% | 1.66% | 0.6% |
| RSG | 7.9% | satellite | 222.47 | 0.38% | -0.37% | 3.44% |
| IEF | 6.2% | core | 91.9 | -0.28% | -0.22% | -0.69% |
| BLFS | 4.0% | satellite | 34.93 | -1.27% | -1.52% | 0.32% |
| GOLD | 3.5% | satellite | 49.33 | 3.92% | 14.3% | 13.56% |
| PRGO | 2.9% | satellite | 14.34 | -1.65% | -0.62% | 13.89% |
| UPST | 2.8% | satellite | 25.89 | -4.04% | -5.48% | -13.38% |
| TWST | 2.1% | satellite | 125.52 | -1.98% | -4.95% | 1.95% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.0%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -3.3%
- Beta vs SPY: 0.751 · posiciones efectivas: 12.9 · HHI: 0.0774

**Por que estos satellite (señales WATCHDOG):**

- **RSG** · score agregado 488.9 · 7 señales · fuentes: corporate_insider, large_holder
- **CSQ** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **TWST** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **BLFS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PRGO** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GOLD** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **UPST** · score agregado 66.0 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GRCE | 78 | corporate_insider | Kohli Prashant | 2 | $214,000 | cluster_buy |
| PRTS | 77 | corporate_insider | Meniane David | 2 | $133,295 | cluster_buy |
| RSG | 72 | corporate_insider | CASCADE INVESTMENT, L.L.C | 0 | $55,425,001 | - |
| PRTS | 72 | corporate_insider | Huffaker Michael | 2 | $133,295 | cluster_buy |
| RSG | 72 | corporate_insider | CASCADE INVESTMENT, L.L.C | 0 | $47,226,807 | - |
| ZDGE | 72 | large_holder | Michael Jonas |  | - | - |
| MGX | 72 | large_holder | Thomas Brian C. |  | - | - |
| BLFS | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| TWST | 72 | large_holder | ARK Investment Management |  | - | - |
| TWST | 72 | large_holder | FMR LLC |  | - | - |
| QVCG | 72 | large_holder | Barclays PLC |  | - | - |
| QVCG | 72 | large_holder | Barclays PLC |  | - | - |
| PRGO | 72 | large_holder | T. Rowe Price Associates, |  | - | - |
| SIG | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| GRCE | 71 | corporate_insider | Opaleye Management Inc. | 2 | $19,699 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| QVCG | 58 | corporate_insider | Silver Point Capital L.P. | $26,000,000 | - |
| LRCX | 58 | corporate_insider | ARCHER TIMOTHY | $9,577,800 | - |
| SITM | 58 | corporate_insider | VASHIST RAJESH | $7,241,640 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $5,725,979 | - |
| DDOG | 57 | corporate_insider | Pomel Olivier | $5,063,681 | - |
| VST | 56 | corporate_insider | HUDSON SCOTT A | $4,377,228 | - |
| LASR | 56 | corporate_insider | Keeney Scott H | $4,101,000 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $4,002,735 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 762.4 (-0.46% / 0.08% / -1.06%) [2026-09-09]
- QQQ: 716.31 (-0.29% / 1.23% / -0.3%) [2026-09-09]
- IWM: 290.64 (-1.37% / 0.02% / -3.44%) [2026-09-09]
- DIA: 524.07 (-0.75% / -0.7% / -2.38%) [2026-09-09]
- TLT: 81.73 (-0.57% / -0.17% / -0.18%) [2026-09-09]
- IEF: 91.9 (-0.28% / -0.22% / -0.69%) [2026-09-09]
- GLD: 403.35 (0.91% / 1.66% / 0.6%) [2026-09-09]
- ^VIX: 17.84 (8.38% / 24.58% / 21.94%) [2026-09-10]
- BTC-USD: 76809.0 (-1.85% / -3.78% / -1.95%) [2026-09-11]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.43 (delta 1m: 0.18) [2026-09-09]
- Treasury 10Y yield: 4.83 (delta 1m: 0.11) [2026-09-09]
- Curva 10Y-2Y: 0.39 (delta 1m: -0.09) [2026-09-10]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.71 (delta 1m: -0.01) [2026-09-09]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.4 (delta 1m: 0.13) [2026-09-10]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (4), regulatory (3), stock (2), earnings (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DELL] Dell Technologies ( NYSE : DELL ) Shares Down 5 . 3 % Following Insider Selling (2026-09-10)
- [DELL] Royal Bank Of Canada Initiates Coverage on Dell Technologies ( NYSE : DELL ) (2026-09-10)
- [CRWV] CoreWeave ( NASDAQ : CRWV ) Trading Up 11 . 7 % – Here Why (2026-09-10)
- [DELL] Dell ( DELL ) Reports $60 . 9B of AI Server Orders and a $95B Backlog . Can the Demand Surge Produce Durable Cash Flow ? (2026-09-10)
- [DELL] Dell AI Server Orders Reached $61 Billion in the Second Quarter , and the Pipeline Keeps Growing (2026-09-10)
- [DELL] Dell AI Server Orders Reached $61 Billion in the Second Quarter , and the Pipeline Keeps Growing (2026-09-10)
- [AXON] Covington will get AI , tasers and a drone from Axon , but not license plate readers (2026-09-09)
- [ACMR] Financial Analysis : ACM Research ( NASDAQ : ACMR ) vs . Ascent Solar Technologies ( NASDAQ : ASTI ) (2026-09-02)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $47.2M el 2026-09-09 [senal en multiples fuentes].
- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $55.4M el 2026-09-08 [senal en multiples fuentes].
- CEO KHOSROWSHAHI DARA compro UBER por $10.0M el 2026-09-10.
- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro QVCG por $26.0M el 2026-09-08 [senal en multiples fuentes].
- CEO ARCHER TIMOTHY vendio LRCX por $9.6M el 2026-09-09.
- CEO Gu Paul compro UPST por $1.3M el 2026-09-10.
- CEO VASHIST RAJESH vendio SITM por $7.2M el 2026-09-09.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.

**Polymarket — smart money (traders con mejor track record):**

- theowalcott · PnL $185,347 · win rate 100% · categorias: sports
- Diabolical-Prize · PnL $408,398 · win rate 94% · categorias: sports
- mmklop · PnL $72,795 · win rate 96% · categorias: sports
- Kch-Temp · PnL $156,283 · win rate 89% · categorias: sports
- CORGI8 · PnL $73,067 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 757 registros 30d · ultimo dato 2026-09-10
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-10
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BLFS, CSQ, GLD, GOLD, IEF, PRGO, QQQ, RSG, SPY, TLT, TWST, UPST`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **90.0%** (el resto es cash). Estamos en regimen `risk_on`.
3. **Peso maximo por posicion**: <= **12.0%**.
4. **Sin apalancamiento y sin cortos**: todos los pesos >= 0, suma <= 1.
5. **Liquidez para posiciones NUEVAS**: precio >= $5 y volumen medio >= $2M/dia. Mantener una posicion abierta que se volvio iliquida es legal; abrir una nueva iliquida no.
6. **Justifica cada cambio** con una razon concreta basada en los datos de este briefing (señal, regimen, riesgo, precio). Nada de datos externos. Recuerda: cada rebalanceo paga 0.15% del importe operado (se descuenta del P&L real).

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

- `final_weights` = cartera COMPLETA que propones. Es lo unico que el codigo ejecuta. El cash es lo que sobra hasta 1.0 (no lo pongas en final_weights).
- Si tu veredicto es `accept`, copia los pesos exactos de la seccion 2.
- Si no propones cambios, `adjustments` puede ir vacio.

**Recuerda**: esto no es asesoramiento financiero; solo hipotesis sobre datos publicos con retraso legal. Cuantifica la incertidumbre, no afirmes certezas.
