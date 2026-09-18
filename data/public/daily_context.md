# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-18T18:45:12+00:00 · ventana señales 2026-08-19 -> 2026-09-18_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.14)
- Tendencia: `bull` (SPY 760.48 · MA50 759.71 · MA200 714.24 · dist MA200: 6.47%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.27)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 760.48 | -0.28% | -0.5% | -0.28% |
| QQQ | 12.0% | core | 718.12 | 0.17% | 0.45% | 1.01% |
| TLT | 12.0% | core | 81.23 | -0.67% | 0.45% | -0.97% |
| GLD | 9.3% | core | 401.78 | 0.86% | 0.75% | -3.25% |
| SBLK | 8.6% | satellite | 32.46 | 2.24% | 4.14% | 11.32% |
| FANG | 8.5% | satellite | 193.0 | -2.0% | -5.84% | -8.54% |
| MEOH | 7.6% | satellite | 61.35 | 0.52% | -2.18% | 4.8% |
| IEF | 6.2% | core | 90.86 | -0.43% | -0.17% | -1.96% |
| VG | 4.8% | satellite | 14.25 | -1.17% | -9.56% | -0.01% |
| USAR | 4.0% | satellite | 15.29 | -2.18% | -1.74% | -10.64% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.6%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -2.7%
- Beta vs SPY: 0.409 · posiciones efectivas: 12.5 · HHI: 0.08

**Por que estos satellite (señales WATCHDOG):**

- **SBLK** · score agregado 482.4 · 6 señales · fuentes: corporate_insider
- **MEOH** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **FANG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **VG** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SBLK | 83 | corporate_insider | Pappa Milena Maria | 5 | $2,103,288 | cluster_buy |
| SBLK | 82 | corporate_insider | Zagari Raffaele | 5 | $1,413,500 | cluster_buy |
| SBLK | 82 | corporate_insider | Pappas Alexandros | 5 | $2,103,288 | cluster_buy |
| SBLK | 79 | corporate_insider | Reskos Nikolaos | 5 | $282,700 | cluster_buy |
| SBLK | 79 | corporate_insider | Zagari Raffaele | 5 | $282,700 | cluster_buy |
| SBLK | 77 | corporate_insider | Plakantonaki Charis | 5 | $84,810 | cluster_buy |
| BENF | 76 | corporate_insider | Silk James G. | 3 | $10,000 | cluster_buy,small_amount |
| BENF | 73 | corporate_insider | CANGANY PETER T JR | 3 | $20,000 | cluster_buy,small_amount |
| FANG | 72 | large_holder | SGF FANG Holdings, LP |  | - | - |
| NYAX | 72 | large_holder | MEITAV INVESTMENT HOUSE L |  | - | - |
| VG | 72 | large_holder | D. E. Shaw & Co., L.P. |  | - | - |
| RVSB | 72 | corporate_insider | Wills Bessie Ross | 3 | $11,170 | cluster_buy,small_amount |
| RVSB | 72 | corporate_insider | Graham Stacey | 3 | $9,975 | cluster_buy,small_amount |
| TROO | 70 | large_holder | JMD CORPORATE SERVICES LI |  | - | - |
| CHR | 70 | large_holder | Bing Zhang |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| AUR | 61 | corporate_insider | Uber Technologies, Inc | $182,238,436 | - |
| MEDP | 58 | corporate_insider | Troendle August J. | $9,915,436 | - |
| TVTX | 57 | corporate_insider | Dube Eric M | $6,567,876 | - |
| TVTX | 57 | corporate_insider | Dube Eric M | $6,307,964 | - |
| TVTX | 57 | corporate_insider | Dube Eric M | $6,117,289 | - |
| PSX | 57 | corporate_insider | Mandell Brian | $6,202,381 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $6,126,440 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $6,285,688 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 760.48 (-0.28% / -0.5% / -0.28%) [2026-09-18]
- QQQ: 718.12 (0.17% / 0.45% / 1.01%) [2026-09-18]
- IWM: 283.47 (-0.69% / -1.62% / -4.52%) [2026-09-18]
- DIA: 515.94 (-0.46% / -1.87% / -2.11%) [2026-09-18]
- TLT: 81.23 (-0.67% / 0.45% / -0.97%) [2026-09-18]
- IEF: 90.86 (-0.43% / -0.17% / -1.96%) [2026-09-18]
- GLD: 401.78 (0.86% / 0.75% / -3.25%) [2026-09-18]
- ^VIX: 15.14 (-1.94% / -4.42% / 0.07%) [2026-09-18]
- BTC-USD: 80959.13 (5.96% / 5.36% / 3.47%) [2026-09-18]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.74 (delta 1m: 0.55) [2026-09-16]
- Treasury 10Y yield: 5.01 (delta 1m: 0.29) [2026-09-16]
- Curva 10Y-2Y: 0.27 (delta 1m: -0.25) [2026-09-17]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.03) [2026-09-17]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.33 (delta 1m: 0.03) [2026-09-17]
- Dolar broad index: 118.2126 (delta 1m: -0.905) [2026-09-11]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (10), stock (5), regulatory (4), earnings (3)

**Titulares recientes (GDELT, tickers con mas señales):**

- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [AI] Analysts Set C3 . ai , Inc . ( NYSE : AI ) Price Target at $8 . 70 (2026-09-13)
- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [CRWD] Jensen Huang Says Cybersecurity Is AI Next Blockbuster App . CrowdStrike Is Already Building It With Nvidia (2026-09-11)
- [AI] YieldMax AI Option Income Strategy ETF ( NYSEARCA : AIYY ) Trading Down 0 . 5 % – Time to Sell ? (2026-09-11)
- [TVTX] Travere Therapeutics ( NASDAQ : TVTX ) Director Jeffrey Meckler Sells 20 , 000 Shares of Stock (2026-09-11)
- [AI] Head to Head Comparison : C3 . ai ( NYSE : AI ) and Nvni Group ( NASDAQ : NVNI ) (2026-09-11)
- [WAL] Squarepoint Ops LLC Sells 226 , 768 Shares of Western Alliance Bancorporation $WAL (2026-09-10)
- [WAL] Western Alliance Bancorporation $WAL Shares Sold by Squarepoint Ops LLC (2026-09-10)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Uber Technologies, Inc vendio AUR por $182.2M el 2026-09-15.
- CEO Lyons Michael P. compro TFC por $1.0M el 2026-09-17.
- CEO Dube Eric M vendio TVTX por $6.6M el 2026-09-17.
- CEO Dube Eric M vendio TVTX por $6.3M el 2026-09-16.
- CEO Mandell Brian vendio PSX por $6.2M el 2026-09-16.
- CEO Troendle August J. vendio MEDP por $5.4M el 2026-09-16.
- CEO Troendle August J. vendio MEDP por $9.9M el 2026-09-15.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.

**Polymarket — smart money (traders con mejor track record):**

- JnStrtPrdctnMrkts · PnL $199,334 · win rate 91% · categorias: crypto
- Kosherlocks · PnL $40,787 · win rate 96% · categorias: sports, crypto
- punyapple · PnL $21,777 · win rate 100% · categorias: crypto, sports
- lllllllIlll · PnL $22,745 · win rate 94% · categorias: sports
- retordedgremlin125 · PnL $38,281 · win rate 91% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 743 registros 30d · ultimo dato 2026-09-17
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-18
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`FANG, GLD, IEF, MEOH, QQQ, SBLK, SPY, TLT, USAR, VG`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
