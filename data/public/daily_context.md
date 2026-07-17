# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-17T06:43:20+00:00 · ventana señales 2026-06-17 -> 2026-07-17_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.73)
- Tendencia: `bull` (SPY 750.72 · MA50 742.81 · MA200 693.01 · dist MA200: 8.33%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.41)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 750.72 | -0.54% | -0.13% | 0.31% |
| QQQ | 12.0% | core | 705.94 | -1.64% | -2.4% | -3.17% |
| TLT | 12.0% | core | 84.21 | -0.04% | -0.33% | -1.94% |
| BEP | 12.0% | satellite | 31.8 | -2.21% | -3.58% | -7.23% |
| GLD | 11.3% | core | 364.96 | -1.98% | -3.5% | -8.22% |
| MPWR | 10.0% | satellite | 1305.65 | -3.48% | -4.98% | -12.75% |
| CELC | 8.2% | satellite | 88.29 | -3.52% | -22.22% | 1.11% |
| IEF | 7.5% | core | 93.72 | -0.06% | 0.01% | -0.52% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 16.1%
- VaR 95% 1d: 1.5% · CVaR 95% 1d: 2.0%
- Max drawdown historico: -6.5%
- Beta vs SPY: 0.935 · posiciones efectivas: 10.8 · HHI: 0.0927

**Por que estos satellite (señales WATCHDOG):**

- **CELC** · score agregado 142.0 · 2 señales · fuentes: large_holder
- **MPWR** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| CRDF | 78 | corporate_insider | PACE GARY W | 2 | $1,000,000 | cluster_buy |
| CRDF | 75 | corporate_insider | Mohindru Mani | 2 | $50,000 | cluster_buy |
| CELC | 72 | large_holder | Baker Bros. Advisors LP |  | - | - |
| MPWR | 72 | large_holder | Invesco Ltd. |  | - | - |
| HQY | 72 | large_holder | Wasatch Advisors LP |  | - | - |
| VOYG | 72 | large_holder | BANK OF NOVA SCOTIA |  | - | - |
| MQ | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| DSGR | 70 | large_holder | LKCM Private Discipline M |  | - | - |
| DMRC | 70 | large_holder | Ocho Investments LLC |  | - | - |
| AFB | 70 | large_holder | KARPUS MANAGEMENT, INC. |  | - | - |
| USCB | 70 | large_holder | Patriot Financial Partner |  | - | - |
| ELTX | 70 | large_holder | Moti Investments LLC |  | - | - |
| NRRWF | 70 | large_holder | Pacific Investment Holdin |  | - | - |
| VDTA | 70 | large_holder | Hamble International Inc. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| CRDO | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |
| SMTC | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |
| ABT | 61 | congress | Rick Larsen | $15,000 | small_amount |
| SPGI | 61 | congress | Rick Larsen | $15,000 | small_amount |
| FLL | 61 | congress | Susie Lee | $15,000 | small_amount |
| BRCM | 61 | congress | Gilbert Cisneros | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 750.72 (-0.54% / -0.13% / 0.31%) [2026-07-16]
- QQQ: 705.94 (-1.64% / -2.4% / -3.17%) [2026-07-16]
- IWM: 295.59 (-0.06% / -0.56% / 1.2%) [2026-07-16]
- DIA: 524.83 (-0.21% / 0.12% / 0.92%) [2026-07-16]
- TLT: 84.21 (-0.04% / -0.33% / -1.94%) [2026-07-16]
- IEF: 93.72 (-0.06% / 0.01% / -0.52%) [2026-07-16]
- GLD: 364.96 (-1.98% / -3.5% / -8.22%) [2026-07-16]
- ^VIX: 16.73 (6.76% / 5.62% / 1.95%) [2026-07-16]
- BTC-USD: 62837.73 (-1.49% / -1.44% / 4.83%) [2026-07-17]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.13 (delta 1m: 0.04) [2026-07-15]
- Treasury 10Y yield: 4.55 (delta 1m: 0.07) [2026-07-15]
- Curva 10Y-2Y: 0.41 (delta 1m: 0.01) [2026-07-16]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.71 (delta 1m: 0.0) [2026-07-15]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.22 (delta 1m: -0.1) [2026-07-16]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (1), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWV] Down 50 % From Its High , Is CoreWeave a Bargain or a Value Trap ? (2026-07-16)
- [CRWV] Here Why the CoreWeave Stock Price is Diving and Why it May Hit $50 (2026-07-16)
- [GTLS] Baystreet . ca - Baker Hughes Climbs on Buying Chart Industries (2026-07-16)
- [MDB] Mandatum Life Insurance Co Ltd Makes New $1 . 25 Million Investment in MongoDB , Inc . $MDB (2026-07-15)
- [BRSL] Brightstar Lottery seals multi - year extension with Washington Lottery (2026-07-14)
- [MDB] Teachers Retirement System of The State of Kentucky Reduces Stock Holdings in MongoDB , Inc . $MDB (2026-07-14)
- [UTHR] Insider Selling : United Therapeutics ( NASDAQ : UTHR ) CEO Sells 9 , 500 Shares (2026-07-13)
- [GTLS] Chart Industries ( NYSE : GTLS ) Reaches New 52 - Week High – What Next ? (2026-07-07)
- [FCPT] Analyzing Four Corners Property Trust ( NYSE : FCPT ) & Global Net Lease ( NYSE : GNL ) (2026-07-06)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Guo Li opero AIOS por $2.5B el 2026-07-14 [senal en multiples fuentes].
- CEO Vinci Gerald F vendio GTLS por $5.7M el 2026-07-16.
- Insider BAKER BROS. ADVISORS LP vendio CELC por $291.0M el 2026-07-14 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.
- Institutional manager Geode Capital Management LLC compro JPMORGAN CHASE & CO por $13.1B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $263,177 · win rate 86% · categorias: sports
- esportGG · PnL $26,956 · win rate 94% · categorias: sports
- comon119 · PnL $10,285 · win rate 99% · categorias: sports, crypto, politics
- onekey02 · PnL $10,301 · win rate 96% · categorias: politics, crypto, sports
- Themsnw · PnL $49,365 · win rate 88% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 40 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 726 registros 30d · ultimo dato 2026-07-16
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-16
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, CELC, GLD, IEF, MPWR, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
