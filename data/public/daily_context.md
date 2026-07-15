# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-15T14:25:27+00:00 · ventana señales 2026-06-15 -> 2026-07-15_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.99)
- Tendencia: `bull` (SPY 753.36 · MA50 741.43 · MA200 692.04 · dist MA200: 8.86%)
- Credito: `tight` (HY spread 2.72)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 753.36 | 0.56% | 0.76% | 1.83% |
| QQQ | 12.0% | core | 716.57 | 0.68% | 1.01% | -0.55% |
| TLT | 12.0% | core | 84.22 | 0.3% | -0.39% | -1.44% |
| GLD | 9.3% | core | 372.14 | 1.36% | -1.42% | -3.73% |
| BEP | 6.7% | satellite | 32.5 | 2.01% | -1.31% | -5.3% |
| IEF | 6.2% | core | 93.71 | 0.44% | 0.01% | -0.18% |
| NMM | 4.9% | satellite | 74.05 | -1.8% | -1.5% | -1.65% |
| NVRI | 4.2% | satellite | 22.88 | -0.17% | 1.55% | 7.17% |
| SHOE | 4.1% | satellite | 14.63 | -4.88% | -3.11% | -14.81% |
| ETSY | 4.0% | satellite | 86.07 | 3.62% | 11.49% | 19.23% |
| RYAM | 3.5% | satellite | 7.78 | 7.61% | 7.61% | -14.32% |
| NTSK | 2.4% | satellite | 14.62 | 2.45% | 22.65% | 65.95% |
| INTC | 2.1% | satellite | 103.01 | -0.11% | -6.69% | -17.31% |
| ARTV | 1.5% | satellite | 9.43 | 0.86% | 1.29% | 2.72% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.7%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.8%
- Max drawdown historico: -5.6%
- Beta vs SPY: 0.822 · posiciones efectivas: 14.2 · HHI: 0.0702

**Por que estos satellite (señales WATCHDOG):**

- **NTSK** · score agregado 321.8 · 4 señales · fuentes: corporate_insider
- **NMM** · score agregado 174.3 · 3 señales · fuentes: corporate_insider
- **RYAM** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **NVRI** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **SHOE** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **ARTV** · score agregado 116.5 · 2 señales · fuentes: corporate_insider
- **ETSY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NTSK | 82 | corporate_insider | Griffith William J.G. | 2 | $2,961,151 | cluster_buy |
| NTSK | 82 | corporate_insider | ICONIQ Strategic Partners | 2 | $2,961,151 | cluster_buy |
| NTSK | 79 | corporate_insider | Griffith William J.G. | 2 | $804,546 | cluster_buy |
| NTSK | 79 | corporate_insider | ICONIQ Strategic Partners | 2 | $804,546 | cluster_buy |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| EEX | 72 | large_holder | Onex Corporation |  | - | - |
| TRC | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| ETSY | 72 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| RYAM | 70 | large_holder | Lightship Capital III LP |  | - | - |
| HOFT | 70 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |
| GLOB | 70 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |
| SCSC | 70 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |
| XAIR | 70 | large_holder | Lin Yi-Chien |  | - | - |
| AIBZ | 70 | large_holder | Bakhashwain Mohammed |  | - | - |

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

- SPY: 753.36 (0.56% / 0.76% / 1.83%) [2026-07-15]
- QQQ: 716.57 (0.68% / 1.01% / -0.55%) [2026-07-15]
- IWM: 295.6 (0.72% / -0.2% / 1.14%) [2026-07-15]
- DIA: 526.49 (0.39% / -0.37% / 2.9%) [2026-07-15]
- TLT: 84.22 (0.3% / -0.39% / -1.44%) [2026-07-15]
- IEF: 93.71 (0.44% / 0.01% / -0.18%) [2026-07-15]
- GLD: 372.14 (1.36% / -1.42% / -3.73%) [2026-07-15]
- ^VIX: 15.99 (-6.82% / -0.87% / -9.56%) [2026-07-15]
- BTC-USD: 65158.97 (0.31% / 1.61% / 9.1%) [2026-07-15]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.26 (delta 1m: 0.13) [2026-07-13]
- Treasury 10Y yield: 4.62 (delta 1m: 0.07) [2026-07-13]
- Curva 10Y-2Y: 0.4 (delta 1m: 0.0) [2026-07-14]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.72 (delta 1m: 0.06) [2026-07-14]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: -0.04) [2026-07-14]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (6), ai (4), earnings (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [LQDA] Liquidia ( NASDAQ : LQDA ) Insider Rajeev Saggar Sells 9 , 926 Shares (2026-07-15)
- [LQDA] Archer Investment Corp Makes New Investment in Liquidia Corporation $LQDA (2026-07-15)
- [LQDA] Liquidia ( NASDAQ : LQDA ) Trading Up 8 % – Should You Buy ? (2026-07-14)
- [RBRK] Rubrik ( RBRK ) Stock Could Be Pricey Despite $500 Million united kingdom Expansion (2026-07-14)
- [KFY] Ross Steelman claims first Korn Ferry Tour title with Blue Championship victory (2026-07-13)
- [RBRK] Rubrik Stock Flirts With Buy Point Amid Path To Profitability | Investor Business Daily (2026-07-13)
- [KFY] Ross Steelman claims first Korn Ferry Tour title with Blue Championship victory (2026-07-13)
- [RBRK] Cybersecurity giant Rubrik bets big on united kingdom with $500 million investment | Indiablooms - First Portal on Digital News Management (2026-07-12)
- [RBRK] Rubrik ( RBRK ) is One of the Best Up and Coming Stocks to Invest In Right Now , Here Why (2026-07-12)
- [RBRK] Rubrik ( RBRK ) is One of the Best Up and Coming Stocks to Invest In Right Now , Here Why (2026-07-12)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Ullal Jayshree vendio ANET por $30.1M el 2026-07-10.
- Director Chang Hung Pen opero ASX por $123.3M el 2026-07-13.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.
- Institutional manager Geode Capital Management LLC compro JPMORGAN CHASE & CO por $13.1B.
- Institutional manager Goldman Sachs Group Inc vendio META PLATFORMS INC por $7.2B.

**Polymarket — smart money (traders con mejor track record):**

- 0xe11Ff8cd2718F51a4d9403D166c20eaAAbE253F4-1777047101622 · PnL $85,321 · win rate 88% · categorias: sports
- JnStTrdrBnusFnd · PnL $49,305 · win rate 91% · categorias: crypto
- CORGI8 · PnL $48,011 · win rate 91% · categorias: sports
- epend · PnL $38,863 · win rate 91% · categorias: sports
- esportGG · PnL $15,322 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 63 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 542 registros 30d · ultimo dato 2026-07-15
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-15
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ARTV, BEP, ETSY, GLD, IEF, INTC, NMM, NTSK, NVRI, QQQ, RYAM, SHOE, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
