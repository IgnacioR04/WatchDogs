# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-14T20:01:27+00:00 · ventana señales 2026-06-14 -> 2026-07-14_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.41)
- Tendencia: `bull` (SPY 752.23 · MA50 741.4 · MA200 692.03 · dist MA200: 8.7%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 752.23 | 0.41% | 0.6% | 1.67% |
| QQQ | 12.0% | core | 720.18 | 1.19% | 1.52% | -0.05% |
| TLT | 12.0% | core | 84.1 | 0.15% | -0.53% | -1.58% |
| GLD | 9.3% | core | 372.16 | 1.37% | -1.41% | -3.72% |
| BEP | 7.2% | satellite | 32.12 | 0.83% | -2.44% | -6.4% |
| IEF | 6.2% | core | 93.54 | 0.27% | -0.17% | -0.35% |
| ENR | 4.5% | satellite | 20.4 | -0.34% | -1.4% | 0.74% |
| BBIO | 4.4% | satellite | 84.12 | 1.26% | 7.98% | 25.94% |
| GGAL | 3.8% | satellite | 50.8 | -1.19% | -0.59% | -7.9% |
| YEXT | 3.6% | satellite | 5.42 | 4.03% | 5.65% | 33.5% |
| RH | 3.1% | satellite | 174.46 | 7.81% | 6.57% | 13.99% |
| IPX | 2.4% | satellite | 25.54 | 3.53% | -1.2% | -29.15% |
| ULCC | 2.4% | satellite | 6.4 | -2.59% | -13.04% | 2.4% |
| INTC | 2.2% | satellite | 107.78 | 4.52% | -2.36% | -13.48% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 15.4%
- VaR 95% 1d: 1.6% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -3.9%
- Beta vs SPY: 0.951 · posiciones efectivas: 14.3 · HHI: 0.0702

**Por que estos satellite (señales WATCHDOG):**

- **IPX** · score agregado 234.7 · 3 señales · fuentes: corporate_insider
- **YEXT** · score agregado 126.7 · 2 señales · fuentes: corporate_insider, large_holder
- **ENR** · score agregado 124.6 · 2 señales · fuentes: corporate_insider
- **GGAL** · score agregado 123.3 · 2 señales · fuentes: corporate_insider
- **ULCC** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BBIO** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **RH** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| IPX | 80 | corporate_insider | Arima Anastasios | 2 | $497,228 | cluster_buy |
| IPX | 78 | corporate_insider | Hannigan Todd | 2 | $1,075,980 | cluster_buy |
| IPX | 77 | corporate_insider | Hannigan Todd | 2 | $805,185 | cluster_buy |
| BUKS | 72 | corporate_insider | Daly Joseph Patrick | 2 | $33,375 | cluster_buy |
| BUKS | 72 | corporate_insider | Daly Joseph Patrick | 2 | $30,380 | cluster_buy |
| AMPH | 72 | large_holder | Dimensional Fund Advisors |  | - | - |
| ULCC | 72 | large_holder | Group Holdings - Frontier |  | - | - |
| BBIO | 72 | large_holder | VIKING GLOBAL INVESTORS L |  | - | - |
| RH | 72 | large_holder | Gary G. Friedman |  | - | - |
| BUKS | 72 | corporate_insider | Daly Joseph Patrick | 2 | $26,100 | cluster_buy |
| BUKS | 71 | corporate_insider | Daly Joseph Patrick | 2 | $22,000 | cluster_buy,small_amount |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| AIBZ | 70 | large_holder | Bakhashwain Mohammed |  | - | - |
| VYNE | 70 | large_holder | Zhang Xiaofan |  | - | - |
| NVRI | 70 | large_holder | BlackRock, Inc. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| XOM | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| GE | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 752.23 (0.41% / 0.6% / 1.67%) [2026-07-14]
- QQQ: 720.18 (1.19% / 1.52% / -0.05%) [2026-07-14]
- IWM: 294.46 (0.33% / -0.58% / 0.75%) [2026-07-14]
- DIA: 524.74 (0.05% / -0.7% / 2.56%) [2026-07-14]
- TLT: 84.1 (0.15% / -0.53% / -1.58%) [2026-07-14]
- IEF: 93.54 (0.27% / -0.17% / -0.35%) [2026-07-14]
- GLD: 372.16 (1.37% / -1.41% / -3.72%) [2026-07-14]
- ^VIX: 16.41 (-4.37% / 1.74% / -7.18%) [2026-07-14]
- BTC-USD: 64543.52 (3.7% / 2.14% / 5.82%) [2026-07-14]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.21 (delta 1m: 0.08) [2026-07-10]
- Treasury 10Y yield: 4.56 (delta 1m: 0.03) [2026-07-10]
- Curva 10Y-2Y: 0.36 (delta 1m: -0.06) [2026-07-13]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.69 (delta 1m: -0.02) [2026-07-13]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.26 (delta 1m: -0.08) [2026-07-13]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (5), regulatory (2), ai (1), merger (1), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DELL] Dell , HP Enterprise , and Okta are among the group seeing gains after IBM warning ( IBM : NYSE ) (2026-07-14)
- [CRWD] FinancialContent - Why CrowdStrike ( CRWD ) Stock Is Trading Up Today (2026-07-14)
- [CRWD] Is SentinelOne the Next CrowdStrike ? | The Motley Fool (2026-07-14)
- [DDOG] Datadog , Inc . $DDOG Shares Sold by Teachers Retirement System of The State of Kentucky (2026-07-14)
- [DELL] Fifth Third Bancorp Acquires 99 , 204 Shares of Dell Technologies Inc . $DELL (2026-07-14)
- [UTHR] Insider Selling : United Therapeutics ( NASDAQ : UTHR ) CEO Sells 9 , 500 Shares (2026-07-13)
- [DDOG] Y . D . More Investments Ltd Lowers Position in Datadog , Inc . $DDOG (2026-07-13)
- [UTHR] United Therapeutics ( UTHR ) Following FDA Approval Is The Stock Fully Valued (2026-07-11)

**Actores que han movido ficha este mes (top movimientos):**

- CFO Liu Chitung vendio UMC por $294.3M el 2026-07-13.
- 10% owner Group Holdings - Frontier LLC vendio ULCC por $84.2M el 2026-07-09 [senal en multiples fuentes].
- 10% owner Wang Xuning vendio SN por $401.2M el 2026-07-10.
- CEO Seto Wai Yue compro TDIC por $2.2M el 2026-07-07 [senal en multiples fuentes].
- CEO Huang Jack Jiajia compro COE por $3.5M el 2026-07-07.
- CEO Ullal Jayshree vendio ANET por $21.3M el 2026-07-09.
- CEO Huang Jack Jiajia compro COE por $3.1M el 2026-07-08.
- CEO Huang Jack Jiajia compro COE por $2.7M el 2026-07-06.

**Polymarket — smart money (traders con mejor track record):**

- Allezpapa · PnL $49,495 · win rate 99% · categorias: sports
- Hashbrown · PnL $67,180 · win rate 93% · categorias: crypto, sports, politics
- therighteousdog · PnL $39,759 · win rate 96% · categorias: sports
- 0xe11Ff8cd2718F51a4d9403D166c20eaAAbE253F4-1777047101622 · PnL $125,028 · win rate 88% · categorias: sports
- JnStTrdrBnusFnd · PnL $61,214 · win rate 91% · categorias: crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 71 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 597 registros 30d · ultimo dato 2026-07-14
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-14
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BBIO, BEP, ENR, GGAL, GLD, IEF, INTC, IPX, QQQ, RH, SPY, TLT, ULCC, YEXT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
