# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-02T15:38:41+00:00 · ventana señales 2026-07-03 -> 2026-08-02_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.99)
- Tendencia: `bull` (SPY 747.03 · MA50 744.22 · MA200 697.41 · dist MA200: 7.12%)
- Credito: `tight` (HY spread 2.84)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 747.03 | 0.72% | 1.1% | 0.3% |
| QQQ | 12.0% | core | 687.99 | 0.65% | 0.55% | -3.45% |
| TLT | 12.0% | core | 82.25 | -0.66% | -1.2% | -3.81% |
| BEP | 10.8% | satellite | 32.86 | 0.61% | -0.79% | -3.01% |
| GLD | 9.3% | core | 371.54 | -1.49% | -0.1% | -1.74% |
| MIDD | 7.3% | satellite | 133.58 | 0.2% | -0.22% | -5.19% |
| IEF | 6.2% | core | 92.95 | -0.28% | -0.09% | -1.24% |
| CPRI | 5.9% | satellite | 15.93 | 0.25% | 3.17% | -15.98% |
| NRIX | 4.3% | satellite | 23.21 | -1.57% | -0.73% | -3.17% |
| PRIM | 2.7% | satellite | 84.41 | -1.45% | -2.43% | -4.3% |
| SPCX | 2.6% | satellite | 108.37 | -3.41% | -5.82% | -33.1% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.9%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 1.5%
- Max drawdown historico: -5.8%
- Beta vs SPY: 0.779 · posiciones efectivas: 12.6 · HHI: 0.0793

**Por que estos satellite (señales WATCHDOG):**

- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **PRIM** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CPRI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MIDD** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NRIX** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| HCWB | 79 | corporate_insider | Wong Hing C | 3 | $59,998 | cluster_buy |
| BBASX | 79 | corporate_insider | AMG New York Holdings Cor | 2 | $897,184 | cluster_buy |
| XAIR | 78 | corporate_insider | Goodman Robert Scott | 2 | $199,999 | cluster_buy |
| BBASX | 76 | corporate_insider | BROWN BROTHERS HARRIMAN C | 2 | $224,341 | cluster_buy |
| HCWB | 74 | corporate_insider | Flowers Lee | 3 | $19,998 | cluster_buy,small_amount |
| HCWB | 73 | corporate_insider | GARRETT SCOTT T | 3 | $19,998 | cluster_buy,small_amount |
| XAIR | 72 | corporate_insider | MOORHEAD DANIEL J | 2 | $24,998 | cluster_buy,small_amount |
| PRIM | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| SNX | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| ICHR | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| CPRI | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| LKFN | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| MIDD | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| NRIX | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| LEVI | 72 | large_holder | Vanguard Capital Manageme |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| ADBE | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| INTU | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 747.03 (0.72% / 1.1% / 0.3%) [2026-07-31]
- QQQ: 687.99 (0.65% / 0.55% / -3.45%) [2026-07-31]
- IWM: 291.2 (-0.48% / 0.01% / -2.14%) [2026-07-31]
- DIA: 524.32 (0.54% / 1.07% / -0.65%) [2026-07-31]
- TLT: 82.25 (-0.66% / -1.2% / -3.81%) [2026-07-31]
- IEF: 92.95 (-0.28% / -0.09% / -1.24%) [2026-07-31]
- GLD: 371.54 (-1.49% / -0.1% / -1.74%) [2026-07-31]
- ^VIX: 15.99 (-6.44% / -13.94% / -0.99%) [2026-07-31]
- BTC-USD: 63075.85 (0.5% / -1.25% / 1.34%) [2026-08-02]

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

**Temas dominantes**: merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [SKYT] IonQ Acquires SkyWater Technology (2026-07-31)
- [UEC] Uranium Energy Is Down Sharply in 2026 . Here What the Next 10 Years Could Realistically Look Like . (2026-07-30)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner TPG GP A, LLC compro TPG Twin Brook Capital Income Fund por $50.0M el 2026-07-29.
- 10% owner Catalyst4, Inc. compro MLPT por $13.0M el 2026-07-30.
- CEO Huang Jack Jiajia compro COE por $7.7M el 2026-07-27.
- 10% owner Refo SCSp vendio REF por $41.7M el 2026-07-31.
- CEO Huang Jack Jiajia compro COE por $3.0M el 2026-07-24.
- 10% owner FTV VII, L.P. vendio NP por $62.0M el 2026-07-29.
- 10% owner BSIV Hold 101, LP vendio NP por $54.2M el 2026-07-29.
- 10% owner Bregal Sagemount I, L.P. opero LPRO por $23.8M el 2026-07-28.

**Polymarket — smart money (traders con mejor track record):**

- 111111111115 · PnL $120,512 · win rate 94% · categorias: sports
- PleaseWinPlease · PnL $70,726 · win rate 91% · categorias: sports
- ToeTickler98 · PnL $56,695 · win rate 91% · categorias: sports
- Dota2winner · PnL $33,276 · win rate 95% · categorias: sports
- JnStTrdrBnusFnd · PnL $34,531 · win rate 92% · categorias: crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 45 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 599 registros 30d · ultimo dato 2026-07-31
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-31
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, CPRI, GLD, IEF, MIDD, NRIX, PRIM, QQQ, SPCX, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
