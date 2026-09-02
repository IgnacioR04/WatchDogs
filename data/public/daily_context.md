# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-02T18:59:32+00:00 · ventana señales 2026-08-03 -> 2026-09-02_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.24)
- Tendencia: `bull` (SPY 764.7 · MA50 755.33 · MA200 708.78 · dist MA200: 7.89%)
- Credito: `tight` (HY spread 2.65)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 764.7 | 0.38% | -0.18% | -0.66% |
| QQQ | 12.0% | core | 708.09 | 0.06% | -0.46% | -1.28% |
| TLT | 12.0% | core | 81.82 | -0.05% | -1.39% | -1.04% |
| ECAT | 9.9% | satellite | 15.25 | 0.46% | -1.93% | 0.09% |
| GLD | 9.3% | core | 401.15 | 1.11% | -4.79% | 2.95% |
| DGICA | 6.3% | satellite | 19.43 | 1.36% | 1.73% | -1.07% |
| IEF | 6.2% | core | 92.08 | -0.02% | -0.97% | -0.96% |
| BPRE | 3.9% | satellite | 11.98 | -0.29% | 0.97% | -9.49% |
| KIDS | 3.3% | satellite | 22.89 | -0.48% | -4.74% | 2.6% |
| VST | 3.0% | satellite | 141.96 | 2.81% | 1.38% | 0.99% |
| PESI | 1.8% | satellite | 18.09 | 1.43% | -0.25% | 2.46% |
| AUGO | 1.7% | satellite | 84.81 | 7.29% | -5.03% | 30.16% |
| WIX | 1.5% | satellite | 87.28 | -1.24% | 6.06% | 35.17% |
| SUJA | 1.1% | satellite | 10.26 | -1.63% | 8.69% | 67.1% |
| FGL | 0.9% | satellite | 15.81 | -8.27% | -17.68% | -81.03% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.1%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -4.1%
- Beta vs SPY: 0.682 · posiciones efectivas: 13.5 · HHI: 0.0742

**Por que estos satellite (señales WATCHDOG):**

