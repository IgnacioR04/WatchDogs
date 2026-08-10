# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-10T21:16:49+00:00 · ventana señales 2026-07-11 -> 2026-08-10_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.46)
- Tendencia: `bull` (SPY 773.03 · MA50 747.02 · MA200 700.67 · dist MA200: 10.33%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.47)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.03 | -0.03% | 2.03% | 3.18% |
| QQQ | 12.0% | core | 720.87 | -0.3% | 2.97% | 1.28% |
| TLT | 12.0% | core | 82.06 | -0.85% | -0.16% | -1.88% |
| GLD | 9.3% | core | 402.54 | 1.02% | 8.29% | 9.65% |
| IEF | 6.2% | core | 92.76 | -0.44% | -0.06% | -0.23% |
| FWONK | 5.3% | satellite | 102.73 | -0.12% | 5.11% | 3.1% |
| VEON | 5.0% | satellite | 55.9 | -2.1% | 5.23% | 7.4% |
| BWFG | 4.4% | satellite | 66.83 | -0.1% | -1.02% | 14.3% |
| CHRW | 4.1% | satellite | 148.29 | -0.71% | 0.88% | -24.53% |
| LTH | 3.7% | satellite | 42.46 | -3.08% | -3.87% | 2.39% |
| AOS | 3.7% | satellite | 62.41 | -2.45% | 2.77% | 5.47% |
| LEG | 3.4% | satellite | 9.46 | -1.66% | -5.49% | -11.59% |
| FBIN | 1.7% | satellite | 47.99 | -5.49% | -8.01% | -4.55% |
| SPCX | 1.1% | satellite | 138.74 | 4.23% | 21.14% | -0.29% |
| WOLF | 1.0% | satellite | 29.3 | -10.86% | 20.33% | -12.93% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.4%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.0%
- Max drawdown historico: -2.0%
- Beta vs SPY: None · posiciones efectivas: 14.5 · HHI: 0.0692

**Por que estos satellite (señales WATCHDOG):**

- **BWFG** · score agregado 337.3 · 6 señales · fuentes: corporate_insider
- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **VEON** · score agregado 247.0 · 4 señales · fuentes: corporate_insider, large_holder
- **WOLF** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **FBIN** · score agregado 193.1 · 3 señales · fuentes: corporate_insider
- **SPCX** · score agregado 180.7 · 3 señales · fuentes: congress
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **LEG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **AOS** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| TSM | 76 | corporate_insider | Wei Che-Chia | 30 | $11,143 | cluster_buy,small_amount |
| ELAN | 75 | corporate_insider | VanHimbergen Robert M | 2 | $96,926 | cluster_buy |
| ELAN | 74 | corporate_insider | Herendeen Paul | 2 | $236,850 | cluster_buy |
| CZWI | 73 | corporate_insider | Bianchi Stephen M | 2 | $20,500 | cluster_buy,small_amount |
| SCKT | 72 | large_holder | Mills Enrico Kevin |  | - | - |
| VEON | 72 | large_holder | Giovanni Agnelli B.V. |  | - | - |
| MATW | 72 | large_holder | Oaktree Capital Managemen |  | - | - |
| AVR | 72 | large_holder | L1 Capital Pty Ltd |  | - | - |
| PINS | 72 | large_holder | Ameriprise Financial, Inc |  | - | - |
| LEG | 72 | large_holder | FMR LLC |  | - | - |
| AOS | 72 | large_holder | FMR LLC |  | - | - |
| WAY | 72 | large_holder | FMR LLC |  | - | - |
| BYRN | 72 | large_holder | FMR LLC |  | - | - |
| TSM | 71 | corporate_insider | Huang Jen-Chau | 30 | $2,126 | cluster_buy,small_amount |
| RDGL | 71 | corporate_insider | Korenko Michael K | 2 | $7,965 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TSCO | 65 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| LLY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| HSY | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.03 (-0.03% / 2.03% / 3.18%) [2026-08-10]
- QQQ: 720.87 (-0.3% / 2.97% / 1.28%) [2026-08-10]
- IWM: 299.98 (-0.52% / 1.27% / 2.21%) [2026-08-10]
- DIA: 538.99 (-0.12% / 1.46% / 2.8%) [2026-08-10]
- TLT: 82.06 (-0.85% / -0.16% / -1.88%) [2026-08-10]
- IEF: 92.76 (-0.44% / -0.06% / -0.23%) [2026-08-10]
- GLD: 402.54 (1.02% / 8.29% / 9.65%) [2026-08-10]
- ^VIX: 15.46 (3.76% / -2.52% / -9.91%) [2026-08-10]
- BTC-USD: 64058.33 (-1.21% / -0.83% / -3.68%) [2026-08-10]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: 0.03) [2026-08-07]
- Treasury 10Y yield: 4.65 (delta 1m: 0.11) [2026-08-07]
- Curva 10Y-2Y: 0.47 (delta 1m: 0.12) [2026-08-10]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: 0.0) [2026-08-07]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.29 (delta 1m: 0.05) [2026-08-10]
- Dolar broad index: 119.0649 (delta 1m: -1.688) [2026-08-07]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: earnings (7), stock (4)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TMO] FinancialContent - Plug Power ( NASDAQ : PLUG ) Q2 CY2026 Sales Top Estimates , Stock Soars (2026-08-10)
- [DDOG] Datadog coverage update : BofA stays bullish on weakness (2026-08-09)
- [UTHR] United Therapeutics Q2 Earnings Call Highlights (2026-08-08)
- [WEYS] Insider Selling : Weyco Group ( NASDAQ : WEYS ) VP Sells $109 , 554 . 93 in Stock (2026-08-07)
- [OC] This building materials stock has a favorable setup , charts show (2026-08-06)
- [UTHR] United Therapeutics Q2 Earnings Call Highlights (2026-08-05)
- [WEYS] Weyco Group Q2 Earnings Call Highlights (2026-08-05)
- [WEYS] Weyco Group ( NASDAQ : WEYS ) Posts Earnings Results (2026-08-05)
- [WEYS] Weyco : Q2 Earnings Snapshot (2026-08-04)
- [WEYS] Weyco : Q2 Earnings Snapshot (2026-08-04)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Huang Jack Jiajia compro COE por $6.2M el 2026-08-03.
- 10% owner Corre Partners Management, LLC vendio TISI por $57.0M el 2026-08-06 [senal en multiples fuentes].
- CEO Huang Jack Jiajia compro COE por $3.0M el 2026-08-05.
- CEO Huang Jack Jiajia compro COE por $2.4M el 2026-08-04.
- 10% owner venBio Global Strategic Fund IV, L.P. compro ATTO por $6.5M el 2026-08-06.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.

**Polymarket — smart money (traders con mejor track record):**

- Shori888 · PnL $24,326 · win rate 100% · categorias: sports
- quavoo · PnL $208,417 · win rate 84% · categorias: sports, politics, economy
- VD721lsj4938Dk388 · PnL $34,679 · win rate 91% · categorias: sports
- BrotherObama · PnL $60,591 · win rate 87% · categorias: sports
- lzh1 · PnL $28,087 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 73 registros 30d · ultimo dato 2026-07-31 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 589 registros 30d · ultimo dato 2026-08-10
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-10
- **institutional_13f**: `warning` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress, institutional_13f

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AOS, BWFG, CHRW, FBIN, FWONK, GLD, IEF, LEG, LTH, QQQ, SPCX, SPY, TLT, VEON, WOLF`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
