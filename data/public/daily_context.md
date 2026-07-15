# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-15T00:22:08+00:00 · ventana señales 2026-06-15 -> 2026-07-15_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.5)
- Tendencia: `bull` (SPY 751.83 · MA50 741.39 · MA200 692.03 · dist MA200: 8.64%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 751.83 | 0.36% | 0.55% | 1.62% |
| QQQ | 12.0% | core | 719.71 | 1.12% | 1.45% | -0.12% |
| TLT | 12.0% | core | 84.08 | 0.13% | -0.56% | -1.61% |
| BEP | 10.7% | satellite | 32.11 | 0.78% | -2.49% | -6.44% |
| GLD | 9.3% | core | 372.15 | 1.37% | -1.41% | -3.72% |
| NVRI | 6.7% | satellite | 22.55 | -1.61% | 0.09% | 5.62% |
| ETSY | 6.3% | satellite | 83.06 | 3.14% | 7.05% | 19.55% |
| IEF | 6.2% | core | 93.55 | 0.28% | -0.16% | -0.34% |
| NTSK | 3.9% | satellite | 14.27 | 11.48% | 18.42% | 57.85% |
| INTC | 3.3% | satellite | 107.76 | 4.5% | -2.38% | -13.49% |
| ARTV | 2.4% | satellite | 9.35 | 4.7% | -1.37% | 9.48% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 14.4%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.8%
- Max drawdown historico: -5.9%
- Beta vs SPY: 0.84 · posiciones efectivas: 12.7 · HHI: 0.079

**Por que estos satellite (señales WATCHDOG):**

- **NTSK** · score agregado 321.8 · 4 señales · fuentes: corporate_insider
- **NVRI** · score agregado 141.0 · 2 señales · fuentes: large_holder
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
| EEX | 72 | large_holder | Onex Corporation |  | - | - |
| TRC | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| ETSY | 72 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| XAIR | 70 | large_holder | Lin Yi-Chien |  | - | - |
| AIBZ | 70 | large_holder | Bakhashwain Mohammed |  | - | - |
| VYNE | 70 | large_holder | Zhang Xiaofan |  | - | - |
| RNTX | 70 | large_holder | Voss Value Master Fund, L |  | - | - |
| GENI | 70 | large_holder | Voss Value Master Fund, L |  | - | - |
| FIVN | 70 | large_holder | Voss Value Master Fund, L |  | - | - |
| CSR | 70 | large_holder | Voss Value Master Fund, L |  | - | - |

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

- SPY: 751.83 (0.36% / 0.55% / 1.62%) [2026-07-14]
- QQQ: 719.71 (1.12% / 1.45% / -0.12%) [2026-07-14]
- IWM: 294.51 (0.35% / -0.57% / 0.77%) [2026-07-14]
- DIA: 524.69 (0.04% / -0.71% / 2.55%) [2026-07-14]
- TLT: 84.08 (0.13% / -0.56% / -1.61%) [2026-07-14]
- IEF: 93.55 (0.28% / -0.16% / -0.34%) [2026-07-14]
- GLD: 372.15 (1.37% / -1.41% / -3.72%) [2026-07-14]
- ^VIX: 16.5 (-3.85% / 2.29% / -6.67%) [2026-07-14]
- BTC-USD: 64844.12 (4.19% / 2.61% / 6.31%) [2026-07-15]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.26 (delta 1m: 0.13) [2026-07-13]
- Treasury 10Y yield: 4.62 (delta 1m: 0.07) [2026-07-13]
- Curva 10Y-2Y: 0.4 (delta 1m: 0.0) [2026-07-14]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.69 (delta 1m: -0.02) [2026-07-13]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: -0.04) [2026-07-14]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (6), regulatory (2), leadership (1), earnings (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [RBRK] Rubrik ( RBRK ) Stock Could Be Pricey Despite $500 Million united kingdom Expansion (2026-07-14)
- [UTHR] Insider Selling : United Therapeutics ( NASDAQ : UTHR ) CEO Sells 9 , 500 Shares (2026-07-13)
- [RBRK] Rubrik Stock Flirts With Buy Point Amid Path To Profitability | Investor Business Daily (2026-07-13)
- [RBRK] Cybersecurity giant Rubrik bets big on united kingdom with $500 million investment | Indiablooms - First Portal on Digital News Management (2026-07-12)
- [RBRK] Rubrik ( RBRK ) is One of the Best Up and Coming Stocks to Invest In Right Now , Here Why (2026-07-12)
- [RBRK] Rubrik ( RBRK ) is One of the Best Up and Coming Stocks to Invest In Right Now , Here Why (2026-07-12)
- [UTHR] United Therapeutics ( UTHR ) Following FDA Approval Is The Stock Fully Valued (2026-07-11)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Ullal Jayshree vendio ANET por $30.1M el 2026-07-10.
- 10% owner Liberty Broadband Corp vendio CHTR por $17.7M el 2026-07-14.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.
- Institutional manager Geode Capital Management LLC compro JPMORGAN CHASE & CO por $13.1B.
- Institutional manager Goldman Sachs Group Inc vendio META PLATFORMS INC por $7.2B.

**Polymarket — smart money (traders con mejor track record):**

- Allezpapa · PnL $396,879 · win rate 99% · categorias: sports
- therighteousdog · PnL $562,823 · win rate 96% · categorias: sports
- GoldenAlpha168 · PnL $194,530 · win rate 100% · categorias: sports
- BreakTheBank · PnL $970,640 · win rate 86% · categorias: sports
- Kch-Temp · PnL $178,502 · win rate 95% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 63 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 533 registros 30d · ultimo dato 2026-07-14
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-14
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ARTV, BEP, ETSY, GLD, IEF, INTC, NTSK, NVRI, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
