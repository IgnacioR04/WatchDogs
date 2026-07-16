# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-16T17:01:27+00:00 · ventana señales 2026-06-16 -> 2026-07-16_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.35)
- Tendencia: `bull` (SPY 752.94 · MA50 742.85 · MA200 693.03 · dist MA200: 8.65%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.42)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 752.94 | -0.25% | 0.16% | 0.61% |
| QQQ | 12.0% | core | 709.0 | -1.22% | -1.97% | -2.75% |
| TLT | 12.0% | core | 84.07 | -0.2% | -0.5% | -2.1% |
| GLD | 9.3% | core | 366.28 | -1.63% | -3.15% | -7.88% |
| ECAT | 8.8% | satellite | 15.62 | -0.19% | 0.82% | 3.04% |
| IEF | 6.2% | core | 93.65 | -0.14% | -0.06% | -0.59% |
| PB | 5.9% | satellite | 74.61 | 2.92% | 4.35% | 4.2% |
| BEP | 5.3% | satellite | 31.69 | -2.54% | -3.9% | -7.54% |
| HQY | 3.7% | satellite | 98.7 | 3.82% | 4.1% | 15.22% |
| ENR | 3.1% | satellite | 20.83 | 0.68% | 3.07% | 2.21% |
| OSK | 3.0% | satellite | 147.38 | 1.26% | 3.23% | 6.72% |
| FIVN | 2.0% | satellite | 25.06 | 0.8% | 0.52% | 21.15% |
| LUNR | 1.1% | satellite | 13.68 | -7.88% | -19.05% | -41.44% |
| BOT | 0.6% | satellite | 30.1 | -4.72% | -10.5% | -7.33% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.6%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -3.2%
- Beta vs SPY: 0.648 · posiciones efectivas: 13.6 · HHI: 0.0737

**Por que estos satellite (señales WATCHDOG):**

- **ENR** · score agregado 307.6 · 5 señales · fuentes: corporate_insider
- **HQY** · score agregado 73.0 · 1 señales · fuentes: large_holder
- **LUNR** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **FIVN** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PB** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **OSK** · score agregado 71.8 · 1 señales · fuentes: large_holder
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
| MPWR | 72 | large_holder | Invesco Ltd. |  | - | - |
| LUNR | 72 | large_holder | BANK OF NOVA SCOTIA |  | - | - |
| VOYG | 72 | large_holder | BANK OF NOVA SCOTIA |  | - | - |
| FIVN | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| TRC | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| PB | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| OSK | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| AOSL | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| BOT | 70 | corporate_insider | Kang Andrew Kai | 0 | $9,999,988 | - |
| USCB | 70 | large_holder | Patriot Financial Partner |  | - | - |

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

- SPY: 752.94 (-0.25% / 0.16% / 0.61%) [2026-07-16]
- QQQ: 709.0 (-1.22% / -1.97% / -2.75%) [2026-07-16]
- IWM: 296.08 (0.11% / -0.39% / 1.37%) [2026-07-16]
- DIA: 526.45 (0.1% / 0.43% / 1.24%) [2026-07-16]
- TLT: 84.07 (-0.2% / -0.5% / -2.1%) [2026-07-16]
- IEF: 93.65 (-0.14% / -0.06% / -0.59%) [2026-07-16]
- GLD: 366.28 (-1.63% / -3.15% / -7.88%) [2026-07-16]
- ^VIX: 16.35 (4.34% / 3.22% / -0.37%) [2026-07-16]
- BTC-USD: 64456.4 (-0.4% / 1.03% / 7.4%) [2026-07-16]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.18 (delta 1m: 0.13) [2026-07-14]
- Treasury 10Y yield: 4.58 (delta 1m: 0.13) [2026-07-14]
- Curva 10Y-2Y: 0.42 (delta 1m: 0.03) [2026-07-15]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.71 (delta 1m: 0.0) [2026-07-15]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.23 (delta 1m: -0.08) [2026-07-15]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), regulatory (2), leadership (2), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [NET] Cloudflare uses eBPF to boost edge security & routing (2026-07-16)
- [BLLN] BillionToOne to Report Second Quarter 2026 Financial Results on August 5 , 2026 (2026-07-15)
- [BLLN] Billiontoone , Inc . $BLLN Shares Bought by Emerald Mutual Fund Advisers Trust (2026-07-14)
- [BLLN] Insider Selling : Billiontoone ( NASDAQ : BLLN ) CEO Sells $1 , 576 , 250 . 00 in Stock (2026-07-13)
- [BLLN] A BillionToOne Insider Sold 801 Shares as Revenue Jumped 84 % (2026-07-13)
- [BLLN] Billiontoone ( NASDAQ : BLLN ) CEO Oguzhan Atay Sells 26 , 250 Shares of Stock (2026-07-09)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Kang Andrew Kai compro BOT por $10.0M el 2026-07-14.
- CEO Porter James Richard opero NUVL por $25.2M el 2026-07-15.
- CEO Guo Li opero AIOS por $2.5B el 2026-07-14 [senal en multiples fuentes].
- CEO Zaslav David vendio WBD por $56.9M el 2026-07-13.
- CEO Holeman David K vendio WSR por $22.1M el 2026-07-14.
- CEO Mastandrea Christine J vendio WSR por $13.7M el 2026-07-14.
- CEO McLaughlin Edward Grunde opero MA por $4.5M el 2026-07-15 [senal en multiples fuentes].
- CEO Pomel Olivier vendio DDOG por $10.8M el 2026-07-13.

**Polymarket — smart money (traders con mejor track record):**

- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $258,874 · win rate 96% · categorias: sports
- Kingdmandan · PnL $48,422 · win rate 97% · categorias: sports
- matenghehe · PnL $38,609 · win rate 95% · categorias: sports, crypto
- comon119 · PnL $19,664 · win rate 99% · categorias: sports, crypto, politics
- esportGG · PnL $35,488 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 44 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 737 registros 30d · ultimo dato 2026-07-16
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-16
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BOT, ECAT, ENR, FIVN, GLD, HQY, IEF, LUNR, OSK, PB, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
