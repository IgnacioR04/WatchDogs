# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-28T10:05:51+00:00 · ventana señales 2026-06-28 -> 2026-07-28_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.86)
- Tendencia: `neutral` (SPY 739.09 · MA50 744.08 · MA200 695.81 · dist MA200: 6.22%)
- Credito: `tight` (HY spread 2.79)
- Tipos: `flat` (curva 10y-2y 0.34)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 739.09 | 0.02% | -0.4% | 1.39% |
| QQQ | 9.8% | core | 682.12 | -0.31% | -2.0% | -3.45% |
| TLT | 9.8% | core | 83.75 | 0.6% | -0.17% | -3.78% |
| GLD | 7.3% | core | 374.63 | 0.73% | 1.91% | 0.27% |
| FSBC | 6.9% | satellite | 47.21 | -0.3% | -3.28% | -1.01% |
| BEP | 5.1% | satellite | 32.13 | -2.84% | 1.16% | -8.8% |
| IEF | 4.9% | core | 93.28 | 0.46% | -0.6% | -1.27% |
| FIS | 4.0% | satellite | 43.16 | 7.79% | 2.98% | 14.0% |
| NMM | 3.7% | satellite | 77.71 | 1.16% | 8.88% | 11.44% |
| BSY | 3.5% | satellite | 33.71 | 11.92% | 4.24% | 17.42% |
| ENR | 3.1% | satellite | 21.04 | 1.89% | 4.0% | -5.86% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.7%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -3.8%
- Beta vs SPY: 0.512 · posiciones efectivas: 18.6 · HHI: 0.0537

**Por que estos satellite (señales WATCHDOG):**

- **FSBC** · score agregado 557.7 · 7 señales · fuentes: corporate_insider
- **ENR** · score agregado 369.3 · 6 señales · fuentes: corporate_insider
- **NMM** · score agregado 189.8 · 3 señales · fuentes: corporate_insider
- **BSY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **FIS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| FSBC | 86 | corporate_insider | Allbaugh Larry Eugene | 6 | $3,999,996 | cluster_buy |
| FSBC | 82 | corporate_insider | Perry-Smith Robert Truxtu | 6 | $1,379,972 | cluster_buy |
| FSBC | 80 | corporate_insider | Allbaugh Larry Eugene | 6 | $250,008 | cluster_buy |
| FSBC | 78 | corporate_insider | Deary-Bell Shannon | 6 | $250,008 | cluster_buy |
| FSBC | 78 | corporate_insider | Ramos Kevin Francis | 6 | $250,008 | cluster_buy |
| FSBC | 76 | corporate_insider | Riggs Judson Teichert | 6 | $100,012 | cluster_buy |
| FSBC | 75 | corporate_insider | Lucas Donna | 6 | $49,984 | cluster_buy |
| NMM | 74 | corporate_insider | Frangou Angeliki | 0 | $846,122,589 | - |
| SCTX | 72 | corporate_insider | Parrot David | 2 | $19,995 | cluster_buy,small_amount |
| SCTX | 72 | corporate_insider | Parrot David | 2 | $19,995 | cluster_buy,small_amount |
| CRAI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| BSY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ADBE | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ACHC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CRDO | 72 | large_holder | BlackRock, Inc. |  | - | - |

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
| CSX | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 739.09 (0.02% / -0.4% / 1.39%) [2026-07-27]
- QQQ: 682.12 (-0.31% / -2.0% / -3.45%) [2026-07-27]
- IWM: 292.91 (0.6% / 0.21% / -2.31%) [2026-07-27]
- DIA: 521.26 (0.48% / 0.64% / 0.71%) [2026-07-27]
- TLT: 83.75 (0.6% / -0.17% / -3.78%) [2026-07-27]
- IEF: 93.28 (0.46% / -0.6% / -1.27%) [2026-07-27]
- GLD: 374.63 (0.73% / 1.91% / 0.27%) [2026-07-27]
- ^VIX: 18.86 (1.02% / 1.13% / 2.44%) [2026-07-28]
- BTC-USD: 63301.12 (-0.67% / -2.68% / 1.68%) [2026-07-28]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.33 (delta 1m: 0.22) [2026-07-24]
- Treasury 10Y yield: 4.69 (delta 1m: 0.28) [2026-07-24]
- Curva 10Y-2Y: 0.34 (delta 1m: 0.03) [2026-07-27]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.79 (delta 1m: 0.01) [2026-07-24]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.21 (delta 1m: 0.0) [2026-07-27]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (2), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DDOG] CoreWeave vs . Datadog : What Do the Revenue Trends of These High - Growth Tech Companies Tell Investors ? (2026-07-25)
- [SYM] Why Symbotic Stock Dropped 24 % in the First Half of 2026 And Is a Screaming Buy Now (2026-07-23)
- [SYM] Is Symbotic ( SYM ) One Of The Best Low - Priced AI Stocks To Buy Right Now ? (2026-07-16)
- [SYM] Is Symbotic ( SYM ) One Of The Best Low - Priced AI Stocks To Buy Right Now ? (2026-07-14)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Frangou Angeliki compro NMM por $846.1M el 2026-07-23.
- CEO Huang Jack Jiajia compro COE por $8.3M el 2026-07-21.
- 10% owner Abu Dhabi Investment Authority compro Jefferies Credit Partners BDC Inc. por $25.0M el 2026-07-23.
- CEO Huang Jack Jiajia compro COE por $4.8M el 2026-07-23.
- CEO Palmer Sheryl vendio TMHC por $19.4M el 2026-07-24.
- CEO Huang Jack Jiajia compro COE por $2.0M el 2026-07-22.
- 10% owner ASSURED GUARANTY LTD compro Sound Point Direct Lending BDC por $5.2M el 2026-07-22.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- monkeymashingkeyboard · PnL $125,831 · win rate 91% · categorias: sports
- 0xe11Ff8cd2718F51a4d9403D166c20eaAAbE253F4-1777047101622 · PnL $112,719 · win rate 89% · categorias: sports, crypto
- 0x27c5C1EEE404a07F39FE70078AFf815E5a656D61-1763107503028 · PnL $122,359 · win rate 88% · categorias: sports, crypto
- comon119 · PnL $11,489 · win rate 98% · categorias: sports, crypto, politics
- 0x6982049c65e98606f65A0CE71fDb9b61296dA165-1777135114945 · PnL $11,685 · win rate 98% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 71 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 496 registros 30d · ultimo dato 2026-07-27
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-27
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BSY, ENR, FIS, FSBC, GLD, IEF, NMM, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
