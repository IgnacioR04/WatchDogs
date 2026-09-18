# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-18T14:46:37+00:00 · ventana señales 2026-08-19 -> 2026-09-18_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.44)
- Tendencia: `neutral` (SPY 758.98 · MA50 759.68 · MA200 714.23 · dist MA200: 6.27%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.27)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 758.98 | -0.47% | -0.69% | -0.47% |
| QQQ | 9.8% | core | 716.27 | -0.09% | 0.19% | 0.75% |
| TLT | 9.8% | core | 81.23 | -0.67% | 0.45% | -0.97% |
| GLD | 7.3% | core | 399.01 | 0.16% | 0.06% | -3.91% |
| SBLK | 5.1% | satellite | 32.12 | 1.18% | 3.06% | 10.17% |
| FANG | 5.1% | satellite | 195.08 | -0.94% | -4.83% | -7.55% |
| IEF | 4.9% | core | 90.86 | -0.43% | -0.17% | -1.96% |
| MEOH | 4.5% | satellite | 60.94 | -0.15% | -2.84% | 4.1% |
| USO | 3.6% | satellite | 156.99 | 1.08% | 1.35% | 16.69% |
| VG | 2.9% | satellite | 14.42 | 0.0% | -8.49% | 1.17% |
| KRMN | 2.8% | satellite | 35.97 | 2.04% | 1.96% | -33.83% |
| USAR | 2.4% | satellite | 15.35 | -1.82% | -1.38% | -10.32% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 7.9%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -2.1%
- Beta vs SPY: 0.329 · posiciones efectivas: 19.3 · HHI: 0.0518

**Por que estos satellite (señales WATCHDOG):**

- **SBLK** · score agregado 482.4 · 6 señales · fuentes: corporate_insider
- **MEOH** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **USO** · score agregado 132.0 · 2 señales · fuentes: corporate_insider
- **KRMN** · score agregado 81.5 · 1 señales · fuentes: corporate_insider
- **FANG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **VG** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SBLK | 83 | corporate_insider | Pappa Milena Maria | 5 | $2,103,288 | cluster_buy |
| SBLK | 82 | corporate_insider | Zagari Raffaele | 5 | $1,413,500 | cluster_buy |
| SBLK | 82 | corporate_insider | Pappas Alexandros | 5 | $2,103,288 | cluster_buy |
| KRMN | 82 | corporate_insider | Stinnett David | 3 | $1,007,648 | cluster_buy |
| SBLK | 79 | corporate_insider | Reskos Nikolaos | 5 | $282,700 | cluster_buy |
| SBLK | 79 | corporate_insider | Zagari Raffaele | 5 | $282,700 | cluster_buy |
| SBLK | 77 | corporate_insider | Plakantonaki Charis | 5 | $84,810 | cluster_buy |
| BENF | 76 | corporate_insider | Silk James G. | 3 | $10,000 | cluster_buy,small_amount |
| BENF | 73 | corporate_insider | CANGANY PETER T JR | 3 | $20,000 | cluster_buy,small_amount |
| KRMN | 73 | corporate_insider | Petryszyn Mary D | 3 | $18,720 | cluster_buy,small_amount |
| FANG | 72 | large_holder | SGF FANG Holdings, LP |  | - | - |
| NYAX | 72 | large_holder | MEITAV INVESTMENT HOUSE L |  | - | - |
| VG | 72 | large_holder | D. E. Shaw & Co., L.P. |  | - | - |
| RVSB | 72 | corporate_insider | Wills Bessie Ross | 3 | $11,170 | cluster_buy,small_amount |
| KRMN | 72 | corporate_insider | Twitty Stephen | 3 | $10,117 | cluster_buy,small_amount |

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

- SPY: 758.98 (-0.47% / -0.69% / -0.47%) [2026-09-18]
- QQQ: 716.27 (-0.09% / 0.19% / 0.75%) [2026-09-18]
- IWM: 283.09 (-0.82% / -1.75% / -4.65%) [2026-09-18]
- DIA: 514.38 (-0.77% / -2.17% / -2.41%) [2026-09-18]
- TLT: 81.23 (-0.67% / 0.45% / -0.97%) [2026-09-18]
- IEF: 90.86 (-0.43% / -0.17% / -1.96%) [2026-09-18]
- GLD: 399.01 (0.16% / 0.06% / -3.91%) [2026-09-18]
- ^VIX: 15.44 (0.0% / -2.53% / 2.05%) [2026-09-18]
- BTC-USD: 80701.69 (5.63% / 5.03% / 3.14%) [2026-09-18]

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

**Temas dominantes**: ai (6), earnings (4), regulatory (3), stock (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [AI] Analysts Set C3 . ai , Inc . ( NYSE : AI ) Price Target at $8 . 70 (2026-09-13)
- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [AI] YieldMax AI Option Income Strategy ETF ( NYSEARCA : AIYY ) Trading Down 0 . 5 % – Time to Sell ? (2026-09-11)
- [AI] Head to Head Comparison : C3 . ai ( NYSE : AI ) and Nvni Group ( NASDAQ : NVNI ) (2026-09-11)
- [WLTH] Wealthfront ( WLTH ) Q2 2027 Earnings Call Transcript (2026-09-10)
- [WAL] Squarepoint Ops LLC Sells 226 , 768 Shares of Western Alliance Bancorporation $WAL (2026-09-10)
- [WAL] Western Alliance Bancorporation $WAL Shares Sold by Squarepoint Ops LLC (2026-09-10)
- [WAL] Western Alliance Bancorporation ( NYSE : WAL ) and First Bancorp , Inc ( ME ) ( NASDAQ : FNLC ) Head - To - Head Survey (2026-09-09)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Uber Technologies, Inc vendio AUR por $182.2M el 2026-09-15.
- 10% owner HRT FINANCIAL LP compro USO por $4.6M el 2026-09-16.
- CEO Lyons Michael P. compro TFC por $1.0M el 2026-09-17.
- CEO Dube Eric M vendio TVTX por $6.6M el 2026-09-17.
- CEO Dube Eric M vendio TVTX por $6.3M el 2026-09-16.
- CEO Mandell Brian vendio PSX por $6.2M el 2026-09-16.
- CEO Troendle August J. vendio MEDP por $5.4M el 2026-09-16.
- CEO Troendle August J. vendio MEDP por $9.9M el 2026-09-15.

**Polymarket — smart money (traders con mejor track record):**

- JnStrtPrdctnMrkts · PnL $152,074 · win rate 91% · categorias: crypto
- Kosherlocks · PnL $40,767 · win rate 96% · categorias: sports, crypto
- punyapple · PnL $21,775 · win rate 100% · categorias: crypto, sports
- TAIWANNUMBERONE · PnL $26,666 · win rate 93% · categorias: sports, politics
- equalsignificance · PnL $20,637 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 821 registros 30d · ultimo dato 2026-09-17
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-18
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`FANG, GLD, IEF, KRMN, MEOH, QQQ, SBLK, SPY, TLT, USAR, USO, VG`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **70.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
