# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-10T16:27:17+00:00 · ventana señales 2026-07-11 -> 2026-08-10_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.12)
- Tendencia: `bull` (SPY 773.79 · MA50 747.04 · MA200 700.67 · dist MA200: 10.44%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.79 | 0.07% | 2.13% | 3.29% |
| QQQ | 12.0% | core | 723.19 | 0.02% | 3.3% | 1.61% |
| TLT | 12.0% | core | 82.25 | -0.61% | 0.08% | -1.65% |
| GLD | 9.3% | core | 400.31 | 0.46% | 7.69% | 9.04% |
| FWONK | 8.2% | satellite | 102.86 | 0.01% | 5.24% | 3.23% |
| BWFG | 6.7% | satellite | 66.25 | -0.98% | -1.89% | 13.3% |
| CHRW | 6.4% | satellite | 148.83 | -0.35% | 1.24% | -24.26% |
| IEF | 6.2% | core | 92.86 | -0.33% | 0.04% | -0.12% |
| LTH | 5.9% | satellite | 42.94 | -1.99% | -2.78% | 3.54% |
| DNTH | 3.1% | satellite | 108.55 | -0.34% | 2.39% | 10.05% |
| SPCX | 1.7% | satellite | 130.46 | -1.99% | 13.91% | -6.24% |
| WOLF | 1.5% | satellite | 30.57 | -7.0% | 25.54% | -9.15% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.6%
- VaR 95% 1d: 0.6% · CVaR 95% 1d: 0.8%
- Max drawdown historico: -1.3%
- Beta vs SPY: None · posiciones efectivas: 13.2 · HHI: 0.076

**Por que estos satellite (señales WATCHDOG):**

- **BWFG** · score agregado 337.3 · 6 señales · fuentes: corporate_insider
- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **WOLF** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **DNTH** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress

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
| DNTH | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| DNTH | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| AVR | 72 | large_holder | L1 Capital Pty Ltd |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 65 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ANET | 63 | corporate_insider | Ullal Jayshree | $74,391,542 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| UNH | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.79 (0.07% / 2.13% / 3.29%) [2026-08-10]
- QQQ: 723.19 (0.02% / 3.3% / 1.61%) [2026-08-10]
- IWM: 299.9 (-0.55% / 1.24% / 2.19%) [2026-08-10]
- DIA: 538.81 (-0.15% / 1.43% / 2.76%) [2026-08-10]
- TLT: 82.25 (-0.61% / 0.08% / -1.65%) [2026-08-10]
- IEF: 92.86 (-0.33% / 0.04% / -0.12%) [2026-08-10]
- GLD: 400.31 (0.46% / 7.69% / 9.04%) [2026-08-10]
- ^VIX: 15.12 (1.48% / -4.67% / -11.89%) [2026-08-10]
- BTC-USD: 64065.59 (-1.2% / -0.82% / -3.67%) [2026-08-10]

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

**Temas dominantes**: stock (7), earnings (6), leadership (4), ai (3), regulatory (1), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TSM] Chip equipment stocks rise after Taiwan Semiconductor revenue surges 45 % (2026-08-10)
- [TSM] Chip equipment stocks rise after Taiwan Semiconductor revenue surges 45 % (2026-08-10)
- [TSM] Why Taiwan Semiconductor ( TSM ) Could Be a Top AI Infrastructure Winner (2026-08-10)
- [GFF] Griffon Q3 Earnings Call Highlights (2026-08-09)
- [DNTH] Dianthus Therapeutics ( NASDAQ : DNTH ) CEO Marino Garcia Sells 166 , 000 Shares (2026-08-08)
- [ANET] Arista Network ( ANET )  Overweight  Rating Reiterated at Piper Sandler (2026-08-08)
- [ANET] Insider Selling : Arista Networks ( NYSE : ANET ) Major Shareholder Sells 300 , 000 Shares of Stock (2026-08-07)
- [GFF] Griffon ( NYSE : GFF ) CEO Ronald Kramer Sells 100 , 000 Shares (2026-08-07)
- [ANET] Insider Selling : Arista Networks ( NYSE : ANET ) CEO Sells $154 , 341 , 575 . 38 in Stock (2026-08-07)
- [ETD] Ethan Allen CEO Defends Leadership After Activist Challenge (2026-08-07)

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

- quavoo · PnL $262,352 · win rate 84% · categorias: sports, politics, economy
- BrotherObama · PnL $66,749 · win rate 87% · categorias: sports
- lzh1 · PnL $31,094 · win rate 92% · categorias: sports
- 0x5dd9da6e · PnL $15,536 · win rate 96% · categorias: sports
- VD721lsj4938Dk388 · PnL $29,519 · win rate 91% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 73 registros 30d · ultimo dato 2026-07-31 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 723 registros 30d · ultimo dato 2026-08-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-10
- **institutional_13f**: `warning` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress, institutional_13f

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BWFG, CHRW, DNTH, FWONK, GLD, IEF, LTH, QQQ, SPCX, SPY, TLT, WOLF`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
