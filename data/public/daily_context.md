# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-17T18:29:46+00:00 · ventana señales 2026-08-18 -> 2026-09-17_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.56)
- Tendencia: `bull` (SPY 762.72 · MA50 759.53 · MA200 713.81 · dist MA200: 6.85%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.27)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 762.72 | 1.15% | 0.65% | -0.82% |
| QQQ | 12.0% | core | 716.32 | 1.65% | 1.08% | 0.03% |
| TLT | 12.0% | core | 81.63 | 0.93% | 1.05% | -1.3% |
| GLD | 9.3% | core | 399.4 | 1.96% | 0.77% | -3.49% |
| SBLK | 9.2% | satellite | 31.93 | 3.43% | 3.87% | 9.1% |
| FOX | 8.2% | satellite | 58.82 | -0.56% | 1.31% | -2.12% |
| DT | 6.8% | satellite | 55.4 | 0.38% | 7.74% | 11.69% |
| IEF | 6.2% | core | 91.14 | 0.46% | -0.04% | -2.04% |
| PLNT | 5.9% | satellite | 50.21 | 0.37% | 0.45% | -6.94% |
| USAR | 3.3% | satellite | 15.77 | 4.47% | -1.65% | -12.8% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.2%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -6.7%
- Beta vs SPY: 0.697 · posiciones efectivas: 12.5 · HHI: 0.0802

**Por que estos satellite (señales WATCHDOG):**

- **SBLK** · score agregado 640.3 · 8 señales · fuentes: corporate_insider
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **DT** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **FOX** · score agregado 70.6 · 1 señales · fuentes: corporate_insider
- **PLNT** · score agregado 56.9 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SBLK | 83 | corporate_insider | Pappa Milena Maria | 7 | $2,103,288 | cluster_buy |
| SBLK | 83 | corporate_insider | Spyrou Symeon | 7 | $424,050 | cluster_buy |
| SBLK | 82 | corporate_insider | Zagari Raffaele | 7 | $1,413,500 | cluster_buy |
| SBLK | 82 | corporate_insider | Pappas Alexandros | 7 | $2,103,288 | cluster_buy |
| ADC | 80 | corporate_insider | Agree Joey | 2 | $500,922 | cluster_buy |
| SBLK | 79 | corporate_insider | Reskos Nikolaos | 7 | $282,700 | cluster_buy |
| SBLK | 79 | corporate_insider | Zagari Raffaele | 7 | $282,700 | cluster_buy |
| ADC | 78 | corporate_insider | RAKOLTA JOHN JR | 2 | $1,375,600 | cluster_buy |
| SBLK | 77 | corporate_insider | Plakantonaki Charis | 7 | $84,810 | cluster_buy |
| BUKS | 76 | corporate_insider | Veradace Partners LP | 2 | $163,600 | cluster_buy |
| SBLK | 75 | corporate_insider | Karellis Nikolaos | 7 | $56,540 | cluster_buy |
| BUKS | 73 | corporate_insider | Veradace Partners LP | 2 | $58,650 | cluster_buy |
| GABC | 73 | corporate_insider | Bawel Zachary W | 3 | $20,000 | cluster_buy,small_amount |
| LMB | 72 | corporate_insider | Gaboury David Richard | 2 | $99,619 | cluster_buy |
| DT | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| UMC | 62 | corporate_insider | Liu Chitung | $170,799,600 | - |
| UMC | 61 | corporate_insider | Liu Chitung | $58,000,000 | - |
| FOX | 58 | corporate_insider | MURDOCH LACHLAN K | $10,274,977 | - |
| MRNA | 57 | corporate_insider | Hoge Stephen | $5,883,846 | - |
| MRNA | 57 | corporate_insider | Hoge Stephen | $5,807,574 | - |
| SNPS | 57 | corporate_insider | Ghazi Sassine | $5,474,683 | - |
| MTB | 57 | corporate_insider | JONES RENE F | $4,642,433 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $3,280,636 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 762.72 (1.15% / 0.65% / -0.82%) [2026-09-17]
- QQQ: 716.32 (1.65% / 1.08% / 0.03%) [2026-09-17]
- IWM: 286.33 (0.85% / -0.22% / -4.85%) [2026-09-17]
- DIA: 518.63 (0.66% / -0.41% / -2.85%) [2026-09-17]
- TLT: 81.63 (0.93% / 1.05% / -1.3%) [2026-09-17]
- IEF: 91.14 (0.46% / -0.04% / -2.04%) [2026-09-17]
- GLD: 399.4 (1.96% / 0.77% / -3.49%) [2026-09-17]
- ^VIX: 15.56 (-12.14% / -12.78% / -2.81%) [2026-09-17]
- BTC-USD: 76678.06 (0.69% / -0.77% / -1.48%) [2026-09-17]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.67 (delta 1m: 0.5) [2026-09-15]
- Treasury 10Y yield: 5.0 (delta 1m: 0.32) [2026-09-15]
- Curva 10Y-2Y: 0.27 (delta 1m: -0.26) [2026-09-16]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.05) [2026-09-16]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.33 (delta 1m: 0.05) [2026-09-16]
- Dolar broad index: 118.2126 (delta 1m: -0.905) [2026-09-11]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (7), ai (2), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [SNOW] Rep . Gilbert Ray Cisneros , Jr . Acquires Shares of Snowflake Inc . ( NYSE : SNOW ) (2026-09-13)
- [SOFI] Where Will SoFi Stock Be in 5 Years ? | The Motley Fool (2026-09-12)
- [SOFI] Where Will SoFi Stock Be in 5 Years ? | The Motley Fool (2026-09-12)
- [SOFI] Where Will SoFi Stock Be in 5 Years ? (2026-09-12)
- [SNOW] Jim Cramer Said Snowflake Inc . ( NYSE : SNOW ) Q2 Was Great For AI (2026-09-12)
- [DDOG] Datadog ( NASDAQ : DDOG ) Stock Rating Upgraded by Wedbush (2026-09-12)
- [W] Wayfair Is Opening Its First Monmouth County , NJ Location (2026-09-11)
- [SOFI] SoFi Technologies ( NASDAQ : SOFI ) Shares Down 3 . 8 % – Here Why (2026-09-11)
- [SOFI] FinancialContent - Why SoFi ( SOFI ) Stock Is Down Today (2026-09-09)
- [AX] Critical Review : MidWestOne Financial Group ( NASDAQ : MOFG ) & Axos Financial ( NYSE : AX ) (2026-09-05)

**Actores que han movido ficha este mes (top movimientos):**

- CEO MURDOCH LACHLAN K compro FOX por $10.3M el 2026-09-15.
- CFO Liu Chitung vendio UMC por $170.8M el 2026-09-16.
- CFO Liu Chitung vendio UMC por $58.0M el 2026-09-17.
- CEO Hoge Stephen vendio MRNA por $5.9M el 2026-09-15.
- CEO Ghazi Sassine vendio SNPS por $5.5M el 2026-09-15.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- lllllllIlll · PnL $116,574 · win rate 94% · categorias: sports
- JnStrtPrdctnMrkts · PnL $124,396 · win rate 91% · categorias: crypto
- TAIWANNUMBERONE · PnL $69,726 · win rate 93% · categorias: sports, politics
- monkeymashingkeyboard · PnL $46,087 · win rate 93% · categorias: sports
- BrotherObama · PnL $123,213 · win rate 85% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 733 registros 30d · ultimo dato 2026-09-17
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-17
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`DT, FOX, GLD, IEF, PLNT, QQQ, SBLK, SPY, TLT, USAR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
