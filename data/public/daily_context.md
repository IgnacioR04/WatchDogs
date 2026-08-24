# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-24T20:03:11+00:00 · ventana señales 2026-07-25 -> 2026-08-24_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.88)
- Tendencia: `bull` (SPY 763.54 · MA50 752.11 · MA200 705.45 · dist MA200: 8.23%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `steep` (curva 10y-2y 0.5)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 763.54 | -0.28% | -1.18% | 3.31% |
| QQQ | 12.0% | core | 706.32 | -1.0% | -3.23% | 3.55% |
| TLT | 12.0% | core | 82.56 | 0.62% | 1.49% | -1.02% |
| GLD | 9.3% | core | 426.71 | 0.79% | 5.23% | 13.9% |
| GRNT | 7.4% | satellite | 5.05 | -1.27% | -4.09% | 10.39% |
| CART | 7.3% | satellite | 51.78 | 3.91% | 5.98% | 17.52% |
| BABA | 6.3% | satellite | 118.47 | -0.73% | -5.0% | 3.02% |
| IEF | 6.2% | core | 93.01 | 0.2% | 0.18% | 0.05% |
| CHTR | 5.5% | satellite | 150.3 | 0.09% | 4.3% | 14.2% |
| ELF | 4.9% | satellite | 105.94 | 3.92% | 13.11% | 26.1% |
| CBRS | 2.1% | satellite | 185.43 | -5.46% | -26.41% | -1.69% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.4%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -3.4%
- Beta vs SPY: 0.574 · posiciones efectivas: 13.1 · HHI: 0.0763

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 213.8 · 3 señales · fuentes: large_holder
- **BABA** · score agregado 167.6 · 2 señales · fuentes: corporate_insider
- **ELF** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GRNT** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **CART** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BABA | 85 | corporate_insider | Wu Yongming | 2 | $4,984,000 | cluster_buy |
| BABA | 83 | corporate_insider | Tsai Joseph C | 2 | $10,288,800 | cluster_buy |
| GWRS | 81 | corporate_insider | Levine Jonathan L | 2 | $5,766,819 | cluster_buy |
| INV | 80 | corporate_insider | Haskell Gregory W | 4 | $75,600 | cluster_buy |
| INV | 79 | corporate_insider | Otworth Michael | 4 | $349,295 | cluster_buy |
| INV | 79 | corporate_insider | Donnally James O | 4 | $337,500 | cluster_buy |
| GWRS | 78 | corporate_insider | Cohn Andrew M. | 2 | $1,233,186 | cluster_buy |
| IDAI | 78 | corporate_insider | Genner Gareth Neville | 3 | $28,558 | cluster_buy |
| SCTH | 76 | corporate_insider | SITRA J SCOTT | 0 | $100,000,000 | - |
| INV | 75 | corporate_insider | Brown Bruce | 4 | $45,399 | cluster_buy |
| IDAI | 73 | corporate_insider | Genner Gareth Neville | 3 | $3,210 | cluster_buy,small_amount |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| CHTR | 72 | large_holder | Advance/Newhouse Partners |  | - | - |
| QXL | 72 | large_holder | Nissim Daniel |  | - | - |
| CHTR | 72 | large_holder | Ronald A. Duncan |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MDLZ | 58 | corporate_insider | Van de Put Dirk | $8,559,806 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $27,432,882 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $24,899,013 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $24,128,863 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $22,534,734 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $4,491,084 | - |
| CBRS | 56 | corporate_insider | Lie Sean | $19,223,823 | - |
| CZR | 56 | corporate_insider | Yunker Bret | $6,165,782 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 763.54 (-0.28% / -1.18% / 3.31%) [2026-08-24]
- QQQ: 706.32 (-1.0% / -3.23% / 3.55%) [2026-08-24]
- IWM: 297.96 (-0.67% / -2.01% / 1.72%) [2026-08-24]
- DIA: 533.66 (0.27% / -0.02% / 2.46%) [2026-08-24]
- TLT: 82.56 (0.62% / 1.49% / -1.02%) [2026-08-24]
- IEF: 93.01 (0.2% / 0.18% / 0.05%) [2026-08-24]
- GLD: 426.71 (0.79% / 5.23% / 13.9%) [2026-08-24]
- ^VIX: 15.88 (4.96% / 4.54% / -14.94%) [2026-08-24]
- BTC-USD: 78632.02 (1.13% / 13.52% / 22.76%) [2026-08-24]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: -0.12) [2026-08-20]
- Treasury 10Y yield: 4.69 (delta 1m: 0.02) [2026-08-20]
- Curva 10Y-2Y: 0.5 (delta 1m: 0.16) [2026-08-21]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.07) [2026-08-21]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.06) [2026-08-21]
- Dolar broad index: 118.9028 (delta 1m: -1.428) [2026-08-14]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [LIFE] Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Major Shareholder Us ( Ttgp ) Ltd . Sc Sells 107 , 795 Shares of Stock (2026-08-22)
- [LIFE] Lingke Wang Sells 118 , 333 Shares of Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Stock (2026-08-21)
- [INTA] Intapp launches Celeste AI for compliance and timekeeping (2026-08-20)
- [LIFE] Brandt Walter Kucharski Sells 77 , 436 Shares of Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Stock (2026-08-19)
- [INTA] Intapp ( NASDAQ : INTA ) Upgraded at Wall Street Zen (2026-08-18)
- [INTA] Intapp , Inc . ( NASDAQ : INTA ) Receives $37 . 86 Average Price Target from Brokerages (2026-08-13)

**Actores que han movido ficha este mes (top movimientos):**

- CEO SITRA J SCOTT compro SCTH por $100.0M el 2026-08-21.
- CEO Wu Yongming compro BABA por $5.0M el 2026-08-24.
- Officer Lie Sean vendio CBRS por $27.4M el 2026-08-20 [senal en multiples fuentes].
- Director Tsai Joseph C compro BABA por $10.3M el 2026-08-24.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.

**Polymarket — smart money (traders con mejor track record):**

- SPCEXBUYER · PnL $160,333 · win rate 93% · categorias: sports
- TAIWANNUMBERONE · PnL $96,971 · win rate 92% · categorias: sports, politics
- Donghui · PnL $42,094 · win rate 92% · categorias: sports
- gransaaa · PnL $42,341 · win rate 88% · categorias: sports
- vibing123 · PnL $19,848 · win rate 90% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 613 registros 30d · ultimo dato 2026-08-24
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-24
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BABA, CART, CBRS, CHTR, ELF, GLD, GRNT, IEF, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
