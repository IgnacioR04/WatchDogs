# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-16T20:23:52+00:00 · ventana señales 2026-08-17 -> 2026-09-16_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.69)
- Tendencia: `neutral` (SPY 754.05 · MA50 759.19 · MA200 713.39 · dist MA200: 5.7%)
- Credito: `tight` (HY spread 2.76)
- Tipos: `flat` (curva 10y-2y 0.33)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 754.05 | -0.44% | -1.1% | -1.75% |
| QQQ | 9.8% | core | 704.72 | 0.03% | -1.62% | -1.78% |
| TLT | 9.8% | core | 80.88 | 0.21% | -1.04% | -0.58% |
| GLD | 7.3% | core | 391.74 | -0.61% | -2.88% | -1.71% |
| CSQ | 7.1% | satellite | 20.16 | -0.59% | -2.68% | -2.4% |
| EVRG | 6.9% | satellite | 80.39 | 0.24% | -1.02% | -3.63% |
| IEF | 4.9% | core | 90.73 | -0.1% | -1.27% | -2.02% |
| SBLK | 3.2% | satellite | 30.87 | -1.09% | -0.93% | 5.62% |
| MCFT | 3.0% | satellite | 19.15 | -2.25% | -15.97% | -23.83% |
| GOLD | 2.2% | satellite | 46.82 | -2.05% | -5.09% | 11.9% |
| CELH | 1.6% | satellite | 28.25 | 2.24% | 2.21% | -5.52% |
| USAR | 1.3% | satellite | 15.1 | -1.95% | -11.49% | -18.42% |
| DELL | 1.1% | satellite | 563.29 | 3.64% | 5.24% | 20.19% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.2%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -3.6%
- Beta vs SPY: 0.629 · posiciones efectivas: 18.6 · HHI: 0.0538

**Por que estos satellite (señales WATCHDOG):**

