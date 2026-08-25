# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-25T21:03:23+00:00 · ventana señales 2026-07-26 -> 2026-08-25_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.45)
- Tendencia: `bull` (SPY 765.91 · MA50 752.63 · MA200 705.92 · dist MA200: 8.5%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.91 | 0.32% | -0.2% | 3.38% |
| QQQ | 12.0% | core | 710.72 | 0.62% | -0.95% | 5.22% |
| TLT | 12.0% | core | 83.47 | 1.1% | 2.22% | -0.51% |
| DGICA | 12.0% | satellite | 19.13 | 0.79% | 2.79% | 0.62% |
| GNK | 11.5% | satellite | 27.32 | 1.41% | 4.88% | 10.97% |
| GLD | 10.7% | core | 428.07 | 0.32% | 7.41% | 15.89% |
| CHTR | 7.7% | satellite | 155.14 | 3.22% | 4.58% | 10.84% |
| IEF | 7.1% | core | 93.51 | 0.54% | 0.62% | 0.29% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.5%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -5.8%
- Beta vs SPY: 0.515 · posiciones efectivas: 10.7 · HHI: 0.0932

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **DGICA** · score agregado 119.8 · 2 señales · fuentes: corporate_insider
- **GNK** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| TISI | 77 | corporate_insider | Roeder Clinton William | 2 | $183,200 | cluster_buy |
| TISI | 72 | corporate_insider | Roeder Clinton William | 2 | $22,840 | cluster_buy,small_amount |
| LFT | 72 | corporate_insider | Flynn James Peter | 2 | $13,642 | cluster_buy,small_amount |
| USIO | 72 | large_holder | TALL PINES CAPITAL, LLC |  | - | - |
| PCQ | 72 | large_holder | JPMorgan Chase Bank, Nati |  | - | - |
| PNI | 72 | large_holder | JPMorgan Chase Bank, Nati |  | - | - |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| CDTG | 72 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| TG | 72 | large_holder | John D. Gottwald |  | - | - |
| GO | 72 | large_holder | Pertento Partners LLP |  | - | - |
| CLBT | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| TENX | 72 | large_holder | Millennium Management LLC |  | - | - |
| LFT | 71 | corporate_insider | BRIGGS JAMES A | 2 | $13,798 | cluster_buy,small_amount |
| HKHC | 71 | corporate_insider | Rosenthal Brent D | 2 | $54,000 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $45,800 | cluster_buy |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MEDP | 58 | corporate_insider | Troendle August J. | $8,739,178 | - |
| GNK | 56 | corporate_insider | DIANA SHIPPING INC. | $10,027,500 | - |
| GNK | 56 | corporate_insider | DIANA SHIPPING INC. | $9,971,250 | - |
| COR | 56 | corporate_insider | Campbell Elizabeth S | $3,662,663 | - |
| PACS | 56 | corporate_insider | Murray Jason Hulse | $3,389,088 | - |
| CRCL | 55 | corporate_insider | Fox-Geen Jeremy | $4,050,000 | - |
| AMZN | 55 | corporate_insider | Zapolsky David | $2,404,951 | - |
| UTHR | 55 | corporate_insider | ROTHBLATT MARTINE A | $1,840,743 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.91 (0.32% / -0.2% / 3.38%) [2026-08-25]
- QQQ: 710.72 (0.62% / -0.95% / 5.22%) [2026-08-25]
- IWM: 299.23 (0.42% / -0.33% / 2.0%) [2026-08-25]
- DIA: 535.24 (0.3% / 0.52% / 1.67%) [2026-08-25]
- TLT: 83.47 (1.1% / 2.22% / -0.51%) [2026-08-25]
- IEF: 93.51 (0.54% / 0.62% / 0.29%) [2026-08-25]
- GLD: 428.07 (0.32% / 7.41% / 15.89%) [2026-08-25]
- ^VIX: 15.45 (-2.52% / -2.46% / -15.16%) [2026-08-25]
- BTC-USD: 78133.21 (-1.05% / 6.98% / 20.95%) [2026-08-25]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.24 (delta 1m: -0.09) [2026-08-24]
- Treasury 10Y yield: 4.7 (delta 1m: 0.01) [2026-08-24]
- Curva 10Y-2Y: 0.46 (delta 1m: 0.1) [2026-08-24]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.69 (delta 1m: -0.1) [2026-08-24]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.32 (delta 1m: 0.06) [2026-08-24]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (2), ai (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TENB] Tenable ( NASDAQ : TENB ) Stock Price Down 3 . 9 % – Time to Sell ? (2026-08-25)
- [RVMD] Billionaire Stanley Druckenmiller Continues to Load Up on Revolution Medicines . Does He Know Something Wall Street Doesnt ? (2026-08-25)
- [RVMD] Billionaire Stanley Druckenmiller Continues to Load Up on Revolution Medicines . Does He Know Something Wall Street Doesnt ? (2026-08-25)
- [LQDT] Liquidity Services to Present and Host 1x1 Investor Meetings at the 17th Annual Midwest IDEAS Investor Conference on August 26th in Chicago , IL (2026-08-21)
- [LQDT] Liquidity Services ( NASDAQ : LQDT ) Upgraded at Wall Street Zen (2026-08-19)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Host-Plus Pty Ltd as trustee for the HOSTPLUS Pooled Superannuation Trust compro EBR Systems, Inc. por $20.8M el 2026-08-21.
- Director Tsai Joseph C compro BABA por $10.4M el 2026-08-25.
- 10% owner DIANA SHIPPING INC. vendio GNK por $10.0M el 2026-08-24 [senal en multiples fuentes].
- CEO Gamble Sean vendio CNK por $5.3M el 2026-08-24.
- CEO Troendle August J. vendio MEDP por $8.7M el 2026-08-21.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- comon119 · PnL $27,272 · win rate 97% · categorias: sports, crypto
- cruzzzz · PnL $24,940 · win rate 95% · categorias: sports, politics
- AV23IUa · PnL $291,935 · win rate 76% · categorias: sports, crypto
- 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 · PnL $23,331 · win rate 88% · categorias: sports
- 0x0CdFf1E562Faf5EcE704Ef15f6A9fc4232E7eC9E-1780718136344 · PnL $29,592 · win rate 83% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 691 registros 30d · ultimo dato 2026-08-25
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-25
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CHTR, DGICA, GLD, GNK, IEF, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
