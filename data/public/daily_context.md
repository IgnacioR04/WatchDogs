# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-08T20:57:16+00:00 · ventana señales 2026-06-08 -> 2026-07-08_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.9)
- Tendencia: `bull` (SPY 745.4 · MA50 738.24 · MA200 690.16 · dist MA200: 8.0%)
- Credito: `tight` (HY spread 2.67)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 745.4 | -0.31% | -0.18% | 1.1% |
| QQQ | 12.0% | core | 711.44 | 0.28% | -3.39% | -0.54% |
| TLT | 12.0% | core | 84.36 | -0.22% | -2.02% | 0.06% |
| IEF | 12.0% | core | 93.51 | -0.2% | -0.79% | 0.32% |
| GLD | 12.0% | core | 374.45 | -0.81% | 1.65% | -5.74% |
| VFLEX | 12.0% | satellite | 27.64 | -0.11% | -0.54% | 0.36% |
| IDCC | 2.2% | satellite | 267.76 | -2.99% | -5.43% | 4.76% |
| ROKU | 2.1% | satellite | 139.25 | -1.39% | 0.8% | 12.69% |
| LQDA | 1.6% | satellite | 79.47 | -2.17% | -0.33% | 24.37% |
| NUVL | 1.4% | satellite | 123.8 | 0.02% | 0.24% | 39.9% |
| MERC | 1.3% | satellite | 0.65 | -4.78% | -1.89% | -19.06% |
| COE | 1.3% | satellite | 16.7 | 3.41% | 4.7% | -22.36% |
| INTC | 1.2% | satellite | 110.24 | -0.14% | -21.05% | -0.03% |
| APGE | 1.1% | satellite | 133.25 | -0.22% | 0.39% | 60.52% |
| INTZ | 1.0% | satellite | 0.9 | 3.45% | -3.23% | 23.29% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 11.3%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.5%
- Max drawdown historico: -5.5%
- Beta vs SPY: 0.681 · posiciones efectivas: 11.3 · HHI: 0.0884

**Por que estos satellite (señales WATCHDOG):**

- **COE** · score agregado 470.2 · 7 señales · fuentes: corporate_insider
- **APGE** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **MERC** · score agregado 170.8 · 3 señales · fuentes: corporate_insider
- **VFLEX** · score agregado 162.4 · 2 señales · fuentes: corporate_insider
- **LQDA** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTZ** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NUVL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **ROKU** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **IDCC** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| VFLEX | 85 | corporate_insider | PECK MICHAEL D | 2 | $4,999,988 | cluster_buy |
| FTECX | 82 | corporate_insider | PECK MICHAEL D | 2 | $1,499,990 | cluster_buy |
| VFLEX | 77 | corporate_insider | CHAD EISENBERG | 2 | $1,500,002 | cluster_buy |
| FTECX | 74 | corporate_insider | CHAD EISENBERG | 2 | $399,990 | cluster_buy |
| CAG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| LQDA | 72 | large_holder | BlackRock, Inc. |  | - | - |
| INTZ | 72 | large_holder | Tego Cyber, Inc. |  | - | - |
| OVID | 72 | large_holder | Federated Hermes, Inc. |  | - | - |
| NUVL | 72 | large_holder | FMR LLC |  | - | - |
| CYTK | 72 | large_holder | FMR LLC |  | - | - |
| ROKU | 72 | large_holder | FMR LLC |  | - | - |
| IDCC | 72 | large_holder | T. Rowe Price Associates, |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| PLCE | 70 | large_holder | Mithaq Capital SPC |  | - | - |
| CZWI | 70 | large_holder | Gale Hoese |  | - | - |

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

- SPY: 745.4 (-0.31% / -0.18% / 1.1%) [2026-07-08]
- QQQ: 711.44 (0.28% / -3.39% / -0.54%) [2026-07-08]
- IWM: 293.48 (-0.91% / -2.32% / 3.54%) [2026-07-08]
- DIA: 522.77 (-1.07% / 0.07% / 3.0%) [2026-07-08]
- TLT: 84.36 (-0.22% / -2.02% / 0.06%) [2026-07-08]
- IEF: 93.51 (-0.2% / -0.79% / 0.32%) [2026-07-08]
- GLD: 374.45 (-0.81% / 1.65% / -5.74%) [2026-07-08]
- ^VIX: 16.9 (4.77% / 2.74% / -10.68%) [2026-07-08]
- BTC-USD: 62058.49 (-1.96% / -0.78% / -1.33%) [2026-07-08]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: 0.14) [2026-07-07]
- Treasury 10Y yield: 4.55 (delta 1m: 0.08) [2026-07-07]
- Curva 10Y-2Y: 0.36 (delta 1m: -0.06) [2026-07-07]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.67 (delta 1m: -0.08) [2026-07-07]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.25 (delta 1m: -0.11) [2026-07-07]
- Dolar broad index: 120.6902 (delta 1m: 1.654) [2026-07-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: regulatory (1), ai (1), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWD] Grant Thornton Picks CrowdStrike ( CRWD ) to Power Its Global Cybersecurity Platform (2026-07-08)
- [MIAX] Miami International Holdings Reports June 2026 Trading Results (2026-07-07)
- [HPE] Dell Is Up 6 % Today : Is It Outperforming Other AI Server Stocks Like Hewlett Packard Enterprise and Super Micro ? (2026-07-06)
- [HPE] Hewlett Packard ( HPE ) Pricing Power Is Driving its Bullish Thesis (2026-06-30)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Huang Jack Jiajia compro COE por $9.3M el 2026-07-02.
- CEO PECK MICHAEL D compro VFLEX por $5.0M el 2026-07-02.
- CEO Huang Jack Jiajia compro COE por $4.8M el 2026-07-01.
- CEO Tenev Vladimir vendio HOOD por $13.6M el 2026-07-06.
- CEO TYLER BRIAN S. vendio MCK por $6.7M el 2026-07-07.
- CEO Wolf Kurt James vendio PBI por $4.9M el 2026-07-07.
- CEO PECK MICHAEL D compro FTECX por $1.5M el 2026-07-02.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $136,957 · win rate 97% · categorias: sports
- Sassy-Bucket · PnL $233,299 · win rate 92% · categorias: sports
- waterx- · PnL $48,845 · win rate 93% · categorias: crypto, sports
- 0x0x23kjookhaiuohduoayh8c9 · PnL $30,123 · win rate 93% · categorias: sports, crypto
- Dota2winner · PnL $24,456 · win rate 93% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 85 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 666 registros 30d · ultimo dato 2026-07-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-08
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`APGE, COE, GLD, IDCC, IEF, INTC, INTZ, LQDA, MERC, NUVL, QQQ, ROKU, SPY, TLT, VFLEX`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
