# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-09T00:29:52+00:00 · ventana señales 2026-08-10 -> 2026-09-09_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.72)
- Tendencia: `bull` (SPY 770.19 · MA50 756.86 · MA200 709.87 · dist MA200: 8.5%)
- Credito: `tight` (HY spread 2.68)
- Tipos: `flat` (curva 10y-2y 0.41)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 770.19 | -0.39% | 0.11% | -0.4% |
| QQQ | 12.0% | core | 718.96 | 0.18% | 0.35% | -0.56% |
| TLT | 12.0% | core | 82.21 | 0.17% | -0.43% | -0.28% |
| GLD | 9.3% | core | 406.77 | -0.84% | -0.52% | 2.08% |
| CSQ | 9.2% | satellite | 20.98 | -0.52% | 0.19% | 0.45% |
| IEF | 6.2% | core | 92.25 | -0.03% | -0.29% | -0.63% |
| LTH | 4.5% | satellite | 43.23 | 0.32% | -0.64% | -1.32% |
| WTS | 4.5% | satellite | 363.13 | 2.14% | -0.71% | -7.26% |
| UBER | 3.9% | satellite | 75.76 | -0.26% | -3.88% | 0.99% |
| KMT | 3.2% | satellite | 31.02 | 5.4% | 5.01% | -5.77% |
| GOLD | 2.9% | satellite | 46.13 | 11.21% | 1.27% | 6.02% |
| INBX | 2.1% | satellite | 121.17 | -0.89% | -1.82% | 36.67% |
| TXG | 2.0% | satellite | 62.65 | -0.9% | 1.8% | 20.41% |
| SUJA | 1.2% | satellite | 10.51 | 3.14% | 12.17% | 67.89% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 11.8%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -3.3%
- Beta vs SPY: 0.778 · posiciones efectivas: 13.8 · HHI: 0.0727

**Por que estos satellite (señales WATCHDOG):**

