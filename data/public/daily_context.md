# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-03T20:13:49+00:00 · ventana señales 2026-07-04 -> 2026-08-03_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.73)
- Tendencia: `bull` (SPY 757.64 · MA50 744.59 · MA200 697.91 · dist MA200: 8.56%)
- Credito: `tight` (HY spread 2.84)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 757.64 | 1.42% | 2.51% | 0.85% |
| QQQ | 12.0% | core | 700.07 | 1.76% | 2.63% | -3.15% |
| TLT | 12.0% | core | 82.19 | -0.07% | -1.86% | -3.82% |
| BEP | 11.4% | satellite | 33.69 | 2.51% | 4.84% | -0.31% |
| GLD | 9.3% | core | 371.71 | 0.05% | -0.78% | -2.73% |
| NTST | 8.5% | satellite | 21.38 | -0.33% | -2.2% | -0.42% |
| IEF | 6.2% | core | 92.82 | -0.14% | -0.49% | -1.44% |
| TRIP | 4.8% | satellite | 14.5 | 2.33% | 1.54% | 4.47% |
| PWP | 4.1% | satellite | 17.17 | -2.72% | 6.18% | -0.29% |
| PRIM | 2.5% | satellite | 87.89 | 4.12% | 2.76% | -2.56% |
| SPCX | 2.1% | satellite | 114.53 | 5.68% | 0.91% | -28.61% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.6%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -2.4%
- Beta vs SPY: None · posiciones efectivas: 12.3 · HHI: 0.0811

**Por que estos satellite (señales WATCHDOG):**

- **NTST** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **PWP** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **TRIP** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **PRIM** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| HCWB | 79 | corporate_insider | Wong Hing C | 3 | $59,998 | cluster_buy |
| XAIR | 78 | corporate_insider | Goodman Robert Scott | 2 | $199,999 | cluster_buy |
| HCWB | 74 | corporate_insider | Flowers Lee | 3 | $19,998 | cluster_buy,small_amount |
| HCWB | 73 | corporate_insider | GARRETT SCOTT T | 3 | $19,998 | cluster_buy,small_amount |
| XAIR | 72 | corporate_insider | MOORHEAD DANIEL J | 2 | $24,998 | cluster_buy,small_amount |
| PRIM | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| ICHR | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| AGNT | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| LKFN | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| BAP | 70 | large_holder | BlackRock, Inc. |  | - | - |
| EWAV | 70 | large_holder | Space Summit Capital LLC |  | - | - |
| MWC | 70 | large_holder | O-WELL Corp |  | - | - |
| CISS | 70 | large_holder | CVI Investments, Inc. |  | - | - |
| NCA | 70 | large_holder | UBS Group AG |  | - | - |
| WATT | 70 | large_holder | Raymond James Financial S |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| INTU | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| ADBE | 61 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 757.64 (1.42% / 2.51% / 0.85%) [2026-08-03]
- QQQ: 700.07 (1.76% / 2.63% / -3.15%) [2026-08-03]
- IWM: 296.22 (1.72% / 1.13% / -0.9%) [2026-08-03]
- DIA: 531.29 (1.33% / 1.92% / 0.25%) [2026-08-03]
- TLT: 82.19 (-0.07% / -1.86% / -3.82%) [2026-08-03]
- IEF: 92.82 (-0.14% / -0.49% / -1.44%) [2026-08-03]
- GLD: 371.71 (0.05% / -0.78% / -2.73%) [2026-08-03]
- ^VIX: 15.73 (-1.63% / -15.75% / 1.03%) [2026-08-03]
- BTC-USD: 63874.31 (0.62% / -0.05% / -1.67%) [2026-08-03]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.23 (delta 1m: 0.09) [2026-07-30]
- Treasury 10Y yield: 4.68 (delta 1m: 0.24) [2026-07-30]
- Curva 10Y-2Y: 0.47 (delta 1m: 0.16) [2026-07-31]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.84 (delta 1m: 0.1) [2026-07-30]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.28 (delta 1m: 0.05) [2026-07-31]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: merger (1), regulatory (1), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [SKYT] IonQ Acquires SkyWater Technology (2026-07-31)
- [SHBI] Research Analyst Recent Ratings Changes for Shore Bancshares ( SHBI ) (2026-07-28)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner TPG GP A, LLC compro TPG Twin Brook Capital Income Fund por $50.0M el 2026-07-29.
- 10% owner MITSUBISHI UFJ FINANCIAL GROUP INC vendio MS por $88.4M el 2026-07-30 [senal en multiples fuentes].
- 10% owner FTV VII, L.P. vendio NP por $62.0M el 2026-07-29.
- 10% owner BSIV Hold 101, LP vendio NP por $54.2M el 2026-07-29.
- CEO MURPHY JOHN vendio KO por $13.3M el 2026-07-31.
- CEO Christopher Gregory L. opero MLI por $13.7M el 2026-07-30.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.

**Polymarket — smart money (traders con mejor track record):**

- 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 · PnL $461,472 · win rate 84% · categorias: sports
- CORGI8 · PnL $123,725 · win rate 91% · categorias: sports
- matenghehe · PnL $25,928 · win rate 96% · categorias: sports, crypto
- SemyonMarmeladov · PnL $57,296 · win rate 88% · categorias: sports, economy, politics
- facai86868 · PnL $17,514 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 45 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 522 registros 30d · ultimo dato 2026-08-03
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-03
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, GLD, IEF, NTST, PRIM, PWP, QQQ, SPCX, SPY, TLT, TRIP`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