- **CSQ** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **SBLK** · score agregado 235.5 · 3 señales · fuentes: corporate_insider
- **CELH** · score agregado 227.1 · 3 señales · fuentes: corporate_insider
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **MCFT** · score agregado 146.8 · 2 señales · fuentes: corporate_insider
- **EVRG** · score agregado 107.4 · 2 señales · fuentes: corporate_insider
- **DELL** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **GOLD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SBLK | 83 | corporate_insider | Spyrou Symeon | 3 | $424,050 | cluster_buy |
| VENU | 79 | corporate_insider | ROTH JAY W | 2 | $350,000 | cluster_buy |
| RWT | 78 | corporate_insider | Robinson Dashiell I | 2 | $251,580 | cluster_buy |
| SBLK | 78 | corporate_insider | Erhardt Koert | 3 | $169,620 | cluster_buy |
| CELH | 76 | corporate_insider | DeSantis Damon | 2 | $553,000 | cluster_buy |
| CELH | 76 | corporate_insider | DeSantis Damon | 2 | $447,200 | cluster_buy |
| RWT | 76 | corporate_insider | Carillo Brooke | 2 | $100,238 | cluster_buy |
| SBLK | 75 | corporate_insider | Karellis Nikolaos | 3 | $56,540 | cluster_buy |
| VENU | 75 | corporate_insider | Finke Thomas M | 2 | $350,000 | cluster_buy |
| CELH | 75 | corporate_insider | Kravitz Hal | 2 | $336,000 | cluster_buy |
| MCFT | 75 | corporate_insider | Nelson Bradley M. | 2 | $46,800 | cluster_buy |
| LMB | 72 | corporate_insider | Gaboury David Richard | 2 | $99,619 | cluster_buy |
| CBKM | 72 | corporate_insider | Lober Ralph J II | 2 | $13,192 | cluster_buy,small_amount |
| MCFT | 72 | corporate_insider | Lambert Roch | 2 | $75,016 | cluster_buy |
| ARDC | 72 | large_holder | THRIVENT FINANCIAL FOR LU |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| LFST | 61 | corporate_insider | TPG GP A, LLC | $226,255,274 | - |
| DELL | 60 | corporate_insider | Trizzino Peter | $21,137,638 | - |
| HPE | 59 | corporate_insider | Neri Antonio F | $15,110,500 | - |
| KLAC | 59 | corporate_insider | WALLACE RICHARD P | $12,378,626 | - |
| ROST | 58 | corporate_insider | Conroy James Grant | $11,291,775 | - |
| MTB | 57 | corporate_insider | JONES RENE F | $4,642,433 | - |
| HSTM | 56 | corporate_insider | FRIST ROBERT A JR | $4,250,006 | - |
| CRWV | 56 | corporate_insider | Agrawal Nitin | $5,303,445 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 754.05 (-0.44% / -1.1% / -1.75%) [2026-09-16]
- QQQ: 704.72 (0.03% / -1.62% / -1.78%) [2026-09-16]
- IWM: 283.93 (-0.42% / -2.05% / -5.18%) [2026-09-16]
- DIA: 515.22 (-1.15% / -1.69% / -3.24%) [2026-09-16]
- TLT: 80.88 (0.21% / -1.04% / -0.58%) [2026-09-16]
- IEF: 90.73 (-0.1% / -1.27% / -2.02%) [2026-09-16]
- GLD: 391.74 (-0.61% / -2.88% / -1.71%) [2026-09-16]
- ^VIX: 17.69 (2.85% / 7.47% / 18.8%) [2026-09-16]
- BTC-USD: 76280.0 (0.88% / -1.16% / -4.96%) [2026-09-16]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.67 (delta 1m: 0.5) [2026-09-15]
- Treasury 10Y yield: 5.0 (delta 1m: 0.32) [2026-09-15]
- Curva 10Y-2Y: 0.33 (delta 1m: -0.18) [2026-09-15]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.76 (delta 1m: 0.06) [2026-09-15]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.38 (delta 1m: 0.11) [2026-09-15]
- Dolar broad index: 118.2126 (delta 1m: -0.905) [2026-09-11]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (2), ai (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DDOG] Datadog ( NASDAQ : DDOG ) Stock Rating Upgraded by Wedbush (2026-09-12)
- [QLYS] Qualys ( NASDAQ : QLYS ) Upgraded by Wedbush to  Hold  Rating (2026-09-12)
- [RVMD] Revolution Medicines ( RVMD ) Gets its First Approved Drug , and the Market Shrugs (2026-09-12)
- [QLYS] Fair Isaac ( NYSE : FICO ) & Qualys ( NASDAQ : QLYS ) Financial Survey (2026-09-11)
- [QLYS] Qualys ( NASDAQ : QLYS ) versus Fair Isaac ( NYSE : FICO ) Head to Head Analysis (2026-09-11)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Trizzino Peter vendio DELL por $21.1M el 2026-09-11 [senal en multiples fuentes].
- 10% owner TPG GP A, LLC vendio LFST por $226.3M el 2026-09-11.
- CEO WALLACE RICHARD P vendio KLAC por $12.4M el 2026-09-15.
- CEO Conroy James Grant vendio ROST por $11.3M el 2026-09-14.
- 10% owner THRIVENT FINANCIAL FOR LUTHERANS compro ARDC por $6.0M el 2026-09-14 [senal en multiples fuentes].
- 10% owner BANKERS LIFE & CASUALTY CO compro Privacore VPC Asset Backed Credit Fund por $8.0M el 2026-09-14.
- 10% owner THRIVENT FINANCIAL FOR LUTHERANS opero ARDC por $9.0M el 2026-09-15 [senal en multiples fuentes].
- CEO Neri Antonio F vendio HPE por $15.1M el 2026-09-11.

**Polymarket — smart money (traders con mejor track record):**

- ethanaz · PnL $277,825 · win rate 89% · categorias: sports, crypto
- TheyAreTakingTheHobitsToIsengard · PnL $123,789 · win rate 90% · categorias: sports, economy
- SDTrading · PnL $54,452 · win rate 94% · categorias: sports
- WinterIsLeaving · PnL $34,836 · win rate 95% · categorias: sports, economy, politics
- 0x5966Db1fE50763C9e3C014d756369BAd07E1F804-1777648534241 · PnL $40,485 · win rate 90% · categorias: sports, crypto, economy

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 554 registros 30d · ultimo dato 2026-09-16
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-16
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CELH, CSQ, DELL, EVRG, GLD, GOLD, IEF, MCFT, QQQ, SBLK, SPY, TLT, USAR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