- **INBX** · score agregado 655.0 · 8 señales · fuentes: corporate_insider
- **SUJA** · score agregado 260.4 · 4 señales · fuentes: corporate_insider, large_holder
- **CSQ** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **GOLD** · score agregado 136.7 · 2 señales · fuentes: corporate_insider, large_holder
- **UBER** · score agregado 124.5 · 2 señales · fuentes: corporate_insider
- **TXG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WTS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **LTH** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KMT** · score agregado 57.4 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| INBX | 86 | corporate_insider | Lappe Mark | 3 | $1,087,001 | cluster_buy |
| INBX | 85 | corporate_insider | Lappe Mark | 3 | $664,719 | cluster_buy |
| INBX | 84 | corporate_insider | Lappe Mark | 3 | $585,343 | cluster_buy |
| GPUS | 81 | corporate_insider | AULT MILTON C III | 4 | $361,496 | cluster_buy |
| INBX | 81 | corporate_insider | Lappe Mark | 3 | $136,382 | cluster_buy |
| INBX | 81 | corporate_insider | Lappe Mark | 3 | $117,836 | cluster_buy |
| INBX | 80 | corporate_insider | Kayyem Jon Faiz | 3 | $567,580 | cluster_buy |
| INBX | 79 | corporate_insider | Lappe Mark | 3 | $54,118 | cluster_buy |
| GPUS | 79 | corporate_insider | Nisser Henry Carl | 4 | $46,775 | cluster_buy |
| INBX | 79 | corporate_insider | FORSYTH DOUGLAS | 3 | $286,617 | cluster_buy |
| GPUS | 77 | corporate_insider | Horne William B. | 4 | $20,000 | cluster_buy,small_amount |
| GPUS | 76 | corporate_insider | AULT MILTON C III | 4 | $37,904 | cluster_buy |
| GPUS | 76 | corporate_insider | CRAGUN KENNETH S | 4 | $18,650 | cluster_buy,small_amount |
| GPUS | 76 | corporate_insider | Horne William B. | 4 | $11,220 | cluster_buy,small_amount |
| GPUS | 73 | corporate_insider | AULT MILTON C III | 4 | $7,117 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| NVDA | 58 | corporate_insider | STEVENS MARK A | $54,976,302 | - |
| NVDA | 58 | corporate_insider | STEVENS MARK A | $45,974,100 | - |
| NVDA | 58 | corporate_insider | STEVENS MARK A | $45,431,041 | - |
| NVDA | 58 | corporate_insider | STEVENS MARK A | $45,244,670 | - |
| NVDA | 57 | corporate_insider | STEVENS MARK A | $42,636,607 | - |
| BNTX | 57 | corporate_insider | Sahin Ugur | $4,628,232 | - |
| QVCG | 57 | corporate_insider | Silver Point Capital L.P. | $11,844,000 | - |
| SMCI | 56 | corporate_insider | Liang Charles | $4,000,000 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 770.19 (-0.39% / 0.11% / -0.4%) [2026-09-04]
- QQQ: 718.96 (0.18% / 0.35% / -0.56%) [2026-09-04]
- IWM: 296.01 (0.28% / 0.09% / -1.84%) [2026-09-04]
- DIA: 534.08 (-0.53% / -0.18% / -0.94%) [2026-09-04]
- TLT: 82.21 (0.17% / -0.43% / -0.28%) [2026-09-04]
- IEF: 92.25 (-0.03% / -0.29% / -0.63%) [2026-09-04]
- GLD: 406.77 (-0.84% / -0.52% / 2.08%) [2026-09-04]
- ^VIX: 15.72 (2.75% / -3.79% / 2.88%) [2026-09-08]
- BTC-USD: 78625.66 (-0.62% / -3.26% / 13.51%) [2026-09-09]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.37 (delta 1m: 0.12) [2026-09-04]
- Treasury 10Y yield: 4.78 (delta 1m: 0.09) [2026-09-04]
- Curva 10Y-2Y: 0.41 (delta 1m: -0.05) [2026-09-08]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.68 (delta 1m: -0.02) [2026-09-07]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.37 (delta 1m: 0.12) [2026-09-08]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), earnings (2), merger (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CWT] California Water Service Kicks Off Back - to - School Season With 13th Year of Tap Into Learning Program (2026-09-09)
- [DDOG] 7 , 985 Shares in Datadog , Inc . $DDOG Acquired by FirstWave Capital Management LLC (2026-09-05)
- [DDOG] FirstWave Capital Management LLC Invests $2 . 08 Million in Datadog , Inc . $DDOG (2026-09-05)
- [ESTC] Elastic ( NYSE : ESTC ) CTO Sells $14 , 908 , 334 . 46 in Stock (2026-09-03)
- [CWT] Lester Snow Sells 500 Shares of California Water Service Group ( NYSE : CWT ) Stock (2026-09-01)
- [ESTC] Elastic ( ESTC ) Finally Delivered After Years of Head - Fakes and Wall Street Still Cant Agree It Lasts (2026-09-01)
- [ESTC] Elastic ( NYSE : ESTC ) Price Target Raised to $105 . 00 (2026-08-31)
- [KTCC] Key Tronic ( NASDAQ : KTCC ) vs . Tempo Automation ( NASDAQ : TMPOW ) Critical Review (2026-08-30)
- [KTCC] Key Tronic Corp ( KTCC ) ( Q4 2026 ) Earnings Call Highlights : Revenue Surges 14 % Sequentially , ... (2026-08-29)
- [KTCC] Key Tronic Corporation Announces Results for the Fourth Quarter and Year End of Fiscal 2026 · EMSNow (2026-08-28)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro QVCG por $11.8M el 2026-09-03 [senal en multiples fuentes].
- 10% owner Tether Global Investments Fund, S.I.C.A.F., S.A. compro GOLD por $3.9M el 2026-09-03 [senal en multiples fuentes].
- CEO Lappe Mark compro INBX por $1.1M el 2026-09-08.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- theowalcott · PnL $95,203 · win rate 100% · categorias: sports
- BreakTheBank · PnL $483,911 · win rate 85% · categorias: sports
- 0xe987c520c086Cf3930b0d163067B5470ba0FF0E1-1780518901092 · PnL $52,245 · win rate 98% · categorias: sports, crypto
- TAIWANNUMBERONE · PnL $62,402 · win rate 92% · categorias: sports, politics
- SemyonMarmeladov · PnL $93,204 · win rate 88% · categorias: sports, economy, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 535 registros 30d · ultimo dato 2026-09-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-08
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CSQ, GLD, GOLD, IEF, INBX, KMT, LTH, QQQ, SPY, SUJA, TLT, TXG, UBER, WTS`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
