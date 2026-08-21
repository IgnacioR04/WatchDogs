# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-21T19:55:55+00:00 · ventana señales 2026-07-22 -> 2026-08-21_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.14)
- Tendencia: `bull` (SPY 765.89 · MA50 751.56 · MA200 704.98 · dist MA200: 8.64%)
- Credito: `tight` (HY spread 2.75)
- Tipos: `steep` (curva 10y-2y 0.5)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.89 | 0.43% | -1.35% | 3.65% |
| QQQ | 12.0% | core | 713.4 | 0.35% | -2.42% | 4.26% |
| TLT | 12.0% | core | 82.03 | -0.38% | -0.02% | -1.07% |
| GLD | 9.3% | core | 423.98 | 2.1% | 5.61% | 14.01% |
| FWONK | 6.7% | satellite | 105.12 | 0.92% | 1.17% | 8.32% |
| IEF | 6.2% | core | 92.82 | -0.2% | -0.24% | 0.11% |
| CHRW | 5.5% | satellite | 141.46 | -1.65% | -4.79% | -24.15% |
| LTH | 5.3% | satellite | 45.17 | 1.01% | -0.2% | 6.71% |
| MED | 5.0% | satellite | 11.99 | 3.18% | 4.81% | 23.86% |
| BBIO | 3.7% | satellite | 81.5 | -1.74% | 2.05% | -3.0% |
| HRI | 3.4% | satellite | 161.22 | -0.27% | -7.08% | -0.84% |
| AMR | 2.6% | satellite | 211.87 | 9.04% | 27.59% | 48.22% |
| CBRS | 1.3% | satellite | 195.82 | -6.69% | -10.58% | -1.66% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.9%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -2.5%
- Beta vs SPY: 0.688 · posiciones efectivas: 13.9 · HHI: 0.0719

**Por que estos satellite (señales WATCHDOG):**

- **AMR** · score agregado 353.3 · 6 señales · fuentes: corporate_insider
- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **MED** · score agregado 119.0 · 2 señales · fuentes: corporate_insider
- **HRI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **BBIO** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| INV | 80 | corporate_insider | Haskell Gregory W | 4 | $75,600 | cluster_buy |
| INV | 79 | corporate_insider | Otworth Michael | 4 | $349,295 | cluster_buy |
| INV | 79 | corporate_insider | Donnally James O | 4 | $337,500 | cluster_buy |
| IDAI | 78 | corporate_insider | Genner Gareth Neville | 3 | $28,558 | cluster_buy |
| IDAI | 76 | corporate_insider | Genner Gareth Neville | 3 | $9,840 | cluster_buy,small_amount |
| INV | 75 | corporate_insider | Brown Bruce | 4 | $45,399 | cluster_buy |
| IDAI | 74 | corporate_insider | Genner Gareth Neville | 3 | $5,040 | cluster_buy,small_amount |
| ELF | 73 | large_holder | Fenelon Opportunity Fund  |  | - | - |
| IDAI | 72 | corporate_insider | Genner Gareth Neville | 3 | $2,472 | cluster_buy,small_amount |
| TG | 72 | large_holder | John D. Gottwald |  | - | - |
| PRTA | 72 | large_holder | Fennell Todd W. |  | - | - |
| BY | 72 | large_holder | MBG INVESTORS I, LP |  | - | - |
| HRI | 72 | large_holder | Coliseum Capital Manageme |  | - | - |
| IDAI | 71 | corporate_insider | Genner Gareth Neville | 3 | $1,545 | cluster_buy,small_amount |
| IDAI | 71 | corporate_insider | Genner Gareth Neville | 3 | $1,265 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| T | 65 | congress | Tim Moore | $100,000 | - |
| PINS | 65 | congress | Christian D. Menefee | $50,000 | - |
| TSCO | 64 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| CCI | 63 | congress | Michael Rulli | $15,000 | small_amount |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| WAB | 62 | congress | April McClain Delaney | $15,000 | small_amount |
| WAB | 62 | congress | April McClain Delaney | $50,000 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.89 (0.43% / -1.35% / 3.65%) [2026-08-21]
- QQQ: 713.4 (0.35% / -2.42% / 4.26%) [2026-08-21]
- IWM: 300.2 (0.85% / -1.6% / 3.1%) [2026-08-21]
- DIA: 532.53 (0.95% / -0.8% / 2.65%) [2026-08-21]
- TLT: 82.03 (-0.38% / -0.02% / -1.07%) [2026-08-21]
- IEF: 92.82 (-0.2% / -0.24% / 0.11%) [2026-08-21]
- GLD: 423.98 (2.1% / 5.61% / 14.01%) [2026-08-21]
- ^VIX: 15.14 (-5.43% / 6.25% / -18.51%) [2026-08-21]
- BTC-USD: 77104.84 (5.58% / 22.74% / 22.85%) [2026-08-21]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: -0.07) [2026-08-19]
- Treasury 10Y yield: 4.65 (delta 1m: 0.02) [2026-08-19]
- Curva 10Y-2Y: 0.5 (delta 1m: 0.14) [2026-08-20]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.75 (delta 1m: 0.07) [2026-08-20]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.06) [2026-08-20]
- Dolar broad index: 118.9028 (delta 1m: -1.428) [2026-08-14]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CTKB] Analyzing Cytek Biosciences ( NASDAQ : CTKB ) and Quantum - Si ( NASDAQ : QSI ) (2026-08-19)
- [CTKB] Cytek Biosciences ( NASDAQ : CTKB ) versus Quantum - Si ( NASDAQ : QSI ) Critical Review (2026-08-19)
- [CTKB] Cytek ( CTKB ) Q2 2026 Earnings Call Transcript (2026-08-13)

**Actores que han movido ficha este mes (top movimientos):**

- CEO WIRTH JAMES F opero IHT por $5487.8B el 2026-08-18.
- CEO GELFOND RICHARD L vendio IMAX por $10.9M el 2026-08-19.
- CEO Gallagher Thomas P. vendio MIAX por $6.2M el 2026-08-19.
- 10% owner Mindlin Marcos Marcelo compro PAM por $3.0M el 2026-08-19.
- CEO GELFOND RICHARD L vendio IMAX por $5.3M el 2026-08-20.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- BOOMBOYS.Kiritych · PnL $1,163,266 · win rate 92% · categorias: sports
- HongYunX · PnL $42,410 · win rate 100% · categorias: sports
- 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 · PnL $166,752 · win rate 90% · categorias: sports
- JnStrtPrdctnMrkts · PnL $99,422 · win rate 90% · categorias: crypto
- CORGI8 · PnL $69,940 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 106 registros 30d · ultimo dato 2026-08-14 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 909 registros 30d · ultimo dato 2026-08-21
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-21
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMR, BBIO, CBRS, CHRW, FWONK, GLD, HRI, IEF, LTH, MED, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
