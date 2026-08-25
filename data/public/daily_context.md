# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-25T14:20:36+00:00 · ventana señales 2026-07-26 -> 2026-08-25_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.83)
- Tendencia: `bull` (SPY 765.6 · MA50 752.63 · MA200 705.92 · dist MA200: 8.45%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.6 | 0.28% | -0.24% | 3.34% |
| QQQ | 12.0% | core | 710.47 | 0.59% | -0.98% | 5.18% |
| TLT | 12.0% | core | 83.08 | 0.64% | 1.75% | -0.97% |
| GLD | 9.3% | core | 423.74 | -0.69% | 6.32% | 14.72% |
| CHTR | 8.2% | satellite | 149.29 | -0.67% | 0.63% | 6.66% |
| AMR | 6.8% | satellite | 204.39 | -2.64% | 20.63% | 40.89% |
| IEF | 6.2% | core | 93.31 | 0.32% | 0.4% | 0.07% |
| GSHD | 5.7% | satellite | 72.11 | -1.22% | 11.32% | 4.78% |
| CLBT | 5.4% | satellite | 11.48 | -0.13% | 4.32% | -22.73% |
| PRE | 4.8% | satellite | 22.88 | 4.86% | 17.94% | 25.3% |
| AIAI | 2.6% | satellite | 5.24 | -1.32% | -11.19% | -4.9% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.6%
- VaR 95% 1d: 1.5% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -5.3%
- Beta vs SPY: 0.644 · posiciones efectivas: 13.1 · HHI: 0.0762

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **PRE** · score agregado 184.6 · 3 señales · fuentes: corporate_insider
- **AMR** · score agregado 183.2 · 3 señales · fuentes: corporate_insider
- **AIAI** · score agregado 171.0 · 3 señales · fuentes: corporate_insider
- **CLBT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GSHD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| ODYS | 86 | corporate_insider | Arkin Moshe | 3 | $3,600,000 | cluster_buy |
| ODYS | 77 | corporate_insider | Goldwasser Benad | 3 | $150,000 | cluster_buy |
| ODYS | 76 | corporate_insider | Vurembrand Zeev | 3 | $100,000 | cluster_buy |
| SCTH | 76 | corporate_insider | SITRA J SCOTT | 0 | $100,000,000 | - |
| GEVO | 72 | corporate_insider | Barber James J | 2 | $77,000 | cluster_buy |
| QXL | 72 | large_holder | Nissim Daniel |  | - | - |
| QXL | 72 | large_holder | L.I.A. Pure Capital Ltd. |  | - | - |
| GO | 72 | large_holder | Pertento Partners LLP |  | - | - |
| CLBT | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| TENX | 72 | large_holder | Millennium Management LLC |  | - | - |
| CINT | 70 | large_holder | Swedbank Robur Fonder AB |  | - | - |
| XXII | 70 | large_holder | Iroquois Capital Manageme |  | - | - |
| CVRX | 70 | large_holder | Chernett Jorey |  | - | - |
| SOGP | 70 | large_holder | THIRUMALA SRINIDHI |  | - | - |
| DTIL | 70 | large_holder | Weinstein Benjamin |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| IHT | 63 | corporate_insider | WIRTH JAMES F | $1,820,621,160 | - |
| ALH | 61 | corporate_insider | BDT CAPITAL PARTNERS, LLC | $589,606,506 | - |
| PLTR | 58 | corporate_insider | Karp Alexander C. | $53,597,839 | - |
| V | 57 | corporate_insider | Taneja Rajat | $6,650,860 | - |
| DASH | 56 | corporate_insider | Adarkar Prabir | $3,778,407 | - |
| GH | 56 | corporate_insider | Talasaz AmirAli | $3,533,452 | - |
| PACS | 56 | corporate_insider | Murray Jason Hulse | $3,389,088 | - |
| DASH | 55 | corporate_insider | Inukonda Ravi | $4,303,271 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.6 (0.28% / -0.24% / 3.34%) [2026-08-25]
- QQQ: 710.47 (0.59% / -0.98% / 5.18%) [2026-08-25]
- IWM: 298.53 (0.19% / -0.57% / 1.76%) [2026-08-25]
- DIA: 534.55 (0.17% / 0.39% / 1.54%) [2026-08-25]
- TLT: 83.08 (0.64% / 1.75% / -0.97%) [2026-08-25]
- IEF: 93.31 (0.32% / 0.4% / 0.07%) [2026-08-25]
- GLD: 423.74 (-0.69% / 6.32% / 14.72%) [2026-08-25]
- ^VIX: 15.83 (-0.13% / -0.06% / -13.07%) [2026-08-25]
- BTC-USD: 78961.99 (-0.0% / 8.12% / 22.24%) [2026-08-25]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.24 (delta 1m: -0.13) [2026-08-21]
- Treasury 10Y yield: 4.74 (delta 1m: 0.03) [2026-08-21]
- Curva 10Y-2Y: 0.46 (delta 1m: 0.1) [2026-08-24]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.07) [2026-08-21]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.32 (delta 1m: 0.06) [2026-08-24]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), ai (3), leadership (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [PLTR] Fitz - Gerald Group Keith Fitz - Gerald Breaks Down Long - Term Prospects For NVDA , PLTR and TSLA (2026-08-25)
- [PLTR] Insider Selling : Palantir Technologies ( NASDAQ : PLTR ) Insider Sells $86 , 057 , 506 . 92 in Stock (2026-08-25)
- [RBLX] Teenage Roblox entrepreneur raises $1m to fight online predators (2026-08-25)
- [RBLX] Mother says teen unknowingly waived right to sue Roblox , Discord , TikTok before death (2026-08-25)
- [ANET] Cisco Systems ( CSCO ) & Arista Networks ( ANET ): Cisco Just Beat Every Estimate . Why Did the Stock Still Drop 8 %? (2026-08-24)
- [ANET] Greenland Capital Management LP Purchases Shares of 4 , 085 Arista Networks , Inc . $ANET (2026-08-23)
- [COIN] Coinbase CEO : Bitcoin  Very Likely  to Reach $400 , 000 by 2030 – NaturalNews . com (2026-08-23)
- [PKOH] Head to Head Contrast : Park - Ohio ( NASDAQ : PKOH ) & Gold . com ( NYSE : GOLD ) (2026-08-22)
- [ANET] Korea Investment CORP Reduces Position in Arista Networks , Inc . $ANET (2026-08-22)
- [ANET] Arista Networks vs . Salesforce : Which Technology Stock Is a Better Buy in 2026 ? (2026-08-22)

**Actores que han movido ficha este mes (top movimientos):**

- CEO SITRA J SCOTT compro SCTH por $100.0M el 2026-08-21.
- CEO WIRTH JAMES F vendio IHT por $1.8B el 2026-08-21.
- 10% owner Host-Plus Pty Ltd as trustee for the HOSTPLUS Pooled Superannuation Trust compro EBR Systems, Inc. por $20.8M el 2026-08-21.
- 10% owner BDT CAPITAL PARTNERS, LLC vendio ALH por $589.6M el 2026-08-20.
- Director Tsai Joseph C compro BABA por $10.4M el 2026-08-25.
- CFO Visoso Luis Felipe opero SNDK por $41.1M el 2026-08-20.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- AV23IUa · PnL $285,854 · win rate 76% · categorias: sports, crypto
- thatguythatguy · PnL $27,780 · win rate 95% · categorias: sports
- BrotherObama · PnL $37,781 · win rate 81% · categorias: sports
- casualbet2020 · PnL $12,477 · win rate 89% · categorias: sports
- tennischamp · PnL $10,592 · win rate 88% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 657 registros 30d · ultimo dato 2026-08-25
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-25
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AIAI, AMR, CHTR, CLBT, GLD, GSHD, IEF, PRE, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
