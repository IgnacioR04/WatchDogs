# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-03T15:34:54+00:00 · ventana señales 2026-07-04 -> 2026-08-03_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.63)
- Tendencia: `bull` (SPY 755.4 · MA50 744.54 · MA200 697.9 · dist MA200: 8.24%)
- Credito: `tight` (HY spread 2.84)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 755.4 | 1.12% | 2.21% | 0.55% |
| QQQ | 12.0% | core | 696.82 | 1.28% | 2.16% | -3.6% |
| TLT | 12.0% | core | 82.22 | -0.04% | -1.83% | -3.78% |
| GLD | 9.3% | core | 369.89 | -0.44% | -1.27% | -3.2% |
| BEP | 7.3% | satellite | 33.96 | 3.35% | 5.7% | 0.5% |
| NRIM | 6.5% | satellite | 27.08 | 2.15% | 1.27% | -0.7% |
| NTST | 6.5% | satellite | 21.32 | -0.63% | -2.49% | -0.72% |
| IEF | 6.2% | core | 92.79 | -0.17% | -0.53% | -1.48% |
| CPRI | 4.0% | satellite | 16.33 | 2.51% | 2.83% | -13.32% |
| TRIP | 3.5% | satellite | 14.27 | 0.67% | -0.11% | 2.77% |
| PWP | 2.2% | satellite | 16.82 | -4.7% | 4.02% | -2.32% |
| PRIM | 1.8% | satellite | 86.76 | 2.79% | 1.44% | -3.81% |
| SPCX | 1.8% | satellite | 110.56 | 2.02% | -2.59% | -31.08% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.8%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -4.3%
- Beta vs SPY: 0.575 · posiciones efectivas: 13.6 · HHI: 0.0734

**Por que estos satellite (señales WATCHDOG):**

- **NTST** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **PWP** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **TRIP** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **PRIM** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CPRI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NRIM** · score agregado 71.8 · 1 señales · fuentes: large_holder
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
| NRIM | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| MIDD | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| NOA | 70 | large_holder | CIBC Global Asset Managme |  | - | - |

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

- SPY: 755.4 (1.12% / 2.21% / 0.55%) [2026-08-03]
- QQQ: 696.82 (1.28% / 2.16% / -3.6%) [2026-08-03]
- IWM: 295.37 (1.43% / 0.84% / -1.18%) [2026-08-03]
- DIA: 529.57 (1.0% / 1.59% / -0.07%) [2026-08-03]
- TLT: 82.22 (-0.04% / -1.83% / -3.78%) [2026-08-03]
- IEF: 92.79 (-0.17% / -0.53% / -1.48%) [2026-08-03]
- GLD: 369.89 (-0.44% / -1.27% / -3.2%) [2026-08-03]
- ^VIX: 15.63 (-2.25% / -16.28% / 0.39%) [2026-08-03]
- BTC-USD: 63711.5 (0.36% / -0.31% / -1.92%) [2026-08-03]

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

**Temas dominantes**: ai (1), stock (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CPRI] Capri jeans are back : 4 street style - proof ways to wear the 2000s trend (2026-08-03)
- [TLRY] Tilray Brands climbs 8 %, extending prior day gains ( TLRY : NASDAQ ) (2026-07-31)
- [TLRY] Tilray Brands ( NASDAQ : TLRY ) Stock Price Up 5 . 3 % – Should You Buy ? (2026-07-30)
- [TLRY] Tilray Brands ( NASDAQ : TLRY ) Trading Up 5 . 3 % – Should You Buy ? (2026-07-30)
- [TLRY] Tilray Brands Q4 Earnings Call Highlights (2026-07-30)
- [UEC] Uranium Energy Is Down Sharply in 2026 . Here What the Next 10 Years Could Realistically Look Like . (2026-07-30)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner TPG GP A, LLC compro TPG Twin Brook Capital Income Fund por $50.0M el 2026-07-29.
- 10% owner MITSUBISHI UFJ FINANCIAL GROUP INC vendio MS por $88.4M el 2026-07-30 [senal en multiples fuentes].
- 10% owner Refo SCSp vendio REF por $41.7M el 2026-07-31.
- 10% owner FTV VII, L.P. vendio NP por $62.0M el 2026-07-29.
- 10% owner BSIV Hold 101, LP vendio NP por $54.2M el 2026-07-29.
- 10% owner Bregal Sagemount I, L.P. opero LPRO por $23.8M el 2026-07-28.
- CEO Christopher Gregory L. opero MLI por $13.7M el 2026-07-30.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- 0x6982049c65e98606f65A0CE71fDb9b61296dA165-1777135114945 · PnL $14,849 · win rate 98% · categorias: sports, crypto
- matenghehe · PnL $17,117 · win rate 96% · categorias: sports, crypto
- esportGG · PnL $11,011 · win rate 95% · categorias: sports
- TAIWANNUMBERONE · PnL $19,379 · win rate 91% · categorias: sports, politics
- 0x0x23kjookhaiuohduoayh8c9 · PnL $10,525 · win rate 94% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 45 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 590 registros 30d · ultimo dato 2026-08-01
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-03
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, CPRI, GLD, IEF, NRIM, NTST, PRIM, PWP, QQQ, SPCX, SPY, TLT, TRIP`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
