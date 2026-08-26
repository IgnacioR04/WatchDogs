# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-26T19:42:09+00:00 · ventana señales 2026-07-27 -> 2026-08-26_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.31)
- Tendencia: `bull` (SPY 766.68 · MA50 752.91 · MA200 706.43 · dist MA200: 8.53%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 766.68 | 0.1% | -0.31% | 5.1% |
| QQQ | 12.0% | core | 712.04 | 0.19% | -0.56% | 7.6% |
| TLT | 12.0% | core | 83.22 | -0.29% | 0.25% | 0.86% |
| GLD | 9.3% | core | 421.63 | -1.5% | 1.88% | 13.62% |
| BWFG | 9.3% | satellite | 65.9 | 0.23% | 0.4% | -2.88% |
| MED | 7.0% | satellite | 12.3 | 1.15% | 6.22% | 27.59% |
| IEF | 6.2% | core | 93.29 | -0.24% | -0.1% | 0.47% |
| CHTR | 4.8% | satellite | 154.84 | -0.19% | 1.55% | 6.64% |
| MAIR | 4.0% | satellite | 28.34 | 1.25% | 1.0% | -10.43% |
| AMR | 3.9% | satellite | 216.72 | 0.51% | 11.47% | 55.73% |
| PRE | 2.6% | satellite | 25.47 | 9.53% | 35.74% | 41.32% |
| CBRS | 1.9% | satellite | 182.98 | -0.51% | -15.17% | 8.02% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.8%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.8%
- Max drawdown historico: -5.5%
- Beta vs SPY: 0.756 · posiciones efectivas: 13.2 · HHI: 0.0758

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **MED** · score agregado 126.8 · 2 señales · fuentes: corporate_insider, large_holder
- **PRE** · score agregado 122.2 · 2 señales · fuentes: corporate_insider
- **AMR** · score agregado 120.3 · 2 señales · fuentes: corporate_insider
- **BWFG** · score agregado 110.3 · 2 señales · fuentes: corporate_insider
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **MAIR** · score agregado 60.2 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| TISI | 77 | corporate_insider | Roeder Clinton William | 2 | $183,200 | cluster_buy |
| TISI | 72 | corporate_insider | Roeder Clinton William | 2 | $22,840 | cluster_buy,small_amount |
| LFT | 72 | corporate_insider | Flynn James Peter | 2 | $13,642 | cluster_buy,small_amount |
| VTMX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CHY | 72 | large_holder | THRIVENT FINANCIAL FOR LU |  | - | - |
| CCD | 72 | large_holder | THRIVENT FINANCIAL FOR LU |  | - | - |
| CHI | 72 | large_holder | THRIVENT FINANCIAL FOR LU |  | - | - |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| MED | 72 | large_holder | Steamboat Capital Partner |  | - | - |
| CDTG | 72 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| LFT | 71 | corporate_insider | BRIGGS JAMES A | 2 | $13,798 | cluster_buy,small_amount |
| HKHC | 71 | corporate_insider | Rosenthal Brent D | 2 | $54,000 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $45,800 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $46,300 | cluster_buy |
| LFT | 71 | corporate_insider | Flynn James Peter | 2 | $6,825 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| CBRS | 59 | corporate_insider | Feldman Andrew D. | $13,203,021 | - |
| CBRS | 58 | corporate_insider | Feldman Andrew D. | $8,545,099 | - |
| LASR | 57 | corporate_insider | Keeney Scott H | $6,825,002 | - |
| CBRS | 57 | corporate_insider | Feldman Andrew D. | $6,719,365 | - |
| CBRS | 57 | corporate_insider | Feldman Andrew D. | $6,512,988 | - |
| HCC | 57 | corporate_insider | SCHELLER WALTER J | $5,500,000 | - |
| LASR | 57 | corporate_insider | Keeney Scott H | $5,302,960 | - |
| MU | 57 | corporate_insider | MEHROTRA SANJAY | $5,082,623 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 766.68 (0.1% / -0.31% / 5.1%) [2026-08-26]
- QQQ: 712.04 (0.19% / -0.56% / 7.6%) [2026-08-26]
- IWM: 299.01 (-0.07% / -0.9% / 3.62%) [2026-08-26]
- DIA: 534.54 (-0.13% / 0.13% / 3.8%) [2026-08-26]
- TLT: 83.22 (-0.29% / 0.25% / 0.86%) [2026-08-26]
- IEF: 93.29 (-0.24% / -0.1% / 0.47%) [2026-08-26]
- GLD: 421.63 (-1.5% / 1.88% / 13.62%) [2026-08-26]
- ^VIX: 15.31 (-0.91% / 2.82% / -25.9%) [2026-08-26]
- BTC-USD: 78412.81 (-0.19% / 0.1% / 22.02%) [2026-08-26]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.24 (delta 1m: -0.09) [2026-08-24]
- Treasury 10Y yield: 4.7 (delta 1m: 0.01) [2026-08-24]
- Curva 10Y-2Y: 0.47 (delta 1m: 0.13) [2026-08-25]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.11) [2026-08-25]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.32 (delta 1m: 0.11) [2026-08-25]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (5), earnings (2), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TPR] The Bayeux tapestry lesser - known tale of bromance : William and Harold were friends before they were enemies (2026-08-26)
- [TENB] Tenable ( NASDAQ : TENB ) Stock Price Down 3 . 9 % – Time to Sell ? (2026-08-25)
- [CBRS] As Cerebras Launches a New , Record - Setting AI Accelerator , Here How You Should Play CBRS Stock (2026-08-25)
- [CBRS] Cerebras Systems ( CBRS ) Revenue Surges : Why Did CBRS Stock Crash , and What About AMD ? (2026-08-24)
- [LQDT] Liquidity Services to Present and Host 1x1 Investor Meetings at the 17th Annual Midwest IDEAS Investor Conference on August 26th in Chicago , IL (2026-08-21)
- [KE] Kimball Electronics ( KE ) Q4 2026 Earnings Call Transcript (2026-08-21)
- [LQDT] Liquidity Services ( NASDAQ : LQDT ) Upgraded at Wall Street Zen (2026-08-19)
- [KE] Kimball Electronics ( NASDAQ : KE ) Stock Price Down 10 . 2 % – What Next ? (2026-08-18)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Host-Plus Pty Ltd as trustee for the HOSTPLUS Pooled Superannuation Trust compro EBR Systems, Inc. por $20.8M el 2026-08-21.
- CEO Feldman Andrew D. vendio CBRS por $13.2M el 2026-08-21 [senal en multiples fuentes].
- CEO Keeney Scott H vendio LASR por $6.8M el 2026-08-24.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- SPCEXBUYER · PnL $175,377 · win rate 92% · categorias: sports
- ExplosiveNinja · PnL $68,930 · win rate 97% · categorias: sports
- Donghui · PnL $44,174 · win rate 92% · categorias: sports
- comon119 · PnL $21,860 · win rate 97% · categorias: sports, crypto
- BreakTheBank · PnL $78,249 · win rate 85% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 645 registros 30d · ultimo dato 2026-08-26
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-26
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMR, BWFG, CBRS, CHTR, GLD, IEF, MAIR, MED, PRE, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
