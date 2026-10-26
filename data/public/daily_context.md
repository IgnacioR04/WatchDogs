# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-26T23:27:24+00:00 · ventana señales 2026-09-26 -> 2026-10-26_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `neutral`  -> **presupuesto de riesgo recomendado: 60.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.39)
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
| NATH | 5.3% | satellite | 102.05 | 0.11% | 0.15% | 0.49% |
| IEF | 4.0% | core | 91.12 | 0.08% | 1.15% | 2.13% |
| BBT | 3.2% | satellite | 30.86 | 2.63% | 12.79% | 10.97% |
| NXG | 3.0% | satellite | 46.15 | 3.92% | -1.22% | -13.21% |
| BPRE | 2.6% | satellite | 12.56 | 0.88% | 3.68% | 1.68% |
| STC | 2.2% | satellite | 42.96 | -2.52% | -17.61% | -25.34% |
| PRTA | 1.6% | satellite | 8.4 | 2.44% | -0.94% | -3.67% |
| THRM | 1.5% | satellite | 28.59 | -0.03% | -0.07% | -9.36% |
| BWMN | 0.9% | satellite | 42.84 | 0.02% | 0.12% | 0.54% |
| CIFR | 0.7% | satellite | 7.71 | -2.9% | -13.76% | -53.94% |
| NBIS | 0.7% | satellite | 153.27 | -3.45% | -9.97% | -33.9% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 6.7%
- VaR 95% 1d: 0.7% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -3.2%
- Beta vs SPY: 0.492 · posiciones efectivas: 25.4 · HHI: 0.0393

**Por que estos satellite (señales WATCHDOG):**

- **STC** · score agregado 302.6 · 4 señales · fuentes: corporate_insider
- **CIFR** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **NBIS** · score agregado 163.4 · 3 señales · fuentes: corporate_insider
- **BPRE** · score agregado 155.1 · 2 señales · fuentes: corporate_insider
- **THRM** · score agregado 153.2 · 2 señales · fuentes: corporate_insider
- **NXG** · score agregado 148.2 · 2 señales · fuentes: corporate_insider
- **BBT** · score agregado 128.4 · 2 señales · fuentes: corporate_insider, large_holder
- **PRTA** · score agregado 124.6 · 2 señales · fuentes: corporate_insider
- **NATH** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BWMN** · score agregado 65.0 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BPRE | 78 | corporate_insider | KAMFAR RAMIN | 2 | $1,368,063 | cluster_buy |
| THRM | 77 | corporate_insider | Presley William T. | 2 | $130,000 | cluster_buy |
| BPRE | 77 | corporate_insider | KAMFAR RAMIN | 2 | $758,029 | cluster_buy |
| STC | 76 | corporate_insider | Corey William S. Jr. | 3 | $93,640 | cluster_buy |
| STC | 76 | corporate_insider | BRADLEY C ALLEN JR | 3 | $94,600 | cluster_buy |
| THRM | 76 | corporate_insider | MASCARENAS PAUL ANTHONY | 2 | $532,600 | cluster_buy |
| STC | 75 | corporate_insider | Apel Thomas G | 3 | $48,000 | cluster_buy |
| STC | 75 | corporate_insider | Apel Thomas G | 3 | $47,470 | cluster_buy |
| NXG | 75 | corporate_insider | Swank Jerry V | 2 | $439,493 | cluster_buy |
| NXG | 74 | corporate_insider | Nelson Blake | 2 | $39,582 | cluster_buy |
| BPRE | 74 | corporate_insider | Ruddy Jordan B. | 2 | $24,987 | cluster_buy,small_amount |
| LONA | 72 | large_holder | Perceptive Advisors LLC |  | - | - |
| NATH | 72 | large_holder | Howard M. Lorber |  | - | - |
| CHKP | 72 | large_holder | Gil Shwed |  | - | - |
| DEVSF | 72 | large_holder | Helena Global Investment  |  | - | - |

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
- ^VIX: 18.39 (-5.45% / -0.27% / 14.44%) [2026-10-26]
- BTC-USD: 79885.16 (-0.17% / -4.91% / -6.63%) [2026-10-26]

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

**Temas dominantes**: stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ALMR] Alamar Biosciences ( NASDAQ : ALMR ) Major Shareholder Corporate Gp Vi Ltd . Qiming Sells 133 , 811 Shares of Stock (2026-10-24)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Carrillo Antonio vendio ACA por $100.1M el 2026-10-23.
- CEO Essl Reid S vendio ACA por $19.8M el 2026-10-23.
- CFO Peck Gail M vendio ACA por $19.3M el 2026-10-23.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $8.7M el 2026-10-22.
- CEO Cole Kerry S vendio ACA por $7.8M el 2026-10-23.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- RJW1 · PnL $192,931 · win rate 99% · categorias: sports
- monkeymashingkeyboard · PnL $202,940 · win rate 92% · categorias: sports
- 1l2ihj34li12u34 · PnL $57,894 · win rate 99% · categorias: sports
- TAIWANNUMBERONE · PnL $147,676 · win rate 93% · categorias: sports, politics
- CyberScore.live · PnL $50,881 · win rate 97% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 726 registros 30d · ultimo dato 2026-10-26
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-26
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BBT, BPRE, BWMN, CIFR, GLD, IEF, NATH, NBIS, NXG, PRTA, QQQ, SPY, STC, THRM, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
