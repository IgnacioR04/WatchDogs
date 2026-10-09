# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-09T21:11:21+00:00 · ventana señales 2026-09-09 -> 2026-10-09_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 85.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.84)
- Tendencia: `bull` (SPY 778.57 · MA50 766.28 · MA200 719.66 · dist MA200: 8.19%)
- Credito: `normal` (HY spread 3.15)
- Tipos: `flat` (curva 10y-2y 0.44)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+); VIX calmado (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 778.57 | 0.6% | 1.16% | 2.12% |
| QQQ | 12.0% | core | 751.27 | 0.49% | 0.23% | 5.2% |
| TLT | 12.0% | core | 77.98 | 0.14% | 0.65% | -3.19% |
| IOSP | 10.5% | satellite | 95.65 | -2.09% | -1.81% | 2.6% |
| GLD | 9.3% | core | 384.58 | 1.57% | 1.17% | -3.56% |
| HQY | 6.5% | satellite | 92.61 | -0.47% | 2.85% | -3.79% |
| IEF | 6.2% | core | 89.4 | -0.06% | 0.39% | -1.43% |
| ICFI | 5.8% | satellite | 87.55 | 0.84% | 6.95% | 1.86% |
| PRTA | 5.1% | satellite | 8.84 | 2.67% | 5.74% | -1.01% |
| MATV | 3.8% | satellite | 11.6 | -2.19% | -2.52% | -2.85% |
| CIFR | 1.8% | satellite | 13.52 | 0.15% | -13.94% | -19.76% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.2%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -3.6%
- Beta vs SPY: 0.593 · posiciones efectivas: 12.7 · HHI: 0.0788

**Por que estos satellite (señales WATCHDOG):**

- **ICFI** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **MATV** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **IOSP** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **PRTA** · score agregado 126.5 · 2 señales · fuentes: corporate_insider
- **HQY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CIFR** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NRXS | 74 | corporate_insider | Henrichs Timothy Robert | 3 | $9,375 | cluster_buy,small_amount |
| HQY | 72 | large_holder | Wasatch Advisors LP |  | - | - |
| COE | 71 | corporate_insider | Huang Jack Jiajia | 0 | $14,117,400 | - |
| NRXS | 71 | corporate_insider | Carrico Brian Allen | 3 | $1,297 | cluster_buy,small_amount |
| COE | 71 | corporate_insider | Huang Jack Jiajia | 0 | $10,318,950 | - |
| GWLL | 70 | large_holder | Ming Zhou |  | - | - |
| WBUY | 70 | large_holder | Zheng Mingjie |  | - | - |
| MLCO | 70 | large_holder | Melco International Devel |  | - | - |
| FMTOF | 70 | large_holder | Corley Thomas John |  | - | - |
| SOBR | 70 | large_holder | Corley Thomas John |  | - | - |
| TENX | 70 | large_holder | Dellora Investments Maste |  | - | - |
| BGB | 70 | large_holder | Coastal Bridge Advisors,  |  | - | - |
| OSS | 70 | large_holder | Galkin Vladimir |  | - | - |
| QTTB | 70 | large_holder | Frazier Life Sciences Pub |  | - | - |
| WBUY | 70 | large_holder | Hongliang Mao |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ANET | 62 | corporate_insider | Ullal Jayshree | $54,986,498 | - |
| TT | 60 | corporate_insider | Regnery David S | $23,083,680 | - |
| WBD | 60 | corporate_insider | Perrette Jean-Briac | $101,265,028 | - |
| WBD | 60 | corporate_insider | Zaslav David | $115,914,433 | - |
| ANET | 59 | corporate_insider | Ullal Jayshree | $13,928,003 | - |
| WBD | 59 | corporate_insider | Zeiler Gerhard | $69,379,674 | - |
| WBD | 59 | corporate_insider | Wiedenfels Gunnar | $92,506,222 | - |
| ANET | 58 | corporate_insider | Ullal Jayshree | $10,996,450 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 778.57 (0.6% / 1.16% / 2.12%) [2026-10-09]
- QQQ: 751.27 (0.49% / 0.23% / 5.2%) [2026-10-09]
- IWM: 278.94 (0.49% / -0.92% / -3.19%) [2026-10-09]
- DIA: 516.11 (0.87% / 0.98% / -1.61%) [2026-10-09]
- TLT: 77.98 (0.14% / 0.65% / -3.19%) [2026-10-09]
- IEF: 89.4 (-0.06% / 0.39% / -1.43%) [2026-10-09]
- GLD: 384.58 (1.57% / 1.17% / -3.56%) [2026-10-09]
- ^VIX: 14.84 (-3.7% / -3.07% / -6.31%) [2026-10-09]
- BTC-USD: 82505.83 (1.02% / -4.6% / 1.57%) [2026-10-09]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.75 (delta 1m: 0.32) [2026-10-08]
- Treasury 10Y yield: 5.22 (delta 1m: 0.39) [2026-10-08]
- Curva 10Y-2Y: 0.44 (delta 1m: 0.05) [2026-10-09]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.15 (delta 1m: 0.44) [2026-10-08]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.33 (delta 1m: -0.07) [2026-10-09]
- Dolar broad index: 121.3848 (delta 1m: 2.855) [2026-10-02]

## 5. Noticias y contexto del mundo (30d)

_(sin noticias este ciclo — GDELT no disponible)_

**Actores que han movido ficha este mes (top movimientos):**

- CEO Perrette Jean-Briac vendio WBD por $101.3M el 2026-10-06.
- CEO Zaslav David vendio WBD por $115.9M el 2026-10-06.
- CEO Zeiler Gerhard vendio WBD por $69.4M el 2026-10-06.
- CEO Ullal Jayshree vendio ANET por $55.0M el 2026-10-06.
- CFO Wiedenfels Gunnar vendio WBD por $92.5M el 2026-10-06.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $20.9M el 2026-10-07.
- CEO Regnery David S vendio TT por $23.1M el 2026-10-06.
- CEO Huang Jack Jiajia compro COE por $14.1M el 2026-09-25.

**Polymarket — smart money (traders con mejor track record):**

- monkeymashingkeyboard · PnL $64,107 · win rate 92% · categorias: sports
- esportsbetter1 · PnL $42,603 · win rate 94% · categorias: sports
- taylorsversion · PnL $79,120 · win rate 87% · categorias: sports, crypto
- ethanaz · PnL $58,340 · win rate 88% · categorias: sports, crypto
- OhWhenTheReds · PnL $83,792 · win rate 100% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 538 registros 30d · ultimo dato 2026-10-09
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-09
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CIFR, GLD, HQY, ICFI, IEF, IOSP, MATV, PRTA, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **85.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
