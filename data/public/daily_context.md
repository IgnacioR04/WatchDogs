# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-10T15:31:34+00:00 · ventana señales 2026-07-11 -> 2026-08-10_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.16)
- Tendencia: `bull` (SPY 773.77 · MA50 747.04 · MA200 700.67 · dist MA200: 10.43%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.77 | 0.07% | 2.12% | 3.28% |
| QQQ | 12.0% | core | 721.75 | -0.18% | 3.1% | 1.41% |
| TLT | 12.0% | core | 82.21 | -0.67% | 0.02% | -1.71% |
| GLD | 9.3% | core | 398.97 | 0.13% | 7.33% | 8.67% |
| FWONK | 7.5% | satellite | 102.56 | -0.28% | 4.93% | 2.93% |
| BWFG | 7.4% | satellite | 66.67 | -0.35% | -1.27% | 14.02% |
| IEF | 6.2% | core | 92.86 | -0.33% | 0.05% | -0.11% |
| LTH | 6.1% | satellite | 43.26 | -1.27% | -2.07% | 4.3% |
| PINS | 3.9% | satellite | 24.16 | 2.01% | -0.02% | 6.88% |
| CHRW | 3.4% | satellite | 148.58 | -0.52% | 1.07% | -24.39% |
| DNTH | 3.4% | satellite | 109.43 | 0.47% | 3.22% | 10.94% |
| SPCX | 1.8% | satellite | 131.49 | -1.22% | 14.81% | -5.5% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.5%
- VaR 95% 1d: 0.6% · CVaR 95% 1d: 0.8%
- Max drawdown historico: -1.4%
- Beta vs SPY: 0.475 · posiciones efectivas: 13.4 · HHI: 0.0747

**Por que estos satellite (señales WATCHDOG):**

- **BWFG** · score agregado 337.3 · 6 señales · fuentes: corporate_insider
- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **DNTH** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **PINS** · score agregado 73.0 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BRVE | 86 | corporate_insider | Murdoch Travis | 6 | $1,499,994 | cluster_buy |
| BRVE | 83 | corporate_insider | Rickey James Paul | 6 | $499,986 | cluster_buy |
| BRVE | 82 | corporate_insider | Viehbacher Christopher | 6 | $1,499,994 | cluster_buy |
| BRVE | 82 | corporate_insider | Lubner David Charles | 6 | $999,990 | cluster_buy |
| CCB | 80 | corporate_insider | Sprink Eric M | 2 | $444,500 | cluster_buy |
| OKYO | 77 | corporate_insider | Dempsey Robert John | 6 | $23,085 | cluster_buy,small_amount |
| OKYO | 76 | corporate_insider | CERRONE GABRIELE M | 6 | $35,000 | cluster_buy |
| OKYO | 76 | corporate_insider | CERRONE GABRIELE M | 6 | $32,625 | cluster_buy |
| BRVE | 76 | corporate_insider | Malek David I | 6 | $74,988 | cluster_buy |
| TSM | 76 | corporate_insider | Wei Che-Chia | 30 | $11,143 | cluster_buy,small_amount |
| OKYO | 74 | corporate_insider | Mantelli Flavio | 6 | $28,000 | cluster_buy |
| BRVE | 74 | corporate_insider | Anderson Michele A. | 6 | $19,998 | cluster_buy,small_amount |
| PINS | 73 | large_holder | Ameriprise Financial, Inc |  | - | - |
| DNTH | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| DNTH | 72 | large_holder | T. Rowe Price Investment  |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PINS | 68 | congress | Christian D. Menefee | $50,000 | - |
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 65 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ANET | 63 | corporate_insider | Ullal Jayshree | $74,391,542 | - |
| CCI | 63 | congress | Michael Rulli | $15,000 | small_amount |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.77 (0.07% / 2.12% / 3.28%) [2026-08-10]
- QQQ: 721.75 (-0.18% / 3.1% / 1.41%) [2026-08-10]
- IWM: 300.16 (-0.46% / 1.33% / 2.28%) [2026-08-10]
- DIA: 539.65 (0.0% / 1.59% / 2.92%) [2026-08-10]
- TLT: 82.21 (-0.67% / 0.02% / -1.71%) [2026-08-10]
- IEF: 92.86 (-0.33% / 0.05% / -0.11%) [2026-08-10]
- GLD: 398.97 (0.13% / 7.33% / 8.67%) [2026-08-10]
- ^VIX: 15.16 (1.74% / -4.41% / -11.66%) [2026-08-10]
- BTC-USD: 64336.8 (-0.78% / -0.4% / -3.26%) [2026-08-10]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.25 (delta 1m: 0.04) [2026-08-06]
- Treasury 10Y yield: 4.69 (delta 1m: 0.13) [2026-08-06]
- Curva 10Y-2Y: 0.46 (delta 1m: 0.08) [2026-08-07]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: 0.0) [2026-08-07]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: 0.02) [2026-08-07]
- Dolar broad index: 119.7034 (delta 1m: -1.442) [2026-07-31]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (10), earnings (6), leadership (5), regulatory (2), ai (1), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [SVV] Savers Value Village ( NYSE : SVV ) Insider Sells $164 , 700 . 00 in Stock (2026-08-10)
- [YOU] CLEAR Secure Q2 Earnings Call Highlights (2026-08-09)
- [SVV] Mark Walsh Sells 7 , 941 Shares of Savers Value Village ( NYSE : SVV ) Stock (2026-08-09)
- [GFF] Griffon Q3 Earnings Call Highlights (2026-08-09)
- [CRCL] Quantinno Capital Management LP Increases Holdings in Circle Internet Group , Inc . $CRCL (2026-08-09)
- [SVV] Savers Value Village ( SVV ) Is Up 19 . 1 % After ThriftIQ AI Rollout Boosts Q2 Results and Guidance (2026-08-09)
- [SVV] Savers Value Village U . S . Sales Rose 6 . 6 %. Its CEO Just Sold $2 . 4 Million in Stock (2026-08-08)
- [CRCL] Circle Internet Group ( NYSE : CRCL ) Director Danita Ostling Sells 20 , 000 Shares (2026-08-08)
- [DNTH] Dianthus Therapeutics ( NASDAQ : DNTH ) CEO Marino Garcia Sells 166 , 000 Shares (2026-08-08)
- [ANET] Arista Network ( ANET )  Overweight  Rating Reiterated at Piper Sandler (2026-08-08)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Lazar David E. opero QUCY por $6.3B el 2026-08-05 [senal en multiples fuentes].
- CEO Ullal Jayshree vendio ANET por $74.4M el 2026-08-05 [senal en multiples fuentes].
- CEO Garcia Marino vendio DNTH por $11.2M el 2026-08-07 [senal en multiples fuentes].
- CEO Huang Jack Jiajia compro COE por $6.2M el 2026-08-03.
- CEO Harik Mario A opero XPO por $33.9M el 2026-08-07.
- CEO Huang Jack Jiajia compro COE por $3.0M el 2026-08-05.
- CEO Murdoch Travis compro BRVE por $1.5M el 2026-08-07.
- CEO ARCHER TIMOTHY vendio LRCX por $9.0M el 2026-08-06.

**Polymarket — smart money (traders con mejor track record):**

- quavoo · PnL $263,104 · win rate 84% · categorias: sports, politics, economy
- BrotherObama · PnL $69,365 · win rate 87% · categorias: sports
- lzh1 · PnL $32,785 · win rate 92% · categorias: sports
- VD721lsj4938Dk388 · PnL $29,521 · win rate 91% · categorias: sports
- JnStTrdrBnusFnd · PnL $24,834 · win rate 92% · categorias: crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 79 registros 30d · ultimo dato 2026-08-07 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 722 registros 30d · ultimo dato 2026-08-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-10
- **institutional_13f**: `warning` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress, institutional_13f

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BWFG, CHRW, DNTH, FWONK, GLD, IEF, LTH, PINS, QQQ, SPCX, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
