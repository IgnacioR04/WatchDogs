# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-09T13:14:11+00:00 · ventana señales 2026-06-09 -> 2026-07-09_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.79)
- Tendencia: `bull` (SPY 745.4 · MA50 738.24 · MA200 690.16 · dist MA200: 8.0%)
- Credito: `tight` (HY spread 2.67)
- Tipos: `flat` (curva 10y-2y 0.35)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 745.4 | -0.31% | -0.18% | 1.1% |
| QQQ | 12.0% | core | 711.44 | 0.28% | -3.39% | -0.54% |
| TLT | 12.0% | core | 84.36 | -0.22% | -2.02% | 0.06% |
| GLD | 9.3% | core | 374.45 | -0.81% | 1.65% | -5.74% |
| FVR | 7.2% | satellite | ? | ? | ? | ? |
| IEF | 6.2% | core | 93.51 | -0.2% | -0.79% | 0.32% |
| EPAM | 4.0% | satellite | ? | ? | ? | ? |
| RSI | 3.8% | satellite | ? | ? | ? | ? |
| ROKU | 3.4% | satellite | ? | ? | ? | ? |
| GLUE | 3.3% | satellite | ? | ? | ? | ? |
| RBLX | 2.7% | satellite | ? | ? | ? | ? |
| LQDA | 2.5% | satellite | 79.47 | -2.17% | -0.33% | 24.37% |
| WRBY | 2.3% | satellite | 27.67 | -1.32% | -8.8% | 17.69% |
| NUVL | 2.2% | satellite | 123.8 | 0.02% | 0.24% | 39.9% |
| INTC | 2.0% | satellite | ? | ? | ? | ? |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.8%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.8%
- Max drawdown historico: -6.0%
- Beta vs SPY: 0.789 · posiciones efectivas: 14.5 · HHI: 0.0691

**Por que estos satellite (señales WATCHDOG):**

- **FVR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **EPAM** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **RSI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WRBY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **LQDA** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NUVL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **ROKU** · score agregado 70.5 · 1 señales · fuentes: large_holder
- **RBLX** · score agregado 70.5 · 1 señales · fuentes: large_holder
- **GLUE** · score agregado 70.5 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| TSM | 76 | corporate_insider | Wei Che-Chia | 31 | $11,187 | cluster_buy,small_amount |
| RSI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CAG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| WRBY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| LQDA | 72 | large_holder | BlackRock, Inc. |  | - | - |
| OVID | 72 | large_holder | Federated Hermes, Inc. |  | - | - |
| NUVL | 72 | large_holder | FMR LLC |  | - | - |
| CYTK | 72 | large_holder | FMR LLC |  | - | - |
| TSM | 71 | corporate_insider | Huang Jen-Chau | 31 | $2,145 | cluster_buy,small_amount |
| TSM | 71 | corporate_insider | Chin Yung-Pei | 31 | $5,287 | cluster_buy,small_amount |
| TSM | 71 | corporate_insider | Mii Yuh-Jier | 31 | $5,210 | cluster_buy,small_amount |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| FLX | 70 | large_holder | CDH Venture Capital III L |  | - | - |
| PLCE | 70 | large_holder | Mithaq Capital SPC |  | - | - |
| APLD | 70 | large_holder | Wesley Cummins |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| AESI | 64 | congress | Chip Roy | $250,000 | - |
| META | 64 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| XOM | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 745.4 (-0.31% / -0.18% / 1.1%) [2026-07-08]
- QQQ: 711.44 (0.28% / -3.39% / -0.54%) [2026-07-08]
- IWM: 293.48 (-0.91% / -2.32% / 3.54%) [2026-07-08]
- DIA: 522.77 (-1.07% / 0.07% / 3.0%) [2026-07-08]
- TLT: 84.36 (-0.22% / -2.02% / 0.06%) [2026-07-08]
- IEF: 93.51 (-0.2% / -0.79% / 0.32%) [2026-07-08]
- GLD: 374.45 (-0.81% / 1.65% / -5.74%) [2026-07-08]
- ^VIX: 16.79 (-0.65% / 1.21% / -15.5%) [2026-07-09]
- BTC-USD: 62709.37 (0.73% / -0.6% / -1.31%) [2026-07-09]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: 0.14) [2026-07-07]
- Treasury 10Y yield: 4.55 (delta 1m: 0.08) [2026-07-07]
- Curva 10Y-2Y: 0.35 (delta 1m: -0.03) [2026-07-08]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.67 (delta 1m: -0.08) [2026-07-07]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: -0.11) [2026-07-08]
- Dolar broad index: 120.6902 (delta 1m: 1.654) [2026-07-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [SPOT] Oregon Public Employees Retirement Fund Buys 14 , 179 Shares of Palo Alto Networks , Inc . $PANW (2026-07-09)
- [PTCT] PTC Therapeutics , Inc . ( NASDAQ : PTCT ) Receives $91 . 36 Average PT from Analysts (2026-07-09)
- [CRWV] Meta Vs . Coreweave : Despite 2032 Partnership ,  Meta Compute  Remains a Massive Threat to Coreweave (2026-07-09)
- [OMDA] Omada Health ( NASDAQ : OMDA ) CFO Sells 23 , 263 Shares of Stock (2026-07-09)
- [CRCL] How Circle Internet Group Stock Lost 45 % Last Month (2026-07-08)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Beck Peter vendio RKLB por $38.7M el 2026-07-07.
- CEO Huang Jack Jiajia compro COE por $9.3M el 2026-07-02.
- CEO Beck Peter vendio RKLB por $29.2M el 2026-07-08.
- CEO Huang Jack Jiajia compro COE por $4.8M el 2026-07-01.
- CEO Beck Peter vendio RKLB por $19.8M el 2026-07-06.
- CEO Wohlin Hakan compro VII por $3.0M el 2026-07-06.
- 10% owner Globalharvest Holdings Venture Ltd compro AVO por $8.3M el 2026-07-06.
- CEO Tenev Vladimir vendio HOOD por $13.6M el 2026-07-06.

**Polymarket — smart money (traders con mejor track record):**

- comon119 · PnL $76,149 · win rate 99% · categorias: sports, crypto, politics
- SDTrading · PnL $35,502 · win rate 93% · categorias: sports
- Uniform123 · PnL $23,155 · win rate 92% · categorias: sports
- Bagwell306 · PnL $15,973 · win rate 93% · categorias: sports, economy
- lpcapital1 · PnL $22,169 · win rate 90% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 80 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 974 registros 30d · ultimo dato 2026-07-09
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-09
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`EPAM, FVR, GLD, GLUE, IEF, INTC, LQDA, NUVL, QQQ, RBLX, ROKU, RSI, SPY, TLT, WRBY`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
