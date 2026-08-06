# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-06T10:14:54+00:00 · ventana señales 2026-07-07 -> 2026-08-06_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.9)
- Tendencia: `bull` (SPY 769.79 · MA50 745.72 · MA200 699.04 · dist MA200: 10.12%)
- Credito: `tight` (HY spread 2.73)
- Tipos: `flat` (curva 10y-2y 0.45)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 769.79 | -0.2% | 5.53% | 3.27% |
| QQQ | 12.0% | core | 717.3 | -0.9% | 8.4% | 0.82% |
| TLT | 12.0% | core | 83.0 | 0.22% | 0.58% | -1.22% |
| GLD | 9.3% | core | 389.64 | 4.14% | 5.0% | 4.06% |
| IEF | 6.2% | core | 93.31 | 0.06% | 0.49% | 0.13% |
| FWONK | 5.1% | satellite | 96.05 | -0.39% | -5.73% | -0.46% |
| NTST | 4.9% | satellite | 21.15 | 0.33% | -3.51% | -3.34% |
| SCI | 4.6% | satellite | 85.34 | -0.3% | -0.4% | 11.18% |
| LTH | 4.1% | satellite | 45.31 | 1.3% | -0.85% | 9.18% |
| TSCO | 3.8% | satellite | 33.41 | 0.88% | 7.77% | 12.95% |
| LW | 3.6% | satellite | 53.3 | 0.23% | -1.26% | 15.57% |
| MORN | 2.3% | satellite | 199.33 | -0.46% | 0.34% | 21.15% |
| CHRW | 2.1% | satellite | 153.6 | -0.74% | -11.6% | -19.14% |
| WHD | 1.9% | satellite | 65.91 | -1.93% | 25.97% | 22.67% |
| SPCX | 1.2% | satellite | 108.27 | -13.61% | -3.8% | -26.99% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 7.5%
- VaR 95% 1d: 0.6% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -1.8%
- Beta vs SPY: 0.373 · posiciones efectivas: 14.6 · HHI: 0.0686

**Por que estos satellite (señales WATCHDOG):**

- **NTST** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **MORN** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **TSCO** · score agregado 123.7 · 2 señales · fuentes: corporate_insider
- **LW** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WHD** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **SCI** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| MBRX | 80 | corporate_insider | KLEMP WALTER V | 3 | - | cluster_buy |
| MBRX | 80 | corporate_insider | Foster Jonathan P. | 3 | - | cluster_buy |
| MBRX | 77 | corporate_insider | PICKER DONALD H | 3 | - | cluster_buy |
| CAMP | 76 | corporate_insider | Mandel-Brehm Josh | 4 | $10,809 | cluster_buy,small_amount |
| CAMP | 75 | corporate_insider | Gold Kelly | 4 | $10,809 | cluster_buy,small_amount |
| CAMP | 74 | corporate_insider | Young Richard A | 4 | $27,024 | cluster_buy |
| CAMP | 72 | corporate_insider | Maricich Yuri | 4 | $10,809 | cluster_buy,small_amount |
| MORN | 72 | large_holder | Joseph D. Mansueto |  | - | - |
| LW | 72 | large_holder | JPMORGAN CHASE & CO |  | - | - |
| WHD | 72 | large_holder | Boston Partners |  | - | - |
| ZBRA | 72 | large_holder | Boston Partners |  | - | - |
| MORN | 72 | large_holder | Daniel Mansueto |  | - | - |
| SCI | 72 | large_holder | BAILLIE GIFFORD & CO |  | - | - |
| ETD | 70 | large_holder | DGB Investment, Inc. |  | - | - |
| EA | 70 | large_holder | PUBLIC INVESTMENT FUND |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 65 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| SCI | 62 | congress | April McClain Delaney | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 769.79 (-0.2% / 5.53% / 3.27%) [2026-08-05]
- QQQ: 717.3 (-0.9% / 8.4% / 0.82%) [2026-08-05]
- IWM: 299.77 (-0.64% / 3.88% / 2.14%) [2026-08-05]
- DIA: 542.81 (0.44% / 5.32% / 3.86%) [2026-08-05]
- TLT: 83.0 (0.22% / 0.58% / -1.22%) [2026-08-05]
- IEF: 93.31 (0.06% / 0.49% / 0.13%) [2026-08-05]
- GLD: 389.64 (4.14% / 5.0% / 4.06%) [2026-08-05]
- ^VIX: 15.9 (0.57% / -6.96% / 0.38%) [2026-08-06]
- BTC-USD: 64532.19 (-0.1% / 2.82% / 0.99%) [2026-08-06]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.2 (delta 1m: 0.07) [2026-08-04]
- Treasury 10Y yield: 4.63 (delta 1m: 0.15) [2026-08-04]
- Curva 10Y-2Y: 0.45 (delta 1m: 0.09) [2026-08-05]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.73 (delta 1m: 0.01) [2026-08-04]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.22 (delta 1m: -0.03) [2026-08-05]
- Dolar broad index: 119.7034 (delta 1m: -1.442) [2026-07-31]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (2), stock (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [BLLN] BillionToOne Stock ( BLLN ) Falls After Hours : Here What Driving the Move - BillionToOne ( NASDAQ : BLLN ) (2026-08-06)
- [CRWV] AI cloud firm CoreWeave enters Indonesia with three data centres (2026-08-06)
- [BLLN] Billiontoone Q2 Earnings Call Highlights (2026-08-05)
- [CRWV] Piper Sandler Initiates Coverage Of CoreWeave ( NASDAQ : CRWV ) And Nebius ( NASDAQ : NBIS ) Calls CRWV Top AI Cloud Pick (2026-08-05)
- [BLLN] Does BillionToOne  ( BLLN ) Have Another Major Growth Engine Beyond Prenatal Testing ? (2026-08-04)
- [IBTA] Morning Market Movers : AMRC , INHD , AHCO , IBTA See Big Swings (2026-08-04)
- [BLLN] Critical Analysis : Billiontoone ( NASDAQ : BLLN ) and Lumexa Imaging ( NASDAQ : LMRI ) (2026-07-24)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Harrison Street Real Assets Fund LLC compro NFRX por $10.0M el 2026-08-04.
- CEO Bastian Edward H vendio DAL por $19.2M el 2026-08-04.
- CEO FLORANCE ANDREW C compro CSGP por $2.5M el 2026-08-04.
- CEO Huang Jack Jiajia compro COE por $3.3M el 2026-07-30.
- CEO Huang Jack Jiajia compro COE por $1.8M el 2026-07-29.
- CEO Bender Scott vendio WHD por $6.4M el 2026-08-03 [senal en multiples fuentes].
- CEO Lawton III Harry A compro TSCO por $417K el 2026-08-04 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- JnStTrdrBnusFnd · PnL $48,959 · win rate 92% · categorias: crypto
- Shori888 · PnL $9,966 · win rate 100% · categorias: sports
- BreakTheBank · PnL $86,700 · win rate 85% · categorias: sports
- comon119 · PnL $10,877 · win rate 98% · categorias: sports, crypto, politics
- monkeymashingkeyboard · PnL $29,270 · win rate 91% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 101 registros 30d · ultimo dato 2026-07-31
- **sec_insiders**: `ok` · 853 registros 30d · ultimo dato 2026-08-05
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-05
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CHRW, FWONK, GLD, IEF, LTH, LW, MORN, NTST, QQQ, SCI, SPCX, SPY, TLT, TSCO, WHD`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
