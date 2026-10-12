# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-12T15:38:52+00:00 · ventana señales 2026-09-12 -> 2026-10-12_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.2)
- Tendencia: `bull` (SPY 778.2 · MA50 766.94 · MA200 720.14 · dist MA200: 8.06%)
- Credito: `normal` (HY spread 3.15)
- Tipos: `flat` (curva 10y-2y 0.44)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 778.2 | -0.05% | 0.43% | 2.53% |
| QQQ | 11.4% | core | 746.35 | -0.65% | -1.3% | 5.35% |
| TLT | 11.4% | core | 77.97 | -0.01% | 1.12% | -3.26% |
| GLD | 8.6% | core | 382.04 | -0.66% | 0.66% | -2.75% |
| BPRE | 8.1% | satellite | 12.87 | -1.61% | 1.1% | 9.14% |
| HQY | 7.8% | satellite | 91.47 | -1.23% | -0.08% | -4.75% |
| ULS | 7.0% | satellite | 71.01 | 1.46% | 4.05% | 2.18% |
| IEF | 5.7% | core | 89.38 | -0.03% | 0.51% | -1.37% |
| PRTA | 5.6% | satellite | 8.5 | -3.85% | 2.78% | -4.06% |
| CIFR | 2.3% | satellite | 13.06 | -3.44% | -15.67% | -16.5% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.3%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -6.4%
- Beta vs SPY: 0.6 · posiciones efectivas: 13.8 · HHI: 0.0725

**Por que estos satellite (señales WATCHDOG):**

- **BPRE** · score agregado 252.5 · 4 señales · fuentes: corporate_insider
- **PRTA** · score agregado 126.5 · 2 señales · fuentes: corporate_insider
- **HQY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **ULS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CIFR** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NRXS | 74 | corporate_insider | Henrichs Timothy Robert | 3 | $9,375 | cluster_buy,small_amount |
| HQY | 72 | large_holder | Wasatch Advisors LP |  | - | - |
| ULS | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| COE | 71 | corporate_insider | Huang Jack Jiajia | 0 | $14,117,400 | - |
| NRXS | 71 | corporate_insider | Carrico Brian Allen | 3 | $1,297 | cluster_buy,small_amount |
| LCU | 71 | corporate_insider | Alford Tony L | 2 | $19,950 | cluster_buy,small_amount |
| COE | 71 | corporate_insider | Huang Jack Jiajia | 0 | $10,318,950 | - |
| GWLL | 70 | large_holder | Ming Zhou |  | - | - |
| WBUY | 70 | large_holder | Zheng Mingjie |  | - | - |
| MLCO | 70 | large_holder | Melco International Devel |  | - | - |
| FMTOF | 70 | large_holder | Corley Thomas John |  | - | - |
| SOBR | 70 | large_holder | Corley Thomas John |  | - | - |
| TENX | 70 | large_holder | Dellora Investments Maste |  | - | - |
| BGB | 70 | large_holder | Coastal Bridge Advisors,  |  | - | - |
| OSS | 70 | large_holder | Galkin Vladimir |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| IHT | 63 | corporate_insider | WIRTH JAMES F | $2,173,259,999 | - |
| ANET | 62 | corporate_insider | Ullal Jayshree | $54,986,498 | - |
| TT | 60 | corporate_insider | Regnery David S | $23,083,680 | - |
| ANET | 59 | corporate_insider | Ullal Jayshree | $15,041,778 | - |
| ANET | 59 | corporate_insider | Ullal Jayshree | $13,928,003 | - |
| WBD | 59 | corporate_insider | Wiedenfels Gunnar | $92,506,222 | - |
| ANET | 58 | corporate_insider | Ullal Jayshree | $10,996,450 | - |
| ANET | 58 | corporate_insider | Ullal Jayshree | $10,996,450 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 778.2 (-0.05% / 0.43% / 2.53%) [2026-10-12]
- QQQ: 746.35 (-0.65% / -1.3% / 5.35%) [2026-10-12]
- IWM: 278.67 (-0.1% / -1.66% / -2.96%) [2026-10-12]
- DIA: 518.35 (0.43% / 1.22% / -0.94%) [2026-10-12]
- TLT: 77.97 (-0.01% / 1.12% / -3.26%) [2026-10-12]
- IEF: 89.38 (-0.03% / 0.51% / -1.37%) [2026-10-12]
- GLD: 382.04 (-0.66% / 0.66% / -2.75%) [2026-10-12]
- ^VIX: 15.2 (2.43% / -2.06% / -11.11%) [2026-10-12]
- BTC-USD: 82634.42 (-1.25% / -0.77% / -4.11%) [2026-10-12]

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

**Temas dominantes**: ai (3), stock (3), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWD] CrowdStrike , Okta , Rubrik all reach one - year highs as AI continues to rally cyber sector (2026-10-01)
- [UTHR] Stocks making the biggest moves midday : ACN SNPS UTHR VICR (2026-10-01)
- [UTHR] United Therapeutics Won Its Patent War and Liquidia Collapsed (2026-10-01)
- [UTHR] United Therapeutics Won Its Patent War and Liquidia Collapsed (2026-10-01)
- [UTHR] United Therapeutics Corporation Prevails in Patent Litigation Against Liquidia (2026-10-01)
- [UTHR] FinancialContent - Why Is United Therapeutics ( UTHR ) Stock Rocketing Higher Today (2026-09-30)
- [DDOG] Can Datadog ( DDOG ) Platform Keep Growing as Companies Embrace AI ? (2026-09-30)

**Actores que han movido ficha este mes (top movimientos):**

- CEO WIRTH JAMES F vendio IHT por $2.2B el 2026-10-07.
- CEO Ullal Jayshree vendio ANET por $55.0M el 2026-10-06.
- CFO Wiedenfels Gunnar vendio WBD por $92.5M el 2026-10-06.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $20.9M el 2026-10-07.
- CEO Regnery David S vendio TT por $23.1M el 2026-10-06.
- CEO Huang Jack Jiajia compro COE por $14.1M el 2026-09-25.
- Director Yin Chung-Yao compro GGR por $26.5M el 2026-10-07.
- CEO Huang Jack Jiajia compro COE por $10.3M el 2026-09-23.

**Polymarket — smart money (traders con mejor track record):**

- Kch-Temp · PnL $60,880 · win rate 93% · categorias: sports
- alwaysfade · PnL $85,353 · win rate 90% · categorias: sports, politics, economy
- mooseborzoii · PnL $376,884 · win rate 73% · categorias: sports
- monkeymashingkeyboard · PnL $13,553 · win rate 92% · categorias: sports
- THEHIGHLIFE · PnL $119,936 · win rate 78% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 557 registros 30d · ultimo dato 2026-10-09
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-09
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BPRE, CIFR, GLD, HQY, IEF, PRTA, QQQ, SPY, TLT, ULS`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
