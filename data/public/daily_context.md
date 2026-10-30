# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-30T08:54:23+00:00 · ventana señales 2026-09-30 -> 2026-10-30_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.42)
- Tendencia: `bull` (SPY 769.36 · MA50 766.87 · MA200 725.63 · dist MA200: 6.03%)
- Credito: `normal` (HY spread 3.14)
- Tipos: `flat` (curva 10y-2y 0.37)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 769.36 | -0.38% | 0.71% | 0.7% |
| QQQ | 11.4% | core | 715.34 | -1.42% | 1.54% | -3.6% |
| TLT | 11.4% | core | 81.49 | 0.62% | -0.31% | 4.86% |
| GLD | 8.6% | core | 368.57 | -1.32% | -0.12% | -3.71% |
| IEF | 5.7% | core | 91.25 | 0.44% | 0.05% | 2.18% |
| HBAN | 5.2% | satellite | 15.97 | 1.72% | 1.98% | 5.13% |
| CCK | 5.2% | satellite | 118.2 | 1.68% | -0.89% | 11.31% |
| BBT | 5.2% | satellite | 30.66 | 0.92% | 2.37% | 9.11% |
| RNW | 4.1% | satellite | 6.87 | 0.0% | -0.15% | 0.59% |
| BPRE | 4.0% | satellite | 12.56 | 1.05% | 1.54% | 0.64% |
| ACN | 2.1% | satellite | 247.22 | 1.57% | -4.45% | 17.38% |
| PESI | 1.8% | satellite | 13.32 | -2.49% | 8.2% | -13.56% |
| WEAV | 1.7% | satellite | 7.4 | 0.14% | 0.0% | 0.68% |
| TEM | 1.4% | satellite | 77.84 | 1.61% | 21.99% | 1.75% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.9%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -3.2%
- Beta vs SPY: 0.597 · posiciones efectivas: 15.6 · HHI: 0.0639

**Por que estos satellite (señales WATCHDOG):**

