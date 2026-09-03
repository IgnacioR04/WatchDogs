# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-03T14:53:51+00:00 · ventana señales 2026-08-04 -> 2026-09-03_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.95)
- Tendencia: `bull` (SPY 768.24 · MA50 756.04 · MA200 709.29 · dist MA200: 8.31%)
- Credito: `tight` (HY spread 2.66)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 768.24 | 0.4% | -0.37% | -0.04% |
| QQQ | 12.0% | core | 711.72 | 0.35% | -1.3% | -0.41% |
| TLT | 12.0% | core | 82.27 | 0.39% | -0.66% | 0.08% |
| GLD | 9.3% | core | 410.36 | 1.88% | -2.9% | 5.31% |
| STRT | 7.1% | satellite | 73.65 | 0.8% | 4.79% | -15.16% |
| MAX | 7.1% | satellite | 12.0 | -4.23% | -4.53% | -2.76% |
| DT | 7.0% | satellite | 52.31 | 2.83% | -2.1% | 7.04% |
| IEF | 6.2% | core | 92.39 | 0.23% | -0.54% | -0.24% |
| GLOB | 6.2% | satellite | 39.42 | 1.39% | -1.87% | 5.83% |
| WIX | 3.8% | satellite | 84.18 | -2.9% | -1.85% | 38.26% |
| SUJA | 2.3% | satellite | 10.33 | 1.08% | 14.78% | 62.68% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.8%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -1.8%
- Beta vs SPY: 0.542 · posiciones efectivas: 13.1 · HHI: 0.0765

**Por que estos satellite (señales WATCHDOG):**

- **WIX** · score agregado 302.4 · 4 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **DT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GLOB** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MAX** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **STRT** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| WIX | 78 | corporate_insider | Abrahami Avishai | 6 | $39,168 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 6 | $22,519 | cluster_buy,small_amount |
| JUSH | 77 | corporate_insider | Cacioppo James | 2 | $128,712 | cluster_buy |
| WIX | 77 | corporate_insider | Shemesh Lior | 6 | $27,310 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 6 | $16,230 | cluster_buy,small_amount |
| GROV | 76 | corporate_insider | Yurcisin Jeffrey Michael | 2 | $94,689 | cluster_buy |
| OPAL | 76 | corporate_insider | Comora Adam | 2 | $96,500 | cluster_buy |
| WIX | 74 | corporate_insider | Meyer Shelly B | 6 | $28,687 | cluster_buy |
| JUSH | 74 | corporate_insider | Cacioppo James | 2 | $36,560 | cluster_buy |
| WIX | 73 | corporate_insider | Abrahami Avishai | 6 | $3,294 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Shai Omer | 6 | $29,346 | cluster_buy |
| WIX | 72 | corporate_insider | Even-Haim Yaniv | 6 | $19,165 | cluster_buy,small_amount |
| DT | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| GLOB | 72 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |
| ZNB | 72 | large_holder | L1 Capital Global Opportu |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| WHD | 58 | corporate_insider | Bender Joel | $7,037,200 | - |
| WHD | 58 | corporate_insider | Bender Scott | $7,037,200 | - |
| AMBQ | 56 | corporate_insider | Esaka Fumihide | $2,761,534 | - |
| IRM | 55 | corporate_insider | Meaney William L | $2,391,461 | - |
| MRVL | 55 | corporate_insider | Koopmans Chris | $2,032,700 | - |
| AUGO | 54 | corporate_insider | Sousa Mauad Bruno | $10,353,000 | - |
| OKLO | 54 | corporate_insider | DeWitte Jacob | $1,536,000 | - |
| OKLO | 54 | corporate_insider | DeWitte Jacob | $1,546,400 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 768.24 (0.4% / -0.37% / -0.04%) [2026-09-03]
- QQQ: 711.72 (0.35% / -1.3% / -0.41%) [2026-09-03]
- IWM: 294.13 (0.04% / -1.89% / -1.38%) [2026-09-03]
- DIA: 534.58 (0.75% / -0.12% / -0.59%) [2026-09-03]
- TLT: 82.27 (0.39% / -0.66% / 0.08%) [2026-09-03]
- IEF: 92.39 (0.23% / -0.54% / -0.24%) [2026-09-03]
- GLD: 410.36 (1.88% / -2.9% / 5.31%) [2026-09-03]
- ^VIX: 14.95 (-1.64% / 3.03% / -1.32%) [2026-09-03]
- BTC-USD: 80163.94 (3.7% / 2.45% / 27.29%) [2026-09-03]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.39 (delta 1m: 0.14) [2026-09-01]
- Treasury 10Y yield: 4.79 (delta 1m: 0.09) [2026-09-01]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.03) [2026-09-02]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.66 (delta 1m: -0.07) [2026-09-02]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.11) [2026-09-02]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (10), ai (6), regulatory (3), leadership (2), merger (1), legal (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [IVZ] Invesco Ltd . - Invesco Ltd : Form 8 . 3 - Bodycote PLC ; Public dealing disclosure (2026-09-03)
- [IVZ] Tranquilli Financial Advisor LLC Takes Position in Invesco Optimum Yield Diversified Commodity Strategy No K - 1 ETF $PDBC (2026-09-03)
- [WIX] Class Action Lawsuit Filed Against Wix . com Ltd . ( WIX ) - Recover Losses ... (2026-09-03)
- [CRWD] Rubrik and CrowdStrike Bring AI - Driven Automation to Identity Threat Response (2026-09-03)
- [CRWD] MBody AI Orchestrator ( NASDAQ : MBAI ) Earns Finalist Spot Alongside CrowdStrike And CVS Health In 2026 A . I . Awards (2026-09-03)
- [CRWD] With Cybersecurity for Cloud and Artificial Intelligence , CrowdStrike Stock Is Positioned for Sustained Growth (2026-09-03)
- [CRWD] CrowdStrike Is Putting GPT - 5 . 6 Cyber Inside Falcon . Is OpenAI Becoming a Cybersecurity Distribution Partner ? (2026-09-03)
- [WIX] Why Wix . com Stock Soared 60 % In August | The Motley Fool (2026-09-03)
- [WIX] Why Wix . com Stock Soared 60 % In August (2026-09-03)
- [WIX] Why Wix . com Stock Soared 60 % In August | The Motley Fool (2026-09-03)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Williams Charles Alan compro NPB por $1.4M el 2026-09-01.
- CEO Bender Joel vendio WHD por $7.0M el 2026-09-01.
- 10% owner Empery Asset Management, LP compro EMPD por $1.8M el 2026-09-01 [senal en multiples fuentes].
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- kekasaur · PnL $71,779 · win rate 94% · categorias: sports
- theowalcott · PnL $29,710 · win rate 100% · categorias: sports
- rollobravado · PnL $17,447 · win rate 99% · categorias: sports, politics
- cruzzzz · PnL $32,032 · win rate 95% · categorias: sports, politics
- ExplosiveNinja · PnL $18,947 · win rate 97% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 638 registros 30d · ultimo dato 2026-09-03
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-03
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`DT, GLD, GLOB, IEF, MAX, QQQ, SPY, STRT, SUJA, TLT, WIX`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **95.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
