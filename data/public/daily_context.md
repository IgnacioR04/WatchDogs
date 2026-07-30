# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-30T20:56:46+00:00 · ventana señales 2026-06-30 -> 2026-07-30_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.09)
- Tendencia: `neutral` (SPY 741.69 · MA50 743.92 · MA200 696.96 · dist MA200: 6.42%)
- Credito: `tight` (HY spread 2.87)
- Tipos: `flat` (curva 10y-2y 0.45)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 741.69 | 1.68% | 0.48% | -0.55% |
| QQQ | 9.8% | core | 683.55 | 3.3% | -1.22% | -5.74% |
| TLT | 9.8% | core | 82.8 | -0.06% | -0.44% | -3.18% |
| GLD | 7.3% | core | 377.16 | 1.64% | 1.52% | 1.77% |
| BEP | 5.3% | satellite | 32.66 | 3.19% | -1.24% | -4.98% |
| BFST | 5.0% | satellite | 31.94 | -0.22% | 4.82% | 1.65% |
| IEF | 4.9% | core | 93.21 | 0.04% | 0.39% | -0.87% |
| EQBK | 4.7% | satellite | 50.73 | 0.02% | 2.34% | 1.06% |
| ZTS | 4.2% | satellite | 76.03 | -2.44% | 1.96% | 5.67% |
| TSM | 2.1% | satellite | 403.31 | 7.64% | -2.95% | -9.21% |
| REAL | 2.1% | satellite | 11.91 | 1.88% | 4.75% | -2.38% |
| PRGS | 1.6% | satellite | 40.34 | -5.55% | 9.26% | 3.01% |
| SPCX | 1.2% | satellite | 112.2 | -0.31% | -5.11% | -28.78% |
| NXTC | 0.2% | satellite | 5.03 | 0.2% | 20.33% | 157.95% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 7.8%
- VaR 95% 1d: 0.7% · CVaR 95% 1d: 0.8%
- Max drawdown historico: -1.8%
- Beta vs SPY: 0.48 · posiciones efectivas: 19.3 · HHI: 0.0517

**Por que estos satellite (señales WATCHDOG):**

- **SPCX** · score agregado 241.4 · 4 señales · fuentes: congress
- **NXTC** · score agregado 112.5 · 2 señales · fuentes: corporate_insider
- **ZTS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **REAL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PRGS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress
- **TSM** · score agregado 56.3 · 1 señales · fuentes: corporate_insider
- **EQBK** · score agregado 55.0 · 1 señales · fuentes: corporate_insider
- **BFST** · score agregado 54.9 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| [NONE] | 84 | corporate_insider | VEP Group, LLC | 2 | $6,229,807 | cluster_buy |
| STRL | 72 | large_holder | BlackRock, Inc. |  | - | - |
| SMTC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ZTS | 72 | large_holder | BlackRock, Inc. |  | - | - |
| WDAY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| VOYG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| VLTO | 72 | large_holder | BlackRock, Inc. |  | - | - |
| REAL | 72 | large_holder | BlackRock, Inc. |  | - | - |
| PRGS | 72 | large_holder | BlackRock, Inc. |  | - | - |
| PPIH | 72 | large_holder | BlackRock, Inc. |  | - | - |
| PEBK | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NPKI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| LHX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| REKR | 70 | large_holder | Maybank Securities Pte. L |  | - | - |
| VSH | 70 | large_holder | BlackRock, Inc. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| CRDO | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |
| SMTC | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 741.69 (1.68% / 0.48% / -0.55%) [2026-07-30]
- QQQ: 683.55 (3.3% / -1.22% / -5.74%) [2026-07-30]
- IWM: 292.59 (1.39% / 0.17% / -2.25%) [2026-07-30]
- DIA: 521.51 (1.18% / 1.02% / -0.14%) [2026-07-30]
- TLT: 82.8 (-0.06% / -0.44% / -3.18%) [2026-07-30]
- IEF: 93.21 (0.04% / 0.39% / -0.87%) [2026-07-30]
- GLD: 377.16 (1.64% / 1.52% / 1.77%) [2026-07-30]
- ^VIX: 17.09 (-17.28% / -8.61% / 3.01%) [2026-07-30]
- BTC-USD: 64767.07 (1.34% / 0.71% / 1.0%) [2026-07-30]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.22 (delta 1m: 0.12) [2026-07-29]
- Treasury 10Y yield: 4.67 (delta 1m: 0.29) [2026-07-29]
- Curva 10Y-2Y: 0.45 (delta 1m: 0.17) [2026-07-29]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.87 (delta 1m: 0.12) [2026-07-29]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.26 (delta 1m: 0.04) [2026-07-29]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: regulatory (4), stock (1), earnings (1), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [GM] General Motors future models 2026 - 2036 , Part 2 (2026-07-30)
- [BSVN] Jason Estes Sells 3 , 225 Shares of Bank7 ( NASDAQ : BSVN ) Stock (2026-07-28)
- [BSVN] Bank7 ( BSVN ) Q2 2026 Earnings Call Transcript (2026-07-23)
- [BSVN] Bank7 ( NASDAQ : BSVN ) Hits New 1 - Year High – Here Why (2026-07-17)
- [BSVN] Bank7 targets Sept . 3 close for contested NM rival buyout (2026-07-16)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Huang Jack Jiajia compro COE por $7.7M el 2026-07-27.
- 10% owner Abu Dhabi Investment Authority compro Overland Advantage por $22.9M el 2026-07-28.
- 10% owner VEP Group, LLC compro [NONE] por $6.2M el 2026-07-29.
- CEO Huang Jack Jiajia compro COE por $3.0M el 2026-07-24.
- CEO Barra Mary T vendio GM por $9.8M el 2026-07-28.
- 10% owner AH Bio Fund II, L.P. compro SCTX por $5.0M el 2026-07-27 [senal en multiples fuentes].
- CEO Reuss Mark L vendio GM por $6.4M el 2026-07-28.
- CEO Gosin Barry M vendio NMRK por $4.5M el 2026-07-29.

**Polymarket — smart money (traders con mejor track record):**

- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $97,070 · win rate 96% · categorias: sports
- 111111111115 · PnL $77,717 · win rate 94% · categorias: sports
- 0xe11Ff8cd2718F51a4d9403D166c20eaAAbE253F4-1777047101622 · PnL $121,151 · win rate 90% · categorias: sports, crypto
- JnStTrdrBnusFnd · PnL $50,839 · win rate 91% · categorias: crypto
- SDTrading · PnL $35,208 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 47 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 666 registros 30d · ultimo dato 2026-07-30
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-30
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BFST, EQBK, GLD, IEF, NXTC, PRGS, QQQ, REAL, SPCX, SPY, TLT, TSM, ZTS`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