- **WIX** · score agregado 302.4 · 4 señales · fuentes: corporate_insider
- **AUGO** · score agregado 259.2 · 4 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **PESI** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **BPRE** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **VST** · score agregado 127.3 · 2 señales · fuentes: corporate_insider
- **DGICA** · score agregado 119.6 · 2 señales · fuentes: corporate_insider
- **FGL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **ECAT** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **KIDS** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| WIX | 78 | corporate_insider | Abrahami Avishai | 6 | $39,168 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 6 | $22,519 | cluster_buy,small_amount |
| WIX | 77 | corporate_insider | Shemesh Lior | 6 | $27,310 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 6 | $16,230 | cluster_buy,small_amount |
| WIX | 74 | corporate_insider | Meyer Shelly B | 6 | $28,687 | cluster_buy |
| RGCO | 73 | corporate_insider | WILLIAMSON JOHN B III | 3 | $21,300 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Abrahami Avishai | 6 | $3,294 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Shai Omer | 6 | $29,346 | cluster_buy |
| WIX | 72 | corporate_insider | Even-Haim Yaniv | 6 | $19,165 | cluster_buy,small_amount |
| EMPD | 72 | large_holder | Streeterville Capital LLC |  | - | - |
| FGL | 72 | large_holder | Marex Financial |  | - | - |
| AFCG | 72 | large_holder | Leonard M. Tannenbaum |  | - | - |
| VTMX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ESTC | 70 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| DT | 70 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ACT | 59 | corporate_insider | Genworth Holdings, Inc. | $33,953,773 | - |
| PGR | 58 | corporate_insider | Griffith Susan Patricia | $8,195,691 | - |
| TYL | 56 | corporate_insider | MOORE H LYNN JR | $3,448,280 | - |
| CHYM | 56 | corporate_insider | Britt Christopher R | $3,015,626 | - |
| KIDS | 56 | corporate_insider | Pelizzon David R | $7,527,168 | - |
| PHIN | 55 | corporate_insider | Ericson Brady D | $1,841,503 | - |
| RYTM | 55 | corporate_insider | Smith Hunter C | $2,993,647 | - |
| RYTM | 54 | corporate_insider | Smith Hunter C | $2,413,034 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 764.7 (0.38% / -0.18% / -0.66%) [2026-09-02]
- QQQ: 708.09 (0.06% / -0.46% / -1.28%) [2026-09-02]
- IWM: 293.96 (1.17% / -1.66% / -1.94%) [2026-09-02]
- DIA: 530.0 (0.43% / -0.79% / -2.28%) [2026-09-02]
- TLT: 81.82 (-0.05% / -1.39% / -1.04%) [2026-09-02]
- IEF: 92.08 (-0.02% / -0.97% / -0.96%) [2026-09-02]
- GLD: 401.15 (1.11% / -4.79% / 2.95%) [2026-09-02]
- ^VIX: 15.24 (-6.73% / 0.2% / -3.61%) [2026-09-02]
- BTC-USD: 77342.43 (-0.08% / -0.63% / 21.99%) [2026-09-02]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.34 (delta 1m: 0.06) [2026-08-31]
- Treasury 10Y yield: 4.75 (delta 1m: 0.0) [2026-08-31]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.05) [2026-09-01]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.65 (delta 1m: -0.13) [2026-09-01]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.35 (delta 1m: 0.08) [2026-09-01]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [IVZ] Healthcare ETF Comparison : Fidelity FHLC vs . Invesco Biotech - Focused IBBQ (2026-09-02)
- [IVZ] Invesco Quality Municipal Income Trust ( NYSE : IQI ) Plans Monthly Dividend of $0 . 06 (2026-09-02)
- [IVZ] Invesco Advantage Municipal Income Trust II ( NYSEAMERICAN : VKI ) to Issue Monthly Dividend of $0 . 06 (2026-09-02)
- [TSM] The Firm That Filed a Bet Against Taiwan Semiconductor Then Launched a Foundry Fund Five Days Later (2026-09-02)
- [AUGO] Aura Minerals ( NASDAQ : AUGO ) Director Purchases 252 , 000 Shares of Stock (2026-09-02)
- [AUGO] Insider Selling : Aura Minerals ( NASDAQ : AUGO ) CFO Sells $635 , 672 . 08 in Stock (2026-08-20)
- [AUGO] Aura Minerals ( NASDAQ : AUGO ) Director Mauad Bruno Sousa Sells 280 , 000 Shares of Stock (2026-08-20)
- [AUGO] Aura Minerals ( TSE : ORA ) Share Price Passes Above 200 Day Moving Average – Should You Sell ? (2026-08-19)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Senior Loan Trust por $44.0M el 2026-08-31.
- 10% owner Manufacturers Life Insurance Co (Bermuda Branch) compro John Hancock GA Senior Loan Trust por $23.0M el 2026-08-31.
- CEO Marin Horacio Daniel opero YPF por $4.3B el 2026-08-31.
- 10% owner Genworth Holdings, Inc. vendio ACT por $34.0M el 2026-08-31.
- CEO Griffith Susan Patricia vendio PGR por $8.2M el 2026-09-01.
- 10% owner Empery Asset Management, LP compro EMPD por $1.8M el 2026-09-01 [senal en multiples fuentes].
- Director WU JOHN JIONG vendio HTHT por $45.4M el 2026-09-02.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.

**Polymarket — smart money (traders con mejor track record):**

- 0xd9670ea74384c1e1b9dc1e4267ffadaf4cdd140 · PnL $159,437 · win rate 97% · categorias: sports, crypto
- ExplosiveNinja · PnL $32,853 · win rate 97% · categorias: sports
- monkeymashingkeyboard · PnL $32,943 · win rate 92% · categorias: sports
- dad168168 · PnL $22,713 · win rate 94% · categorias: sports
- Jan777 · PnL $33,706 · win rate 91% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 599 registros 30d · ultimo dato 2026-09-02
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-02
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AUGO, BPRE, DGICA, ECAT, FGL, GLD, IEF, KIDS, PESI, QQQ, SPY, SUJA, TLT, VST, WIX`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
