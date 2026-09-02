# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-02T14:48:39+00:00 · ventana señales 2026-08-03 -> 2026-09-02_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.47)
- Tendencia: `bull` (SPY 765.9 · MA50 755.36 · MA200 708.79 · dist MA200: 8.06%)
- Credito: `tight` (HY spread 2.65)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.9 | 0.54% | -0.02% | -0.51% |
| QQQ | 12.0% | core | 708.95 | 0.18% | -0.34% | -1.16% |
| TLT | 12.0% | core | 81.88 | 0.01% | -1.33% | -0.97% |
| GLD | 9.3% | core | 401.75 | 1.26% | -4.64% | 3.11% |
| DGICA | 8.5% | satellite | 19.44 | 1.41% | 1.78% | -1.02% |
| IEF | 6.2% | core | 92.11 | 0.02% | -0.94% | -0.93% |
| BPRE | 5.2% | satellite | 12.02 | 0.04% | 1.31% | -9.19% |
| KIDS | 4.4% | satellite | 23.33 | 1.43% | -2.91% | 4.57% |
| VST | 4.0% | satellite | 139.62 | 1.11% | -0.3% | -0.69% |
| PESI | 2.3% | satellite | 18.03 | 1.07% | -0.61% | 2.1% |
| AUGO | 2.3% | satellite | 84.35 | 6.71% | -5.55% | 29.45% |
| AMRC | 2.1% | satellite | 22.22 | -1.68% | 0.27% | -13.41% |
| WIX | 2.0% | satellite | 89.31 | 1.06% | 8.53% | 38.32% |
| SUJA | 1.5% | satellite | 10.12 | -2.92% | 7.26% | 64.9% |
| FGL | 1.2% | satellite | 16.25 | -5.69% | -15.37% | -80.49% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 11.5%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -5.2%
- Beta vs SPY: 0.74 · posiciones efectivas: 14.0 · HHI: 0.0715

**Por que estos satellite (señales WATCHDOG):**

- **AUGO** · score agregado 259.2 · 4 señales · fuentes: corporate_insider
- **WIX** · score agregado 228.0 · 3 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **PESI** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **BPRE** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **AMRC** · score agregado 131.4 · 2 señales · fuentes: corporate_insider, large_holder
- **VST** · score agregado 127.3 · 2 señales · fuentes: corporate_insider
- **DGICA** · score agregado 119.6 · 2 señales · fuentes: corporate_insider
- **FGL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KIDS** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| WIX | 78 | corporate_insider | Abrahami Avishai | 4 | $39,168 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 4 | $22,519 | cluster_buy,small_amount |
| WIX | 77 | corporate_insider | Shemesh Lior | 4 | $27,310 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 4 | $16,230 | cluster_buy,small_amount |
| LUCK | 76 | corporate_insider | Young John Alan | 2 | $614,000 | cluster_buy |
| WIX | 73 | corporate_insider | Abrahami Avishai | 4 | $3,294 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Shai Omer | 4 | $29,346 | cluster_buy |
| EMPD | 72 | large_holder | Streeterville Capital LLC |  | - | - |
| FGL | 72 | large_holder | Marex Financial |  | - | - |
| AMRC | 72 | large_holder | Gagnon Securities LLC |  | - | - |
| AFCG | 72 | large_holder | Leonard M. Tannenbaum |  | - | - |
| VTMX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| LUCK | 71 | corporate_insider | MATHRANI SANDEEP | 2 | $59,957 | cluster_buy |
| CON | 70 | large_holder | Robert A. Ortenzio |  | - | - |
| BMHL | 70 | large_holder | Luk Tung Lam |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ACT | 59 | corporate_insider | Genworth Holdings, Inc. | $33,953,773 | - |
| CRNX | 56 | corporate_insider | Struthers Richard Scott | $21,083,655 | - |
| TYL | 56 | corporate_insider | MOORE H LYNN JR | $3,448,280 | - |
| ABNB | 56 | corporate_insider | Blecharczyk Nathan | $8,617,143 | - |
| CRNX | 56 | corporate_insider | Struthers Richard Scott | $15,016,355 | - |
| CHYM | 56 | corporate_insider | Britt Christopher R | $3,015,626 | - |
| KIDS | 56 | corporate_insider | Pelizzon David R | $7,527,168 | - |
| CRNX | 55 | corporate_insider | Struthers Richard Scott | $11,628,425 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.9 (0.54% / -0.02% / -0.51%) [2026-09-02]
- QQQ: 708.95 (0.18% / -0.34% / -1.16%) [2026-09-02]
- IWM: 293.4 (0.97% / -1.85% / -2.12%) [2026-09-02]
- DIA: 531.93 (0.79% / -0.43% / -1.92%) [2026-09-02]
- TLT: 81.88 (0.01% / -1.33% / -0.97%) [2026-09-02]
- IEF: 92.11 (0.02% / -0.94% / -0.93%) [2026-09-02]
- GLD: 401.75 (1.26% / -4.64% / 3.11%) [2026-09-02]
- ^VIX: 15.47 (-5.32% / 1.71% / -2.15%) [2026-09-02]
- BTC-USD: 77193.53 (-0.27% / -0.82% / 21.75%) [2026-09-02]

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

**Temas dominantes**: ai (3), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TSM] The Firm That Filed a Bet Against Taiwan Semiconductor Then Launched a Foundry Fund Five Days Later (2026-09-02)
- [ABNB] Startups want to rent your idle gaming PC for AI tasks Startups pitch an  Airbnb for AI inference , but profitability remains unproven (2026-09-02)
- [ABNB] 18 - year - old killed at Airbnb as Clark County changes short - term rental enforcement (2026-09-02)
- [CSTL] Castle Biosciences , Inc . ( NASDAQ : CSTL ) Receives $42 . 00 Average PT from Analysts (2026-08-23)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Senior Loan Trust por $44.0M el 2026-08-31.
- 10% owner Manufacturers Life Insurance Co (Bermuda Branch) compro John Hancock GA Senior Loan Trust por $23.0M el 2026-08-31.
- CEO Struthers Richard Scott vendio CRNX por $21.1M el 2026-09-01.
- 10% owner Genworth Holdings, Inc. vendio ACT por $34.0M el 2026-08-31.
- 10% owner Empery Asset Management, LP compro EMPD por $1.8M el 2026-09-01 [senal en multiples fuentes].
- Director WU JOHN JIONG vendio HTHT por $45.4M el 2026-09-02.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- monkeymashingkeyboard · PnL $60,528 · win rate 92% · categorias: sports
- dad168168 · PnL $22,713 · win rate 94% · categorias: sports
- Kosherlocks · PnL $13,507 · win rate 96% · categorias: sports, crypto
- Jan777 · PnL $24,024 · win rate 90% · categorias: sports, politics
- vibing123 · PnL $18,388 · win rate 90% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 603 registros 30d · ultimo dato 2026-09-02
- **sec_13d_13g**: `ok` · 241 registros 30d · ultimo dato 2026-09-01
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMRC, AUGO, BPRE, DGICA, FGL, GLD, IEF, KIDS, PESI, QQQ, SPY, SUJA, TLT, VST, WIX`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
