# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-27T22:34:09+00:00 · ventana señales 2026-06-27 -> 2026-07-27_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.67)
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
| FSBC | 8.1% | satellite | 47.21 | 0.85% | -3.73% | -2.54% |
| GLD | 7.3% | core | 374.63 | 0.73% | 1.91% | 0.27% |
| BEP | 5.9% | satellite | 32.13 | -2.99% | 0.25% | -8.9% |
| IEF | 4.9% | core | 93.28 | 0.27% | -0.28% | -1.52% |
| FIS | 4.7% | satellite | 43.16 | 3.97% | 2.11% | 11.9% |
| BSY | 4.0% | satellite | 33.71 | 7.36% | 4.2% | 12.37% |
| ENR | 3.6% | satellite | 21.04 | 0.38% | 3.39% | -7.07% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.7%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -3.8%
- Beta vs SPY: 0.502 · posiciones efectivas: 17.8 · HHI: 0.0563

**Por que estos satellite (señales WATCHDOG):**

- **FSBC** · score agregado 557.7 · 7 señales · fuentes: corporate_insider
- **ENR** · score agregado 369.3 · 6 señales · fuentes: corporate_insider
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
| CRAI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| BSY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ADBE | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ACHC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CRDO | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NCO | 72 | large_holder | Feis Equities LLC |  | - | - |
| FIS | 72 | large_holder | JPMORGAN CHASE & CO. |  | - | - |
| EVGN | 70 | large_holder | L.I.A. Pure Capital Ltd. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| ADBE | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CSX | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| HSY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CRDO | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 739.09 (0.02% / -0.4% / 1.39%) [2026-07-27]
- QQQ: 682.12 (-0.31% / -2.0% / -3.45%) [2026-07-27]
- IWM: 292.91 (0.6% / 0.21% / -2.31%) [2026-07-27]
- DIA: 521.26 (0.48% / 0.64% / 0.71%) [2026-07-27]
- TLT: 83.75 (0.6% / -0.17% / -3.78%) [2026-07-27]
- IEF: 93.28 (0.27% / -0.28% / -1.52%) [2026-07-27]
- GLD: 374.63 (0.73% / 1.91% / 0.27%) [2026-07-27]
- ^VIX: 18.67 (0.48% / 0.11% / 1.41%) [2026-07-27]
- BTC-USD: 64533.71 (-1.23% / -2.37% / 1.95%) [2026-07-27]

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

**Temas dominantes**: merger (3), stock (3), earnings (2), ai (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TMHC] Taylor Morrison Home Shareholders Approve Berkshire Hathaway Merger (2026-07-25)
- [DDOG] CoreWeave vs . Datadog : What Do the Revenue Trends of These High - Growth Tech Companies Tell Investors ? (2026-07-25)
- [TMHC] 2026 - 07 - 24 | Berkshire Hathaway Completes Acquisition of Taylor Morrison | TSX : BRK (2026-07-24)
- [TMHC] Berkshire Hathaway Completes Acquisition of Taylor Morrison (2026-07-24)
- [SYM] Why Symbotic Stock Dropped 24 % in the First Half of 2026 And Is a Screaming Buy Now (2026-07-23)
- [TMHC] Taylor Morrison Home ( TMHC ) Expected to Announce Quarterly Earnings on Wednesday (2026-07-21)
- [SYM] Is Symbotic ( SYM ) One Of The Best Low - Priced AI Stocks To Buy Right Now ? (2026-07-16)
- [SYM] Is Symbotic ( SYM ) One Of The Best Low - Priced AI Stocks To Buy Right Now ? (2026-07-14)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Huang Jack Jiajia compro COE por $8.3M el 2026-07-21.
- 10% owner Abu Dhabi Investment Authority compro Jefferies Credit Partners BDC Inc. por $25.0M el 2026-07-23.
- CEO Huang Jack Jiajia compro COE por $4.8M el 2026-07-23.
- CEO Palmer Sheryl vendio TMHC por $19.4M el 2026-07-24.
- CEO Huang Jack Jiajia compro COE por $2.0M el 2026-07-22.
- 10% owner ASSURED GUARANTY LTD compro Sound Point Direct Lending BDC por $5.2M el 2026-07-22.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.

**Polymarket — smart money (traders con mejor track record):**

- SDTrading · PnL $41,755 · win rate 93% · categorias: sports
- ToeTickler98 · PnL $34,012 · win rate 91% · categorias: sports
- laozishudaosan · PnL $16,853 · win rate 94% · categorias: sports
- Uniform123 · PnL $42,737 · win rate 87% · categorias: sports
- wan123 · PnL $93,686 · win rate 79% · categorias: sports, politics, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-07-20
- **sec_insiders**: `ok` · 488 registros 30d · ultimo dato 2026-07-27
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-27
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BSY, ENR, FIS, FSBC, GLD, IEF, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
