# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-08T11:58:07+00:00 · ventana señales 2026-07-09 -> 2026-08-08_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.9)
- Tendencia: `bull` (SPY 773.26 · MA50 746.61 · MA200 700.13 · dist MA200: 10.45%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.26 | 0.61% | 3.51% | 2.43% |
| QQQ | 12.0% | core | 723.03 | 1.17% | 5.09% | -0.34% |
| TLT | 12.0% | core | 82.76 | 0.29% | 1.03% | -1.63% |
| GLD | 9.3% | core | 398.47 | 2.26% | 7.25% | 5.69% |
| FWONK | 8.8% | satellite | 102.85 | 3.17% | 4.81% | 6.99% |
| NMM | 7.4% | satellite | 79.35 | 0.4% | -1.75% | 4.75% |
| LTH | 7.3% | satellite | 43.81 | 0.76% | -2.86% | 4.58% |
| IEF | 6.2% | core | 93.17 | 0.24% | 0.58% | -0.15% |
| CHRW | 4.0% | satellite | 149.35 | 1.83% | 1.1% | -22.82% |
| DNTH | 4.0% | satellite | 108.92 | -0.91% | 1.87% | 11.6% |
| SPCX | 2.1% | satellite | 133.11 | 15.83% | 22.83% | -8.39% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.4%
- VaR 95% 1d: 0.5% · CVaR 95% 1d: 0.8%
- Max drawdown historico: -1.3%
- Beta vs SPY: 0.458 · posiciones efectivas: 12.9 · HHI: 0.0778

**Por que estos satellite (señales WATCHDOG):**

- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **NMM** · score agregado 174.3 · 3 señales · fuentes: corporate_insider
- **DNTH** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BRVE | 91 | corporate_insider | Forbion Growth Opportunit | 7 | $34,560,000 | cluster_buy |
| BRVE | 91 | corporate_insider | Forbion Growth Opportunit | 7 | $30,240,000 | cluster_buy |
| BRVE | 86 | corporate_insider | Murdoch Travis | 7 | $1,499,994 | cluster_buy |
| BRVE | 83 | corporate_insider | Rickey James Paul | 7 | $499,986 | cluster_buy |
| BRVE | 82 | corporate_insider | Viehbacher Christopher | 7 | $1,499,994 | cluster_buy |
| BRVE | 82 | corporate_insider | Lubner David Charles | 7 | $999,990 | cluster_buy |
| CCB | 80 | corporate_insider | Sprink Eric M | 2 | $444,500 | cluster_buy |
| OKYO | 77 | corporate_insider | Dempsey Robert John | 6 | $23,085 | cluster_buy,small_amount |
| OKYO | 76 | corporate_insider | CERRONE GABRIELE M | 6 | $35,000 | cluster_buy |
| OKYO | 76 | corporate_insider | CERRONE GABRIELE M | 6 | $32,625 | cluster_buy |
| BRVE | 76 | corporate_insider | Malek David I | 7 | $74,988 | cluster_buy |
| OKYO | 74 | corporate_insider | Mantelli Flavio | 6 | $28,000 | cluster_buy |
| BRVE | 74 | corporate_insider | Anderson Michele A. | 7 | $19,998 | cluster_buy,small_amount |
| DNTH | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| DNTH | 72 | large_holder | T. Rowe Price Investment  |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 65 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 65 | congress | Sam T. Liccardo | $50,000 | - |
| ANET | 63 | corporate_insider | Ullal Jayshree | $74,391,542 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| NVDA | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.26 (0.61% / 3.51% / 2.43%) [2026-08-07]
- QQQ: 723.03 (1.17% / 5.09% / -0.34%) [2026-08-07]
- IWM: 301.56 (1.11% / 3.56% / 1.88%) [2026-08-07]
- DIA: 539.62 (0.27% / 2.92% / 2.66%) [2026-08-07]
- TLT: 82.76 (0.29% / 1.03% / -1.63%) [2026-08-07]
- IEF: 93.17 (0.24% / 0.58% / -0.15%) [2026-08-07]
- GLD: 398.47 (2.26% / 7.25% / 5.69%) [2026-08-07]
- ^VIX: 14.9 (-1.65% / -6.82% / -0.86%) [2026-08-07]
- BTC-USD: 64926.75 (0.07% / 2.31% / 0.36%) [2026-08-08]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.25 (delta 1m: 0.04) [2026-08-06]
- Treasury 10Y yield: 4.69 (delta 1m: 0.13) [2026-08-06]
- Curva 10Y-2Y: 0.46 (delta 1m: 0.08) [2026-08-07]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.71 (delta 1m: 0.01) [2026-08-06]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: 0.02) [2026-08-07]
- Dolar broad index: 119.7034 (delta 1m: -1.442) [2026-07-31]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (10), earnings (6), leadership (4), ai (1), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TMO] Is Micron Stock Too Cheap to Ignore ? | The Motley Fool (2026-08-08)
- [TMO] $10 , 000 in Axon Stock a Decade Ago Would Be Worth About $329 , 000 Today . The Stock Is Down Over the Past Year . (2026-08-08)
- [DNTH] Dianthus Therapeutics ( NASDAQ : DNTH ) CEO Marino Garcia Sells 166 , 000 Shares (2026-08-08)
- [SVV] Savers Value Village ( NYSE : SVV ) CFO Sells $613 , 318 . 86 in Stock (2026-08-08)
- [SVV] Savers Value Village ( NYSE : SVV ) CEO Sells 7 , 941 Shares (2026-08-08)
- [GFF] Griffon ( NYSE : GFF ) CEO Ronald Kramer Sells 100 , 000 Shares (2026-08-07)
- [ETD] Ethan Allen CEO Defends Leadership After Activist Challenge (2026-08-07)
- [SVV] Savers Value Village launches AI pricing tool ThriftIQ (2026-08-07)
- [SVV] Savers Value Village ( NYSE : SVV ) Announces Quarterly Earnings Results (2026-08-07)
- [GFF] Griffon ( NYSE : GFF ) Issues Quarterly Earnings Results (2026-08-06)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Lazar David E. opero QUCY por $6.3B el 2026-08-05 [senal en multiples fuentes].
- 10% owner Forbion Growth Opportunities Fund III Cooperatief U.A. compro BRVE por $34.6M el 2026-08-07.
- CEO Ullal Jayshree vendio ANET por $74.4M el 2026-08-05 [senal en multiples fuentes].
- CEO Garcia Marino vendio DNTH por $11.2M el 2026-08-07 [senal en multiples fuentes].
- CEO Harik Mario A opero XPO por $33.9M el 2026-08-07.
- CEO Murdoch Travis compro BRVE por $1.5M el 2026-08-07.
- CEO ARCHER TIMOTHY vendio LRCX por $9.0M el 2026-08-06.
- CEO SRINIVASAN RAMESH vendio AGYS por $7.1M el 2026-08-06.

**Polymarket — smart money (traders con mejor track record):**

- TAIWANNUMBERONE · PnL $67,181 · win rate 91% · categorias: sports, politics
- SDTrading · PnL $45,767 · win rate 93% · categorias: sports
- quavoo · PnL $175,240 · win rate 82% · categorias: sports, politics, economy
- 0x6982049c65e98606f65A0CE71fDb9b61296dA165-1777135114945 · PnL $15,010 · win rate 98% · categorias: sports, crypto
- 0x0x23kjookhaiuohduoayh8c9 · PnL $18,569 · win rate 95% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 105 registros 30d · ultimo dato 2026-07-31 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 776 registros 30d · ultimo dato 2026-08-07
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-07
- **institutional_13f**: `warning` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress, institutional_13f

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CHRW, DNTH, FWONK, GLD, IEF, LTH, NMM, QQQ, SPCX, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **95.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
