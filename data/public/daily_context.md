# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-02T00:33:55+00:00 · ventana señales 2026-08-03 -> 2026-09-02_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.34)
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
| TLT | 12.0% | core | 81.87 | -0.79% | -0.84% | -0.39% |
| RSG | 10.3% | satellite | 223.29 | 1.07% | 0.09% | 6.52% |
| GLD | 9.3% | core | 396.75 | -2.86% | -7.32% | 6.04% |
| IEF | 6.2% | core | 92.1 | -0.69% | -0.98% | -0.78% |
| KIDS | 5.4% | satellite | 23.0 | -1.33% | -8.26% | 10.21% |
| BILL | 4.2% | satellite | 47.62 | -3.27% | -1.12% | 0.85% |
| PESI | 2.9% | satellite | 17.84 | -1.71% | 9.45% | 6.32% |
| AUGO | 2.9% | satellite | 79.04 | -5.43% | -12.63% | 38.05% |
| AMRC | 2.5% | satellite | 22.6 | 2.17% | 7.77% | -0.57% |
| ASTS | 2.0% | satellite | 55.8 | -5.58% | -10.01% | -20.64% |
| SUJA | 1.8% | satellite | 10.43 | 3.57% | 11.79% | -8.51% |
| FGL | 1.5% | satellite | 17.23 | 13.36% | -17.87% | -79.99% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.1%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -5.0%
- Beta vs SPY: 0.755 · posiciones efectivas: 13.5 · HHI: 0.0743

**Por que estos satellite (señales WATCHDOG):**

- **RSG** · score agregado 479.6 · 7 señales · fuentes: corporate_insider
- **AUGO** · score agregado 259.2 · 4 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **ASTS** · score agregado 170.5 · 3 señales · fuentes: corporate_insider
- **PESI** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **AMRC** · score agregado 131.4 · 2 señales · fuentes: corporate_insider, large_holder
- **FGL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KIDS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **BILL** · score agregado 70.2 · 1 señales · fuentes: large_holder

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
| RSG | 71 | corporate_insider | CASCADE INVESTMENT, L.L.C | 0 | $34,513,978 | - |
| LIEN | 71 | corporate_insider | Colonna Bernardino | 2 | $7,685 | cluster_buy,small_amount |
| RSG | 71 | corporate_insider | CASCADE INVESTMENT, L.L.C | 0 | $27,377,581 | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ACT | 59 | corporate_insider | Genworth Holdings, Inc. | $33,953,773 | - |
| TMQ | 58 | corporate_insider | South32 Ltd | $17,827,787 | - |
| CAT | 57 | corporate_insider | Creed Joseph E | $4,953,460 | - |
| CRNX | 56 | corporate_insider | Struthers Richard Scott | $21,083,655 | - |
| CAT | 56 | corporate_insider | Creed Joseph E | $4,084,946 | - |
| CAT | 56 | corporate_insider | Creed Joseph E | $3,931,081 | - |
| TYL | 56 | corporate_insider | MOORE H LYNN JR | $3,448,280 | - |
| ABNB | 56 | corporate_insider | Blecharczyk Nathan | $8,617,143 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 761.78 (-0.69% / -0.54% / -1.24%) [2026-09-01]
- QQQ: 707.64 (-1.27% / -0.43% / -2.24%) [2026-09-01]
- IWM: 290.57 (-1.14% / -2.48% / -1.91%) [2026-09-01]
- DIA: 527.75 (-0.72% / -1.11% / -0.57%) [2026-09-01]
- TLT: 81.87 (-0.79% / -0.84% / -0.39%) [2026-09-01]
- IEF: 92.1 (-0.69% / -0.98% / -0.78%) [2026-09-01]
- GLD: 396.75 (-2.86% / -7.32% / 6.04%) [2026-09-01]
- ^VIX: 16.34 (9.52% / 3.09% / 3.03%) [2026-09-01]
- BTC-USD: 77277.17 (-1.62% / -3.71% / 21.88%) [2026-09-02]

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

**Temas dominantes**: stock (3), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ABNB] Airbnb announces Pepijn Rijvers as Chief Business Officer (2026-09-01)
- [AUGO] Insider Selling : Aura Minerals ( NASDAQ : AUGO ) CFO Sells $635 , 672 . 08 in Stock (2026-08-20)
- [AUGO] Aura Minerals ( NASDAQ : AUGO ) Director Mauad Bruno Sousa Sells 280 , 000 Shares of Stock (2026-08-20)
- [AUGO] Aura Minerals ( TSE : ORA ) Share Price Passes Above 200 Day Moving Average – Should You Sell ? (2026-08-19)
- [AUGO] Aura Minerals ( NASDAQ : AUGO ) COO Sells 1 , 400 Shares of Stock (2026-08-19)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Senior Loan Trust por $44.0M el 2026-08-31.
- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $34.5M el 2026-08-31.
- 10% owner Manufacturers Life Insurance Co (Bermuda Branch) compro John Hancock GA Senior Loan Trust por $23.0M el 2026-08-31.
- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $27.4M el 2026-08-28.
- CEO Struthers Richard Scott vendio CRNX por $21.1M el 2026-09-01.
- 10% owner Genworth Holdings, Inc. vendio ACT por $34.0M el 2026-08-31.
- CEO Savi Luca compro ITT por $1.0M el 2026-08-31.
- 10% owner South32 Ltd vendio TMQ por $17.8M el 2026-08-28 [senal en multiples fuentes].

**Polymarket — smart money (traders con mejor track record):**

- TAIWANNUMBERONE · PnL $115,162 · win rate 92% · categorias: sports, politics
- ExplosiveNinja · PnL $37,992 · win rate 97% · categorias: sports
- c4a759e5c9350491AF61646f2c4A46 · PnL $24,357 · win rate 99% · categorias: sports, crypto
- asd147 · PnL $22,323 · win rate 99% · categorias: sports, crypto, politics
- RJW1 · PnL $22,133 · win rate 98% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 596 registros 30d · ultimo dato 2026-09-01
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-01
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMRC, ASTS, AUGO, BILL, FGL, GLD, IEF, KIDS, PESI, QQQ, RSG, SPY, SUJA, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
