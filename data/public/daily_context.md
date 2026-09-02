# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-02T09:56:01+00:00 · ventana señales 2026-08-03 -> 2026-09-02_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.78)
- Tendencia: `bull` (SPY 761.78 · MA50 754.71 · MA200 708.29 · dist MA200: 7.55%)
- Credito: `tight` (HY spread 2.63)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 761.78 | -0.69% | -0.54% | -1.24% |
| QQQ | 12.0% | core | 707.64 | -1.27% | -0.43% | -2.24% |
| TLT | 12.0% | core | 81.87 | -0.41% | -1.54% | -0.77% |
| GLD | 9.3% | core | 396.75 | -2.86% | -7.32% | 6.04% |
| KIDS | 7.5% | satellite | 23.0 | -1.33% | -6.12% | 10.15% |
| IEF | 6.2% | core | 92.1 | -0.33% | -1.15% | -0.88% |
| BILL | 5.8% | satellite | 47.62 | -3.27% | -0.19% | -1.96% |
| KVYO | 4.3% | satellite | 20.64 | 0.29% | 17.27% | 8.06% |
| PESI | 4.0% | satellite | 17.84 | -1.71% | 0.73% | 0.28% |
| AUGO | 3.9% | satellite | 79.04 | -5.43% | -12.63% | 38.05% |
| AMRC | 3.5% | satellite | 22.6 | 2.17% | 2.4% | -19.11% |
| SUJA | 2.5% | satellite | 10.43 | 3.57% | 11.79% | -8.51% |
| FGL | 2.0% | satellite | 17.23 | 13.36% | -17.95% | -79.99% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 14.3%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 2.0%
- Max drawdown historico: -6.4%
- Beta vs SPY: 0.878 · posiciones efectivas: 13.9 · HHI: 0.0719

**Por que estos satellite (señales WATCHDOG):**

