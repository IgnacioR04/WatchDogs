# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-08T12:16:28+00:00 · ventana señales 2026-06-08 -> 2026-07-08_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.82)
- Tendencia: `bull` (SPY 747.71 · MA50 737.57 · MA200 689.71 · dist MA200: 8.41%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 747.71 | -0.48% | 0.91% | 1.64% |
| QQQ | 12.0% | core | 709.43 | -1.85% | -2.02% | 0.73% |
| TLT | 12.0% | core | 84.55 | -1.05% | -2.96% | -0.23% |
| VFLEX | 12.0% | satellite | 27.67 | 0.0% | -0.43% | 0.47% |
| GLD | 11.4% | core | 377.49 | -1.21% | 2.42% | -4.73% |
| IEF | 7.6% | core | 93.7 | -0.51% | -1.11% | 0.42% |
| EVF | 5.7% | satellite | 4.99 | -0.2% | 0.0% | 1.24% |
| MOMO | 1.7% | satellite | 5.89 | -1.67% | 1.2% | 4.99% |
| ASC | 1.2% | satellite | 15.45 | 1.51% | 7.37% | -6.02% |
| MIAX | 1.2% | satellite | 43.72 | 4.44% | 18.71% | 11.5% |
| ARTW | 1.1% | satellite | 2.56 | -1.92% | -1.92% | -1.54% |
| NWL | 0.9% | satellite | 5.54 | -0.54% | -8.58% | 48.92% |
| EOSE | 0.5% | satellite | 4.74 | -6.32% | -22.17% | -33.05% |
| RYDE | 0.4% | satellite | 0.63 | 0.63% | 0.32% | -23.49% |
| EBRCZ | 0.3% | satellite | 0.31 | 0.0% | 0.0% | -6.13% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.2%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -4.9%
- Beta vs SPY: 0.569 · posiciones efectivas: 12.4 · HHI: 0.0805

**Por que estos satellite (señales WATCHDOG):**

- **MIAX** · score agregado 670.5 · 11 señales · fuentes: corporate_insider
- **MOMO** · score agregado 330.0 · 6 señales · fuentes: corporate_insider
- **NWL** · score agregado 256.2 · 4 señales · fuentes: corporate_insider
- **EOSE** · score agregado 245.2 · 4 señales · fuentes: corporate_insider, large_holder
- **ASC** · score agregado 177.0 · 3 señales · fuentes: corporate_insider
- **VFLEX** · score agregado 162.4 · 2 señales · fuentes: corporate_insider
- **EBRCZ** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **ARTW** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **EVF** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **RYDE** · score agregado 141.0 · 2 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| VFLEX | 85 | corporate_insider | PECK MICHAEL D | 2 | $4,999,988 | cluster_buy |
| FTECX | 82 | corporate_insider | PECK MICHAEL D | 2 | $1,499,990 | cluster_buy |
| VFLEX | 77 | corporate_insider | CHAD EISENBERG | 2 | $1,500,002 | cluster_buy |
| FTECX | 74 | corporate_insider | CHAD EISENBERG | 2 | $399,990 | cluster_buy |
| QNT | 72 | large_holder | Capital World Investors |  | - | - |
| BBSI | 72 | large_holder | Private Capital Managemen |  | - | - |
| ZBAO | 72 | large_holder | Ningbo Pangu Chuangfu Hef |  | - | - |
| MLP | 72 | large_holder | TSP Capital Management Gr |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| SCYX | 70 | large_holder | Federated Hermes, Inc. |  | - | - |
| OVID | 70 | large_holder | Federated Hermes, Inc. |  | - | - |
| NERV | 70 | large_holder | Federated Hermes, Inc. |  | - | - |
| MGPI | 70 | large_holder | Federated Hermes, Inc. |  | - | - |
| FBRX | 70 | large_holder | Federated Hermes, Inc. |  | - | - |
| ATYR | 70 | large_holder | Federated Hermes, Inc. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MIAX | 74 | corporate_insider | Gallagher Thomas P. | $1,758,183 | cluster_buy |
| MIAX | 74 | corporate_insider | Gallagher Thomas P. | $1,193,198 | cluster_buy |
| MIAX | 71 | corporate_insider | Schafer Douglas M. JR | $1,978,560 | cluster_buy |
| MIAX | 70 | corporate_insider | Comly Barbara J. | $1,154,160 | cluster_buy |
| MIAX | 70 | corporate_insider | Jayabalan Harish | $842,400 | cluster_buy |
| MIAX | 69 | corporate_insider | Brown Shelly | $674,080 | cluster_buy |
| MIAX | 68 | corporate_insider | Deitzel Edward | $462,440 | cluster_buy |
| EOSE | 66 | corporate_insider | Kroeker Nathan | $371,166 | cluster_buy |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 747.71 (-0.48% / 0.91% / 1.64%) [2026-07-07]
- QQQ: 709.43 (-1.85% / -2.02% / 0.73%) [2026-07-07]
- IWM: 296.19 (-0.91% / -0.93% / 5.41%) [2026-07-07]
- DIA: 528.45 (-0.31% / 1.3% / 3.96%) [2026-07-07]
- TLT: 84.55 (-1.05% / -2.96% / -0.23%) [2026-07-07]
- IEF: 93.7 (-0.51% / -1.11% / 0.42%) [2026-07-07]
- GLD: 377.49 (-1.21% / 2.42% / -4.73%) [2026-07-07]
- ^VIX: 17.82 (10.48% / 8.33% / -5.81%) [2026-07-08]
- BTC-USD: 62252.49 (-1.65% / -0.47% / -1.02%) [2026-07-08]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.17 (delta 1m: 0.12) [2026-07-01]
- Treasury 10Y yield: 4.48 (delta 1m: 0.01) [2026-07-01]
- Curva 10Y-2Y: 0.35 (delta 1m: -0.06) [2026-07-02]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.75 (delta 1m: 0.0) [2026-07-02]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.23 (delta 1m: -0.16) [2026-07-02]
- Dolar broad index: 120.8866 (delta 1m: 1.704) [2026-06-26]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [MIAX] Miami International Holdings Reports June 2026 Trading Results (2026-07-07)
- [YOU] Your Travel Day Super Hero Has Arrived : CLEAR Teams Up with Marvel Animation  X - Men  97  Season 2 to Help Members Win the Day of Travel (2026-06-30)
- [YOU] Your Travel Day Super Hero Has Arrived : CLEAR Teams Up with Marvel Animation  X - Men  97  Season 2 to Help Members Win the Day of Travel (2026-06-29)
- [CACC] Credit Acceptance ( NASDAQ : CACC ) Insider Nicholas Elliott Sells 1 , 183 Shares (2026-06-27)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner ADVENT INTERNATIONAL, L.P. opero OLPX por $1.0B el 2026-07-07.
- 10% owner ADVENT INTERNATIONAL, L.P. opero OLPX por $1.0B el 2026-07-07.
- 10% owner ADVENT INTERNATIONAL, L.P. opero OLPX por $1.0B el 2026-07-07.
- CEO Baldwin Amanda vendio OLPX por $18.8M el 2026-07-07.
- CEO PECK MICHAEL D compro VFLEX por $5.0M el 2026-07-02.
- Director Glynn Tricia vendio OLPX por $1.0B el 2026-07-07.
- Director MUSSAFER DAVID M vendio OLPX por $1.0B el 2026-07-07.
- Director White Michael James vendio OLPX por $1.0B el 2026-07-07.

**Polymarket — smart money (traders con mejor track record):**

- Sassy-Bucket · PnL $233,288 · win rate 92% · categorias: sports
- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $52,176 · win rate 97% · categorias: sports
- waterx- · PnL $48,832 · win rate 93% · categorias: crypto, sports
- 0x0x23kjookhaiuohduoayh8c9 · PnL $30,824 · win rate 94% · categorias: sports, crypto
- esportGG · PnL $24,271 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 72 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 582 registros 30d · ultimo dato 2026-07-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-08
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ARTW, ASC, EBRCZ, EOSE, EVF, GLD, IEF, MIAX, MOMO, NWL, QQQ, RYDE, SPY, TLT, VFLEX`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
