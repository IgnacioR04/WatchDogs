# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-31T01:04:55+00:00 · ventana señales 2026-10-01 -> 2026-10-31_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 19.42)
- Tendencia: `bull` (SPY 769.36 · MA50 766.87 · MA200 725.63 · dist MA200: 6.03%)
- Credito: `normal` (HY spread 3.26)
- Tipos: `flat` (curva 10y-2y 0.38)
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
| VCTR | 7.6% | satellite | 113.81 | 1.73% | 5.98% | 1.85% |
| SLB | 6.5% | satellite | 53.81 | 0.11% | 8.6% | 10.58% |
| IEF | 5.7% | core | 91.25 | 0.44% | 0.05% | 2.18% |
| WRLD | 5.2% | satellite | 175.92 | 1.02% | 3.69% | 2.5% |
| RAPP | 3.9% | satellite | 24.21 | 7.6% | -8.74% | -26.26% |
| PENG | 2.8% | satellite | 58.79 | -3.31% | 13.25% | 6.93% |
| HIMS | 2.7% | satellite | 29.67 | 1.19% | 1.85% | 1.26% |
| NBIS | 2.2% | satellite | 171.99 | -5.68% | 8.05% | -25.96% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.8%
- VaR 95% 1d: 1.2% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -6.4%
- Beta vs SPY: 0.864 · posiciones efectivas: 14.8 · HHI: 0.0674

**Por que estos satellite (señales WATCHDOG):**

- **RAPP** · score agregado 238.4 · 4 señales · fuentes: corporate_insider
- **NBIS** · score agregado 161.1 · 3 señales · fuentes: corporate_insider
- **VCTR** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PENG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **SLB** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **HIMS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WRLD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BBT | 72 | corporate_insider | Callahan Mary Anne | 2 | $96,672 | cluster_buy |
| PUSA | 72 | large_holder | Michael Sinensky |  | - | - |
| VCTR | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| ZM | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| PENG | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| MRCY | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| SLB | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| HAPN | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| CNXC | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| HIMS | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| HAIN | 72 | large_holder | Vanguard Capital Manageme |  | - | - |
| LEE | 70 | large_holder | Quint Digital Ltd |  | - | - |
| IVAI | 70 | large_holder | YA II PN, Ltd. |  | - | - |
| WIA | 70 | large_holder | KARPUS MANAGEMENT, INC. |  | - | - |
| XPOF | 70 | large_holder | Fund 1 Investments, LLC |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| EAT | 58 | corporate_insider | Hochman Kevin | $8,815,200 | - |
| ROIV | 58 | corporate_insider | Venker Eric | $7,318,000 | - |
| WRLD | 57 | corporate_insider | Prescott General Partners | $15,000,065 | - |
| BROS | 57 | corporate_insider | DM Trust Aggregator, LLC | $11,711,076 | - |
| BROS | 57 | corporate_insider | Boersma Travis | $11,711,076 | - |
| DAL | 56 | corporate_insider | Bastian Edward H | $4,100,000 | - |
| MCO | 56 | corporate_insider | West Michael L | $3,328,065 | - |
| IOT | 56 | corporate_insider | Biswas Sanjit | $3,463,304 | - |

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
- ^VIX: 19.42 (12.91% / -0.15% / 26.85%) [2026-10-30]
- BTC-USD: 77397.63 (-0.49% / -3.28% / -6.65%) [2026-10-31]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.61 (delta 1m: -0.28) [2026-10-29]
- Treasury 10Y yield: 4.98 (delta 1m: -0.28) [2026-10-29]
- Curva 10Y-2Y: 0.38 (delta 1m: -0.03) [2026-10-30]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.26 (delta 1m: 0.14) [2026-10-29]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: -0.02) [2026-10-30]
- Dolar broad index: 121.3202 (delta 1m: 1.203) [2026-10-23]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (6), ai (5), earnings (1), leadership (1), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [NXPI] 3 , 883 Shares of NXP Semiconductors N . V . $NXPI Bought by Private Wealth Partners LLC (2026-10-24)
- [NXPI] NXP Semiconductors N . V . $NXPI Shares Newly Purchased by Sterling Capital Management LLC (2026-10-24)
- [WDC] Western Digital Stock Has Fallen 53 % Since June . Id Consider a Small Position After Its Latest Report . (2026-10-24)
- [WDC] Western Digital Stock Has Fallen 53 % Since June . Id Consider a Small Position After Its Latest Report . (2026-10-24)
- [WDC] Western Digital ( NASDAQ : WDC ) Issues Quarterly Earnings Results , Beats Expectations By $0 . 53 EPS (2026-10-23)
- [WDC] NTU Brings Intel , Western Digital CEOs to AI Summit (2026-10-23)
- [WDC] Western Digital ( NASDAQ : WDC ) Stock Gets Price Target Reduction from Cantor Fitzgerald (2026-10-23)
- [NTRA] Sumitomo Mitsui DS Asset Management Company Ltd Acquires 1 , 317 Shares of Natera , Inc . $NTRA (2026-10-22)
- [NTRA] Natera ( NASDAQ : NTRA ) Price Target Raised to $500 . 00 (2026-10-22)
- [NTRA] Natera ( NTRA ) Is Expanding Cancer Testing Rapidly . Does Its Valuation Leave Room for Error ? (2026-10-20)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Hochman Kevin vendio EAT por $8.8M el 2026-10-29.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $8.7M el 2026-10-28.
- CEO Lyons Michael P. compro TFC por $1.2M el 2026-10-28.
- Director HEALY JAMES compro RAPP por $20.0M el 2026-10-28.
- CEO Pferdehirt Douglas J. opero FTI por $25.1M el 2026-10-27.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- monkeymashingkeyboard · PnL $306,128 · win rate 92% · categorias: sports
- theowalcott · PnL $73,554 · win rate 100% · categorias: sports
- BreakTheBank · PnL $260,727 · win rate 88% · categorias: sports, politics
- Mooseborzoiii · PnL $264,920 · win rate 91% · categorias: sports
- luckycat888888 · PnL $45,717 · win rate 99% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 593 registros 30d · ultimo dato 2026-10-30
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-30
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`GLD, HIMS, IEF, NBIS, PENG, QQQ, RAPP, SLB, SPY, TLT, VCTR, WRLD`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
