# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-03T17:39:10+00:00 · ventana señales 2026-07-04 -> 2026-08-03_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.59)
- Tendencia: `bull` (SPY 757.17 · MA50 744.58 · MA200 697.91 · dist MA200: 8.49%)
- Credito: `tight` (HY spread 2.84)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 757.17 | 1.36% | 2.45% | 0.78% |
| QQQ | 12.0% | core | 699.63 | 1.69% | 2.57% | -3.21% |
| TLT | 12.0% | core | 82.19 | -0.07% | -1.86% | -3.81% |
| GLD | 9.3% | core | 370.18 | -0.37% | -1.19% | -3.13% |
| BEP | 8.0% | satellite | 33.64 | 2.37% | 4.7% | -0.44% |
| IEF | 6.2% | core | 92.81 | -0.16% | -0.51% | -1.46% |
| NTST | 5.9% | satellite | 21.32 | -0.61% | -2.47% | -0.7% |
| NRIM | 5.7% | satellite | 27.32 | 3.04% | 2.15% | 0.17% |
| MIDD | 4.3% | satellite | 134.56 | 0.73% | -1.06% | -6.66% |
| TRIP | 3.3% | satellite | 14.23 | 0.42% | -0.35% | 2.52% |
| PWP | 2.9% | satellite | 17.2 | -2.52% | 6.4% | -0.09% |
| PRIM | 1.8% | satellite | 86.73 | 2.75% | 1.4% | -3.85% |
| SPCX | 1.5% | satellite | 110.46 | 1.93% | -2.68% | -31.14% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.3%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -2.1%
- Beta vs SPY: None · posiciones efectivas: 13.6 · HHI: 0.0733

**Por que estos satellite (señales WATCHDOG):**

- **NTST** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **PWP** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **TRIP** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **PRIM** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NRIM** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MIDD** · score agregado 71.8 · 1 señales · fuentes: large_holder
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
| SNX | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| ICHR | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| LKFN | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| NRIM | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| MIDD | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| BAP | 70 | large_holder | BlackRock, Inc. |  | - | - |
| NCA | 70 | large_holder | UBS Group AG |  | - | - |
| NOA | 70 | large_holder | CIBC Global Asset Managme |  | - | - |
| BSP | 70 | large_holder | BAILLIE GIFFORD & CO |  | - | - |

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

- SPY: 757.17 (1.36% / 2.45% / 0.78%) [2026-08-03]
- QQQ: 699.63 (1.69% / 2.57% / -3.21%) [2026-08-03]
- IWM: 295.53 (1.49% / 0.89% / -1.13%) [2026-08-03]
- DIA: 529.79 (1.04% / 1.64% / -0.03%) [2026-08-03]
- TLT: 82.19 (-0.07% / -1.86% / -3.81%) [2026-08-03]
- IEF: 92.81 (-0.16% / -0.51% / -1.46%) [2026-08-03]
- GLD: 370.18 (-0.37% / -1.19% / -3.13%) [2026-08-03]
- ^VIX: 15.59 (-2.5% / -16.5% / 0.13%) [2026-08-03]
- BTC-USD: 63794.5 (0.49% / -0.18% / -1.79%) [2026-08-03]

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

**Temas dominantes**: earnings (4), stock (3), ai (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TLRY] Tilray Brands climbs 8 %, extending prior day gains ( TLRY : NASDAQ ) (2026-07-31)
- [TLRY] Tilray Brands ( NASDAQ : TLRY ) Stock Price Up 5 . 3 % – Should You Buy ? (2026-07-30)
- [TLRY] Tilray Brands ( NASDAQ : TLRY ) Trading Up 5 . 3 % – Should You Buy ? (2026-07-30)
- [TLRY] Tilray Brands Q4 Earnings Call Highlights (2026-07-30)
- [UEC] Uranium Energy Is Down Sharply in 2026 . Here What the Next 10 Years Could Realistically Look Like . (2026-07-30)
- [HURN] FinancialContent - Why Is Huron ( HURN ) Stock Soaring Today (2026-07-29)
- [HURN] Huron Consulting Group ( NASDAQ : HURN ) Issues FY 2026 Earnings Guidance (2026-07-29)
- [HURN] Huron Consulting Group ( NASDAQ : HURN ) Announces Earnings Results , Beats Expectations By $0 . 29 EPS (2026-07-28)
- [HURN] FinancialContent - Huron ( NASDAQ : HURN ) Reports Strong Q2 CY2026 , Full - Year Outlook Exceeds Expectations (2026-07-28)
- [SHBI] Research Analyst Recent Ratings Changes for Shore Bancshares ( SHBI ) (2026-07-28)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner TPG GP A, LLC compro TPG Twin Brook Capital Income Fund por $50.0M el 2026-07-29.
- 10% owner MITSUBISHI UFJ FINANCIAL GROUP INC vendio MS por $88.4M el 2026-07-30 [senal en multiples fuentes].
- 10% owner Refo SCSp vendio REF por $41.7M el 2026-07-31.
- 10% owner FTV VII, L.P. vendio NP por $62.0M el 2026-07-29.
- 10% owner BSIV Hold 101, LP vendio NP por $54.2M el 2026-07-29.
- CEO MURPHY JOHN vendio KO por $13.3M el 2026-07-31.
- 10% owner Bregal Sagemount I, L.P. opero LPRO por $23.8M el 2026-07-28.
- CEO Christopher Gregory L. opero MLI por $13.7M el 2026-07-30.

**Polymarket — smart money (traders con mejor track record):**

- CORGI8 · PnL $79,361 · win rate 91% · categorias: sports
- 111111111115 · PnL $34,941 · win rate 94% · categorias: sports
- 0x6982049c65e98606f65A0CE71fDb9b61296dA165-1777135114945 · PnL $17,194 · win rate 98% · categorias: sports, crypto
- 0x5F659BcCBC353dBf7BcdffDEE73beE60bB482036-1780496231400 · PnL $45,068 · win rate 91% · categorias: sports, crypto
- matenghehe · PnL $17,139 · win rate 96% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 45 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 563 registros 30d · ultimo dato 2026-08-03
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-03
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, GLD, IEF, MIDD, NRIM, NTST, PRIM, PWP, QQQ, SPCX, SPY, TLT, TRIP`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
