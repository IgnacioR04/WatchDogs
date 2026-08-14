# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-14T20:12:23+00:00 · ventana señales 2026-07-15 -> 2026-08-14_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.3)
- Tendencia: `bull` (SPY 776.32 · MA50 748.54 · MA200 702.75 · dist MA200: 10.47%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.48)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 776.32 | -0.2% | 0.4% | 4.44% |
| QQQ | 12.0% | core | 731.07 | -0.14% | 1.11% | 5.14% |
| TLT | 12.0% | core | 82.04 | -0.67% | -0.87% | -2.54% |
| GLD | 9.3% | core | 401.48 | 0.63% | 0.76% | 8.98% |
| FWONK | 9.0% | satellite | 103.9 | 0.2% | 4.22% | 4.17% |
| IEF | 6.2% | core | 93.04 | -0.28% | -0.14% | -0.51% |
| AMRZ | 5.9% | satellite | 46.69 | -0.12% | -8.83% | -8.76% |
| CHRW | 5.8% | satellite | 148.57 | -0.52% | -0.52% | -28.74% |
| LTH | 5.7% | satellite | 45.24 | 2.11% | 3.28% | 7.34% |
| CODI | 4.0% | satellite | 12.69 | 3.34% | 15.36% | 22.85% |
| ABCL | 3.0% | satellite | 11.38 | 3.74% | 64.21% | 76.02% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.5%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -7.5%
- Beta vs SPY: 0.769 · posiciones efectivas: 13.1 · HHI: 0.0765

**Por que estos satellite (señales WATCHDOG):**

- **AMRZ** · score agregado 473.7 · 6 señales · fuentes: corporate_insider
- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **CODI** · score agregado 217.0 · 3 señales · fuentes: corporate_insider
- **ABCL** · score agregado 154.3 · 2 señales · fuentes: corporate_insider
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BORR | 81 | corporate_insider | Troim Tor Olav | 2 | $6,036,750 | cluster_buy |
| AMRZ | 80 | corporate_insider | Oran Baris | 5 | $141,390 | cluster_buy |
| AMRZ | 80 | corporate_insider | Oran Baris | 5 | $142,140 | cluster_buy |
| AMRZ | 80 | corporate_insider | Hill Jaime | 5 | $70,680 | cluster_buy |
| AMRZ | 79 | corporate_insider | Clark Stephen S | 5 | $248,851 | cluster_buy |
| ABCL | 78 | corporate_insider | Booth Andrew | 2 | $383,904 | cluster_buy |
| AMRZ | 78 | corporate_insider | Gross Mario | 5 | $149,184 | cluster_buy |
| AMRZ | 76 | corporate_insider | Brouwer Roald | 5 | $69,540 | cluster_buy |
| TNC | 76 | corporate_insider | Mulligan Donal L | 2 | $538,720 | cluster_buy |
| BORR | 76 | corporate_insider | Currie Jeffrey | 2 | $501,638 | cluster_buy |
| ABCL | 76 | corporate_insider | Hayden Michael R | 2 | $481,033 | cluster_buy |
| SUNS | 75 | corporate_insider | TANNENBAUM LEONARD M | 2 | $152,000 | cluster_buy |
| CC | 75 | corporate_insider | Dignam Denise | 2 | $50,501 | cluster_buy |
| CODI | 74 | corporate_insider | Sawtelle Zachary T. | 2 | $299,658 | cluster_buy |
| AMRZ | 73 | corporate_insider | Gross Mario | 5 | $17,068 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PINS | 65 | congress | Christian D. Menefee | $50,000 | - |
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 64 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| CCI | 63 | congress | Michael Rulli | $15,000 | small_amount |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 776.32 (-0.2% / 0.4% / 4.44%) [2026-08-14]
- QQQ: 731.07 (-0.14% / 1.11% / 5.14%) [2026-08-14]
- IWM: 305.06 (0.51% / 1.16% / 3.75%) [2026-08-14]
- DIA: 536.81 (-0.2% / -0.52% / 3.07%) [2026-08-14]
- TLT: 82.04 (-0.67% / -0.87% / -2.54%) [2026-08-14]
- IEF: 93.04 (-0.28% / -0.14% / -0.51%) [2026-08-14]
- GLD: 401.48 (0.63% / 0.76% / 8.98%) [2026-08-14]
- ^VIX: 14.3 (-2.26% / -4.03% / -23.81%) [2026-08-14]
- BTC-USD: 62929.06 (-0.75% / -2.95% / -2.15%) [2026-08-14]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.2 (delta 1m: 0.02) [2026-08-12]
- Treasury 10Y yield: 4.68 (delta 1m: 0.1) [2026-08-12]
- Curva 10Y-2Y: 0.48 (delta 1m: 0.06) [2026-08-13]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.71 (delta 1m: 0.0) [2026-08-13]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.24 (delta 1m: 0.01) [2026-08-13]
- Dolar broad index: 119.0649 (delta 1m: -1.688) [2026-08-07]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: earnings (5), stock (4), ai (3)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CHYM] Chime ( CHYM ) Q2 2026 Earnings Call Transcript (2026-08-14)
- [ATTO] Attovia Therapeutics ( NASDAQ : ATTO ) Director Colin Walsh Sells 105 , 807 Shares (2026-08-14)
- [VMC] Diversified Marine Completes M / V Edwin Rider for Vulcan Materials (2026-08-14)
- [P] Everpure Climbs 9 . 7 % on Susquehanna Upgrade Yesterday (2026-08-13)
- [CHYM] Chime Financial explores stablecoin feature on app - report ( CHYM : NASDAQ ) (2026-08-13)
- [AIT] Applied Industrial Sees Growth In FY27 ; Stock Up 4 . 2 % (2026-08-13)
- [AIT] Reviewing NPK International ( NYSE : NPKI ) and Applied Industrial Technologies ( NYSE : AIT ) (2026-08-13)
- [CHYM] Chime ( CHYM ) Q2 2026 Earnings Call Transcript (2026-08-13)
- [CHYM] Here What to Know About Chime Financial Latest Insider Filings After a Strong Quarter (2026-08-11)
- [AIT] Applied Industrial Technologies ( AIT ) Projected to Announce Quarterly Earnings on Thursday (2026-08-11)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Huang Jack Jiajia compro COE por $6.8M el 2026-08-12.
- CEO Huang Jack Jiajia compro COE por $5.0M el 2026-08-11.
- CEO Dove Reid vendio KNX por $9.3M el 2026-08-13.
- 10% owner Empery Asset Management, LP compro EMPD por $2.2M el 2026-08-13 [senal en multiples fuentes].
- Director Troim Tor Olav compro BORR por $6.0M el 2026-08-13 [senal en multiples fuentes].
- CEO Intrator Michael N vendio CRWV por $9.3M el 2026-08-11.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $330,954 · win rate 96% · categorias: sports
- 111111111115 · PnL $518,082 · win rate 93% · categorias: sports
- WTSA · PnL $129,766 · win rate 98% · categorias: sports
- ExplosiveNinja · PnL $90,644 · win rate 97% · categorias: sports
- 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 · PnL $303,802 · win rate 86% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 101 registros 30d · ultimo dato 2026-08-07 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 666 registros 30d · ultimo dato 2026-08-14
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-14
- **institutional_13f**: `warning` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress, institutional_13f

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ABCL, AMRZ, CHRW, CODI, FWONK, GLD, IEF, LTH, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **95.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