- **AUGO** · score agregado 259.2 · 4 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **PESI** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **AMRC** · score agregado 131.4 · 2 señales · fuentes: corporate_insider, large_holder
- **FGL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KIDS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **BILL** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **KVYO** · score agregado 67.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| LUCK | 76 | corporate_insider | Young John Alan | 2 | $614,000 | cluster_buy |
| AIIR | 75 | corporate_insider | Brazier Stuart Damon | 2 | $44,128 | cluster_buy |
| AIIR | 73 | corporate_insider | Lotfy Bassem | 2 | $35,479 | cluster_buy |
| TMQ | 72 | large_holder | South32 Limited |  | - | - |
| NCSM | 72 | large_holder | ADVENT INTERNATIONAL, L.P |  | - | - |
| FGL | 72 | large_holder | Marex Financial |  | - | - |
| AMRC | 72 | large_holder | Gagnon Securities LLC |  | - | - |
| QTEX | 72 | large_holder | M.H. Davidson & Co. |  | - | - |
| AFCG | 72 | large_holder | Leonard M. Tannenbaum |  | - | - |
| VTMX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| EDSA | 72 | large_holder | Stonepine Capital Managem |  | - | - |
| LUCK | 71 | corporate_insider | MATHRANI SANDEEP | 2 | $59,957 | cluster_buy |
| LIEN | 71 | corporate_insider | Colonna Bernardino | 2 | $7,685 | cluster_buy,small_amount |
| CON | 70 | large_holder | Robert A. Ortenzio |  | - | - |
| BMHL | 70 | large_holder | Luk Tung Lam |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ACT | 59 | corporate_insider | Genworth Holdings, Inc. | $33,953,773 | - |
| TMQ | 58 | corporate_insider | South32 Ltd | $17,827,787 | - |
| ROIV | 57 | corporate_insider | Venker Eric | $5,921,065 | - |
| CRNX | 56 | corporate_insider | Struthers Richard Scott | $21,083,655 | - |
| TYL | 56 | corporate_insider | MOORE H LYNN JR | $3,448,280 | - |
| ABNB | 56 | corporate_insider | Blecharczyk Nathan | $8,617,143 | - |
| CRNX | 56 | corporate_insider | Struthers Richard Scott | $15,016,355 | - |
| CHYM | 56 | corporate_insider | Britt Christopher R | $3,015,626 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 761.78 (-0.69% / -0.54% / -1.24%) [2026-09-01]
- QQQ: 707.64 (-1.27% / -0.43% / -2.24%) [2026-09-01]
- IWM: 290.57 (-1.14% / -2.89% / -3.69%) [2026-09-01]
- DIA: 527.75 (-0.72% / -1.4% / -2.27%) [2026-09-01]
- TLT: 81.87 (-0.41% / -1.54% / -0.77%) [2026-09-01]
- IEF: 92.1 (-0.33% / -1.15% / -0.88%) [2026-09-01]
- GLD: 396.75 (-2.86% / -7.32% / 6.04%) [2026-09-01]
- ^VIX: 16.78 (2.69% / 10.32% / 6.14%) [2026-09-02]
- BTC-USD: 76637.44 (-0.99% / -1.53% / 20.88%) [2026-09-02]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.34 (delta 1m: 0.06) [2026-08-31]
- Treasury 10Y yield: 4.75 (delta 1m: 0.0) [2026-08-31]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.05) [2026-09-01]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.63 (delta 1m: -0.22) [2026-08-31]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.35 (delta 1m: 0.08) [2026-09-01]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (5), ai (3)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ABNB] 18 - year - old killed at Airbnb as Clark County changes short - term rental enforcement (2026-09-02)
- [AUGO] Aura Minerals ( NASDAQ : AUGO ) Director Purchases 252 , 000 Shares of Stock (2026-09-02)
- [ABNB] Nathan Blecharczyk Sells 57 , 160 Shares of Airbnb ( NASDAQ : ABNB ) Stock (2026-09-02)
- [ABNB] Airbnb ( NASDAQ : ABNB ) Insider Sells 13 , 615 Shares of Stock (2026-09-02)
- [CSTL] Castle Biosciences , Inc . ( NASDAQ : CSTL ) Receives $42 . 00 Average PT from Analysts (2026-08-23)
- [AUGO] Insider Selling : Aura Minerals ( NASDAQ : AUGO ) CFO Sells $635 , 672 . 08 in Stock (2026-08-20)
- [AUGO] Aura Minerals ( NASDAQ : AUGO ) Director Mauad Bruno Sousa Sells 280 , 000 Shares of Stock (2026-08-20)
- [AUGO] Aura Minerals ( TSE : ORA ) Share Price Passes Above 200 Day Moving Average – Should You Sell ? (2026-08-19)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Senior Loan Trust por $44.0M el 2026-08-31.
- 10% owner Manufacturers Life Insurance Co (Bermuda Branch) compro John Hancock GA Senior Loan Trust por $23.0M el 2026-08-31.
- CEO Struthers Richard Scott vendio CRNX por $21.1M el 2026-09-01.
- 10% owner Genworth Holdings, Inc. vendio ACT por $34.0M el 2026-08-31.
- CEO Savi Luca compro ITT por $1.0M el 2026-08-31.
- 10% owner South32 Ltd vendio TMQ por $17.8M el 2026-08-28 [senal en multiples fuentes].
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- monkeymashingkeyboard · PnL $59,550 · win rate 92% · categorias: sports
- TAIWANNUMBERONE · PnL $49,048 · win rate 92% · categorias: sports, politics
- Donghui · PnL $23,855 · win rate 92% · categorias: sports
- Kosherlocks · PnL $13,514 · win rate 96% · categorias: sports, crypto
- rollobravado · PnL $7,588 · win rate 99% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 581 registros 30d · ultimo dato 2026-09-01
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-01
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMRC, AUGO, BILL, FGL, GLD, IEF, KIDS, KVYO, PESI, QQQ, SPY, SUJA, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
