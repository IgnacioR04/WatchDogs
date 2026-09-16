# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-16T17:12:08+00:00 · ventana señales 2026-08-17 -> 2026-09-16_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.78)
- Tendencia: `bull` (SPY 759.54 · MA50 759.3 · MA200 713.41 · dist MA200: 6.47%)
- Credito: `tight` (HY spread 2.76)
- Tipos: `flat` (curva 10y-2y 0.33)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 759.54 | 0.28% | -0.38% | -1.03% |
| QQQ | 12.0% | core | 709.55 | 0.71% | -0.94% | -1.11% |
| TLT | 12.0% | core | 81.18 | 0.58% | -0.67% | -0.21% |
| GLD | 9.3% | core | 398.17 | 1.02% | -1.28% | -0.1% |
| CSQ | 8.6% | satellite | 20.4 | 0.59% | -1.52% | -1.24% |
| EVRG | 8.4% | satellite | 80.91 | 0.89% | -0.38% | -3.01% |
| IEF | 6.2% | core | 91.14 | 0.35% | -0.83% | -1.57% |
| SBLK | 3.8% | satellite | 30.96 | -0.8% | -0.64% | 5.93% |
| COO | 3.3% | satellite | 54.8 | 2.87% | -13.67% | -27.67% |
| GOLD | 2.6% | satellite | 48.03 | 0.48% | -2.64% | 14.79% |
| CELH | 2.0% | satellite | 28.74 | 4.0% | 3.96% | -3.9% |
| DBI | 1.8% | satellite | 6.22 | -0.4% | 19.25% | 5.87% |
| USAR | 1.6% | satellite | 15.25 | -0.97% | -10.61% | -17.61% |
| DELL | 1.4% | satellite | 567.49 | 4.41% | 6.02% | 21.09% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.7%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -4.2%
- Beta vs SPY: 0.735 · posiciones efectivas: 13.4 · HHI: 0.0746

**Por que estos satellite (señales WATCHDOG):**

