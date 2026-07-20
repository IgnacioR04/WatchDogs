# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-20T18:36:36+00:00 · ventana señales 2026-06-20 -> 2026-07-20_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.74)
- Tendencia: `bull` (SPY 743.83 · MA50 743.47 · MA200 693.86 · dist MA200: 7.2%)
- Credito: `tight` (HY spread 2.73)
- Tipos: `flat` (curva 10y-2y 0.37)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 743.83 | 0.07% | -0.71% | -0.39% |
| QQQ | 12.0% | core | 699.12 | 0.55% | -1.77% | -5.5% |
| TLT | 12.0% | core | 83.85 | -0.8% | -0.15% | -2.99% |
| PNTG | 12.0% | satellite | 41.54 | -0.98% | 4.22% | 24.22% |
| BEP | 12.0% | satellite | 32.07 | 0.98% | 0.66% | -9.0% |
| GLD | 11.1% | core | 367.45 | -0.26% | 0.09% | -5.08% |
| IEF | 7.4% | core | 93.51 | -0.35% | 0.24% | -0.57% |
| MPWR | 6.6% | satellite | 1344.07 | 2.44% | 4.08% | -13.91% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.9%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -4.1%
- Beta vs SPY: 0.781 · posiciones efectivas: 10.6 · HHI: 0.094

**Por que estos satellite (señales WATCHDOG):**

- **MPWR** · score agregado 73.0 · 1 señales · fuentes: large_holder
- **PNTG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GABC | 73 | corporate_insider | Seger Andrew M | 5 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Ryan Christina M | 5 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | KELLY JASON M | 5 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Bawel Zachary W | 5 | $20,000 | cluster_buy,small_amount |
| MPWR | 73 | large_holder | Invesco Ltd. |  | - | - |
| GABC | 72 | corporate_insider | Stokes Ronnie R | 5 | $15,000 | cluster_buy,small_amount |
| KROS | 72 | large_holder | BlackRock Portfolio Manag |  | - | - |
| QNT | 72 | large_holder | BlackRock Portfolio Manag |  | - | - |
| PNTG | 72 | large_holder | Wasatch Advisors LP |  | - | - |
| MGA | 72 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |
| HQY | 72 | large_holder | Wasatch Advisors LP |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| LNBIX | 70 | corporate_insider | Lincoln Financial Investm | 0 | $25,000,000 | - |
| CBNA | 70 | large_holder | Hingham Institution for S |  | - | - |
| GCT | 70 | large_holder | Lei Wu |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 64 | congress | John McGuire | $15,000 | small_amount |
| ADBE | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| MGA | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| AMD | 61 | congress | Dan Newhouse | $15,000 | small_amount |
| GOOGL | 61 | congress | Dan Newhouse | $15,000 | small_amount |
| AMAT | 61 | congress | Dan Newhouse | $15,000 | small_amount |
| CSX | 61 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 743.83 (0.07% / -0.71% / -0.39%) [2026-07-20]
- QQQ: 699.12 (0.55% / -1.77% / -5.5%) [2026-07-20]
- IWM: 293.44 (-0.2% / -0.01% / -0.73%) [2026-07-20]
- DIA: 518.27 (-0.49% / -1.15% / 0.56%) [2026-07-20]
- TLT: 83.85 (-0.8% / -0.15% / -2.99%) [2026-07-20]
- IEF: 93.51 (-0.35% / 0.24% / -0.57%) [2026-07-20]
- GLD: 367.45 (-0.26% / 0.09% / -5.08%) [2026-07-20]
- ^VIX: 17.74 (-5.49% / 3.38% / 8.17%) [2026-07-20]
- BTC-USD: 65466.67 (1.2% / 1.17% / 11.8%) [2026-07-20]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.16 (delta 1m: 0.09) [2026-07-16]
- Treasury 10Y yield: 4.57 (delta 1m: 0.1) [2026-07-16]
- Curva 10Y-2Y: 0.37 (delta 1m: -0.01) [2026-07-17]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.73 (delta 1m: 0.07) [2026-07-17]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.24 (delta 1m: -0.05) [2026-07-17]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), ai (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [MPWR] Rep . Byron Donalds Sells Off Monolithic Power Systems , Inc . ( NASDAQ : MPWR ) Stock (2026-07-19)
- [MPWR] Monolithic Power Systems ( NASDAQ : MPWR ) Stock Unloaded Rep . Byron Donalds (2026-07-19)
- [MPWR] Monolithic Power Systems ( MPWR ) Stock Gets An AI Boost From IBM Spending Signals (2026-07-17)
- [SEZL] Sezzle Sees Unusually High Options Volume ( NASDAQ : SEZL ) (2026-07-15)
- [SEZL] Sezzle to Announce Second Quarter 2026 Results and Participate in Upcoming Investor Conferences (2026-07-14)
- [MPLT] Maplight Therapeutics ( NASDAQ : MPLT ) Sets New 1 - Year High – Time to Buy ? (2026-07-10)
- [MPLT] Research Analyst Recent Ratings Changes for Maplight Therapeutics ( MPLT ) (2026-07-09)
- [SEZL] Sezzle ( NASDAQ : SEZL ) CFO Lee Dickson Brading Sells 100 Shares (2026-07-09)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Manufacturers Life Insurance Co (Bermuda Branch) compro John Hancock GA Mortgage Trust por $36.6M el 2026-07-15.
- 10% owner Lincoln Financial Investments Corp compro LNBIX por $25.0M el 2026-07-16.
- 10% owner Manulife (International) Ltd compro John Hancock GA Mortgage Trust por $22.0M el 2026-07-15.
- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Mortgage Trust por $13.0M el 2026-07-15.
- CEO Huang Jack Jiajia compro COE por $3.7M el 2026-07-13.
- 10% owner Manulife (Singapore) Pte. Ltd. compro John Hancock GA Mortgage Trust por $7.0M el 2026-07-15.
- CEO BOUDREAUX GAIL compro ELV por $753K el 2026-07-17.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- Themsnw · PnL $193,330 · win rate 86% · categorias: sports, politics
- 111111111115 · PnL $20,429 · win rate 94% · categorias: sports
- Uniform123 · PnL $41,128 · win rate 88% · categorias: sports
- 78979879879879 · PnL $19,896 · win rate 86% · categorias: sports, politics
- Amit11111 · PnL $17,112 · win rate 88% · categorias: crypto, sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 72 registros 30d · ultimo dato 2026-07-10
- **sec_insiders**: `ok` · 753 registros 30d · ultimo dato 2026-07-20
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-20
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, GLD, IEF, MPWR, PNTG, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
