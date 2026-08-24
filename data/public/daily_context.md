# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-24T16:15:35+00:00 · ventana señales 2026-07-25 -> 2026-08-24_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.72)
- Tendencia: `bull` (SPY 764.61 · MA50 752.13 · MA200 705.46 · dist MA200: 8.39%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `steep` (curva 10y-2y 0.5)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 764.61 | -0.14% | -1.04% | 3.45% |
| QQQ | 12.0% | core | 708.22 | -0.73% | -2.97% | 3.83% |
| TLT | 12.0% | core | 82.75 | 0.85% | 1.72% | -0.8% |
| GLD | 9.3% | core | 427.17 | 0.9% | 5.35% | 14.02% |
| GRNT | 6.9% | satellite | 5.0 | -2.15% | -4.94% | 9.41% |
| CART | 6.9% | satellite | 51.51 | 3.36% | 5.41% | 16.9% |
| IEF | 6.2% | core | 93.08 | 0.29% | 0.26% | 0.13% |
| BABA | 5.9% | satellite | 119.82 | 0.41% | -3.92% | 4.2% |
| CHTR | 5.2% | satellite | 153.3 | 2.09% | 6.39% | 16.48% |
| ELF | 4.6% | satellite | 104.63 | 2.64% | 11.71% | 24.54% |
| CBRS | 2.0% | satellite | 186.8 | -4.76% | -25.87% | -0.96% |
| AIAI | 1.9% | satellite | 5.74 | -13.29% | 14.57% | 3.24% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.4%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -3.4%
- Beta vs SPY: 0.578 · posiciones efectivas: 13.4 · HHI: 0.0744

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 213.8 · 3 señales · fuentes: large_holder
- **BABA** · score agregado 167.6 · 2 señales · fuentes: corporate_insider
- **AIAI** · score agregado 146.0 · 2 señales · fuentes: corporate_insider
- **ELF** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GRNT** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **CART** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BABA | 85 | corporate_insider | Wu Yongming | 2 | $4,984,000 | cluster_buy |
| BABA | 83 | corporate_insider | Tsai Joseph C | 2 | $10,288,800 | cluster_buy |
| GWRS | 81 | corporate_insider | Levine Jonathan L | 2 | $5,766,819 | cluster_buy |
| INV | 80 | corporate_insider | Haskell Gregory W | 4 | $75,600 | cluster_buy |
| INV | 79 | corporate_insider | Otworth Michael | 4 | $349,295 | cluster_buy |
| INV | 79 | corporate_insider | Donnally James O | 4 | $337,500 | cluster_buy |
| GWRS | 78 | corporate_insider | Cohn Andrew M. | 2 | $1,233,186 | cluster_buy |
| IDAI | 78 | corporate_insider | Genner Gareth Neville | 3 | $28,558 | cluster_buy |
| SCTH | 76 | corporate_insider | SITRA J SCOTT | 0 | $100,000,000 | - |
| INV | 75 | corporate_insider | Brown Bruce | 4 | $45,399 | cluster_buy |
| IDAI | 73 | corporate_insider | Genner Gareth Neville | 3 | $3,210 | cluster_buy,small_amount |
| AIAI | 73 | corporate_insider | Carlton Charles Craig | 2 | $49,518 | cluster_buy |
| AIAI | 73 | corporate_insider | Carlton Charles Craig | 2 | $49,910 | cluster_buy |
| BHRB | 72 | large_holder | LEHMAN KENNETH R |  | - | - |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MDLZ | 58 | corporate_insider | Van de Put Dirk | $8,559,806 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $27,432,882 | - |
| HCC | 57 | corporate_insider | SCHELLER WALTER J | $5,250,000 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $24,899,013 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $24,128,863 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $22,534,734 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $4,491,084 | - |
| CBRS | 56 | corporate_insider | Lie Sean | $19,223,823 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 764.61 (-0.14% / -1.04% / 3.45%) [2026-08-24]
- QQQ: 708.22 (-0.73% / -2.97% / 3.83%) [2026-08-24]
- IWM: 298.35 (-0.54% / -1.88% / 1.86%) [2026-08-24]
- DIA: 533.91 (0.32% / 0.03% / 2.51%) [2026-08-24]
- TLT: 82.75 (0.85% / 1.72% / -0.8%) [2026-08-24]
- IEF: 93.08 (0.29% / 0.26% / 0.13%) [2026-08-24]
- GLD: 427.17 (0.9% / 5.35% / 14.02%) [2026-08-24]
- ^VIX: 15.72 (3.9% / 3.49% / -15.8%) [2026-08-24]
- BTC-USD: 79479.88 (2.22% / 14.75% / 24.08%) [2026-08-24]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: -0.12) [2026-08-20]
- Treasury 10Y yield: 4.69 (delta 1m: 0.02) [2026-08-20]
- Curva 10Y-2Y: 0.5 (delta 1m: 0.16) [2026-08-21]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.07) [2026-08-21]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.06) [2026-08-21]
- Dolar broad index: 118.9028 (delta 1m: -1.428) [2026-08-14]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (8), regulatory (1), merger (1), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [UTHR] Hudson Portfolio Management LLC Purchases Shares of 1 , 365 United Therapeutics Corporation $UTHR (2026-08-23)
- [LIFE] Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Major Shareholder Us ( Ttgp ) Ltd . Sc Sells 107 , 795 Shares of Stock (2026-08-22)
- [CBRS] Cerebras System ( CBRS ) Buy Rating Reiterated at Needham & Company LLC (2026-08-22)
- [LIFE] Lingke Wang Sells 118 , 333 Shares of Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Stock (2026-08-21)
- [CBRS] Cerebras Systems ( NASDAQ : CBRS ) COO Dhiraj Mallick Sells 38 , 889 Shares of Stock (2026-08-21)
- [WBS] Deutsche Bank AG Buys Shares of 759 , 307 Webster Financial Corporation $WBS (2026-08-21)
- [WBS] Santander completes acquisition of Webster Financial Corp . (2026-08-20)
- [LIFE] Brandt Walter Kucharski Sells 77 , 436 Shares of Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Stock (2026-08-19)
- [UTHR] United Therapeutics ( NASDAQ : UTHR ) CEO Martine Rothblatt Sells 9 , 500 Shares of Stock (2026-08-14)
- [UTHR] Liquidia Stock : Top 1 % Biotech Beats Sales Views Amid Ongoing United Therapeutics Rivalry (2026-08-12)

**Actores que han movido ficha este mes (top movimientos):**

- CEO SITRA J SCOTT compro SCTH por $100.0M el 2026-08-21.
- CEO Wu Yongming compro BABA por $5.0M el 2026-08-24.
- Officer Lie Sean vendio CBRS por $27.4M el 2026-08-20 [senal en multiples fuentes].
- Director Tsai Joseph C compro BABA por $10.3M el 2026-08-24.
- CEO MINICUCCI BENITO compro ALK por $1.0M el 2026-08-20.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- SPCEXBUYER · PnL $103,506 · win rate 93% · categorias: sports
- rollobravado · PnL $13,472 · win rate 99% · categorias: sports, politics
- TAIWANNUMBERONE · PnL $33,449 · win rate 92% · categorias: sports, politics
- JnStrtPrdctnMrkts · PnL $28,576 · win rate 90% · categorias: crypto
- WhattDoyoumean · PnL $16,007 · win rate 93% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 650 registros 30d · ultimo dato 2026-08-24
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-24
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AIAI, BABA, CART, CBRS, CHTR, ELF, GLD, GRNT, IEF, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
