# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-03T00:35:54+00:00 · ventana señales 2026-08-04 -> 2026-09-03_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.2)
- Tendencia: `bull` (SPY 761.78 · MA50 754.71 · MA200 708.29 · dist MA200: 7.55%)
- Credito: `tight` (HY spread 2.65)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 761.78 | -0.69% | -0.54% | -1.24% |
| QQQ | 12.0% | core | 707.64 | -1.27% | -0.43% | -2.24% |
| TLT | 12.0% | core | 81.87 | -0.41% | -1.54% | -0.77% |
| MAX | 12.0% | satellite | 12.3 | -2.54% | -3.91% | -3.53% |
| GLOB | 10.7% | satellite | 39.68 | -2.53% | -1.0% | 4.07% |
| GLD | 9.4% | core | 396.75 | -2.86% | -7.32% | 6.04% |
| WIX | 6.7% | satellite | 88.38 | 0.14% | 4.68% | 55.48% |
| IEF | 6.3% | core | 92.1 | -0.33% | -1.15% | -0.88% |
| SUJA | 3.9% | satellite | 10.43 | 3.57% | 11.79% | -8.51% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 17.4%
- VaR 95% 1d: 1.5% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -2.4%
- Beta vs SPY: 0.531 · posiciones efectivas: 11.4 · HHI: 0.0879

**Por que estos satellite (señales WATCHDOG):**

- **WIX** · score agregado 302.4 · 4 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **GLOB** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MAX** · score agregado 71.8 · 1 señales · fuentes: large_holder

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
| RGCO | 73 | corporate_insider | WILLIAMSON JOHN B III | 3 | $21,300 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Abrahami Avishai | 6 | $3,294 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Shai Omer | 6 | $29,346 | cluster_buy |
| WIX | 72 | corporate_insider | Even-Haim Yaniv | 6 | $19,165 | cluster_buy,small_amount |
| DT | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| GLOB | 72 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| WHD | 58 | corporate_insider | Bender Joel | $7,037,200 | - |
| WHD | 58 | corporate_insider | Bender Scott | $7,037,200 | - |
| AMBQ | 56 | corporate_insider | Esaka Fumihide | $2,761,534 | - |
| IRM | 55 | corporate_insider | Meaney William L | $2,391,461 | - |
| V | 55 | corporate_insider | MCINERNEY RYAN | $2,230,444 | - |
| MRVL | 55 | corporate_insider | Koopmans Chris | $2,032,700 | - |
| AUGO | 54 | corporate_insider | Sousa Mauad Bruno | $10,353,000 | - |
| OKLO | 54 | corporate_insider | DeWitte Jacob | $1,536,000 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 761.78 (-0.69% / -0.54% / -1.24%) [2026-09-01]
- QQQ: 707.64 (-1.27% / -0.43% / -2.24%) [2026-09-01]
- IWM: 290.57 (-1.14% / -2.48% / -1.91%) [2026-09-01]
- DIA: 527.75 (-0.72% / -1.11% / -0.57%) [2026-09-01]
- TLT: 81.87 (-0.41% / -1.54% / -0.77%) [2026-09-01]
- IEF: 92.1 (-0.33% / -1.15% / -0.88%) [2026-09-01]
- GLD: 396.75 (-2.86% / -7.32% / 6.04%) [2026-09-01]
- ^VIX: 15.2 (-6.98% / -1.62% / -7.88%) [2026-09-02]
- BTC-USD: 76982.94 (-0.54% / -1.09% / 21.42%) [2026-09-03]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.39 (delta 1m: 0.14) [2026-09-01]
- Treasury 10Y yield: 4.79 (delta 1m: 0.09) [2026-09-01]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.03) [2026-09-02]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.65 (delta 1m: -0.13) [2026-09-01]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.11) [2026-09-02]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (9), ai (4), leadership (2), legal (2), regulatory (2), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [WIX] Lost Money on Wix . com Ltd . ( WIX )? Urged to Join Class Action Before ... (2026-09-03)
- [AXON] Axon Enterprise ( NASDAQ : AXON ) President Sells 16 , 775 Shares (2026-09-02)
- [AMBQ] Ambiq Micro ( NYSE : AMBQ ) CEO Fumihide Esaka Sells 48 , 973 Shares (2026-09-02)
- [AMBQ] Insider Selling : Ambiq Micro ( NYSE : AMBQ ) CEO Sells $2 , 785 , 840 . 00 in Stock (2026-09-02)
- [CNO] CNO Financial Group ( NYSE : CNO ) Insider Sells $360 , 734 . 40 in Stock (2026-09-02)
- [CNO] CNO Financial Group ( NYSE : CNO ) Insider Karen Detoro Sells 9 , 336 Shares of Stock (2026-09-02)
- [WIX] Bragar Eagel & Squire , P . C . Urges Wix . com Ltd . Investors to Contact the Firm Regarding ... (2026-09-01)
- [WIX] Wix . com Ltd . ( WIX ) Shareholders Who Lost Money Have Opportunity to Lead Securities Fraud Lawsuit (2026-09-01)
- [WIX] INVESTOR DEADLINE : Wix . com Ltd . ( WIX ) Investors with Substantial Losses Have Opportunity to Lead the Wix Class Action Lawsuit (2026-09-01)
- [WIX] Wix . com Ltd . ( NASDAQ : WIX ) Sees Significant Drop in Short Interest (2026-09-01)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Williams Charles Alan compro NPB por $1.4M el 2026-09-01.
- CEO Bender Joel vendio WHD por $7.0M el 2026-09-01.
- 10% owner Empery Asset Management, LP compro EMPD por $1.8M el 2026-09-01 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.
- Institutional manager Geode Capital Management LLC vendio ELI LILLY & CO por $13.2B.

**Polymarket — smart money (traders con mejor track record):**

- 0xd9670ea74384c1e1b9dc1e4267ffadaf4cdd140 · PnL $159,850 · win rate 97% · categorias: sports, crypto
- ExplosiveNinja · PnL $30,720 · win rate 97% · categorias: sports
- 0xDECfFdA0cA685646001e7f2f525F39de905f4dAF-1787058581228 · PnL $36,303 · win rate 92% · categorias: sports, politics, crypto
- dad168168 · PnL $22,713 · win rate 94% · categorias: sports
- vibing123 · PnL $31,809 · win rate 90% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 637 registros 30d · ultimo dato 2026-09-02
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-02
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`GLD, GLOB, IEF, MAX, QQQ, SPY, SUJA, TLT, WIX`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
