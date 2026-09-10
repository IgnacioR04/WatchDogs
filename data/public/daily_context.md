# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-10T21:54:26+00:00 · ventana señales 2026-08-11 -> 2026-09-10_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.84)
- Tendencia: `neutral` (SPY 757.83 · MA50 758.25 · MA200 711.5 · dist MA200: 6.51%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.39)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 757.83 | -0.6% | -0.96% | -1.9% |
| QQQ | 9.8% | core | 708.69 | -1.06% | -0.08% | -2.07% |
| TLT | 9.8% | core | 80.78 | -1.16% | -1.43% | -1.24% |
| CSQ | 8.0% | satellite | 20.6 | -1.2% | -1.39% | -0.66% |
| GLD | 7.3% | core | 396.36 | -1.73% | -1.59% | -2.11% |
| RSG | 6.2% | satellite | 221.08 | -0.62% | -0.65% | 3.18% |
| IEF | 4.9% | core | 91.18 | -0.78% | -1.08% | -1.56% |
| BLFS | 3.2% | satellite | 34.92 | -0.03% | -2.78% | -0.14% |
| DT | 2.9% | satellite | 51.42 | 1.62% | 1.08% | 3.75% |
| GOLD | 2.5% | satellite | 45.88 | -6.99% | 4.7% | 2.69% |
| PRGO | 2.0% | satellite | 13.59 | -5.23% | -6.21% | 9.3% |
| TWST | 1.5% | satellite | 126.85 | 1.06% | -3.17% | 1.31% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.9%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -2.5%
- Beta vs SPY: 0.551 · posiciones efectivas: 18.3 · HHI: 0.0546

**Por que estos satellite (señales WATCHDOG):**

- **RSG** · score agregado 488.9 · 7 señales · fuentes: corporate_insider, large_holder
- **CSQ** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **TWST** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **DT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BLFS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PRGO** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GOLD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| CYBN | 78 | corporate_insider | Glavine Paul | 2 | $1,178,280 | cluster_buy |
| GRCE | 78 | corporate_insider | Kohli Prashant | 2 | $214,000 | cluster_buy |
| CYBN | 78 | corporate_insider | So Eric H. L. | 2 | $1,208,900 | cluster_buy |
| RSG | 72 | corporate_insider | CASCADE INVESTMENT, L.L.C | 0 | $55,425,001 | - |
| RSG | 72 | corporate_insider | CASCADE INVESTMENT, L.L.C | 0 | $47,226,807 | - |
| ZDGE | 72 | large_holder | Michael Jonas |  | - | - |
| MGX | 72 | large_holder | Thomas Brian C. |  | - | - |
| DT | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| BLFS | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| TFX | 72 | large_holder | JANUS HENDERSON GROUP Ltd |  | - | - |
| TWST | 72 | large_holder | ARK Investment Management |  | - | - |
| TWST | 72 | large_holder | FMR LLC |  | - | - |
| PRGO | 72 | large_holder | T. Rowe Price Associates, |  | - | - |
| SIG | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| GRCE | 71 | corporate_insider | Opaleye Management Inc. | 2 | $19,699 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| LRCX | 58 | corporate_insider | ARCHER TIMOTHY | $9,577,800 | - |
| DDOG | 57 | corporate_insider | Pomel Olivier | $5,063,681 | - |
| VST | 56 | corporate_insider | HUDSON SCOTT A | $4,377,228 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $4,002,735 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $3,670,518 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $3,520,145 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $2,958,937 | - |
| DCI | 56 | corporate_insider | Carpenter Tod E. | $2,912,285 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 757.83 (-0.6% / -0.96% / -1.9%) [2026-09-10]
- QQQ: 708.69 (-1.06% / -0.08% / -2.07%) [2026-09-10]
- IWM: 287.7 (-1.01% / -2.15% / -4.96%) [2026-09-10]
- DIA: 520.75 (-0.63% / -1.86% / -2.97%) [2026-09-10]
- TLT: 80.78 (-1.16% / -1.43% / -1.24%) [2026-09-10]
- IEF: 91.18 (-0.78% / -1.08% / -1.56%) [2026-09-10]
- GLD: 396.36 (-1.73% / -1.59% / -2.11%) [2026-09-10]
- ^VIX: 17.84 (8.38% / 24.58% / 21.94%) [2026-09-10]
- BTC-USD: 77124.37 (-1.45% / -3.38% / -1.55%) [2026-09-10]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.43 (delta 1m: 0.18) [2026-09-09]
- Treasury 10Y yield: 4.83 (delta 1m: 0.11) [2026-09-09]
- Curva 10Y-2Y: 0.39 (delta 1m: -0.09) [2026-09-10]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.71 (delta 1m: -0.01) [2026-09-09]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.4 (delta 1m: 0.13) [2026-09-10]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (2), merger (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ADI] Analog Devices Wants Robots to Think Without Nvidia | Is ADI the Next Big AI Stock ? (2026-09-10)
- [ADI] Analog Devices ( NASDAQ : ADI ) CFO Richard Puccio , Jr . Sells 1 , 500 Shares (2026-09-10)
- [ADI] Analog Devices acquisition Alif Semiconductor : Analog Devices to buy Alif Semiconductor for $1 . 35 billion (2026-09-10)
- [FROG] Head to Head Survey : JFrog ( NASDAQ : FROG ) & Blackbaud ( NASDAQ : BLKB ) (2026-09-10)
- [FROG] Analysts see upside in JFrog , despite slide from peak (2026-09-09)
- [FROG] Investment Analyst Weekly Ratings Updates for JFrog ( FROG ) (2026-09-09)
- [FROG] JFrog CFO Sells 17 , 216 Shares for $1 . 6 Million Amid a Soaring Stock Price (2026-09-06)
- [LIFE] Ethos ( LIFE ) Grows Revenue 113 % While Margins Quietly Compress (2026-09-04)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $47.2M el 2026-09-09 [senal en multiples fuentes].
- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $55.4M el 2026-09-08 [senal en multiples fuentes].
- CEO KHOSROWSHAHI DARA compro UBER por $10.0M el 2026-09-10.
- CEO ARCHER TIMOTHY vendio LRCX por $9.6M el 2026-09-09.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.

**Polymarket — smart money (traders con mejor track record):**

- theowalcott · PnL $185,347 · win rate 100% · categorias: sports
- Diabolical-Prize · PnL $407,859 · win rate 94% · categorias: sports
- mmklop · PnL $72,795 · win rate 96% · categorias: sports
- Kch-Temp · PnL $156,467 · win rate 89% · categorias: sports
- CORGI8 · PnL $73,487 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 574 registros 30d · ultimo dato 2026-09-10
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-10
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BLFS, CSQ, DT, GLD, GOLD, IEF, PRGO, QQQ, RSG, SPY, TLT, TWST`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
