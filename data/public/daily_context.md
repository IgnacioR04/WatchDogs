# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-08T17:08:41+00:00 · ventana señales 2026-06-08 -> 2026-07-08_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.94)
- Tendencia: `bull` (SPY 744.72 · MA50 738.22 · MA200 690.16 · dist MA200: 7.91%)
- Credito: `tight` (HY spread 2.67)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 744.72 | -0.4% | -0.27% | 1.0% |
| QQQ | 12.0% | core | 709.34 | -0.01% | -3.67% | -0.83% |
| TLT | 12.0% | core | 84.32 | -0.27% | -2.06% | 0.02% |
| GLD | 12.0% | core | 373.29 | -1.11% | 1.33% | -6.04% |
| VFLEX | 12.0% | satellite | 27.67 | 0.0% | -0.43% | 0.47% |
| IEF | 10.0% | core | 93.48 | -0.23% | -0.83% | 0.29% |
| FVR | 3.0% | satellite | 20.73 | 0.14% | 2.47% | 10.33% |
| GF | 2.9% | satellite | 11.5 | -2.04% | 0.35% | -2.46% |
| CACC | 1.9% | satellite | 622.05 | -3.79% | -2.31% | 10.56% |
| EPAM | 1.6% | satellite | 87.09 | -2.75% | 9.75% | -9.96% |
| ROKU | 1.4% | satellite | 140.11 | -0.78% | 1.43% | 13.39% |
| GLUE | 1.4% | satellite | 23.57 | -3.4% | -2.6% | 38.65% |
| RBLX | 1.1% | satellite | 54.37 | -4.14% | -0.03% | 28.52% |
| COE | 0.9% | satellite | 16.57 | 2.6% | 3.89% | -22.97% |
| INTC | 0.8% | satellite | 107.55 | -2.57% | -22.97% | -2.47% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.4%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -5.8%
- Beta vs SPY: 0.634 · posiciones efectivas: 11.8 · HHI: 0.085

**Por que estos satellite (señales WATCHDOG):**

- **COE** · score agregado 470.2 · 7 señales · fuentes: corporate_insider
- **VFLEX** · score agregado 162.4 · 2 señales · fuentes: corporate_insider
- **GLUE** · score agregado 142.0 · 2 señales · fuentes: large_holder
- **FVR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **EPAM** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **GF** · score agregado 119.6 · 2 señales · fuentes: corporate_insider
- **ROKU** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **RBLX** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **CACC** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| VFLEX | 85 | corporate_insider | PECK MICHAEL D | 2 | $4,999,988 | cluster_buy |
| FTECX | 82 | corporate_insider | PECK MICHAEL D | 2 | $1,499,990 | cluster_buy |
| VFLEX | 77 | corporate_insider | CHAD EISENBERG | 2 | $1,500,002 | cluster_buy |
| FTECX | 74 | corporate_insider | CHAD EISENBERG | 2 | $399,990 | cluster_buy |
| CAG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CYTK | 72 | large_holder | FMR LLC |  | - | - |
| ROKU | 72 | large_holder | FMR LLC |  | - | - |
| RBLX | 72 | large_holder | FMR LLC |  | - | - |
| GLUE | 72 | large_holder | T. Rowe Price Associates, |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| PLCE | 70 | large_holder | Mithaq Capital SPC |  | - | - |
| DOMO | 70 | large_holder | BlackRock Portfolio Manag |  | - | - |
| BITA | 70 | large_holder | BlackRock Portfolio Manag |  | - | - |
| FVR | 70 | large_holder | BlackRock Portfolio Manag |  | - | - |
| VIAV | 70 | large_holder | BlackRock, Inc. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| AESI | 64 | congress | Chip Roy | $250,000 | - |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| XOM | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| GE | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 744.72 (-0.4% / -0.27% / 1.0%) [2026-07-08]
- QQQ: 709.34 (-0.01% / -3.67% / -0.83%) [2026-07-08]
- IWM: 292.93 (-1.1% / -2.5% / 3.35%) [2026-07-08]
- DIA: 522.53 (-1.12% / 0.03% / 2.96%) [2026-07-08]
- TLT: 84.32 (-0.27% / -2.06% / 0.02%) [2026-07-08]
- IEF: 93.48 (-0.23% / -0.83% / 0.29%) [2026-07-08]
- GLD: 373.29 (-1.11% / 1.33% / -6.04%) [2026-07-08]
- ^VIX: 16.94 (5.02% / 2.98% / -10.47%) [2026-07-08]
- BTC-USD: 62052.85 (-1.97% / -0.79% / -1.34%) [2026-07-08]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.13 (delta 1m: 0.05) [2026-07-06]
- Treasury 10Y yield: 4.48 (delta 1m: -0.01) [2026-07-06]
- Curva 10Y-2Y: 0.36 (delta 1m: -0.06) [2026-07-07]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.67 (delta 1m: -0.08) [2026-07-07]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: -0.11) [2026-07-07]
- Dolar broad index: 120.6902 (delta 1m: 1.654) [2026-07-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWD] Grant Thornton Picks CrowdStrike ( CRWD ) to Power Its Global Cybersecurity Platform (2026-07-08)
- [YOU] Your Travel Day Super Hero Has Arrived : CLEAR Teams Up with Marvel Animation  X - Men  97  Season 2 to Help Members Win the Day of Travel (2026-06-30)
- [YOU] Your Travel Day Super Hero Has Arrived : CLEAR Teams Up with Marvel Animation  X - Men  97  Season 2 to Help Members Win the Day of Travel (2026-06-29)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner ADVENT INTERNATIONAL, L.P. opero OLPX por $1.0B el 2026-07-07.
- CEO Huang Jack Jiajia compro COE por $9.3M el 2026-07-02.
- CEO Baldwin Amanda vendio OLPX por $18.8M el 2026-07-07.
- CEO PECK MICHAEL D compro VFLEX por $5.0M el 2026-07-02.
- CEO Huang Jack Jiajia compro COE por $4.8M el 2026-07-01.
- CEO Mainolfi Nello vendio KYMR por $6.0M el 2026-07-07.
- CEO Wolf Kurt James vendio PBI por $4.9M el 2026-07-07.
- Director White Emily vendio OLPX por $48.4M el 2026-07-07.

**Polymarket — smart money (traders con mejor track record):**

- Sassy-Bucket · PnL $233,295 · win rate 92% · categorias: sports
- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $57,418 · win rate 97% · categorias: sports
- waterx- · PnL $48,856 · win rate 93% · categorias: crypto, sports
- 0x0x23kjookhaiuohduoayh8c9 · PnL $30,984 · win rate 93% · categorias: sports, crypto
- esportGG · PnL $19,054 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 72 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 589 registros 30d · ultimo dato 2026-07-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-08
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CACC, COE, EPAM, FVR, GF, GLD, GLUE, IEF, INTC, QQQ, RBLX, ROKU, SPY, TLT, VFLEX`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **90.0%** (el resto es cash). Estamos en regimen `risk_on`.
3. **Peso maximo por posicion**: <= **12.0%**.
4. **Sin apalancamiento y sin cortos**: todos los pesos >= 0, suma <= 1.
5. **Justifica cada cambio** con una razon concreta basada en los datos de este briefing (señal, regimen, riesgo, precio). Nada de datos externos.

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
