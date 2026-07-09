# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-09T20:24:21+00:00 · ventana señales 2026-06-09 -> 2026-07-09_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.86)
- Tendencia: `bull` (SPY 751.71 · MA50 739.0 · MA200 690.63 · dist MA200: 8.84%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.35)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 751.71 | 0.85% | 0.8% | 2.25% |
| QQQ | 12.0% | core | 723.28 | 1.66% | -0.26% | 2.3% |
| TLT | 12.0% | core | 84.49 | 0.15% | -1.2% | -0.37% |
| BEP | 12.0% | satellite | 32.98 | -1.2% | -4.04% | -9.54% |
| GLD | 9.3% | core | 378.18 | 1.0% | 2.05% | -3.22% |
| IEF | 6.2% | core | 93.71 | 0.21% | -0.34% | 0.26% |
| RH | 5.3% | satellite | 168.33 | 3.53% | 2.61% | 12.15% |
| WRBY | 4.5% | satellite | 29.32 | 5.96% | -0.17% | 18.13% |
| NUVL | 4.4% | satellite | 123.83 | 0.02% | 0.19% | 0.47% |
| INTC | 3.8% | satellite | 112.54 | 2.09% | -11.4% | 4.28% |
| APGE | 3.5% | satellite | 133.57 | 0.24% | 0.6% | 57.14% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 17.0%
- VaR 95% 1d: 1.6% · CVaR 95% 1d: 2.0%
- Max drawdown historico: -4.7%
- Beta vs SPY: 0.925 · posiciones efectivas: 12.6 · HHI: 0.0796

**Por que estos satellite (señales WATCHDOG):**

- **APGE** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **RH** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WRBY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NUVL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BBASX | 81 | corporate_insider | AMG New York Holdings Cor | 2 | $1,826,012 | cluster_buy |
| BBASX | 78 | corporate_insider | BROWN BROTHERS HARRIMAN C | 2 | $456,503 | cluster_buy |
| TSM | 76 | corporate_insider | Wei Che-Chia | 31 | $11,187 | cluster_buy,small_amount |
| RH | 72 | large_holder | Gary G. Friedman |  | - | - |
| RSI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CAG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| WRBY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| OVID | 72 | large_holder | Federated Hermes, Inc. |  | - | - |
| NUVL | 72 | large_holder | FMR LLC |  | - | - |
| CYTK | 72 | large_holder | FMR LLC |  | - | - |
| TSM | 71 | corporate_insider | Huang Jen-Chau | 31 | $2,145 | cluster_buy,small_amount |
| TSM | 71 | corporate_insider | Chin Yung-Pei | 31 | $5,287 | cluster_buy,small_amount |
| TSM | 71 | corporate_insider | Mii Yuh-Jier | 31 | $5,210 | cluster_buy,small_amount |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| MAAS | 70 | large_holder | Golden Brighter Limited |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| AESI | 64 | congress | Chip Roy | $250,000 | - |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| XOM | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 751.71 (0.85% / 0.8% / 2.25%) [2026-07-09]
- QQQ: 723.28 (1.66% / -0.26% / 2.3%) [2026-07-09]
- IWM: 297.27 (1.29% / -0.68% / 4.55%) [2026-07-09]
- DIA: 524.19 (0.27% / 0.34% / 3.18%) [2026-07-09]
- TLT: 84.49 (0.15% / -1.2% / -0.37%) [2026-07-09]
- IEF: 93.71 (0.21% / -0.34% / 0.26%) [2026-07-09]
- GLD: 378.18 (1.0% / 2.05% / -3.22%) [2026-07-09]
- ^VIX: 15.86 (-6.15% / -4.4% / -20.18%) [2026-07-09]
- BTC-USD: 63188.17 (1.49% / 0.16% / -0.56%) [2026-07-09]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.21 (delta 1m: 0.04) [2026-07-08]
- Treasury 10Y yield: 4.56 (delta 1m: 0.01) [2026-07-08]
- Curva 10Y-2Y: 0.35 (delta 1m: -0.03) [2026-07-08]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.08) [2026-07-08]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: -0.11) [2026-07-08]
- Dolar broad index: 120.6902 (delta 1m: 1.654) [2026-07-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), merger (1), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [RKLB] Rocket Lab Delivers Successful Mission After Shattering Launch Record : Here What It Means for the SpaceX Competitor (2026-07-09)
- [RKLB] Rocket Lab Shares Climb as Wall Street Weighs $8 Billion Iridium Deal , $3 . 6 Billion Bridge Loan - Rocket (2026-07-09)
- [CRWV] Jim Cramer on CoreWeave :  I Think It One of the Stronger Players in the Neocloud Space (2026-07-09)
- [RKLB] Why Rocket Lab Stock Is Plummeting Today (2026-07-09)
- [BLLN] Billiontoone ( NASDAQ : BLLN ) CEO Oguzhan Atay Sells 26 , 250 Shares of Stock (2026-07-09)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Beck Peter vendio RKLB por $38.7M el 2026-07-07.
- CEO Beck Peter vendio RKLB por $29.2M el 2026-07-08.
- CEO Beck Peter vendio RKLB por $19.8M el 2026-07-06.
- CEO Wohlin Hakan compro VII por $3.0M el 2026-07-06.
- CEO FRIEDMAN GARY G vendio RH por $3.9M el 2026-07-08 [senal en multiples fuentes].
- CEO Tenev Vladimir vendio HOOD por $13.6M el 2026-07-06.
- CEO FRIEDMAN GARY G vendio RH por $6.6M el 2026-07-06 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- comon119 · PnL $114,844 · win rate 99% · categorias: sports, crypto, politics
- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $128,678 · win rate 97% · categorias: sports
- SemyonMarmeladov · PnL $95,874 · win rate 88% · categorias: sports, economy, politics
- hi774c · PnL $53,295 · win rate 83% · categorias: sports
- Gourmet1 · PnL $106,387 · win rate 89% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 83 registros 30d · ultimo dato 2026-07-07
- **sec_insiders**: `ok` · 961 registros 30d · ultimo dato 2026-07-09
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-09
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`APGE, BEP, GLD, IEF, INTC, NUVL, QQQ, RH, SPY, TLT, WRBY`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
