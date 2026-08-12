# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-12T17:28:01+00:00 · ventana señales 2026-07-13 -> 2026-08-12_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.67)
- Tendencia: `bull` (SPY 772.96 · MA50 747.67 · MA200 701.74 · dist MA200: 10.15%)
- Credito: `tight` (HY spread 2.72)
- Tipos: `flat` (curva 10y-2y 0.48)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 772.96 | 0.31% | 0.41% | 2.4% |
| QQQ | 12.0% | core | 725.27 | 0.95% | 1.11% | 1.05% |
| TLT | 12.0% | core | 82.32 | 0.16% | -0.82% | -1.89% |
| GLD | 9.3% | core | 404.27 | 0.83% | 3.75% | 8.57% |
| FWONK | 6.9% | satellite | 104.36 | 1.94% | 8.66% | 4.36% |
| KRNY | 6.8% | satellite | 9.5 | -0.31% | -1.86% | 0.32% |
| IEF | 6.2% | core | 93.08 | 0.23% | -0.24% | -0.4% |
| LTH | 5.5% | satellite | 44.07 | 0.59% | -2.74% | 4.93% |
| FSUN | 3.8% | satellite | 40.92 | 0.75% | 2.8% | 15.87% |
| CHRW | 3.0% | satellite | 147.87 | 1.91% | -3.73% | -25.13% |
| SNEX | 2.6% | satellite | 68.01 | 3.09% | -10.54% | -9.91% |
| AMRC | 1.9% | satellite | 27.4 | 5.83% | 6.78% | 11.02% |
| SPCX | 1.6% | satellite | 145.96 | 9.51% | 34.81% | 7.9% |
| CRWV | 1.4% | satellite | 107.61 | 19.14% | 19.71% | 39.54% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 11.3%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -3.7%
- Beta vs SPY: 0.652 · posiciones efectivas: 13.9 · HHI: 0.0719

**Por que estos satellite (señales WATCHDOG):**

- **AMRC** · score agregado 301.7 · 4 señales · fuentes: corporate_insider
- **FSUN** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **SPCX** · score agregado 194.2 · 3 señales · fuentes: congress, large_holder
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **CRWV** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **SNEX** · score agregado 57.5 · 1 señales · fuentes: corporate_insider
- **KRNY** · score agregado 54.8 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| XRN | 79 | corporate_insider | Decker Mark Okey Jr | 2 | $287,040 | cluster_buy |
| XRN | 78 | corporate_insider | Fitzgerald Charles | 2 | $991,944 | cluster_buy |
| AMRC | 78 | corporate_insider | Cox Brian C | 2 | $995,279 | cluster_buy |
| AMRC | 77 | corporate_insider | Sakellaris George P | 2 | $129,750 | cluster_buy |
| AMRC | 74 | corporate_insider | Sakellaris George P | 2 | $25,900 | cluster_buy |
| AMRC | 74 | corporate_insider | Sakellaris George P | 2 | $25,270 | cluster_buy |
| TSCO | 73 | large_holder | Capital International Inv |  | - | - |
| KMPR | 73 | corporate_insider | Camden Bradley T | 2 | $26,340 | cluster_buy |
| ICHR | 72 | large_holder | Capital International Inv |  | - | - |
| CHKP | 72 | large_holder | Gil Shwed |  | - | - |
| FFIV | 72 | large_holder | Hotchkis and Wiley Capita |  | - | - |
| NXTC | 72 | large_holder | Adage Capital Management, |  | - | - |
| CRWV | 72 | large_holder | THE GOLDMAN SACHS GROUP,  |  | - | - |
| FNRN | 72 | large_holder | M3 Funds, LLC |  | - | - |
| SPCX | 72 | large_holder | Antonio J. Gracias |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TSCO | 66 | congress | April McClain Delaney | $50,000 | - |
| PINS | 65 | congress | Christian D. Menefee | $50,000 | - |
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| CCI | 63 | congress | Michael Rulli | $15,000 | small_amount |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 772.96 (0.31% / 0.41% / 2.4%) [2026-08-12]
- QQQ: 725.27 (0.95% / 1.11% / 1.05%) [2026-08-12]
- IWM: 302.25 (0.42% / 0.83% / 2.19%) [2026-08-12]
- DIA: 537.54 (0.05% / -0.97% / 2.23%) [2026-08-12]
- TLT: 82.32 (0.16% / -0.82% / -1.89%) [2026-08-12]
- IEF: 93.08 (0.23% / -0.24% / -0.4%) [2026-08-12]
- GLD: 404.27 (0.83% / 3.75% / 8.57%) [2026-08-12]
- ^VIX: 14.67 (-3.99% / -7.21% / -6.38%) [2026-08-12]
- BTC-USD: 63357.2 (-0.31% / -2.35% / -2.59%) [2026-08-12]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.25 (delta 1m: 0.04) [2026-08-10]
- Treasury 10Y yield: 4.72 (delta 1m: 0.16) [2026-08-10]
- Curva 10Y-2Y: 0.48 (delta 1m: 0.12) [2026-08-11]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.72 (delta 1m: 0.03) [2026-08-11]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.27 (delta 1m: 0.01) [2026-08-11]
- Dolar broad index: 119.0649 (delta 1m: -1.688) [2026-08-07]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: earnings (1), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [AXON] Tracing Jim Cramer Evolving View on Axon Enterprise ( AXON ) (2026-08-10)
- [AXON] Hennion & Walsh Asset Management Inc . Trims Position in Axon Enterprise , Inc $AXON (2026-08-10)
- [MTRN] Materion Q2 Earnings Call Highlights (2026-08-08)
- [AXON] $10 , 000 in Axon Stock a Decade Ago Would Be Worth About $329 , 000 Today . The Stock Is Down Over the Past Year . (2026-08-08)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner AH Bio Fund IV, L.P. compro BRVE por $19.8M el 2026-08-07.
- CEO Huang Jack Jiajia compro COE por $3.9M el 2026-08-10.
- CEO Golub David vendio GBDC por $21.9M el 2026-08-07.
- CEO Ellwanger Russell Craig vendio TSEM por $8.8M el 2026-08-11.
- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro QVCG por $3.9M el 2026-08-10.
- CEO Valenti Douglas vendio QNST por $15.4M el 2026-08-07.
- CEO Huang Jack Jiajia compro COE por $2.0M el 2026-08-06.
- CEO Huang Jack Jiajia compro COE por $1.8M el 2026-08-07.

**Polymarket — smart money (traders con mejor track record):**

- WTSA · PnL $233,699 · win rate 98% · categorias: sports
- ExplosiveNinja · PnL $57,915 · win rate 97% · categorias: sports
- SDTrading · PnL $95,422 · win rate 93% · categorias: sports
- TAIWANNUMBERONE · PnL $70,016 · win rate 91% · categorias: sports, politics
- CORGI8 · PnL $53,554 · win rate 93% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 102 registros 30d · ultimo dato 2026-08-07 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 706 registros 30d · ultimo dato 2026-08-12
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-12
- **institutional_13f**: `warning` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress, institutional_13f

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMRC, CHRW, CRWV, FSUN, FWONK, GLD, IEF, KRNY, LTH, QQQ, SNEX, SPCX, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **95.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
