# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-27T08:06:15+00:00 · ventana señales 2026-09-27 -> 2026-10-27_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `neutral`  -> **presupuesto de riesgo recomendado: 60.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.4)
- Tendencia: `neutral` (SPY 765.37 · MA50 766.72 · MA200 724.41 · dist MA200: 5.65%)
- Credito: `normal` (HY spread 3.38)
- Tipos: `flat` (curva 10y-2y 0.32)
- Fed Funds: 3.75%

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **60.0%** · cash **40.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.37 | 0.71% | -0.14% | -0.03% |
| QQQ | 8.1% | core | 712.2 | 1.11% | -0.86% | -3.3% |
| TLT | 8.1% | core | 81.68 | 0.42% | 2.79% | 4.31% |
| GLD | 6.1% | core | 367.82 | 0.33% | -3.13% | -2.67% |
| NATH | 5.2% | satellite | 102.05 | 0.0% | 0.17% | 0.56% |
| IEF | 4.0% | core | 91.12 | 0.08% | 1.15% | 2.13% |
| BBT | 3.2% | satellite | 30.86 | 2.63% | 12.79% | 10.97% |
| BPRE | 2.8% | satellite | 12.56 | 0.88% | 3.68% | 1.68% |
| STC | 2.4% | satellite | 42.96 | -2.52% | -17.61% | -25.34% |
| GPI | 2.0% | satellite | 243.88 | -0.44% | 1.92% | 0.68% |
| PRTA | 1.8% | satellite | 8.4 | 2.44% | -0.94% | -3.67% |
| THRM | 1.7% | satellite | 28.59 | -0.03% | -0.07% | -9.36% |
| BWMN | 1.2% | satellite | 42.84 | 0.02% | 0.12% | 0.54% |
| CIFR | 0.8% | satellite | 7.71 | -2.9% | -13.76% | -53.94% |
| NBIS | 0.7% | satellite | 153.27 | -3.45% | -9.97% | -33.9% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 7.3%
- VaR 95% 1d: 0.7% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -4.2%
- Beta vs SPY: 0.478 · posiciones efectivas: 25.6 · HHI: 0.0391

**Por que estos satellite (señales WATCHDOG):**

