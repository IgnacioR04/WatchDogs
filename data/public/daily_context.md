# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-26T14:23:25+00:00 · ventana señales 2026-07-27 -> 2026-08-26_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.44)
- Tendencia: `bull` (SPY 765.65 · MA50 752.89 · MA200 706.43 · dist MA200: 8.38%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.65 | -0.03% | -0.44% | 4.96% |
| QQQ | 12.0% | core | 709.25 | -0.21% | -0.95% | 7.18% |
| TLT | 12.0% | core | 83.12 | -0.42% | 0.12% | 0.73% |
| CHTR | 11.7% | satellite | 154.51 | -0.41% | 1.34% | 6.41% |
| GLD | 9.3% | core | 424.08 | -0.93% | 2.48% | 14.28% |
| PRE | 6.9% | satellite | 24.35 | 4.73% | 29.8% | 35.13% |
| TTMI | 6.9% | satellite | 121.76 | 8.42% | 4.62% | 19.64% |
| IEF | 6.2% | core | 93.25 | -0.27% | -0.13% | 0.43% |
| CBRS | 4.6% | satellite | 179.09 | -2.63% | -16.97% | 5.72% |
| XPON | 3.3% | satellite | 9.94 | 88.61% | 165.07% | 188.95% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 19.8%
- VaR 95% 1d: 1.8% · CVaR 95% 1d: 2.3%
- Max drawdown historico: -9.6%
- Beta vs SPY: 1.076 · posiciones efectivas: 12.2 · HHI: 0.0823

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **PRE** · score agregado 122.2 · 2 señales · fuentes: corporate_insider
- **XPON** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **TTMI** · score agregado 65.7 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| TISI | 77 | corporate_insider | Roeder Clinton William | 2 | $183,200 | cluster_buy |
| TISI | 72 | corporate_insider | Roeder Clinton William | 2 | $22,840 | cluster_buy,small_amount |
| LFT | 72 | corporate_insider | Flynn James Peter | 2 | $13,642 | cluster_buy,small_amount |
| PCQ | 72 | large_holder | JPMorgan Chase Bank, Nati |  | - | - |
| PNI | 72 | large_holder | JPMorgan Chase Bank, Nati |  | - | - |
| XPON | 72 | large_holder | Five Narrow Lane LP |  | - | - |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| CDTG | 72 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| TG | 72 | large_holder | John D. Gottwald |  | - | - |
| CLBT | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| LFT | 71 | corporate_insider | BRIGGS JAMES A | 2 | $13,798 | cluster_buy,small_amount |
| HKHC | 71 | corporate_insider | Rosenthal Brent D | 2 | $54,000 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $45,800 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $46,300 | cluster_buy |
| LFT | 71 | corporate_insider | Flynn James Peter | 2 | $6,825 | cluster_buy,small_amount |

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

- SPY: 765.65 (-0.03% / -0.44% / 4.96%) [2026-08-26]
- QQQ: 709.25 (-0.21% / -0.95% / 7.18%) [2026-08-26]
- IWM: 299.43 (0.07% / -0.76% / 3.77%) [2026-08-26]
- DIA: 534.58 (-0.12% / 0.14% / 3.81%) [2026-08-26]
- TLT: 83.12 (-0.42% / 0.12% / 0.73%) [2026-08-26]
- IEF: 93.25 (-0.27% / -0.13% / 0.43%) [2026-08-26]
- GLD: 424.08 (-0.93% / 2.48% / 14.28%) [2026-08-26]
- ^VIX: 15.44 (-0.06% / 3.69% / -25.27%) [2026-08-26]
- BTC-USD: 78506.44 (-0.07% / 0.22% / 22.17%) [2026-08-26]

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

**Temas dominantes**: stock (4), ai (3), regulatory (2), leadership (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [RVMD] Quantbot Technologies LP Takes Position in Revolution Medicines , Inc . $RVMD (2026-08-26)
- [CPAY] Corpay ( NYSE : CPAY ) CEO Ronald Clarke Sells 119 , 486 Shares of Stock (2026-08-26)
- [TENB] Tenable ( NASDAQ : TENB ) Stock Price Down 3 . 9 % – Time to Sell ? (2026-08-25)
- [RVMD] Billionaire Stanley Druckenmiller Continues to Load Up on Revolution Medicines . Does He Know Something Wall Street Doesnt ? (2026-08-25)
- [RVMD] Billionaire Stanley Druckenmiller Continues to Load Up on Revolution Medicines . Does He Know Something Wall Street Doesnt ? (2026-08-25)
- [CBRS] As Cerebras Launches a New , Record - Setting AI Accelerator , Here How You Should Play CBRS Stock (2026-08-25)
- [CBRS] Cerebras Systems ( CBRS ) Revenue Surges : Why Did CBRS Stock Crash , and What About AMD ? (2026-08-24)
- [FMCB] Farmers & Merchants Bank of Long Beach ( OTCMKTS : FMBL ) Reaches New 1 - Year High – Here What Happened (2026-08-21)
- [FMCB] Farmers & Merchants Bancorp ( OTCMKTS : FMCB ) Short Interest Down 50 . 0 % in July (2026-08-16)

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

- SPCEXBUYER · PnL $134,451 · win rate 93% · categorias: sports
- BreakTheBank · PnL $102,695 · win rate 85% · categorias: sports
- comon119 · PnL $16,012 · win rate 97% · categorias: sports, crypto
- 0x0x23kjookhaiuohduoayh8c9 · PnL $15,382 · win rate 95% · categorias: sports, crypto
- Skyfker · PnL $23,858 · win rate 90% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 776 registros 30d · ultimo dato 2026-08-26
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-25
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CBRS, CHTR, GLD, IEF, PRE, QQQ, SPY, TLT, TTMI, XPON`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
