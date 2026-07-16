# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-16T06:46:45+00:00 · ventana señales 2026-06-16 -> 2026-07-16_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.67)
- Tendencia: `bull` (SPY 754.81 · MA50 742.11 · MA200 692.54 · dist MA200: 8.99%)
- Credito: `tight` (HY spread 2.72)
- Tipos: `flat` (curva 10y-2y 0.42)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 754.81 | 0.4% | 1.26% | 0.25% |
| QQQ | 12.0% | core | 717.74 | -0.27% | 0.89% | -3.42% |
| TLT | 12.0% | core | 84.24 | 0.19% | -0.14% | -1.36% |
| ECAT | 10.4% | satellite | 15.65 | 0.19% | 1.66% | 3.24% |
| GLD | 9.3% | core | 372.35 | 0.05% | -0.56% | -6.1% |
| PB | 6.9% | satellite | 72.49 | -0.01% | 2.92% | 1.87% |
| BEP | 6.3% | satellite | 32.52 | 1.28% | -2.58% | -6.09% |
| IEF | 6.2% | core | 93.78 | 0.25% | 0.29% | -0.2% |
| HQY | 4.4% | satellite | 95.07 | 0.6% | 0.36% | 9.31% |
| ENR | 3.6% | satellite | 20.69 | 1.37% | 3.04% | 2.78% |
| LUNR | 1.2% | satellite | 14.85 | -0.4% | -12.75% | -42.35% |
| BOT | 0.7% | satellite | 31.59 | -13.95% | -5.31% | -17.02% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.2%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -2.9%
- Beta vs SPY: 0.623 · posiciones efectivas: 12.7 · HHI: 0.0788

**Por que estos satellite (señales WATCHDOG):**

- **ENR** · score agregado 307.6 · 5 señales · fuentes: corporate_insider
- **HQY** · score agregado 73.0 · 1 señales · fuentes: large_holder
- **LUNR** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PB** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BOT** · score agregado 70.5 · 1 señales · fuentes: corporate_insider
- **ECAT** · score agregado 59.3 · 1 señales · fuentes: corporate_insider
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| HQY | 73 | large_holder | Wasatch Advisors LP |  | - | - |
| RDGL | 72 | corporate_insider | Korenko Michael K | 2 | $11,420 | cluster_buy,small_amount |
| SERA | 72 | large_holder | Aberdeen Group plc |  | - | - |
| FULC | 72 | large_holder | TANG CAPITAL MANAGEMENT,  |  | - | - |
| LUNR | 72 | large_holder | BANK OF NOVA SCOTIA |  | - | - |
| VOYG | 72 | large_holder | BANK OF NOVA SCOTIA |  | - | - |
| EEX | 72 | large_holder | Onex Corporation |  | - | - |
| FIVN | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| TRC | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| PB | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| AOSL | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| BOT | 70 | corporate_insider | Kang Andrew Kai | 0 | $9,999,988 | - |
| RYAM | 70 | large_holder | Lightship Capital III LP |  | - | - |
| ATPC | 70 | large_holder | JANE STREET GROUP, LLC |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| META | 64 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| MSFT | 64 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 754.81 (0.4% / 1.26% / 0.25%) [2026-07-15]
- QQQ: 717.74 (-0.27% / 0.89% / -3.42%) [2026-07-15]
- IWM: 295.77 (0.43% / 0.78% / 0.38%) [2026-07-15]
- DIA: 525.95 (0.24% / 0.61% / 1.73%) [2026-07-15]
- TLT: 84.24 (0.19% / -0.14% / -1.36%) [2026-07-15]
- IEF: 93.78 (0.25% / 0.29% / -0.2%) [2026-07-15]
- GLD: 372.35 (0.05% / -0.56% / -6.1%) [2026-07-15]
- ^VIX: 15.67 (-5.03% / -7.28% / -3.27%) [2026-07-15]
- BTC-USD: 64645.98 (-0.1% / 1.32% / 7.71%) [2026-07-16]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.18 (delta 1m: 0.13) [2026-07-14]
- Treasury 10Y yield: 4.58 (delta 1m: 0.13) [2026-07-14]
- Curva 10Y-2Y: 0.42 (delta 1m: 0.03) [2026-07-15]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.72 (delta 1m: 0.06) [2026-07-14]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.23 (delta 1m: -0.08) [2026-07-15]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (6), leadership (3), merger (2), regulatory (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [NUVL] GSK completes acquisition of Nuvalent , Inc | Company Announcement (2026-07-15)
- [BLLN] BillionToOne to Report Second Quarter 2026 Financial Results on August 5 , 2026 (2026-07-15)
- [BLLN] Billiontoone , Inc . $BLLN Shares Bought by Emerald Mutual Fund Advisers Trust (2026-07-14)
- [TTAN] ServiceTitan Inc . $TTAN Shares Sold by Hsbc Holdings PLC (2026-07-14)
- [BLLN] Insider Selling : Billiontoone ( NASDAQ : BLLN ) CEO Sells $1 , 576 , 250 . 00 in Stock (2026-07-13)
- [WSR] Whitestone REIT Shareholders Approve AREG Merger , Reject Executive Pay Plan (2026-07-13)
- [BLLN] A BillionToOne Insider Sold 801 Shares as Revenue Jumped 84 % (2026-07-13)
- [TTAN] ServiceTitan ( TTAN ): Best Up and Coming Tech Stocks to Buy Now (2026-07-11)
- [BLLN] Billiontoone ( NASDAQ : BLLN ) CEO Oguzhan Atay Sells 26 , 250 Shares of Stock (2026-07-09)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Kang Andrew Kai compro BOT por $10.0M el 2026-07-14.
- CEO Porter James Richard opero NUVL por $25.2M el 2026-07-15.
- CEO Zaslav David vendio WBD por $56.9M el 2026-07-13.
- CEO Holeman David K vendio WSR por $22.1M el 2026-07-14.
- CEO Ullal Jayshree vendio ANET por $30.1M el 2026-07-10.
- CEO Mastandrea Christine J vendio WSR por $13.7M el 2026-07-14.
- CEO McLaughlin Edward Grunde opero MA por $4.5M el 2026-07-15 [senal en multiples fuentes].
- CEO Pomel Olivier vendio DDOG por $10.8M el 2026-07-13.

**Polymarket — smart money (traders con mejor track record):**

- Kingdmandan · PnL $47,027 · win rate 97% · categorias: sports
- 0x0x23kjookhaiuohduoayh8c9 · PnL $17,175 · win rate 93% · categorias: sports, crypto
- ic4cream · PnL $31,771 · win rate 88% · categorias: sports
- 0x2c335066FE58fe9237c3d3Dc7b275C2a034a0563-1759935795465 · PnL $81,783 · win rate 74% · categorias: sports, politics, crypto
- alexfire97 · PnL $7,682 · win rate 84% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 33 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 731 registros 30d · ultimo dato 2026-07-15
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-15
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BOT, ECAT, ENR, GLD, HQY, IEF, LUNR, PB, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