- **ACN** · score agregado 237.6 · 3 señales · fuentes: corporate_insider
- **RNW** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **BBT** · score agregado 150.3 · 2 señales · fuentes: corporate_insider
- **BPRE** · score agregado 123.4 · 2 señales · fuentes: corporate_insider
- **PESI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **TEM** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CCK** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WEAV** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **HBAN** · score agregado 58.0 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| ACN | 84 | corporate_insider | Sweet Julie Spellman | 2 | $2,486,318 | cluster_buy |
| ACN | 80 | corporate_insider | Sweet Julie Spellman | 2 | $514,723 | cluster_buy |
| BBT | 76 | corporate_insider | Callahan Mary Anne | 4 | $96,672 | cluster_buy |
| ACN | 74 | corporate_insider | Price Paula A | 2 | $199,848 | cluster_buy |
| BBT | 74 | corporate_insider | Polito Karyn | 4 | $30,680 | cluster_buy |
| LONA | 74 | corporate_insider | Portman David J. | 0 | $9,919,161,281 | - |
| BBT | 73 | corporate_insider | Rosengren Eric S | 4 | $21,168 | cluster_buy,small_amount |
| RAASY | 72 | large_holder | TB Alternative Assets Ltd |  | - | - |
| TECX | 72 | large_holder | Aberdeen Group plc |  | - | - |
| CSTL | 72 | large_holder | PRINCIPAL GLOBAL INVESTOR |  | - | - |
| RCT | 72 | large_holder | Byland Christina Elisabet |  | - | - |
| RCT | 72 | large_holder | Senn Nikolaus Beat |  | - | - |
| PESI | 72 | large_holder | HOLD Alapkezelo Zrt. |  | - | - |
| TEM | 72 | large_holder | Bradley A. Keywell |  | - | - |
| CCK | 72 | large_holder | BlackRock Portfolio Manag |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| DVA | 60 | corporate_insider | BERKSHIRE HATHAWAY INC | $69,026,033 | - |
| COF | 58 | corporate_insider | FAIRBANK RICHARD D | $9,477,680 | - |
| TALO | 58 | corporate_insider | Control Empresarial de Ca | $21,992,040 | - |
| COF | 58 | corporate_insider | FAIRBANK RICHARD D | $7,526,812 | - |
| DHR | 56 | corporate_insider | McGrew Matthew | $3,683,773 | - |
| IOT | 56 | corporate_insider | Biswas Sanjit | $3,463,304 | - |
| DHR | 56 | corporate_insider | McGrew Matthew | $3,330,470 | - |
| IOT | 56 | corporate_insider | Biswas Sanjit | $3,265,454 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 769.36 (-0.38% / 0.71% / 0.7%) [2026-10-29]
- QQQ: 715.34 (-1.42% / 1.54% / -3.6%) [2026-10-29]
- IWM: 284.01 (0.97% / 2.65% / 1.79%) [2026-10-29]
- DIA: 522.73 (-0.37% / -0.98% / 2.8%) [2026-10-29]
- TLT: 81.49 (0.62% / -0.31% / 4.86%) [2026-10-29]
- IEF: 91.25 (0.44% / 0.05% / 2.18%) [2026-10-29]
- GLD: 368.57 (-1.32% / -0.12% / -3.71%) [2026-10-29]
- ^VIX: 18.42 (7.09% / -5.3% / 20.31%) [2026-10-30]
- BTC-USD: 77830.31 (0.07% / -2.74% / -6.13%) [2026-10-30]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.67 (delta 1m: -0.25) [2026-10-28]
- Treasury 10Y yield: 5.05 (delta 1m: -0.19) [2026-10-28]
- Curva 10Y-2Y: 0.37 (delta 1m: 0.0) [2026-10-29]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.14 (delta 1m: 0.06) [2026-10-28]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.35 (delta 1m: 0.0) [2026-10-29]
- Dolar broad index: 121.3202 (delta 1m: 1.203) [2026-10-23]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [IOT] Nutanix ( NASDAQ : NTNX ) vs . Samsara ( NYSE : IOT ) Critical Survey (2026-10-24)
- [CRWD] CrowdStrike CEO Says a Wave of Cyber Attacks Are Coming (2026-10-24)
- [WEAV] Analyzing Weave Communications ( NYSE : WEAV ) & HealthStream ( NASDAQ : HSTM ) (2026-10-22)
- [DRD] DRDGold cash flow rises as expansion spending starts to ease (2026-10-21)
- [PBF] Delek Logistics Partners ( NYSE : DKL ) and PBF Energy ( NYSE : PBF ) Financial Analysis (2026-10-18)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Portman David J. compro LONA por $9.9B el 2026-10-26 [senal en multiples fuentes].
- 10% owner BERKSHIRE HATHAWAY INC vendio DVA por $69.0M el 2026-10-27.
- CEO Sweet Julie Spellman compro ACN por $2.5M el 2026-10-26.
- CEO Lyons Michael P. compro TFC por $1.2M el 2026-10-28.
- CEO MYERS FRANKLIN compro DINO por $1.1M el 2026-10-29.
- 10% owner Control Empresarial de Capitales S.A. de C.V. vendio TALO por $22.0M el 2026-10-28.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $6.3M el 2026-10-27.
- 10% owner Das Soumen compro SCQCU por $2.7M el 2026-10-28.

**Polymarket — smart money (traders con mejor track record):**

- monkeymashingkeyboard · PnL $297,261 · win rate 92% · categorias: sports
- theowalcott · PnL $73,445 · win rate 100% · categorias: sports
- BreakTheBank · PnL $235,063 · win rate 88% · categorias: sports, politics
- luckycat888888 · PnL $44,907 · win rate 98% · categorias: sports
- lllllllIlll · PnL $58,131 · win rate 95% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 702 registros 30d · ultimo dato 2026-10-29
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-29
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ACN, BBT, BPRE, CCK, GLD, HBAN, IEF, PESI, QQQ, RNW, SPY, TEM, TLT, WEAV`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
