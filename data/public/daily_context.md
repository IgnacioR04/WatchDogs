# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-13T17:41:13+00:00 · ventana señales 2026-06-13 -> 2026-07-13_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.67)
- Tendencia: `bull` (SPY 749.52 · MA50 740.7 · MA200 691.55 · dist MA200: 8.38%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.35)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 749.52 | -0.72% | -0.23% | 1.86% |
| QQQ | 12.0% | core | 712.25 | -1.83% | -1.46% | -0.57% |
| TLT | 12.0% | core | 83.96 | -0.6% | -1.74% | -1.98% |
| GLD | 9.3% | core | 366.68 | -2.74% | -4.04% | -5.08% |
| BEP | 8.5% | satellite | 31.81 | -1.61% | -5.86% | -10.09% |
| IEF | 6.2% | core | 93.29 | -0.36% | -0.94% | -0.78% |
| AVO | 5.3% | satellite | 13.35 | 0.19% | 0.49% | 19.99% |
| TBRG | 4.9% | satellite | 26.24 | 0.0% | 0.0% | 0.65% |
| LION | 4.2% | satellite | 13.3 | -1.26% | -7.57% | -4.45% |
| NTSK | 3.1% | satellite | 12.59 | 2.15% | 2.99% | 44.49% |
| INTC | 2.6% | satellite | 102.8 | -6.41% | -15.88% | -12.11% |
| APGE | 2.5% | satellite | 133.73 | 0.06% | 0.17% | 49.42% |
| IPX | 2.4% | satellite | 25.11 | 0.32% | -11.46% | -31.84% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 14.9%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.9%
- Max drawdown historico: -7.4%
- Beta vs SPY: 0.844 · posiciones efectivas: 13.8 · HHI: 0.0727

**Por que estos satellite (señales WATCHDOG):**

- **LION** · score agregado 481.3 · 8 señales · fuentes: corporate_insider, large_holder
- **IPX** · score agregado 234.7 · 3 señales · fuentes: corporate_insider
- **NTSK** · score agregado 167.6 · 2 señales · fuentes: corporate_insider
- **AVO** · score agregado 138.2 · 2 señales · fuentes: corporate_insider, large_holder
- **TBRG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **APGE** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GLOO | 88 | corporate_insider | Beck Scott Arthur | 3 | $3,500,000 | cluster_buy |
| NTSK | 84 | corporate_insider | ICONIQ Strategic Partners | 2 | $7,213,716 | cluster_buy |
| NTSK | 84 | corporate_insider | Griffith William J.G. | 2 | $7,216,081 | cluster_buy |
| GLOO | 83 | corporate_insider | Green Derek Todd | 3 | $1,999,998 | cluster_buy |
| IPX | 80 | corporate_insider | Arima Anastasios | 2 | $497,228 | cluster_buy |
| GLOO | 80 | corporate_insider | GELSINGER PATRICK P | 3 | $500,000 | cluster_buy |
| IPX | 78 | corporate_insider | Hannigan Todd | 2 | $1,075,980 | cluster_buy |
| IPX | 77 | corporate_insider | Hannigan Todd | 2 | $805,185 | cluster_buy |
| FINS | 74 | corporate_insider | MetLife Investment Manage | 0 | $1,600,000,000,000,000 | - |
| TBRG | 72 | large_holder | L6 Holdings Inc. |  | - | - |
| LION | 72 | large_holder | MHR INSTITUTIONAL PARTNER |  | - | - |
| WRAP | 72 | large_holder | NORRIS ELWOOD G |  | - | - |
| INVE | 72 | large_holder | Grossman Bruce |  | - | - |
| CAG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| APGE | 72 | large_holder | T. Rowe Price Investment  |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| XOM | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| GE | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 749.52 (-0.72% / -0.23% / 1.86%) [2026-07-13]
- QQQ: 712.25 (-1.83% / -1.46% / -0.57%) [2026-07-13]
- IWM: 293.23 (-0.93% / -1.9% / 0.97%) [2026-07-13]
- DIA: 524.29 (-0.28% / -1.09% / 3.21%) [2026-07-13]
- TLT: 83.96 (-0.6% / -1.74% / -1.98%) [2026-07-13]
- IEF: 93.29 (-0.36% / -0.94% / -0.78%) [2026-07-13]
- GLD: 366.68 (-2.74% / -4.04% / -5.08%) [2026-07-13]
- ^VIX: 16.67 (10.91% / 7.06% / -14.25%) [2026-07-13]
- BTC-USD: 61953.52 (-2.83% / -0.49% / -1.14%) [2026-07-13]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.16 (delta 1m: 0.01) [2026-07-09]
- Treasury 10Y yield: 4.54 (delta 1m: -0.02) [2026-07-09]
- Curva 10Y-2Y: 0.35 (delta 1m: -0.05) [2026-07-10]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.69 (delta 1m: -0.09) [2026-07-10]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.24 (delta 1m: -0.09) [2026-07-10]
- Dolar broad index: 120.6902 (delta 1m: 1.654) [2026-07-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DELL] LGT Fund Management Co Ltd . Takes $4 . 55 Million Position in Dell Technologies Inc . $DELL (2026-07-12)
- [DELL] Santa Clarita Children Eligible For $250 From The Dell Family (2026-07-11)
- [DELL] Dell Technologies ( NYSE : DELL ) Stock Price Up 4 . 2 % – Should You Buy ? (2026-07-11)
- [DELL] 2 , 026 Shares in Dell Technologies Inc . $DELL Purchased by Roman Butler Fullerton & Co . (2026-07-11)
- [NYSE: KRC] Investment Analyst Recent Ratings Updates for Kilroy Realty ( KRC ) (2026-06-29)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner MetLife Investment Management, LLC compro FINS por $1600000.0B el 2026-07-08.
- CFO Liu Chitung vendio UMC por $294.3M el 2026-07-13.
- 10% owner Pinetree Capital Ltd. opero TBRG por $55.9M el 2026-07-09 [senal en multiples fuentes].
- 10% owner Globalharvest Holdings Venture Ltd compro AVO por $7.9M el 2026-07-09 [senal en multiples fuentes].
- CEO Beck Scott Arthur compro GLOO por $3.5M el 2026-07-10.
- 10% owner Wang Xuning vendio SN por $401.2M el 2026-07-10.
- CEO Seto Wai Yue compro TDIC por $2.2M el 2026-07-07 [senal en multiples fuentes].
- CEO Huang Jack Jiajia compro COE por $3.5M el 2026-07-07.

**Polymarket — smart money (traders con mejor track record):**

- trashpilot · PnL $27,669 · win rate 88% · categorias: politics, sports, economy
- 0x5F659BcCBC353dBf7BcdffDEE73beE60bB482036-1780496231400 · PnL $20,692 · win rate 89% · categorias: sports, crypto
- 0x2c335066FE58fe9237c3d3Dc7b275C2a034a0563-1759935795465 · PnL $198,133 · win rate 73% · categorias: sports, politics, crypto
- omoi0i0 · PnL $45,481 · win rate 80% · categorias: sports
- TheReturnOfDarthMaul · PnL $382,750 · win rate 61% · categorias: crypto, sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 66 registros 30d · ultimo dato 2026-07-07
- **sec_insiders**: `ok` · 601 registros 30d · ultimo dato 2026-07-13
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-13
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`APGE, AVO, BEP, GLD, IEF, INTC, IPX, LION, NTSK, QQQ, SPY, TBRG, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
