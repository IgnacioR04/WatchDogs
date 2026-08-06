# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-06T15:43:08+00:00 · ventana señales 2026-07-07 -> 2026-08-06_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.46)
- Tendencia: `bull` (SPY 768.56 · MA50 746.12 · MA200 699.59 · dist MA200: 9.86%)
- Credito: `tight` (HY spread 2.75)
- Tipos: `flat` (curva 10y-2y 0.45)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 768.56 | -0.16% | 3.62% | 2.24% |
| QQQ | 12.0% | core | 716.35 | -0.13% | 4.8% | -0.96% |
| TLT | 12.0% | core | 82.66 | -0.41% | 0.24% | -1.77% |
| GLD | 9.3% | core | 389.77 | 0.03% | 3.34% | 3.06% |
| IEF | 6.2% | core | 93.04 | -0.29% | 0.16% | -0.37% |
| FWONK | 5.8% | satellite | 98.74 | 2.8% | -1.26% | 2.95% |
| LTH | 4.5% | satellite | 43.92 | -3.07% | -0.63% | 5.4% |
| TSCO | 4.4% | satellite | 33.97 | 1.69% | 12.46% | 12.8% |
| STOK | 3.4% | satellite | 32.32 | 1.22% | 7.59% | -1.55% |
| PCVX | 3.2% | satellite | 58.03 | 3.77% | 3.7% | -3.01% |
| SMG | 3.0% | satellite | 64.04 | -3.16% | -6.25% | -1.85% |
| GPCR | 3.0% | satellite | 51.65 | 2.22% | 4.41% | -6.33% |
| CHRW | 2.5% | satellite | 148.58 | -3.27% | 1.13% | -22.92% |
| TTAN | 2.4% | satellite | 84.76 | -2.01% | 6.13% | 6.7% |
| SPCX | 1.4% | satellite | 109.99 | 1.59% | -1.97% | -27.71% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.9%
- VaR 95% 1d: 0.7% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -2.7%
- Beta vs SPY: 0.499 · posiciones efectivas: 14.6 · HHI: 0.0684

**Por que estos satellite (señales WATCHDOG):**

- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **TSCO** · score agregado 123.7 · 2 señales · fuentes: corporate_insider
- **PCVX** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **SMG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **TTAN** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GPCR** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **STOK** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| MBRX | 80 | corporate_insider | KLEMP WALTER V | 3 | - | cluster_buy |
| MBRX | 80 | corporate_insider | Foster Jonathan P. | 3 | - | cluster_buy |
| MBRX | 77 | corporate_insider | PICKER DONALD H | 3 | - | cluster_buy |
| VIK | 72 | large_holder | FMR LLC |  | - | - |
| WAB | 72 | large_holder | FMR LLC |  | - | - |
| PCVX | 72 | large_holder | FMR LLC |  | - | - |
| SMG | 72 | large_holder | FMR LLC |  | - | - |
| TTAN | 72 | large_holder | FMR LLC |  | - | - |
| SGI | 72 | large_holder | FMR LLC |  | - | - |
| GPCR | 72 | large_holder | FMR LLC |  | - | - |
| STOK | 72 | large_holder | FMR LLC |  | - | - |
| SCI | 72 | large_holder | FMR LLC |  | - | - |
| SFM | 72 | large_holder | FMR LLC |  | - | - |
| MIRM | 72 | large_holder | FMR LLC |  | - | - |
| META | 72 | large_holder | FMR LLC |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 65 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| SCI | 62 | congress | April McClain Delaney | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 768.56 (-0.16% / 3.62% / 2.24%) [2026-08-06]
- QQQ: 716.35 (-0.13% / 4.8% / -0.96%) [2026-08-06]
- IWM: 300.02 (0.08% / 2.54% / 0.94%) [2026-08-06]
- DIA: 539.38 (-0.63% / 3.43% / 2.93%) [2026-08-06]
- TLT: 82.66 (-0.41% / 0.24% / -1.77%) [2026-08-06]
- IEF: 93.04 (-0.29% / 0.16% / -0.37%) [2026-08-06]
- GLD: 389.77 (0.03% / 3.34% / 3.06%) [2026-08-06]
- ^VIX: 15.46 (-2.21% / -9.54% / -2.4%) [2026-08-06]
- BTC-USD: 64726.01 (0.2% / 3.13% / 1.29%) [2026-08-06]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.2 (delta 1m: 0.07) [2026-08-04]
- Treasury 10Y yield: 4.63 (delta 1m: 0.15) [2026-08-04]
- Curva 10Y-2Y: 0.45 (delta 1m: 0.09) [2026-08-05]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.75 (delta 1m: 0.08) [2026-08-05]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.22 (delta 1m: -0.03) [2026-08-05]
- Dolar broad index: 119.7034 (delta 1m: -1.442) [2026-07-31]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (6), ai (5), earnings (2), regulatory (2), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [NET] Cloudflare , Inc .: Cloudflare Adds AEO Visibility Dashboard to Its AEO Suite , Showing Brands Whether AI Assistants Are Recommending Them (2026-08-06)
- [CRWV] CoreWeave is Off 20 % Over 3 Months : A Prominent Tech Analyst Expects 65 % Gains This Cycle (2026-08-06)
- [NET] Cloudflare OS Open - Sources AI Workspace That Never Hands Keys to Agents (2026-08-06)
- [COIN] After Earnings , Is Coinbase Stock a Buy , a Sell , or Fairly Valued ? (2026-08-06)
- [NTRA] Natera seeks Japan PMDA approval for Signatera test in MIBC (2026-08-06)
- [COIN] Forget Meme Coins : Here Why Im Investing in Prediction Market Contracts Instead (2026-08-06)
- [BLLN] BillionToOne Stock ( BLLN ) Falls After Hours : Here What Driving the Move - BillionToOne ( NASDAQ : BLLN ) (2026-08-06)
- [CRWV] AI cloud firm CoreWeave enters Indonesia with three data centres (2026-08-06)
- [COIN] Baystreet . ca - Watch Amazon , Dexcom , Corteva , and Coinbase (2026-08-06)
- [NTRA] Natera ( NASDAQ : NTRA ) CFO Michael Burkes Brophy Sells 478 Shares (2026-08-06)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Harrison Street Real Assets Fund LLC compro NFRX por $10.0M el 2026-08-04.
- CEO Bastian Edward H vendio DAL por $19.2M el 2026-08-04.
- CEO Huang Jack Jiajia compro COE por $3.3M el 2026-07-30.
- CEO Kon Kenta compro TM por $1.6M el 2026-08-05.
- CEO Huang Jack Jiajia compro COE por $1.8M el 2026-07-29.
- CEO Lawton III Harry A compro TSCO por $417K el 2026-08-04 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.

**Polymarket — smart money (traders con mejor track record):**

- TAIWANNUMBERONE · PnL $107,498 · win rate 91% · categorias: sports, politics
- JnStTrdrBnusFnd · PnL $78,115 · win rate 92% · categorias: crypto
- BreakTheBank · PnL $86,663 · win rate 85% · categorias: sports
- 0x5F659BcCBC353dBf7BcdffDEE73beE60bB482036-1780496231400 · PnL $31,296 · win rate 92% · categorias: sports, crypto
- monkeymashingkeyboard · PnL $29,472 · win rate 91% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 101 registros 30d · ultimo dato 2026-07-31
- **sec_insiders**: `ok` · 804 registros 30d · ultimo dato 2026-08-06
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-06
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CHRW, FWONK, GLD, GPCR, IEF, LTH, PCVX, QQQ, SMG, SPCX, SPY, STOK, TLT, TSCO, TTAN`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
