# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-17T15:52:27+00:00 · ventana señales 2026-07-18 -> 2026-08-17_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.05)
- Tendencia: `bull` (SPY 775.19 · MA50 748.95 · MA200 703.22 · dist MA200: 10.23%)
- Credito: `tight` (HY spread 2.67)
- Tipos: `steep` (curva 10y-2y 0.51)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 775.19 | -0.15% | 0.28% | 4.46% |
| QQQ | 12.0% | core | 733.27 | 0.3% | 1.72% | 5.35% |
| TLT | 12.0% | core | 81.65 | -0.48% | -0.5% | -2.28% |
| GLD | 9.3% | core | 405.74 | 1.06% | 0.79% | 10.38% |
| FWONK | 7.5% | satellite | 101.61 | -2.2% | -1.21% | -0.58% |
| IEF | 6.2% | core | 92.96 | -0.09% | 0.22% | -0.28% |
| CHRW | 6.2% | satellite | 146.86 | -1.15% | -0.96% | -28.64% |
| LTH | 5.2% | satellite | 45.33 | 0.15% | 6.76% | 6.63% |
| BWXT | 4.6% | satellite | 173.28 | 0.03% | 2.61% | 2.19% |
| NP | 3.1% | satellite | 31.3 | -1.31% | -2.26% | 0.85% |
| SEPN | 2.7% | satellite | 44.66 | 0.36% | 15.01% | 33.71% |
| CRWV | 2.2% | satellite | 107.15 | 1.8% | 21.5% | 46.66% |
| MANE | 2.1% | satellite | 106.52 | -5.49% | -6.88% | -4.31% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 11.6%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -2.9%
- Beta vs SPY: 0.648 · posiciones efectivas: 13.8 · HHI: 0.0726

**Por que estos satellite (señales WATCHDOG):**

- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **CRWV** · score agregado 215.4 · 3 señales · fuentes: large_holder
- **NP** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **SEPN** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **MANE** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **BWXT** · score agregado 60.7 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| ONON | 83 | corporate_insider | Coppetti Caspar Felix | 2 | $1,993,790 | cluster_buy |
| BORR | 81 | corporate_insider | Troim Tor Olav | 2 | $6,036,750 | cluster_buy |
| FOCL | 80 | corporate_insider | Rhodes Ryan | 4 | $99,750 | cluster_buy |
| BORR | 79 | corporate_insider | Troim Tor Olav | 2 | $2,193,400 | cluster_buy |
| ONON | 79 | corporate_insider | Bernhard Olivier | 2 | $1,993,790 | cluster_buy |
| REZI | 79 | corporate_insider | SURRAN THOMAS A | 2 | $306,900 | cluster_buy |
| FOCL | 78 | corporate_insider | WILLSEY LANCE | 4 | $237,500 | cluster_buy |
| ABCL | 78 | corporate_insider | Booth Andrew | 2 | $383,904 | cluster_buy |
| ANGX | 77 | corporate_insider | Sarowitz Steven I | 2 | $912,317 | cluster_buy |
| ANGX | 77 | corporate_insider | Harmon Neal | 2 | $125,007 | cluster_buy |
| EDAP | 76 | corporate_insider | Mobeck Kenneth S. | 4 | $23,750 | cluster_buy,small_amount |
| BORR | 76 | corporate_insider | Currie Jeffrey | 2 | $501,638 | cluster_buy |
| ACON | 76 | corporate_insider | Ness Brent | 4 | $12,091 | cluster_buy,small_amount |
| ABCL | 76 | corporate_insider | Hayden Michael R | 2 | $481,033 | cluster_buy |
| ANGX | 76 | corporate_insider | Sarowitz Steven I | 2 | $443,277 | cluster_buy |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PINS | 65 | congress | Christian D. Menefee | $50,000 | - |
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 64 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| CCI | 63 | congress | Michael Rulli | $15,000 | small_amount |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 775.19 (-0.15% / 0.28% / 4.46%) [2026-08-17]
- QQQ: 733.27 (0.3% / 1.72% / 5.35%) [2026-08-17]
- IWM: 303.82 (-0.42% / 1.28% / 3.94%) [2026-08-17]
- DIA: 534.6 (-0.41% / -0.81% / 3.22%) [2026-08-17]
- TLT: 81.65 (-0.48% / -0.5% / -2.28%) [2026-08-17]
- IEF: 92.96 (-0.09% / 0.22% / -0.28%) [2026-08-17]
- GLD: 405.74 (1.06% / 0.79% / 10.38%) [2026-08-17]
- ^VIX: 15.05 (5.61% / -2.65% / -19.3%) [2026-08-17]
- BTC-USD: 64139.53 (2.1% / 1.16% / 0.42%) [2026-08-17]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.15 (delta 1m: 0.02) [2026-08-13]
- Treasury 10Y yield: 4.63 (delta 1m: 0.08) [2026-08-13]
- Curva 10Y-2Y: 0.51 (delta 1m: 0.1) [2026-08-14]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.67 (delta 1m: -0.04) [2026-08-14]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.27 (delta 1m: 0.05) [2026-08-14]
- Dolar broad index: 119.0649 (delta 1m: -1.688) [2026-08-07]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), ai (1), earnings (1), merger (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ANET] Arista Networks vs . Intel : Which Technology Stock Is a Better Buy in 2026 ? (2026-08-16)
- [ANET] Arista Networks , Inc . $ANET Shares Purchased by VCI Wealth Management LLC (2026-08-16)
- [ANET] GraniteShares Advisors LLC Invests $1 . 24 Million in Arista Networks , Inc . $ANET (2026-08-16)
- [W] Wayfair ( W ) Physical Retail Emerging as Growth Engine (2026-08-15)
- [PKOH] Reviewing Northgate ( OTCMKTS : NGTEF ) & Park - Ohio ( NASDAQ : PKOH ) (2026-08-15)
- [ANET] Arista Networks vs . Intel : Which Technology Stock Is a Better Buy in 2026 ? (2026-08-15)
- [PKE] Park Aerospace Corp . Announces the Election of Constantine ( Gus ) Petropoulos as Senior Vice President and Chief Financial Officer of the Company (2026-08-13)
- [PKE] Park Aerospace Corp . $PKE Stake Cut by Dimensional Fund Advisors LP (2026-08-09)
- [WBS] Webster Financial Corporation ( WBS ) to Distribute Quarterly Dividend of $0 . 40 on August 20th (2026-08-08)
- [PKE] What Makes Park Aerospace Corp . ( PKE ) a Bullish Bet ? (2026-08-07)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Ullal Jayshree vendio ANET por $47.2M el 2026-08-12.
- CEO Zaslav David vendio WBD por $19.0M el 2026-08-13.
- CEO Dove Reid vendio KNX por $9.3M el 2026-08-13.
- 10% owner RA CAPITAL MANAGEMENT, L.P. vendio SEPN por $31.7M el 2026-08-12 [senal en multiples fuentes].
- 10% owner Empery Asset Management, LP compro EMPD por $2.2M el 2026-08-13 [senal en multiples fuentes].
- CEO Polen Thomas E Jr vendio BDX por $7.2M el 2026-08-13.
- Director Troim Tor Olav compro BORR por $6.0M el 2026-08-13 [senal en multiples fuentes].
- CEO Seto Wai Yue compro TDIC por $1.2M el 2026-08-13 [senal en multiples fuentes].

**Polymarket — smart money (traders con mejor track record):**

- WTSA · PnL $289,499 · win rate 99% · categorias: sports
- Shori888 · PnL $22,332 · win rate 100% · categorias: sports
- kekasaur · PnL $55,106 · win rate 93% · categorias: sports
- delacsynzy · PnL $14,592 · win rate 99% · categorias: sports
- 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 · PnL $78,266 · win rate 87% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 88 registros 30d · ultimo dato 2026-08-07 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 639 registros 30d · ultimo dato 2026-08-17
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-17
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BWXT, CHRW, CRWV, FWONK, GLD, IEF, LTH, MANE, NP, QQQ, SEPN, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
