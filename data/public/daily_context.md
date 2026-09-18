# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-18T00:31:08+00:00 · ventana señales 2026-08-19 -> 2026-09-18_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.44)
- Tendencia: `neutral` (SPY 754.05 · MA50 759.19 · MA200 713.39 · dist MA200: 5.7%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.27)
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
| ADC | 7.2% | satellite | 68.5 | -2.24% | -5.63% | -7.36% |
| IEF | 4.9% | core | 90.73 | -0.1% | -1.27% | -2.02% |
| MNR | 4.3% | satellite | 10.9 | -2.68% | -13.97% | -13.49% |
| SBLK | 3.2% | satellite | 30.87 | -1.09% | -0.93% | 5.62% |
| FANG | 3.2% | satellite | 194.54 | -8.03% | -3.99% | -7.37% |
| MEOH | 2.9% | satellite | 61.51 | -4.32% | -0.94% | 7.19% |
| USO | 2.3% | satellite | 156.17 | -3.52% | 4.13% | 19.52% |
| VG | 1.8% | satellite | 14.65 | -4.19% | -3.93% | 3.44% |
| USAR | 1.5% | satellite | 15.1 | -1.95% | -11.49% | -18.42% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 5.8%
- VaR 95% 1d: 0.5% · CVaR 95% 1d: 0.7%
- Max drawdown historico: -2.2%
- Beta vs SPY: 0.272 · posiciones efectivas: 19.2 · HHI: 0.0521

**Por que estos satellite (señales WATCHDOG):**

