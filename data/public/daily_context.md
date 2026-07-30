# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-30T09:59:00+00:00 · ventana señales 2026-06-30 -> 2026-07-30_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 19.53)
- Tendencia: `neutral` (SPY 729.46 · MA50 743.82 · MA200 696.49 · dist MA200: 4.73%)
- Credito: `tight` (HY spread 2.84)
- Tipos: `flat` (curva 10y-2y 0.45)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 729.46 | -1.54% | -2.4% | -2.32% |
| QQQ | 9.8% | core | 661.73 | -2.04% | -6.18% | -10.14% |
| TLT | 9.8% | core | 82.85 | -1.65% | -0.71% | -3.78% |
| BEP | 8.3% | satellite | 31.65 | -1.06% | -1.71% | -8.87% |
| EQBK | 7.5% | satellite | 50.72 | -0.51% | 1.52% | 3.53% |
| GLD | 7.3% | core | 371.08 | 0.46% | -2.12% | 0.73% |
| IEF | 4.9% | core | 93.17 | -0.42% | 0.08% | -1.16% |
| VSXY | 3.6% | satellite | 89.13 | -0.2% | 2.05% | 6.77% |
| KTOS | 2.8% | satellite | 43.88 | -9.79% | -8.37% | -11.99% |
| SPCX | 1.8% | satellite | 112.55 | -3.32% | -2.35% | -34.13% |
| ODD | 1.8% | satellite | 14.97 | -11.89% | -8.61% | -1.06% |
| NXTC | 0.3% | satellite | 5.02 | -7.38% | 14.09% | 213.75% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.3%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -2.4%
- Beta vs SPY: 0.518 · posiciones efectivas: 17.7 · HHI: 0.0566

**Por que estos satellite (señales WATCHDOG):**

- **SPCX** · score agregado 241.4 · 4 señales · fuentes: congress
- **NXTC** · score agregado 112.5 · 2 señales · fuentes: corporate_insider
- **VSXY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KTOS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **ODD** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress
- **EQBK** · score agregado 55.0 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SCTX | 87 | corporate_insider | GORDON CARL L | 3 | $15,000,000 | cluster_buy |
| SCTX | 87 | corporate_insider | ORBIMED ADVISORS LLC | 3 | $15,000,000 | cluster_buy |
| SCTX | 87 | corporate_insider | AH Bio Fund II, L.P. | 3 | $4,999,995 | cluster_buy |
| VSXY | 72 | large_holder | BBFIT INVESTMENTS PTE LTD |  | - | - |
| PPIH | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NPKI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| LHX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| MUX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| LMND | 72 | large_holder | BlackRock, Inc. |  | - | - |
| KTOS | 72 | large_holder | BlackRock, Inc. |  | - | - |
| EDIT | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ODD | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NNOX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| MGA | 72 | large_holder | BlackRock, Inc. |  | - | - |
| POR | 72 | large_holder | Clearbridge Investments,  |  | - | - |

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
| MGA | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 729.46 (-1.54% / -2.4% / -2.32%) [2026-07-29]
- QQQ: 661.73 (-2.04% / -6.18% / -10.14%) [2026-07-29]
- IWM: 288.57 (-1.64% / -1.78% / -3.95%) [2026-07-29]
- DIA: 515.41 (-2.18% / -1.16% / -1.31%) [2026-07-29]
- TLT: 82.85 (-1.65% / -0.71% / -3.78%) [2026-07-29]
- IEF: 93.17 (-0.42% / 0.08% / -1.16%) [2026-07-29]
- GLD: 371.08 (0.46% / -2.12% / 0.73%) [2026-07-29]
- ^VIX: 19.53 (-5.47% / 4.44% / 17.72%) [2026-07-30]
- BTC-USD: 64491.43 (0.91% / 0.28% / 0.57%) [2026-07-30]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.26 (delta 1m: 0.19) [2026-07-28]
- Treasury 10Y yield: 4.61 (delta 1m: 0.23) [2026-07-28]
- Curva 10Y-2Y: 0.45 (delta 1m: 0.17) [2026-07-29]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.84 (delta 1m: 0.04) [2026-07-28]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.26 (delta 1m: 0.04) [2026-07-29]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (9), leadership (2), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [NTRA] Natera , Inc . ( NASDAQ : NTRA ) Receives $267 . 83 Consensus Price Target from Brokerages (2026-07-30)
- [NTRA] Michael Burkes Brophy Sells 1 , 863 Shares of Natera ( NASDAQ : NTRA ) Stock (2026-07-30)
- [NTRA] John Fesko Sells 782 Shares of Natera ( NASDAQ : NTRA ) Stock (2026-07-30)
- [NTRA] Natera ( NASDAQ : NTRA ) Insider Solomon Moshkevich Sells 1 , 010 Shares of Stock (2026-07-30)
- [NTRA] Insider Selling : Natera ( NASDAQ : NTRA ) CEO Sells 3 , 580 Shares (2026-07-30)
- [CRWV] Insider Selling : CoreWeave ( NASDAQ : CRWV ) Insider Sells 144 , 000 Shares (2026-07-30)
- [NTRA] Insider Selling : Natera ( NASDAQ : NTRA ) Insider Sells 1 , 204 Shares (2026-07-30)
- [CRWV] CoreWeave CEO Sold Company Stock Worth Nearly $25 Million Amid Share Price Declines . Here a Closer Look at the Transaction . (2026-07-30)
- [CRWV] Nebius ( NASDAQ : NBIS ) And CoreWeave ( NASDAQ : CRWV ) Stock Plunge As Credit - Swap Costs Threaten AI Infrastructure Financing (2026-07-29)
- [CRWV] CoreWeave Stock Hits New 52 - Week Low : What Driving the Neocloud Selloff ? - CoreWeave ( NASDAQ : CRWV ) (2026-07-29)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner BBRC INTERNATIONAL PTE LTD vendio VSXY por $64.0M el 2026-07-28 [senal en multiples fuentes].
- 10% owner Gebbia Joseph vendio ABNB por $175.2M el 2026-07-28.
- 10% owner ADVENT INTERNATIONAL, L.P. vendio LUNR por $147.6M el 2026-07-28.
- CEO Barra Mary T vendio GM por $9.8M el 2026-07-28.
- 10% owner AH Bio Fund II, L.P. compro SCTX por $5.0M el 2026-07-27 [senal en multiples fuentes].
- Director GORDON CARL L compro SCTX por $15.0M el 2026-07-27 [senal en multiples fuentes].
- CEO Reuss Mark L vendio GM por $6.4M el 2026-07-28.
- CEO Lian Brian vendio VKTX por $4.9M el 2026-07-29.

**Polymarket — smart money (traders con mejor track record):**

- 0x27c5C1EEE404a07F39FE70078AFf815E5a656D61-1763107503028 · PnL $117,789 · win rate 88% · categorias: sports, crypto
- esportGG · PnL $36,625 · win rate 95% · categorias: sports
- SDTrading · PnL $43,264 · win rate 92% · categorias: sports
- matenghehe · PnL $12,576 · win rate 96% · categorias: sports, crypto
- JnStTrdrBnusFnd · PnL $21,500 · win rate 91% · categorias: crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 47 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 735 registros 30d · ultimo dato 2026-07-29
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-29
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, EQBK, GLD, IEF, KTOS, NXTC, ODD, QQQ, SPCX, SPY, TLT, VSXY`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