- **COO** · score agregado 315.7 · 4 señales · fuentes: corporate_insider
- **CSQ** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **SBLK** · score agregado 235.5 · 3 señales · fuentes: corporate_insider
- **CELH** · score agregado 227.1 · 3 señales · fuentes: corporate_insider
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **EVRG** · score agregado 107.4 · 2 señales · fuentes: corporate_insider
- **DBI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **DELL** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **GOLD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SBLK | 83 | corporate_insider | Spyrou Symeon | 3 | $424,050 | cluster_buy |
| NTHI | 81 | corporate_insider | Heshmatpour Amir F | 3 | $115,395 | cluster_buy |
| COO | 80 | corporate_insider | Kurzius Lawrence Erik | 3 | $539,150 | cluster_buy |
| NTHI | 79 | corporate_insider | Heshmatpour Amir F | 3 | $59,400 | cluster_buy |
| COO | 79 | corporate_insider | Rosebrough Walter M Jr | 3 | $378,770 | cluster_buy |
| VENU | 79 | corporate_insider | ROTH JAY W | 2 | $350,000 | cluster_buy |
| COO | 78 | corporate_insider | Keel Paul A | 3 | $250,000 | cluster_buy |
| SBLK | 78 | corporate_insider | Erhardt Koert | 3 | $169,620 | cluster_buy |
| COO | 78 | corporate_insider | Rosebrough Walter M Jr | 3 | $162,870 | cluster_buy |
| NTHI | 77 | corporate_insider | CHEN THOMAS C | 3 | $19,998 | cluster_buy,small_amount |
| NTHI | 77 | corporate_insider | CHEN THOMAS C | 3 | $20,002 | cluster_buy,small_amount |
| CELH | 76 | corporate_insider | DeSantis Damon | 2 | $553,000 | cluster_buy |
| CELH | 76 | corporate_insider | DeSantis Damon | 2 | $447,200 | cluster_buy |
| RWT | 76 | corporate_insider | Carillo Brooke | 2 | $100,238 | cluster_buy |
| SBLK | 75 | corporate_insider | Karellis Nikolaos | 3 | $56,540 | cluster_buy |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| LFST | 61 | corporate_insider | TPG GP A, LLC | $226,255,274 | - |
| DELL | 60 | corporate_insider | Trizzino Peter | $21,137,638 | - |
| HPE | 59 | corporate_insider | Neri Antonio F | $15,110,500 | - |
| ROST | 58 | corporate_insider | Conroy James Grant | $11,291,775 | - |
| HSTM | 56 | corporate_insider | FRIST ROBERT A JR | $4,250,006 | - |
| CRVL | 56 | corporate_insider | CORSTAR HOLDINGS INC | $8,968,055 | - |
| CRWV | 56 | corporate_insider | Agrawal Nitin | $5,303,445 | - |
| AMBQ | 55 | corporate_insider | Esaka Fumihide | $2,662,427 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 759.54 (0.28% / -0.38% / -1.03%) [2026-09-16]
- QQQ: 709.55 (0.71% / -0.94% / -1.11%) [2026-09-16]
- IWM: 286.35 (0.42% / -1.22% / -4.38%) [2026-09-16]
- DIA: 520.8 (-0.08% / -0.62% / -2.19%) [2026-09-16]
- TLT: 81.18 (0.58% / -0.67% / -0.21%) [2026-09-16]
- IEF: 91.14 (0.35% / -0.83% / -1.57%) [2026-09-16]
- GLD: 398.17 (1.02% / -1.28% / -0.1%) [2026-09-16]
- ^VIX: 16.78 (-2.44% / 1.94% / 12.69%) [2026-09-16]
- BTC-USD: 75623.37 (0.01% / -2.01% / -5.77%) [2026-09-16]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.65 (delta 1m: 0.5) [2026-09-14]
- Treasury 10Y yield: 4.97 (delta 1m: 0.34) [2026-09-14]
- Curva 10Y-2Y: 0.33 (delta 1m: -0.18) [2026-09-15]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.76 (delta 1m: 0.06) [2026-09-15]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.38 (delta 1m: 0.11) [2026-09-15]
- Dolar broad index: 118.2126 (delta 1m: -0.905) [2026-09-11]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: earnings (4), stock (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CHYM] Chime Financial ( CHYM ) versus The Competition Head to Head Survey (2026-09-12)
- [FLWS] 1 - 800 FLOWERS . COM ( NASDAQ : FLWS ) and a . k . a . Brands ( NYSE : AKA ) Head to Head Analysis (2026-09-12)
- [CHYM] Insider Selling : Chime Financial ( NASDAQ : CHYM ) CAO Sells $642 , 494 . 70 in Stock (2026-09-12)
- [CHYM] Corpay ( NYSE : CPAY ) vs . Chime Financial ( NASDAQ : CHYM ) Head to Head Analysis (2026-09-11)
- [FLWS] 1 - 800 - FLOWERS ( FLWS ) Q4 2026 Earnings Call Transcript (2026-09-11)
- [FLWS] FinancialContent - 1 - 800 - FLOWERS ( NASDAQ : FLWS ) Q2 CY2026 Earnings Results : Non - GAAP EPS Misses Expectations , Stock Drops 15 . 5 % (2026-09-10)
- [FLWS] FinancialContent - What To Expect From 1 - 800 - FLOWERS ( FLWS ) Q2 Earnings (2026-09-09)
- [FLWS] What To Expect From 1 - 800 - FLOWERS ( FLWS ) Q2 Earnings (2026-09-09)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Trizzino Peter vendio DELL por $21.1M el 2026-09-11 [senal en multiples fuentes].
- 10% owner TPG GP A, LLC vendio LFST por $226.3M el 2026-09-11.
- CEO Conroy James Grant vendio ROST por $11.3M el 2026-09-14.
- 10% owner BANKERS LIFE & CASUALTY CO compro Privacore VPC Asset Backed Credit Fund por $8.0M el 2026-09-14.
- CEO Neri Antonio F vendio HPE por $15.1M el 2026-09-11.
- 10% owner THRIVENT FINANCIAL FOR LUTHERANS compro ARDC por $6.0M el 2026-09-14.
- 10% owner THRIVENT FINANCIAL FOR LUTHERANS opero ARDC por $9.0M el 2026-09-15.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.

**Polymarket — smart money (traders con mejor track record):**

- ethanaz · PnL $277,825 · win rate 89% · categorias: sports, crypto
- SDTrading · PnL $46,244 · win rate 94% · categorias: sports
- BrotherObama · PnL $81,866 · win rate 84% · categorias: sports
- DimSumConnoisseur. · PnL $44,100 · win rate 91% · categorias: sports
- xifutloong3 · PnL $96,912 · win rate 78% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 600 registros 30d · ultimo dato 2026-09-16
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-16
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CELH, COO, CSQ, DBI, DELL, EVRG, GLD, GOLD, IEF, QQQ, SBLK, SPY, TLT, USAR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
