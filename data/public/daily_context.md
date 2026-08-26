# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-26T16:13:08+00:00 · ventana señales 2026-07-27 -> 2026-08-26_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.52)
- Tendencia: `bull` (SPY 765.15 · MA50 752.88 · MA200 706.42 · dist MA200: 8.31%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.15 | -0.1% | -0.51% | 4.89% |
| QQQ | 12.0% | core | 709.11 | -0.23% | -0.97% | 7.16% |
| TLT | 12.0% | core | 83.11 | -0.44% | 0.1% | 0.71% |
| BWFG | 12.0% | satellite | 66.26 | 0.78% | 0.94% | -2.35% |
| GLD | 9.3% | core | 421.75 | -1.48% | 1.91% | 13.65% |
| MED | 9.0% | satellite | 12.3 | 1.15% | 6.22% | 27.59% |
| IEF | 6.2% | core | 93.25 | -0.27% | -0.13% | 0.43% |
| CHTR | 6.1% | satellite | 153.04 | -1.35% | 0.37% | 5.4% |
| XPON | 4.0% | satellite | 8.91 | 69.05% | 137.58% | 158.99% |
| CBRS | 2.4% | satellite | 180.07 | -2.09% | -16.51% | 6.3% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.2%
- VaR 95% 1d: 1.6% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -5.4%
- Beta vs SPY: 0.631 · posiciones efectivas: 11.9 · HHI: 0.0841

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **MED** · score agregado 126.8 · 2 señales · fuentes: corporate_insider, large_holder
- **BWFG** · score agregado 110.3 · 2 señales · fuentes: corporate_insider
- **XPON** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| TISI | 77 | corporate_insider | Roeder Clinton William | 2 | $183,200 | cluster_buy |
| AMRZ | 74 | corporate_insider | Singleton Denise R | 2 | $154,402 | cluster_buy |
| TISI | 72 | corporate_insider | Roeder Clinton William | 2 | $22,840 | cluster_buy,small_amount |
| AMRZ | 72 | corporate_insider | Forrest Nollaig | 2 | $66,225 | cluster_buy |
| LFT | 72 | corporate_insider | Flynn James Peter | 2 | $13,642 | cluster_buy,small_amount |
| VTMX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| PCQ | 72 | large_holder | JPMorgan Chase Bank, Nati |  | - | - |
| PNI | 72 | large_holder | JPMorgan Chase Bank, Nati |  | - | - |
| XPON | 72 | large_holder | Five Narrow Lane LP |  | - | - |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| MED | 72 | large_holder | Steamboat Capital Partner |  | - | - |
| CDTG | 72 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| LFT | 71 | corporate_insider | BRIGGS JAMES A | 2 | $13,798 | cluster_buy,small_amount |
| HKHC | 71 | corporate_insider | Rosenthal Brent D | 2 | $54,000 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $45,800 | cluster_buy |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| CPAY | 60 | corporate_insider | Clarke Ronald | $21,552,683 | - |
| CPAY | 60 | corporate_insider | Clarke Ronald | $20,837,193 | - |
| CBRS | 59 | corporate_insider | Feldman Andrew D. | $13,203,021 | - |
| CPAY | 58 | corporate_insider | Clarke Ronald | $10,199,190 | - |
| CBRS | 58 | corporate_insider | Feldman Andrew D. | $8,545,099 | - |
| LASR | 57 | corporate_insider | Keeney Scott H | $6,825,002 | - |
| CPAY | 57 | corporate_insider | Clarke Ronald | $6,877,612 | - |
| CBRS | 57 | corporate_insider | Feldman Andrew D. | $6,719,365 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.15 (-0.1% / -0.51% / 4.89%) [2026-08-26]
- QQQ: 709.11 (-0.23% / -0.97% / 7.16%) [2026-08-26]
- IWM: 298.43 (-0.27% / -1.09% / 3.42%) [2026-08-26]
- DIA: 534.05 (-0.22% / 0.04% / 3.7%) [2026-08-26]
- TLT: 83.11 (-0.44% / 0.1% / 0.71%) [2026-08-26]
- IEF: 93.25 (-0.27% / -0.13% / 0.43%) [2026-08-26]
- GLD: 421.75 (-1.48% / 1.91% / 13.65%) [2026-08-26]
- ^VIX: 15.52 (0.45% / 4.23% / -24.88%) [2026-08-26]
- BTC-USD: 78082.12 (-0.61% / -0.32% / 21.51%) [2026-08-26]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.24 (delta 1m: -0.09) [2026-08-24]
- Treasury 10Y yield: 4.7 (delta 1m: 0.01) [2026-08-24]
- Curva 10Y-2Y: 0.47 (delta 1m: 0.13) [2026-08-25]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.11) [2026-08-25]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.32 (delta 1m: 0.11) [2026-08-25]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (5), ai (4), regulatory (3), earnings (1), legal (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [RVMD] Quantbot Technologies LP Takes Position in Revolution Medicines , Inc . $RVMD (2026-08-26)
- [ARDX] Ardelyx ( NASDAQ : ARDX ) Insider Mike Kelliher Sells 7 , 758 Shares of Stock (2026-08-26)
- [ARDX] Eric Duane Foster Sells 8 , 562 Shares of Ardelyx ( NASDAQ : ARDX ) Stock (2026-08-26)
- [TENB] Tenable ( NASDAQ : TENB ) Stock Price Down 3 . 9 % – Time to Sell ? (2026-08-25)
- [RVMD] Billionaire Stanley Druckenmiller Continues to Load Up on Revolution Medicines . Does He Know Something Wall Street Doesnt ? (2026-08-25)
- [RVMD] Billionaire Stanley Druckenmiller Continues to Load Up on Revolution Medicines . Does He Know Something Wall Street Doesnt ? (2026-08-25)
- [CBRS] As Cerebras Launches a New , Record - Setting AI Accelerator , Here How You Should Play CBRS Stock (2026-08-25)
- [CBRS] Cerebras Systems ( CBRS ) Revenue Surges : Why Did CBRS Stock Crash , and What About AMD ? (2026-08-24)
- [FMCB] Farmers & Merchants Bank of Long Beach ( OTCMKTS : FMBL ) Reaches New 1 - Year High – Here What Happened (2026-08-21)
- [ARDX] Piper Sandler Cuts Ardelyx ( NASDAQ : ARDX ) Price Target to $15 . 00 (2026-08-20)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Clarke Ronald opero CPAY por $67.8M el 2026-08-21.
- CEO Clarke Ronald vendio CPAY por $21.6M el 2026-08-24.
- 10% owner Host-Plus Pty Ltd as trustee for the HOSTPLUS Pooled Superannuation Trust compro EBR Systems, Inc. por $20.8M el 2026-08-21.
- CEO Clarke Ronald vendio CPAY por $20.8M el 2026-08-25.
- CEO Feldman Andrew D. vendio CBRS por $13.2M el 2026-08-21 [senal en multiples fuentes].
- CEO Roks Edwin compro TTMI por $1.1M el 2026-08-25.
- CEO Keeney Scott H vendio LASR por $6.8M el 2026-08-24.
- CEO Gamble Sean vendio CNK por $5.3M el 2026-08-24.

**Polymarket — smart money (traders con mejor track record):**

- SPCEXBUYER · PnL $145,791 · win rate 93% · categorias: sports
- BreakTheBank · PnL $102,238 · win rate 85% · categorias: sports
- comon119 · PnL $16,178 · win rate 97% · categorias: sports, crypto
- Skyfker · PnL $23,860 · win rate 90% · categorias: sports, crypto
- zofgkt1111 · PnL $17,947 · win rate 100% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 783 registros 30d · ultimo dato 2026-08-26
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-26
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BWFG, CBRS, CHTR, GLD, IEF, MED, QQQ, SPY, TLT, XPON`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
