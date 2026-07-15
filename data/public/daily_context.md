# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-15T19:54:16+00:00 · ventana señales 2026-06-15 -> 2026-07-15_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.79)
- Tendencia: `bull` (SPY 754.09 · MA50 742.1 · MA200 692.54 · dist MA200: 8.89%)
- Credito: `tight` (HY spread 2.72)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 754.09 | 0.3% | 1.17% | 0.16% |
| QQQ | 12.0% | core | 717.1 | -0.36% | 0.8% | -3.51% |
| TLT | 12.0% | core | 84.29 | 0.25% | -0.09% | -1.31% |
| ECAT | 9.4% | satellite | 15.67 | -1.38% | 0.06% | 1.62% |
| GLD | 9.3% | core | 371.96 | -0.05% | -0.66% | -6.2% |
| IEF | 6.2% | core | 93.79 | 0.26% | 0.3% | -0.19% |
| BEP | 5.5% | satellite | 32.49 | 1.17% | -2.68% | -6.19% |
| NMM | 4.0% | satellite | 75.13 | 0.82% | -0.91% | 0.95% |
| ENR | 3.4% | satellite | 20.75 | 1.69% | 3.36% | 3.1% |
| ETSY | 3.2% | satellite | 85.49 | 2.92% | 10.73% | 18.42% |
| RYAM | 2.9% | satellite | 7.61 | 5.33% | 5.33% | -16.13% |
| NTSK | 2.0% | satellite | 13.16 | -7.74% | 10.44% | 49.43% |
| INTC | 1.7% | satellite | 103.25 | -4.18% | -6.34% | -19.24% |
| ARTV | 1.3% | satellite | 9.75 | 4.28% | 4.73% | 6.21% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.8%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -5.5%
- Beta vs SPY: 0.794 · posiciones efectivas: 13.7 · HHI: 0.0732

**Por que estos satellite (señales WATCHDOG):**

- **NTSK** · score agregado 321.8 · 4 señales · fuentes: corporate_insider
- **ENR** · score agregado 307.6 · 5 señales · fuentes: corporate_insider
- **NMM** · score agregado 174.3 · 3 señales · fuentes: corporate_insider
- **RYAM** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **ARTV** · score agregado 116.5 · 2 señales · fuentes: corporate_insider
- **ETSY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **ECAT** · score agregado 59.3 · 1 señales · fuentes: corporate_insider
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NTSK | 82 | corporate_insider | Griffith William J.G. | 2 | $2,961,151 | cluster_buy |
| NTSK | 82 | corporate_insider | ICONIQ Strategic Partners | 2 | $2,961,151 | cluster_buy |
| NTSK | 79 | corporate_insider | Griffith William J.G. | 2 | $804,546 | cluster_buy |
| NTSK | 79 | corporate_insider | ICONIQ Strategic Partners | 2 | $804,546 | cluster_buy |
| RDGL | 72 | corporate_insider | Korenko Michael K | 2 | $11,420 | cluster_buy,small_amount |
| SERA | 72 | large_holder | Aberdeen Group plc |  | - | - |
| VOYG | 72 | large_holder | BANK OF NOVA SCOTIA |  | - | - |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| EEX | 72 | large_holder | Onex Corporation |  | - | - |
| TRC | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| ETSY | 72 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| RYAM | 70 | large_holder | Lightship Capital III LP |  | - | - |
| PRQR | 70 | large_holder | STICHTING AESCAP LIFE SCI |  | - | - |
| MGA | 70 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |

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

- SPY: 754.09 (0.3% / 1.17% / 0.16%) [2026-07-15]
- QQQ: 717.1 (-0.36% / 0.8% / -3.51%) [2026-07-15]
- IWM: 295.54 (0.35% / 0.7% / 0.3%) [2026-07-15]
- DIA: 525.76 (0.2% / 0.57% / 1.69%) [2026-07-15]
- TLT: 84.29 (0.25% / -0.09% / -1.31%) [2026-07-15]
- IEF: 93.79 (0.26% / 0.3% / -0.19%) [2026-07-15]
- GLD: 371.96 (-0.05% / -0.66% / -6.2%) [2026-07-15]
- ^VIX: 15.79 (-4.3% / -6.57% / -2.53%) [2026-07-15]
- BTC-USD: 64912.24 (-0.07% / 1.22% / 8.69%) [2026-07-15]

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

**Temas dominantes**: ai (5), stock (5), earnings (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TSEM] Tower Semiconductor announces $3bn manufacturing expansion in Japan (2026-07-15)
- [TSEM] Katamaran Capital LLP Reduces Position in Tower Semiconductor Ltd . $TSEM (2026-07-15)
- [TSEM] Japan to Provide Up to 159 Billion Yen in Subsidies to Tower Semiconductor (2026-07-15)
- [TSEM] Tower Semiconductor to invest $3 bn in Japan , backed by government grants , for capacity expansion (2026-07-15)
- [RBRK] Rubrik ( RBRK ) Stock Could Be Pricey Despite $500 Million united kingdom Expansion (2026-07-14)
- [RBRK] Rubrik Stock Flirts With Buy Point Amid Path To Profitability | Investor Business Daily (2026-07-13)
- [RBRK] Cybersecurity giant Rubrik bets big on united kingdom with $500 million investment | Indiablooms - First Portal on Digital News Management (2026-07-12)
- [RBRK] Rubrik ( RBRK ) is One of the Best Up and Coming Stocks to Invest In Right Now , Here Why (2026-07-12)
- [RBRK] Rubrik ( RBRK ) is One of the Best Up and Coming Stocks to Invest In Right Now , Here Why (2026-07-12)
- [STZ] Constellation Brands : Beer Growth and Buybacks Mask Stock Slump (2026-07-10)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Ullal Jayshree vendio ANET por $30.1M el 2026-07-10.
- Director Chang Hung Pen opero ASX por $123.3M el 2026-07-13.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.
- Institutional manager Geode Capital Management LLC compro JPMORGAN CHASE & CO por $13.1B.
- Institutional manager Invesco Ltd compro WALMART INC WMT por $12.7B.

**Polymarket — smart money (traders con mejor track record):**

- 111111111115 · PnL $204,568 · win rate 98% · categorias: sports
- 0xe11Ff8cd2718F51a4d9403D166c20eaAAbE253F4-1777047101622 · PnL $126,171 · win rate 88% · categorias: sports
- JnStTrdrBnusFnd · PnL $83,155 · win rate 91% · categorias: crypto
- 0xf3ce7f04 · PnL $25,742 · win rate 95% · categorias: sports
- Dota2winner · PnL $26,634 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 63 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 500 registros 30d · ultimo dato 2026-07-15
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-15
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ARTV, BEP, ECAT, ENR, ETSY, GLD, IEF, INTC, NMM, NTSK, QQQ, RYAM, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