- **SBLK** · score agregado 482.4 · 6 señales · fuentes: corporate_insider
- **MEOH** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **ADC** · score agregado 158.2 · 2 señales · fuentes: corporate_insider
- **USO** · score agregado 132.0 · 2 señales · fuentes: corporate_insider
- **MNR** · score agregado 119.7 · 2 señales · fuentes: corporate_insider
- **FANG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **VG** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BWMX | 84 | corporate_insider | CHEVALLIER ANDRES CAMPOS | 3 | $492,291 | cluster_buy |
| SBLK | 83 | corporate_insider | Pappa Milena Maria | 5 | $2,103,288 | cluster_buy |
| BWMX | 83 | corporate_insider | Campos Luis | 3 | $731,646 | cluster_buy |
| BWMX | 82 | corporate_insider | CHEVALLIER ANDRES CAMPOS | 3 | $247,494 | cluster_buy |
| BWMX | 82 | corporate_insider | Campos Luis | 3 | $575,456 | cluster_buy |
| SBLK | 82 | corporate_insider | Zagari Raffaele | 5 | $1,413,500 | cluster_buy |
| SBLK | 82 | corporate_insider | Pappas Alexandros | 5 | $2,103,288 | cluster_buy |
| ADC | 80 | corporate_insider | Agree Joey | 2 | $500,922 | cluster_buy |
| SBLK | 79 | corporate_insider | Reskos Nikolaos | 5 | $282,700 | cluster_buy |
| SBLK | 79 | corporate_insider | Zagari Raffaele | 5 | $282,700 | cluster_buy |
| BWMX | 78 | corporate_insider | CHEVALLIER SANTIAGO CAMPO | 3 | $246,924 | cluster_buy |
| ADC | 78 | corporate_insider | RAKOLTA JOHN JR | 2 | $1,375,600 | cluster_buy |
| SBLK | 77 | corporate_insider | Plakantonaki Charis | 5 | $84,810 | cluster_buy |
| RVSB | 76 | corporate_insider | Sherman Nicole | 4 | $10,043 | cluster_buy,small_amount |
| BENF | 76 | corporate_insider | Silk James G. | 3 | $10,000 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| AUR | 61 | corporate_insider | Uber Technologies, Inc | $182,238,436 | - |
| MEDP | 58 | corporate_insider | Troendle August J. | $9,915,436 | - |
| PSX | 57 | corporate_insider | Mandell Brian | $6,202,381 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $6,126,440 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $6,285,688 | - |
| MEDP | 57 | corporate_insider | Troendle August J. | $5,448,713 | - |
| JOBY | 56 | corporate_insider | Bevirt JoeBen | $3,755,269 | - |
| CRWV | 56 | corporate_insider | Intrator Michael N | $3,371,680 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 754.05 (-0.44% / -1.1% / -1.75%) [2026-09-16]
- QQQ: 704.72 (0.03% / -1.62% / -1.78%) [2026-09-16]
- IWM: 283.92 (-0.43% / -2.06% / -5.19%) [2026-09-16]
- DIA: 515.22 (-1.15% / -1.69% / -3.24%) [2026-09-16]
- TLT: 80.88 (0.21% / -1.04% / -0.58%) [2026-09-16]
- IEF: 90.73 (-0.1% / -1.27% / -2.02%) [2026-09-16]
- GLD: 391.74 (-0.61% / -2.88% / -1.71%) [2026-09-16]
- ^VIX: 15.44 (-12.82% / -13.45% / -3.56%) [2026-09-17]
- BTC-USD: 76316.63 (0.22% / -1.23% / -1.94%) [2026-09-18]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.74 (delta 1m: 0.55) [2026-09-16]
- Treasury 10Y yield: 5.01 (delta 1m: 0.29) [2026-09-16]
- Curva 10Y-2Y: 0.27 (delta 1m: -0.25) [2026-09-17]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.05) [2026-09-16]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.33 (delta 1m: 0.03) [2026-09-17]
- Dolar broad index: 118.2126 (delta 1m: -0.905) [2026-09-11]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (10), earnings (5), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [AI] Analysts Set C3 . ai , Inc . ( NYSE : AI ) Price Target at $8 . 70 (2026-09-13)
- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [AI] C3 . ai vs . UiPath : What Revenue Trends Between These Artificial Intelligence Companies Tell Investors (2026-09-13)
- [CTSH] Head to Head Review : The Hackett Group ( NASDAQ : HCKT ) vs . Cognizant Technology Solutions ( NASDAQ : CTSH ) (2026-09-12)
- [CTSH] Cognizant ( CTSH ): Can 17 AI Agents Turn Productivity Into Revenue ? (2026-09-12)
- [CRWD] Jensen Huang Says Cybersecurity Is AI Next Blockbuster App . CrowdStrike Is Already Building It With Nvidia (2026-09-11)
- [AI] YieldMax AI Option Income Strategy ETF ( NYSEARCA : AIYY ) Trading Down 0 . 5 % – Time to Sell ? (2026-09-11)
- [AI] Head to Head Comparison : C3 . ai ( NYSE : AI ) and Nvni Group ( NASDAQ : NVNI ) (2026-09-11)
- [CTSH] Cognizant ( CTSH ): Can 17 AI Agents Turn Productivity Into Revenue ? (2026-09-10)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Uber Technologies, Inc vendio AUR por $182.2M el 2026-09-15.
- 10% owner HRT FINANCIAL LP compro USO por $4.6M el 2026-09-16.
- CEO Mandell Brian vendio PSX por $6.2M el 2026-09-16.
- CEO Troendle August J. vendio MEDP por $5.4M el 2026-09-16.
- CEO Troendle August J. vendio MEDP por $9.9M el 2026-09-15.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- 0xb85321c2 · PnL $4 · win rate 100% · categorias: sports, politics, crypto
- Kendallwe4 · PnL $4 · win rate 100% · categorias: sports, politics, economy
- 0xdf07d539 · PnL $4 · win rate 100% · categorias: sports, politics, crypto
- 0x01a421ed · PnL $4 · win rate 100% · categorias: sports, politics, economy
- Cadenh6 · PnL $4 · win rate 99% · categorias: politics, sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 782 registros 30d · ultimo dato 2026-09-17
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-17
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `warning` · ? registros 30d · ultimo dato ? — inflated_avg_win_rate:0.8963
- **Fuentes con problemas**: congress, polymarket

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ADC, FANG, GLD, IEF, MEOH, MNR, QQQ, SBLK, SPY, TLT, USAR, USO, VG`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
