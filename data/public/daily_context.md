# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-26T05:12:26+00:00 · ventana señales 2026-07-27 -> 2026-08-26_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.45)
- Tendencia: `bull` (SPY 765.91 · MA50 752.63 · MA200 705.92 · dist MA200: 8.5%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.91 | 0.32% | -0.2% | 3.38% |
| QQQ | 12.0% | core | 710.72 | 0.62% | -0.95% | 5.22% |
| TLT | 12.0% | core | 83.47 | 1.1% | 2.22% | -0.51% |
| CHTR | 12.0% | satellite | 155.14 | 3.22% | 4.58% | 10.84% |
| GLD | 10.5% | core | 428.07 | 0.32% | 7.41% | 15.89% |
| CBRS | 7.1% | satellite | 183.92 | -0.81% | -16.4% | -4.57% |
| SUJA | 7.1% | satellite | 9.33 | 3.09% | 39.05% | -11.06% |
| IEF | 7.0% | core | 93.51 | 0.54% | 0.62% | 0.29% |
| XPON | 5.2% | satellite | 5.27 | -15.0% | 26.99% | 46.8% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 21.3%
- VaR 95% 1d: 1.9% · CVaR 95% 1d: 2.4%
- Max drawdown historico: -11.2%
- Beta vs SPY: 0.818 · posiciones efectivas: 11.6 · HHI: 0.0864

**Por que estos satellite (señales WATCHDOG):**

- **SUJA** · score agregado 335.1 · 5 señales · fuentes: corporate_insider, large_holder
- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **XPON** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder

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
| NNDM | 72 | large_holder | TANG CAPITAL MANAGEMENT,  |  | - | - |
| TG | 72 | large_holder | John D. Gottwald |  | - | - |
| CLBT | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| LFT | 71 | corporate_insider | BRIGGS JAMES A | 2 | $13,798 | cluster_buy,small_amount |
| HKHC | 71 | corporate_insider | Rosenthal Brent D | 2 | $54,000 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $45,800 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $46,300 | cluster_buy |

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

- SPY: 765.91 (0.32% / -0.2% / 3.38%) [2026-08-25]
- QQQ: 710.72 (0.62% / -0.95% / 5.22%) [2026-08-25]
- IWM: 299.23 (0.42% / -0.33% / 2.0%) [2026-08-25]
- DIA: 535.24 (0.3% / 0.52% / 1.67%) [2026-08-25]
- TLT: 83.47 (1.1% / 2.22% / -0.51%) [2026-08-25]
- IEF: 93.51 (0.54% / 0.62% / 0.29%) [2026-08-25]
- GLD: 428.07 (0.32% / 7.41% / 15.89%) [2026-08-25]
- ^VIX: 15.45 (-2.52% / -2.46% / -15.16%) [2026-08-25]
- BTC-USD: 78864.3 (-0.13% / 7.98% / 22.09%) [2026-08-26]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.24 (delta 1m: -0.09) [2026-08-24]
- Treasury 10Y yield: 4.7 (delta 1m: 0.01) [2026-08-24]
- Curva 10Y-2Y: 0.47 (delta 1m: 0.13) [2026-08-25]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.69 (delta 1m: -0.1) [2026-08-24]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.32 (delta 1m: 0.11) [2026-08-25]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), ai (3), regulatory (2), leadership (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [AMZN] Reviewing Americanas ( OTCMKTS : BZWHF ) & Amazon . com ( NASDAQ : AMZN ) (2026-08-26)
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
- CEO GREENBERG WILLIAM ROSS vendio TWO por $14.6M el 2026-08-25.
- CEO Feldman Andrew D. vendio CBRS por $13.2M el 2026-08-21 [senal en multiples fuentes].
- 10% owner PAINE SCHWARTZ FOOD CHAIN FUND V GP, LTD. compro SUJA por $2.2M el 2026-08-25 [senal en multiples fuentes].
- 10% owner PAINE SCHWARTZ FOOD CHAIN FUND V GP, LTD. compro SUJA por $2.1M el 2026-08-24 [senal en multiples fuentes].

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $102,695 · win rate 84% · categorias: sports
- 0x0x23kjookhaiuohduoayh8c9 · PnL $13,157 · win rate 95% · categorias: sports, crypto
- 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 · PnL $23,868 · win rate 88% · categorias: sports
- Donghui · PnL $9,998 · win rate 93% · categorias: sports
- monkeymashingkeyboard · PnL $9,352 · win rate 91% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 807 registros 30d · ultimo dato 2026-08-25
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-25
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CBRS, CHTR, GLD, IEF, QQQ, SPY, SUJA, TLT, XPON`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
