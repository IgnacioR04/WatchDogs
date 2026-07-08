# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-08T14:55:31+00:00 · ventana señales 2026-06-08 -> 2026-07-08_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.91)
- Tendencia: `bull` (SPY 742.34 · MA50 738.18 · MA200 690.14 · dist MA200: 7.56%)
- Credito: `tight` (HY spread 2.67)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 742.34 | -0.72% | -0.59% | 0.68% |
| QQQ | 12.0% | core | 706.49 | -0.41% | -4.06% | -1.23% |
| TLT | 12.0% | core | 84.14 | -0.49% | -2.28% | -0.21% |
| GLD | 12.0% | core | 371.12 | -1.69% | 0.74% | -6.58% |
| VFLEX | 12.0% | satellite | 27.67 | 0.0% | -0.43% | 0.47% |
| IEF | 10.3% | core | 93.41 | -0.31% | -0.9% | 0.21% |
| PSBD | 3.3% | satellite | 10.3 | -1.06% | -1.15% | 0.53% |
| GF | 3.1% | satellite | 11.5 | -2.04% | 0.35% | -2.46% |
| BBSI | 2.5% | satellite | 37.4 | -1.71% | 5.29% | 11.74% |
| ROKU | 1.5% | satellite | 140.27 | -0.67% | 1.54% | 13.51% |
| RBLX | 1.1% | satellite | 54.42 | -4.03% | 0.08% | 28.66% |
| COE | 0.9% | satellite | 16.45 | 1.88% | 3.16% | -23.51% |
| INTC | 0.9% | satellite | 106.63 | -3.41% | -23.63% | -3.3% |
| EOSE | 0.7% | satellite | 4.57 | -3.48% | -22.19% | -31.61% |
| ZBAO | 0.7% | satellite | 0.44 | 1.13% | 7.05% | -35.07% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.3%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -5.7%
- Beta vs SPY: 0.624 · posiciones efectivas: 11.6 · HHI: 0.0859

**Por que estos satellite (señales WATCHDOG):**

- **COE** · score agregado 470.2 · 7 señales · fuentes: corporate_insider
- **PSBD** · score agregado 193.7 · 3 señales · fuentes: corporate_insider, large_holder
- **VFLEX** · score agregado 162.4 · 2 señales · fuentes: corporate_insider
- **GF** · score agregado 119.6 · 2 señales · fuentes: corporate_insider
- **ROKU** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **RBLX** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BBSI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **ZBAO** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **EOSE** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| VFLEX | 85 | corporate_insider | PECK MICHAEL D | 2 | $4,999,988 | cluster_buy |
| FTECX | 82 | corporate_insider | PECK MICHAEL D | 2 | $1,499,990 | cluster_buy |
| VFLEX | 77 | corporate_insider | CHAD EISENBERG | 2 | $1,500,002 | cluster_buy |
| FTECX | 74 | corporate_insider | CHAD EISENBERG | 2 | $399,990 | cluster_buy |
| CYTK | 72 | large_holder | FMR LLC |  | - | - |
| ROKU | 72 | large_holder | FMR LLC |  | - | - |
| RBLX | 72 | large_holder | FMR LLC |  | - | - |
| QNT | 72 | large_holder | Capital World Investors |  | - | - |
| BBSI | 72 | large_holder | Private Capital Managemen |  | - | - |
| PSBD | 72 | large_holder | Alaris Master Fund LP |  | - | - |
| ZBAO | 72 | large_holder | Ningbo Pangu Chuangfu Hef |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| PLCE | 70 | large_holder | Mithaq Capital SPC |  | - | - |
| MEC | 70 | large_holder | Allspring Global Investme |  | - | - |
| SCYX | 70 | large_holder | Federated Hermes, Inc. |  | - | - |

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

- SPY: 742.34 (-0.72% / -0.59% / 0.68%) [2026-07-08]
- QQQ: 706.49 (-0.41% / -4.06% / -1.23%) [2026-07-08]
- IWM: 292.74 (-1.16% / -2.57% / 3.28%) [2026-07-08]
- DIA: 521.31 (-1.35% / -0.21% / 2.72%) [2026-07-08]
- TLT: 84.14 (-0.49% / -2.28% / -0.21%) [2026-07-08]
- IEF: 93.41 (-0.31% / -0.9% / 0.21%) [2026-07-08]
- GLD: 371.12 (-1.69% / 0.74% / -6.58%) [2026-07-08]
- ^VIX: 17.91 (11.04% / 8.88% / -5.34%) [2026-07-08]
- BTC-USD: 61955.59 (-2.12% / -0.94% / -1.5%) [2026-07-08]

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

**Temas dominantes**: ai (4), stock (4)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ANET] Hedge Fund and Insider Trading News : Ray Dalio , Paul Marshall , Warren Buffett , Jain Global , Brevan Howard , Lone Pine Capital , Liquidia Corp ( LQDA ), Arista Networks Inc ( ANET ), and More (2026-07-07)
- [MIAX] Miami International Holdings Reports June 2026 Trading Results (2026-07-07)
- [ANET] Insider Selling : Arista Networks ( NYSE : ANET ) Director Sells 8 , 000 Shares of Stock (2026-07-07)
- [ANET] Here How Arista Networks Is a Major Beneficiary of Big Tech Push to Break Nvidia Grip (2026-07-07)
- [HPE] Dell Is Up 6 % Today : Is It Outperforming Other AI Server Stocks Like Hewlett Packard Enterprise and Super Micro ? (2026-07-06)
- [ANET] What Makes Arista Networks ( ANET ) One of BlackRock 30 Most Important AI Stocks (2026-07-06)
- [ANET] What Makes Arista Networks ( ANET ) One of BlackRock 30 Most Important AI Stocks (2026-07-06)
- [HPE] Hewlett Packard ( HPE ) Pricing Power Is Driving its Bullish Thesis (2026-06-30)
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

- Sassy-Bucket · PnL $233,288 · win rate 92% · categorias: sports
- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $33,397 · win rate 97% · categorias: sports
- waterx- · PnL $48,856 · win rate 93% · categorias: crypto, sports
- 0x0x23kjookhaiuohduoayh8c9 · PnL $30,824 · win rate 94% · categorias: sports, crypto
- .Sisyphus. · PnL $31,818 · win rate 90% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 72 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 608 registros 30d · ultimo dato 2026-07-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-08
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BBSI, COE, EOSE, GF, GLD, IEF, INTC, PSBD, QQQ, RBLX, ROKU, SPY, TLT, VFLEX, ZBAO`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
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
