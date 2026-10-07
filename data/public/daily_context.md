# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-07T20:54:30+00:00 · ventana señales 2026-09-07 -> 2026-10-07_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.08)
- Tendencia: `bull` (SPY 777.22 · MA50 764.58 · MA200 718.67 · dist MA200: 8.15%)
- Credito: `normal` (HY spread 3.03)
- Tipos: `flat` (curva 10y-2y 0.48)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 777.22 | -0.24% | 1.91% | 2.2% |
| QQQ | 11.4% | core | 757.73 | -0.25% | 2.43% | 5.89% |
| TLT | 11.4% | core | 77.14 | -0.17% | -0.42% | -5.23% |
| GLD | 8.6% | core | 375.88 | -1.67% | -1.3% | -6.81% |
| TOST | 6.2% | satellite | 30.55 | 0.99% | 5.38% | -5.86% |
| SAH | 6.0% | satellite | 60.52 | -0.79% | 0.28% | -20.2% |
| RGEN | 5.7% | satellite | 167.22 | -4.37% | -13.01% | 1.31% |
| IEF | 5.7% | core | 89.11 | -0.02% | 0.12% | -2.7% |
| AVR | 5.1% | satellite | 6.82 | -3.26% | -12.23% | -20.05% |
| SWKS | 5.1% | satellite | 83.43 | 0.77% | -2.4% | 9.0% |
| CIFR | 2.6% | satellite | 14.56 | -6.06% | -7.99% | -13.85% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.9%
- VaR 95% 1d: 1.2% · CVaR 95% 1d: 1.5%
- Max drawdown historico: -6.9%
- Beta vs SPY: 0.788 · posiciones efectivas: 14.7 · HHI: 0.0679

**Por que estos satellite (señales WATCHDOG):**

- **SAH** · score agregado 186.2 · 3 señales · fuentes: corporate_insider
- **SWKS** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **AVR** · score agregado 131.7 · 2 señales · fuentes: corporate_insider
- **RGEN** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **TOST** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CIFR** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| AGMB | 79 | corporate_insider | Knotnerus Tim Jasper | 3 | $50,880 | cluster_buy |
| AGMB | 79 | corporate_insider | Knotnerus Tim Jasper | 3 | $43,500 | cluster_buy |
| AGMB | 78 | corporate_insider | Kemula Pierre Thadee Vict | 3 | $42,850 | cluster_buy |
| AGMB | 77 | corporate_insider | Kemula Pierre Thadee Vict | 3 | $26,010 | cluster_buy |
| AGMB | 76 | corporate_insider | Kemula Pierre Thadee Vict | 3 | $17,080 | cluster_buy,small_amount |
| AGMB | 75 | corporate_insider | Epstein David R | 3 | $43,500 | cluster_buy |
| AGMB | 75 | corporate_insider | Epstein David R | 3 | $42,850 | cluster_buy |
| RYN | 72 | large_holder | Cohen & Steers, Inc. |  | - | - |
| ABUS | 72 | large_holder | Morgan Stanley |  | - | - |
| SWKS | 72 | large_holder | FMR LLC |  | - | - |
| RGEN | 72 | large_holder | FMR LLC |  | - | - |
| SWKS | 72 | large_holder | Capital World Investors |  | - | - |
| TOST | 72 | large_holder | BlackRock, Inc. |  | - | - |
| SGRP | 70 | large_holder | BROWN ROBERT G/ |  | - | - |
| DBI | 70 | large_holder | Stone House Capital Manag |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| RITE | 61 | corporate_insider | Hendricks Lloyd Bernard I | $106,724,935 | - |
| HOOD | 60 | corporate_insider | Tenev Vladimir | $22,098,092 | - |
| HOOD | 60 | corporate_insider | Tenev Vladimir | $17,994,382 | - |
| S | 59 | corporate_insider | Weingarten Tomer | $13,323,531 | - |
| BNTX | 58 | corporate_insider | Sahin Ugur | $7,000,646 | - |
| PBF | 56 | corporate_insider | Control Empresarial de Ca | $10,095,096 | - |
| NBIS | 56 | corporate_insider | Nave Ophir | $25,104,342 | - |
| WDAY | 56 | corporate_insider | DUFFIELD DAVID A | $8,583,245 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 777.22 (-0.24% / 1.91% / 2.2%) [2026-10-07]
- QQQ: 757.73 (-0.25% / 2.43% / 5.89%) [2026-10-07]
- IWM: 277.7 (-1.29% / -0.07% / -4.2%) [2026-10-07]
- DIA: 511.02 (-0.69% / 0.49% / -2.27%) [2026-10-07]
- TLT: 77.14 (-0.17% / -0.42% / -5.23%) [2026-10-07]
- IEF: 89.11 (-0.02% / 0.12% / -2.7%) [2026-10-07]
- GLD: 375.88 (-1.67% / -1.3% / -6.81%) [2026-10-07]
- ^VIX: 15.08 (0.47% / -7.71% / -8.38%) [2026-10-07]
- BTC-USD: 83334.56 (-2.6% / -1.38% / 9.07%) [2026-10-07]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.79 (delta 1m: 0.42) [2026-10-06]
- Treasury 10Y yield: 5.27 (delta 1m: 0.49) [2026-10-06]
- Curva 10Y-2Y: 0.48 (delta 1m: 0.07) [2026-10-06]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.03 (delta 1m: 0.35) [2026-10-06]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.36 (delta 1m: 0.01) [2026-10-06]
- Dolar broad index: 121.3848 (delta 1m: 2.855) [2026-10-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [NBIS] Nebius Group ( NASDAQ : NBIS ) Stock : Insider John Wilson Iv Boynton Sells 50 Shares (2026-10-01)
- [NBIS] Could Palantir ( PLTR ) Partnership with Nebius Group ( NBIS ) Accelerate its AI Growth ? (2026-09-24)
- [NBIS] Nebius Group ( NASDAQ : NBIS ) Trading Down 4 % – Here What Happened (2026-09-23)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Hendricks Lloyd Bernard III opero RITE por $103.5M el 2026-09-30.
- CEO Weingarten Tomer vendio S por $13.3M el 2026-10-05.
- CEO Tenev Vladimir vendio HOOD por $22.1M el 2026-10-05.
- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro Keenova Therapeutics plc por $42.1M el 2026-09-24.
- 10% owner L1 Capital Pty Ltd compro AVR por $4.9M el 2026-10-05.
- CEO Sahin Ugur vendio BNTX por $7.0M el 2026-10-05.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- Sharky6999 · PnL $147,724 · win rate 97% · categorias: crypto, sports, economy
- Diabolical-Prize · PnL $87,003 · win rate 95% · categorias: sports, economy
- fantasy7788 · PnL $43,705 · win rate 98% · categorias: sports, crypto
- 0x16bb9951a36fce71e2ef57890b786145e0ba8492 · PnL $70,562 · win rate 95% · categorias: sports
- CyberScore.live · PnL $23,597 · win rate 97% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 585 registros 30d · ultimo dato 2026-10-07
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-07
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AVR, CIFR, GLD, IEF, QQQ, RGEN, SAH, SPY, SWKS, TLT, TOST`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
