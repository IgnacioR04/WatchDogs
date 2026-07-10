# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-10T22:33:56+00:00 · ventana señales 2026-06-10 -> 2026-07-10_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.03)
- Tendencia: `bull` (SPY 754.95 · MA50 739.91 · MA200 691.09 · dist MA200: 9.24%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.35)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 754.95 | 0.43% | 1.37% | 4.34% |
| QQQ | 12.0% | core | 725.51 | 0.31% | 1.81% | 4.7% |
| TLT | 12.0% | core | 84.47 | -0.02% | -1.22% | -0.12% |
| BEP | 9.9% | satellite | 32.33 | -1.97% | -4.57% | -8.34% |
| GLD | 9.3% | core | 377.01 | -0.31% | -0.3% | 0.65% |
| AVO | 6.7% | satellite | 13.33 | -0.15% | 6.73% | 18.59% |
| IEF | 6.2% | core | 93.63 | -0.09% | -0.52% | 0.27% |
| TBRG | 5.7% | satellite | 26.24 | 0.04% | 0.23% | 1.04% |
| LION | 4.6% | satellite | 13.47 | -0.15% | -8.12% | -1.61% |
| CNXC | 3.5% | satellite | 22.2 | 5.87% | -5.93% | -13.79% |
| INTC | 3.1% | satellite | 109.84 | -2.4% | -8.73% | 2.62% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.6%
- VaR 95% 1d: 1.2% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -6.3%
- Beta vs SPY: 0.718 · posiciones efectivas: 12.9 · HHI: 0.0776

**Por que estos satellite (señales WATCHDOG):**

- **AVO** · score agregado 138.2 · 2 señales · fuentes: corporate_insider, large_holder
- **TBRG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **LION** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CNXC** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GLOO | 88 | corporate_insider | Beck Scott Arthur | 3 | $3,500,000 | cluster_buy |
| GLOO | 83 | corporate_insider | Green Derek Todd | 3 | $1,999,998 | cluster_buy |
| GLOO | 80 | corporate_insider | GELSINGER PATRICK P | 3 | $500,000 | cluster_buy |
| WRAP | 78 | corporate_insider | Cohen Scot | 2 | $230,288 | cluster_buy |
| FINS | 74 | corporate_insider | MetLife Investment Manage | 0 | $1,600,000,000,000,000 | - |
| WRAP | 73 | corporate_insider | Cohen Scot | 2 | $23,914 | cluster_buy,small_amount |
| WRAP | 73 | corporate_insider | SHULMAN JOHN D | 2 | $110,000 | cluster_buy |
| TBRG | 72 | large_holder | L6 Holdings Inc. |  | - | - |
| LION | 72 | large_holder | MHR INSTITUTIONAL PARTNER |  | - | - |
| WRAP | 72 | large_holder | NORRIS ELWOOD G |  | - | - |
| CAG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CNXC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| PHUN | 70 | large_holder | Goldenwise Capital Group  |  | - | - |
| EVGN | 70 | large_holder | L.I.A. Pure Capital Ltd. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| XOM | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| GE | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 754.95 (0.43% / 1.37% / 4.34%) [2026-07-10]
- QQQ: 725.51 (0.31% / 1.81% / 4.7%) [2026-07-10]
- IWM: 295.99 (-0.42% / -0.53% / 5.19%) [2026-07-10]
- DIA: 525.78 (0.3% / -0.4% / 5.39%) [2026-07-10]
- TLT: 84.47 (-0.02% / -1.22% / -0.12%) [2026-07-10]
- IEF: 93.63 (-0.09% / -0.52% / 0.27%) [2026-07-10]
- GLD: 377.01 (-0.31% / -0.3% / 0.65%) [2026-07-10]
- ^VIX: 15.03 (-5.11% / -6.93% / -32.36%) [2026-07-10]
- BTC-USD: 64104.04 (1.44% / 0.88% / -0.21%) [2026-07-10]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.16 (delta 1m: 0.01) [2026-07-09]
- Treasury 10Y yield: 4.54 (delta 1m: -0.02) [2026-07-09]
- Curva 10Y-2Y: 0.35 (delta 1m: -0.05) [2026-07-10]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.1) [2026-07-09]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.24 (delta 1m: -0.09) [2026-07-10]
- Dolar broad index: 120.6902 (delta 1m: 1.654) [2026-07-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (9), ai (5), leadership (3), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [SAIL] SailPoint ( NASDAQ : SAIL ) Shares Down 6 . 9 % on Insider Selling (2026-07-10)
- [CRWV] CoreWeave CEO Dumped Nearly 370 , 000 Shares for $30 . 8 Million . What Does That Mean for Investors ? (2026-07-10)
- [CRWV] CoreWeave CEO Sells Another $22 Million in Stock (2026-07-10)
- [IOT] Samsara ( NYSE : IOT ) Insider John Bicket Sells 17 , 975 Shares of Stock (2026-07-10)
- [SAIL] Insider Selling : SailPoint ( NASDAQ : SAIL ) CEO Sells $1 , 438 , 069 . 20 in Stock (2026-07-09)
- [SAIL] Insider Selling : SailPoint ( NASDAQ : SAIL ) CAO Sells 3 , 881 Shares of Stock (2026-07-09)
- [SAIL] Insider Selling : SailPoint ( NASDAQ : SAIL ) General Counsel Sells $291 , 283 . 80 in Stock (2026-07-09)
- [SAIL] Insider Selling : SailPoint ( NASDAQ : SAIL ) CFO Sells 46 , 002 Shares (2026-07-09)
- [AXON] Axon Enterprise , Inc $AXON Shares Sold by Swedbank AB (2026-07-09)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner MetLife Investment Management, LLC compro FINS por $1600000.0B el 2026-07-08.
- 10% owner Pinetree Capital Ltd. opero TBRG por $55.9M el 2026-07-09 [senal en multiples fuentes].
- 10% owner Globalharvest Holdings Venture Ltd compro AVO por $7.9M el 2026-07-09 [senal en multiples fuentes].
- CEO Beck Scott Arthur compro GLOO por $3.5M el 2026-07-10.
- 10% owner Endeavor Blockchain, LLC compro BGDE por $16.7M el 2026-06-30 [senal en multiples fuentes].
- CEO Fowler Christopher L vendio TBRG por $3.2M el 2026-07-09 [senal en multiples fuentes].
- Director Upitis Andris vendio TBRG por $29.2M el 2026-07-09 [senal en multiples fuentes].
- 10% owner AEROEQUITY GP, LLC opero YSS por $77.8M el 2026-07-08.

**Polymarket — smart money (traders con mejor track record):**

- Sassy-Bucket · PnL $392,530 · win rate 92% · categorias: sports
- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $182,208 · win rate 97% · categorias: sports
- shijiebeifacai · PnL $121,107 · win rate 97% · categorias: sports
- HongYunX · PnL $62,641 · win rate 100% · categorias: sports
- ramadamaramadam · PnL $619,365 · win rate 89% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 91 registros 30d · ultimo dato 2026-07-07
- **sec_insiders**: `ok` · 700 registros 30d · ultimo dato 2026-07-10
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-10
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AVO, BEP, CNXC, GLD, IEF, INTC, LION, QQQ, SPY, TBRG, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
