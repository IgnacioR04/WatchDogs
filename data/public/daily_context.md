# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-28T19:01:05+00:00 · ventana señales 2026-07-29 -> 2026-08-28_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.49)
- Tendencia: `bull` (SPY 768.69 · MA50 753.94 · MA200 707.42 · dist MA200: 8.66%)
- Credito: `tight` (HY spread 2.63)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 768.69 | -0.31% | 0.39% | 2.9% |
| QQQ | 12.0% | core | 715.52 | -0.78% | 0.29% | 4.0% |
| TLT | 12.0% | core | 82.93 | -0.24% | 1.07% | 1.23% |
| GLD | 9.3% | core | 408.78 | -3.27% | -3.44% | 10.02% |
| WELL | 7.3% | satellite | 238.88 | -0.3% | -0.14% | 2.28% |
| SCHL | 6.5% | satellite | 39.12 | 0.03% | -2.54% | -3.76% |
| IEF | 6.2% | core | 92.88 | -0.38% | 0.06% | 0.27% |
| IMTX | 4.4% | satellite | 9.45 | 0.96% | 5.82% | 9.12% |
| MED | 3.9% | satellite | 12.31 | 1.23% | 3.01% | 25.23% |
| MAIR | 3.8% | satellite | 26.26 | -3.35% | 1.04% | -9.64% |
| CHTR | 3.0% | satellite | 153.62 | 3.57% | 2.3% | 5.96% |
| AMRC | 2.9% | satellite | 21.9 | -4.41% | 2.43% | 3.94% |
| RGNX | 1.7% | satellite | 9.5 | 1.39% | -11.38% | -1.96% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 11.2%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -4.7%
- Beta vs SPY: 0.699 · posiciones efectivas: 13.8 · HHI: 0.0722

**Por que estos satellite (señales WATCHDOG):**

