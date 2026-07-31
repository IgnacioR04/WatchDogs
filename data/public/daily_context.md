# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-31T17:13:20+00:00 · ventana señales 2026-07-01 -> 2026-07-31_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.85)
- Tendencia: `bull` (SPY 745.22 · MA50 744.19 · MA200 697.4 · dist MA200: 6.86%)
- Credito: `tight` (HY spread 2.84)
- Tipos: `flat` (curva 10y-2y 0.45)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 745.22 | 0.48% | 0.85% | 0.06% |
| QQQ | 12.0% | core | 688.1 | 0.67% | 0.57% | -3.44% |
| TLT | 12.0% | core | 81.99 | -0.98% | -1.51% | -4.12% |
| GLD | 9.3% | core | 370.82 | -1.68% | -0.29% | -1.93% |
| BEP | 8.4% | satellite | 32.77 | 0.34% | -1.06% | -3.28% |
| IEF | 6.2% | core | 92.78 | -0.47% | -0.27% | -1.43% |
| NMM | 6.1% | satellite | 80.19 | 1.17% | 1.38% | 10.66% |
| MIDD | 5.7% | satellite | 133.87 | 0.41% | -0.01% | -4.98% |
| CPRI | 4.6% | satellite | 15.98 | 0.6% | 3.53% | -15.69% |
| NRIX | 3.4% | satellite | 23.13 | -1.91% | -1.07% | -3.5% |
| TSM | 3.4% | satellite | 407.57 | 1.06% | 1.03% | -6.13% |
| SPCX | 2.0% | satellite | 109.09 | -2.77% | -5.2% | -32.66% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.0%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -4.8%
- Beta vs SPY: 0.762 · posiciones efectivas: 13.4 · HHI: 0.0745

**Por que estos satellite (señales WATCHDOG):**

- **SPCX** · score agregado 241.4 · 4 señales · fuentes: congress
- **NMM** · score agregado 174.3 · 3 señales · fuentes: corporate_insider
- **CPRI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MIDD** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NRIX** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress
- **TSM** · score agregado 56.3 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| [NONE] | 84 | corporate_insider | VEP Group, LLC | 2 | $6,229,807 | cluster_buy |
| TTD | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| SMTC | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| ICHR | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| AGX | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| JKHY | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| CAG | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| ASH | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| HQY | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| CPRI | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| MIDD | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| NRIX | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| MPLT | 70 | large_holder | Novo Holdings A/S |  | - | - |
| RAASY | 70 | large_holder | TB Alternative Assets Ltd |  | - | - |
| PLAB | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| SMTC | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 745.22 (0.48% / 0.85% / 0.06%) [2026-07-31]
- QQQ: 688.1 (0.67% / 0.57% / -3.44%) [2026-07-31]
- IWM: 291.23 (-0.46% / 0.02% / -2.13%) [2026-07-31]
- DIA: 523.95 (0.47% / 1.0% / -0.72%) [2026-07-31]
- TLT: 81.99 (-0.98% / -1.51% / -4.12%) [2026-07-31]
- IEF: 92.78 (-0.47% / -0.27% / -1.43%) [2026-07-31]
- GLD: 370.82 (-1.68% / -0.29% / -1.93%) [2026-07-31]
- ^VIX: 16.85 (-1.4% / -9.31% / 4.33%) [2026-07-31]
- BTC-USD: 62809.19 (-2.96% / -3.87% / -1.56%) [2026-07-31]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.22 (delta 1m: 0.12) [2026-07-29]
- Treasury 10Y yield: 4.67 (delta 1m: 0.29) [2026-07-29]
- Curva 10Y-2Y: 0.45 (delta 1m: 0.15) [2026-07-30]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.84 (delta 1m: 0.1) [2026-07-30]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.27 (delta 1m: 0.03) [2026-07-30]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (2), earnings (2), merger (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWV] Is CoreWeave Stock a Buy After a Company Insider Shed 6 , 455 Shares ? (2026-07-31)
- [CRWD] CrowdStrike Stock Just Scored a New  Buy  Rating . Here Why . (2026-07-30)
- [SKYT] IonQ ( NYSE : IONQ ) Clears Final Regulatory Hurdle To Close SkyWater Technology ( NASDAQ : SKYT ) Acquisition (2026-07-29)
- [GSHD] Goosehead Insurance ( GSHD ) – Research Analyst Recent Ratings Changes (2026-07-23)
- [GSHD] Goosehead Insurance ( NASDAQ : GSHD ) Issues Earnings Results , Beats Estimates By $0 . 17 EPS (2026-07-23)
- [GSHD] Goosehead Insurance ( NASDAQ : GSHD ) Posts Earnings Results , Beats Expectations By $0 . 17 EPS (2026-07-23)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Catalyst4, Inc. compro MLPT por $13.0M el 2026-07-30.
- CEO Huang Jack Jiajia compro COE por $7.7M el 2026-07-27.
- 10% owner Abu Dhabi Investment Authority compro Overland Advantage por $22.9M el 2026-07-28.
- 10% owner VEP Group, LLC compro [NONE] por $6.2M el 2026-07-29.
- CEO Huang Jack Jiajia compro COE por $3.0M el 2026-07-24.
- 10% owner Bregal Sagemount I, L.P. opero LPRO por $23.8M el 2026-07-28.
- CEO Christopher Gregory L. opero MLI por $13.7M el 2026-07-30.
- 10% owner Edenbrook Capital, LLC vendio FEIM por $31.9M el 2026-07-28.

**Polymarket — smart money (traders con mejor track record):**

- TAIWANNUMBERONE · PnL $120,431 · win rate 91% · categorias: sports, politics
- 0xf3ce7f04 · PnL $21,045 · win rate 96% · categorias: sports
- esportGG · PnL $22,095 · win rate 95% · categorias: sports
- BreakTheBank · PnL $69,070 · win rate 86% · categorias: sports
- MeiGuNiuBi · PnL $77,001 · win rate 83% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 47 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 627 registros 30d · ultimo dato 2026-07-31
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-31
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, CPRI, GLD, IEF, MIDD, NMM, NRIX, QQQ, SPCX, SPY, TLT, TSM`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