- **GPI** · score agregado 1782.6 · 29 señales · fuentes: corporate_insider
- **STC** · score agregado 302.6 · 4 señales · fuentes: corporate_insider
- **CIFR** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **NBIS** · score agregado 163.4 · 3 señales · fuentes: corporate_insider
- **THRM** · score agregado 153.2 · 2 señales · fuentes: corporate_insider
- **BBT** · score agregado 128.4 · 2 señales · fuentes: corporate_insider, large_holder
- **PRTA** · score agregado 124.6 · 2 señales · fuentes: corporate_insider
- **BPRE** · score agregado 123.1 · 2 señales · fuentes: corporate_insider
- **NATH** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BWMN** · score agregado 65.0 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| THRM | 77 | corporate_insider | Presley William T. | 2 | $130,000 | cluster_buy |
| STC | 76 | corporate_insider | Corey William S. Jr. | 3 | $93,640 | cluster_buy |
| STC | 76 | corporate_insider | BRADLEY C ALLEN JR | 3 | $94,600 | cluster_buy |
| THRM | 76 | corporate_insider | MASCARENAS PAUL ANTHONY | 2 | $532,600 | cluster_buy |
| STC | 75 | corporate_insider | Apel Thomas G | 3 | $48,000 | cluster_buy |
| STC | 75 | corporate_insider | Apel Thomas G | 3 | $47,470 | cluster_buy |
| LONA | 72 | large_holder | Perceptive Advisors LLC |  | - | - |
| NATH | 72 | large_holder | Howard M. Lorber |  | - | - |
| OPTU | 72 | large_holder | SUBIN NEIL S |  | - | - |
| CHKP | 72 | large_holder | Gil Shwed |  | - | - |
| BBT | 72 | large_holder | Integrated Core Strategie |  | - | - |
| SAFX | 70 | large_holder | EEME Energy SPV I, LLC |  | - | - |
| SLMT | 70 | large_holder | RBCH Ltd. |  | - | - |
| GSM | 70 | large_holder | Hosking Partners LLP |  | - | - |
| GCDT | 70 | large_holder | Xuewen Liu |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ACA | 60 | corporate_insider | Carrillo Antonio | $100,086,000 | - |
| LRCX | 58 | corporate_insider | ARCHER TIMOTHY | $7,128,428 | - |
| PG | 57 | corporate_insider | Jejurikar Shailesh | $5,708,048 | - |
| PEP | 56 | corporate_insider | Laguarta Ramon | $4,053,891 | - |
| ACA | 56 | corporate_insider | Essl Reid S | $19,825,650 | - |
| SNOW | 55 | corporate_insider | Dageville Benoit | $16,087,000 | - |
| ACA | 55 | corporate_insider | Peck Gail M | $19,343,400 | - |
| PACS | 55 | corporate_insider | Murray Jason Hulse | $2,253,785 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.37 (0.71% / -0.14% / -0.03%) [2026-10-26]
- QQQ: 712.2 (1.11% / -0.86% / -3.3%) [2026-10-26]
- IWM: 276.99 (0.45% / 2.1% / -1.08%) [2026-10-26]
- DIA: 522.97 (0.31% / 0.78% / 1.76%) [2026-10-26]
- TLT: 81.68 (0.42% / 2.79% / 4.31%) [2026-10-26]
- IEF: 91.12 (0.08% / 1.15% / 2.13%) [2026-10-26]
- GLD: 367.82 (0.33% / -3.13% / -2.67%) [2026-10-26]
- ^VIX: 18.4 (0.05% / 6.3% / 14.71%) [2026-10-27]
- BTC-USD: 79810.76 (-0.24% / -1.85% / -4.16%) [2026-10-27]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.69 (delta 1m: -0.16) [2026-10-23]
- Treasury 10Y yield: 5.0 (delta 1m: -0.11) [2026-10-23]
- Curva 10Y-2Y: 0.32 (delta 1m: 0.01) [2026-10-26]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.38 (delta 1m: 0.58) [2026-10-23]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.01) [2026-10-26]
- Dolar broad index: 121.3202 (delta 1m: 1.203) [2026-10-23]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3)

**Titulares recientes (GDELT, tickers con mas señales):**

- [GPI] Conifer Management Buys $16 . 9 Million Group 1 Automotive Shares . What Does This Mean for Investors ? (2026-10-24)
- [STX] Seagate Technology Holdings PLC $STX Holdings Trimmed by XXI Wealth LLC (2026-10-24)
- [STX] Seagate Technology Holdings PLC $STX Stake Lowered by Atlatl Advisers LLC (2026-10-24)
- [STX] Seagate Technology ( NASDAQ : STX ) Shares Down 7 . 9 % – Time to Sell ? (2026-10-23)
- [JBL] Jabil ( JBL ) Guides to 24 % Growth , but Can Thin Margins Carry the Plan ? (2026-10-21)
- [JBL] Analyzing Yaskawa Electric ( OTCMKTS : YASKY ) and Jabil ( NYSE : JBL ) (2026-10-17)
- [JBL] Jabil , Inc . $JBL Stock : Triasima Portfolio Management inc . Grows Stake (2026-10-16)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Carrillo Antonio vendio ACA por $100.1M el 2026-10-23.
- CEO Essl Reid S vendio ACA por $19.8M el 2026-10-23.
- CFO Peck Gail M vendio ACA por $19.3M el 2026-10-23.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $8.7M el 2026-10-22.
- CEO Cole Kerry S vendio ACA por $7.8M el 2026-10-23.
- 10% owner Conifer Management, L.L.C. compro GPI por $4.6M el 2026-10-22.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $2,563,871 · win rate 88% · categorias: sports, politics
- RJW1 · PnL $204,413 · win rate 99% · categorias: sports
- monkeymashingkeyboard · PnL $387,061 · win rate 92% · categorias: sports
- juice-fruit · PnL $91,473 · win rate 96% · categorias: sports
- googleplay · PnL $2,088,550 · win rate 78% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 734 registros 30d · ultimo dato 2026-10-26
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-26
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BBT, BPRE, BWMN, CIFR, GLD, GPI, IEF, NATH, NBIS, PRTA, QQQ, SPY, STC, THRM, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **60.0%** (el resto es cash). Estamos en regimen `neutral`.
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