- **WELL** · score agregado 241.6 · 4 señales · fuentes: corporate_insider
- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **IMTX** · score agregado 137.7 · 2 señales · fuentes: corporate_insider, large_holder
- **AMRC** · score agregado 132.1 · 2 señales · fuentes: corporate_insider, large_holder
- **MED** · score agregado 131.9 · 2 señales · fuentes: corporate_insider, large_holder
- **RGNX** · score agregado 119.8 · 2 señales · fuentes: corporate_insider
- **MAIR** · score agregado 73.5 · 1 señales · fuentes: corporate_insider
- **SCHL** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BMRA | 79 | corporate_insider | Irani Zackary S. | 5 | $50,000 | cluster_buy |
| BMRA | 75 | corporate_insider | Gary M. Huff | 5 | $50,000 | cluster_buy |
| BMRA | 74 | corporate_insider | BARBIERI ALLEN | 5 | $32,000 | cluster_buy |
| MAIR | 74 | corporate_insider | BERTARELLI ERNESTO | 0 | $218,999,984 | - |
| BMRA | 72 | corporate_insider | MOATAZEDI DAVID | 5 | $16,000 | cluster_buy,small_amount |
| GRX | 72 | large_holder | Saba Capital Management,  |  | - | - |
| SCHL | 72 | large_holder | Iole Lucchese |  | - | - |
| IMTX | 72 | large_holder | Perceptive Advisors LLC |  | - | - |
| AMRC | 72 | large_holder | Gagnon Securities LLC |  | - | - |
| VTMX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| MED | 72 | large_holder | Steamboat Capital Partner |  | - | - |
| TG | 72 | large_holder | John D. Gottwald |  | - | - |
| BMRA | 72 | corporate_insider | Chin Eric | 5 | $10,000 | cluster_buy,small_amount |
| LIEN | 71 | corporate_insider | Gordon Scott | 2 | $50,940 | cluster_buy |
| KLAR | 70 | corporate_insider | Siemiatkowski Sebastian | 0 | $9,949,164 | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| IHT | 63 | corporate_insider | WIRTH JAMES F | $215,037,053 | - |
| RLAY | 61 | corporate_insider | SVF Pauling (Cayman) Ltd | $116,400,000 | - |
| FIX | 60 | corporate_insider | Lane Brian E. | $25,769,923 | - |
| ABT | 60 | corporate_insider | Ford Robert B | $25,256,090 | - |
| ABT | 60 | corporate_insider | Ford Robert B | $20,948,708 | - |
| CRWV | 59 | corporate_insider | Intrator Michael N | $11,838,813 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $6,374,399 | - |
| CRS | 57 | corporate_insider | Thene Tony R | $5,766,410 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 768.69 (-0.31% / 0.39% / 2.9%) [2026-08-28]
- QQQ: 715.52 (-0.78% / 0.29% / 4.0%) [2026-08-28]
- IWM: 295.98 (-1.28% / -1.33% / 1.64%) [2026-08-28]
- DIA: 534.93 (-0.05% / 0.51% / 2.11%) [2026-08-28]
- TLT: 82.93 (-0.24% / 1.07% / 1.23%) [2026-08-28]
- IEF: 92.88 (-0.38% / 0.06% / 0.27%) [2026-08-28]
- GLD: 408.78 (-3.27% / -3.44% / 10.02%) [2026-08-28]
- ^VIX: 14.49 (-0.14% / -4.23% / -9.38%) [2026-08-28]
- BTC-USD: 77523.01 (-3.41% / -0.3% / 19.44%) [2026-08-28]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: -0.07) [2026-08-26]
- Treasury 10Y yield: 4.66 (delta 1m: 0.05) [2026-08-26]
- Curva 10Y-2Y: 0.47 (delta 1m: 0.02) [2026-08-27]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.63 (delta 1m: -0.24) [2026-08-27]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.33 (delta 1m: 0.07) [2026-08-27]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [LITE] Optics Stocks Slide as AI Hardware Trade Cools : Applied Optoelectronics and Lumentum Fall 6 %, Coherent Drops 5 % (2026-08-28)
- [GOOGL] Alphabet ( GOOGL ) Early SpaceX ( SPCX ) Investment Skyrockets 100 - Fold to $94 Billion Over a Decade (2026-08-28)
- [GOOGL] Google Retreats Across 30 Markets to Defuse a 10 % Revenue Risk (2026-08-28)
- [FIG] Figma ( NYSE : FIG ) Trading Up 10 . 1 % – Here What Happened (2026-08-27)
- [LITE] Lumentum ( NASDAQ : LITE ) Insider Yuen Wupen Sells 500 Shares (2026-08-27)
- [LITE] Lumentum ( LITE ) – Analyst Recent Ratings Changes (2026-08-26)
- [ILMN] Evolve Private Wealth LLC Takes $1 . 86 Million Position in Illumina , Inc . $ILMN (2026-08-23)
- [WEYS] Wall Street Zen Upgrades Weyco Group ( NASDAQ : WEYS ) to  Strong - Buy (2026-08-17)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner BERTARELLI ERNESTO compro MAIR por $219.0M el 2026-08-25.
- CEO WIRTH JAMES F vendio IHT por $215.0M el 2026-08-25.
- CEO Siemiatkowski Sebastian compro KLAR por $9.9M el 2026-08-26.
- CEO Lane Brian E. vendio FIX por $25.8M el 2026-08-26.
- 10% owner SVF Pauling (Cayman) Ltd vendio RLAY por $116.4M el 2026-08-25.
- CEO Goeckeler David opero SNDK por $73.7M el 2026-08-25.
- CEO Ford Robert B vendio ABT por $25.3M el 2026-08-25.
- CEO THOMPSON SCOTT L compro SGI por $1.9M el 2026-08-27.

**Polymarket — smart money (traders con mejor track record):**

- TheyAreTakingTheHobitsToIsengard · PnL $112,161 · win rate 99% · categorias: sports
- SPCEXBUYER · PnL $248,419 · win rate 93% · categorias: sports
- TAIWANNUMBERONE · PnL $79,339 · win rate 92% · categorias: sports, politics
- ethanaz · PnL $80,634 · win rate 89% · categorias: sports, crypto
- alexdave888 · PnL $67,228 · win rate 88% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 642 registros 30d · ultimo dato 2026-08-27
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-28
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMRC, CHTR, GLD, IEF, IMTX, MAIR, MED, QQQ, RGNX, SCHL, SPY, TLT, WELL`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
