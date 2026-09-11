# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-11T09:57:28+00:00 · ventana señales 2026-08-12 -> 2026-09-11_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.21)
- Tendencia: `neutral` (SPY 757.83 · MA50 758.25 · MA200 711.5 · dist MA200: 6.51%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.39)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 757.83 | -0.6% | -0.96% | -1.9% |
| CSQ | 12.0% | satellite | 20.6 | -1.2% | -1.39% | -0.66% |
| QQQ | 9.8% | core | 708.69 | -1.06% | -0.08% | -2.07% |
| TLT | 9.8% | core | 80.78 | -1.16% | -1.43% | -1.24% |
| GLD | 7.3% | core | 396.36 | -1.73% | -1.59% | -2.11% |
| IEF | 4.9% | core | 91.18 | -0.78% | -1.08% | -1.56% |
| BLFS | 4.8% | satellite | 34.92 | -0.03% | -2.78% | -0.14% |
| PRGO | 3.5% | satellite | 13.59 | -5.23% | -6.21% | 9.3% |
| UPST | 3.4% | satellite | 25.1 | -3.05% | -10.9% | -13.75% |
| TWST | 2.5% | satellite | 126.85 | 1.06% | -3.17% | 1.31% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 11.8%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -3.1%
- Beta vs SPY: 0.762 · posiciones efectivas: 16.4 · HHI: 0.0611

**Por que estos satellite (señales WATCHDOG):**

- **CSQ** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **TWST** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **BLFS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PRGO** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **UPST** · score agregado 66.0 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GRCE | 78 | corporate_insider | Kohli Prashant | 2 | $214,000 | cluster_buy |
| PRTS | 77 | corporate_insider | Meniane David | 2 | $133,295 | cluster_buy |
| PRTS | 72 | corporate_insider | Huffaker Michael | 2 | $133,295 | cluster_buy |
| ZDGE | 72 | large_holder | Michael Jonas |  | - | - |
| MGX | 72 | large_holder | Thomas Brian C. |  | - | - |
| BLFS | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| TWST | 72 | large_holder | ARK Investment Management |  | - | - |
| TWST | 72 | large_holder | FMR LLC |  | - | - |
| QVCG | 72 | large_holder | Barclays PLC |  | - | - |
| QVCG | 72 | large_holder | Barclays PLC |  | - | - |
| PRGO | 72 | large_holder | T. Rowe Price Associates, |  | - | - |
| SIG | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| GRCE | 71 | corporate_insider | Opaleye Management Inc. | 2 | $19,699 | cluster_buy,small_amount |
| QVCG | 71 | corporate_insider | GOLDENTREE ASSET MANAGEME | 0 | $26,000,000 | - |
| UBER | 70 | corporate_insider | KHOSROWSHAHI DARA | 0 | $10,005,952 | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| QVCG | 58 | corporate_insider | Silver Point Capital L.P. | $26,000,000 | - |
| LRCX | 58 | corporate_insider | ARCHER TIMOTHY | $9,577,800 | - |
| SITM | 58 | corporate_insider | VASHIST RAJESH | $7,241,640 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $5,725,979 | - |
| DDOG | 57 | corporate_insider | Pomel Olivier | $5,063,681 | - |
| VST | 56 | corporate_insider | HUDSON SCOTT A | $4,377,228 | - |
| LASR | 56 | corporate_insider | Keeney Scott H | $4,101,000 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $4,002,735 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 757.83 (-0.6% / -0.96% / -1.9%) [2026-09-10]
- QQQ: 708.69 (-1.06% / -0.08% / -2.07%) [2026-09-10]
- IWM: 287.7 (-1.01% / -2.15% / -4.96%) [2026-09-10]
- DIA: 520.75 (-0.63% / -1.86% / -2.97%) [2026-09-10]
- TLT: 80.78 (-1.16% / -1.43% / -1.24%) [2026-09-10]
- IEF: 91.18 (-0.78% / -1.08% / -1.56%) [2026-09-10]
- GLD: 396.36 (-1.73% / -1.59% / -2.11%) [2026-09-10]
- ^VIX: 17.21 (-3.53% / 18.44% / 20.77%) [2026-09-11]
- BTC-USD: 76998.61 (0.56% / -4.17% / -0.11%) [2026-09-11]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.43 (delta 1m: 0.18) [2026-09-09]
- Treasury 10Y yield: 4.83 (delta 1m: 0.11) [2026-09-09]
- Curva 10Y-2Y: 0.39 (delta 1m: -0.09) [2026-09-10]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.71 (delta 1m: -0.01) [2026-09-09]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.4 (delta 1m: 0.13) [2026-09-10]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), leadership (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [RBRK] Arvind Nithrakashyap Sells 12 , 820 Shares of Rubrik ( NYSE : RBRK ) Stock (2026-09-11)
- [CRCL] Insider Selling : Circle Internet Group ( NYSE : CRCL ) CEO Sells 56 , 200 Shares of Stock (2026-09-10)
- [CRWV] CoreWeave ( NASDAQ : CRWV ) Trading Up 11 . 7 % – Here Why (2026-09-10)
- [CRCL] Nikhil Chandhok Sells 26 , 666 Shares of Circle Internet Group ( NYSE : CRCL ) Stock (2026-09-10)
- [RBRK] Is CrowdStrike Holdings ( CRWD ) Stock Still the Better Cybersecurity Bet as Rubrik ( RBRK ) Accelerates ? (2026-09-09)

**Actores que han movido ficha este mes (top movimientos):**

- CEO KHOSROWSHAHI DARA compro UBER por $10.0M el 2026-09-10.
- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro QVCG por $26.0M el 2026-09-08 [senal en multiples fuentes].
- CEO ARCHER TIMOTHY vendio LRCX por $9.6M el 2026-09-09.
- CEO Gu Paul compro UPST por $1.3M el 2026-09-10.
- CEO VASHIST RAJESH vendio SITM por $7.2M el 2026-09-09.
- CEO Miles Patrick compro ATEC por $1.0M el 2026-09-10.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- Diabolical-Prize · PnL $249,864 · win rate 94% · categorias: sports
- Kch-Temp · PnL $239,355 · win rate 89% · categorias: sports
- BreakTheBank · PnL $420,413 · win rate 85% · categorias: sports
- mmklop · PnL $39,273 · win rate 96% · categorias: sports
- JnStrtPrdctnMrkts · PnL $36,194 · win rate 91% · categorias: crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 757 registros 30d · ultimo dato 2026-09-10
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-10
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BLFS, CSQ, GLD, IEF, PRGO, QQQ, SPY, TLT, TWST, UPST`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **70.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
