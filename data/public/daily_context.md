# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-22T07:49:47+00:00 · ventana señales 2026-09-22 -> 2026-10-22_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.23)
- Tendencia: `bull` (SPY 773.09 · MA50 767.35 · MA200 723.24 · dist MA200: 6.89%)
- Credito: `normal` (HY spread 3.33)
- Tipos: `flat` (curva 10y-2y 0.32)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.09 | 0.53% | 0.45% | 0.69% |
| QQQ | 11.4% | core | 725.2 | 1.05% | -0.51% | -2.16% |
| TLT | 11.4% | core | 80.24 | 0.14% | 1.71% | 0.13% |
| GLD | 8.6% | core | 378.95 | 0.34% | 0.79% | -3.55% |
| FBK | 7.5% | satellite | 52.1 | -0.29% | 3.41% | -1.03% |
| IEF | 5.7% | core | 90.23 | -0.02% | 0.58% | 0.39% |
| BPRE | 5.0% | satellite | 12.3 | 0.3% | -0.9% | 0.54% |
| LLY | 4.6% | satellite | 1270.75 | -1.01% | 5.13% | 10.4% |
| TALO | 3.4% | satellite | 18.07 | 0.11% | 6.11% | 9.12% |
| SE | 3.1% | satellite | 77.94 | -3.1% | -18.22% | -24.54% |
| BZH | 2.5% | satellite | 33.48 | 0.09% | 0.15% | 0.36% |
| CAMT | 2.0% | satellite | 133.09 | 4.06% | -1.94% | -9.5% |
| CIFR | 1.3% | satellite | 9.13 | 2.82% | -8.15% | -50.25% |
| NBIS | 1.3% | satellite | 171.57 | 0.07% | -7.76% | -24.29% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.7%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -4.3%
- Beta vs SPY: 0.686 · posiciones efectivas: 15.4 · HHI: 0.065

**Por que estos satellite (señales WATCHDOG):**

- **CIFR** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **CAMT** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **BPRE** · score agregado 185.0 · 3 señales · fuentes: corporate_insider
- **FBK** · score agregado 121.9 · 2 señales · fuentes: corporate_insider
- **SE** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BZH** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **TALO** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **LLY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NBIS** · score agregado 53.5 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NVA | 72 | corporate_insider | Gerteisen Christopher | 2 | $14,183 | cluster_buy,small_amount |
| IOT | 72 | large_holder | BAILLIE GIFFORD & CO |  | - | - |
| SE | 72 | large_holder | BAILLIE GIFFORD & CO |  | - | - |
| JILL | 72 | large_holder | ROYCE & ASSOCIATES LP |  | - | - |
| BZH | 72 | large_holder | Allan P. Merrill |  | - | - |
| TALO | 72 | large_holder | Carlos Slim Helu |  | - | - |
| LLY | 72 | large_holder | LILLY ENDOWMENT, INC. |  | - | - |
| BLND | 72 | large_holder | Capricorn Fund Managers L |  | - | - |
| NVA | 71 | corporate_insider | Gerteisen Christopher | 2 | $7,750 | cluster_buy,small_amount |
| YORW | 70 | corporate_insider | Velazquez David M | 2 | $40,000 | cluster_buy |
| GXVIX | 70 | corporate_insider | GLOBAL X MANAGEMENT COMPA | 0 | $25,000,000 | - |
| CPAC | 70 | large_holder | Inversiones ASPI S.A. |  | - | - |
| IOND | 70 | large_holder | Sachem Head Capital Manag |  | - | - |
| SGRP | 70 | large_holder | Brown Rory William |  | - | - |
| XAIR | 70 | large_holder | Lin Yi-Chien |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TALO | 59 | corporate_insider | Control Empresarial de Ca | $38,562,754 | - |
| MU | 57 | corporate_insider | Deboer Scott J | $25,599,600 | - |
| SNOW | 56 | corporate_insider | Slootman Frank | $26,156,811 | - |
| ATKR | 56 | corporate_insider | Waltz William E Jr. | $18,204,152 | - |
| SNOW | 56 | corporate_insider | Slootman Frank | $21,628,970 | - |
| SNOW | 55 | corporate_insider | Slootman Frank | $12,896,145 | - |
| CVX | 55 | corporate_insider | Pate R. Hewitt | $9,224,777 | - |
| SNOW | 55 | corporate_insider | Slootman Frank | $12,506,903 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.09 (0.53% / 0.45% / 0.69%) [2026-10-21]
- QQQ: 725.2 (1.05% / -0.51% / -2.16%) [2026-10-21]
- IWM: 276.48 (0.25% / 1.88% / -1.93%) [2026-10-21]
- DIA: 527.7 (0.64% / 2.36% / 2.63%) [2026-10-21]
- TLT: 80.24 (0.14% / 1.71% / 0.13%) [2026-10-21]
- IEF: 90.23 (-0.02% / 0.58% / 0.39%) [2026-10-21]
- GLD: 378.95 (0.34% / 0.79% / -3.55%) [2026-10-21]
- ^VIX: 18.23 (9.29% / 10.75% / 16.34%) [2026-10-22]
- BTC-USD: 82174.93 (-2.19% / 0.97% / -2.75%) [2026-10-22]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.79 (delta 1m: 0.03) [2026-10-20]
- Treasury 10Y yield: 5.12 (delta 1m: 0.11) [2026-10-20]
- Curva 10Y-2Y: 0.32 (delta 1m: 0.12) [2026-10-21]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.33 (delta 1m: 0.67) [2026-10-20]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.37 (delta 1m: 0.03) [2026-10-21]
- Dolar broad index: 121.4048 (delta 1m: 2.484) [2026-10-16]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [UTHR] United Therapeutics ( NASDAQ : UTHR ) Price Target Raised to $725 . 00 (2026-10-22)
- [DNA] Ginkgo Bioworks ( NYSE : DNA ) Major Shareholder Barry Canton Sells 22 , 369 Shares of Company Stock (2026-10-21)
- [UBER] Uber Technologies , Inc . $UBER Stock Sold by Prime Capital Investment Advisors LLC (2026-10-21)
- [UBER] Uber Technologies ( NYSE : UBER ) Stock Falls 1 . 5 % – Should You Sell ? (2026-10-20)
- [UBER] Uber Technologies ( UBER ) Is Generating Cash , but Can Robotaxi Spending Preserve Its Valuation ? (2026-10-20)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner GLOBAL X MANAGEMENT COMPANY, INC. compro GXVIX por $25.0M el 2026-10-19.
- 10% owner Control Empresarial de Capitales S.A. de C.V. vendio TALO por $38.6M el 2026-10-19 [senal en multiples fuentes].
- CEO Waltz William E Jr. vendio ATKR por $18.2M el 2026-10-19.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $5.6M el 2026-10-19.
- 10% owner Saba Capital Management, L.P. opero IAE por $10.2M el 2026-10-16 [senal en multiples fuentes].
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $1,442,765 · win rate 87% · categorias: sports, politics
- www511zwin · PnL $109,847 · win rate 100% · categorias: sports
- monkeymashingkeyboard · PnL $89,718 · win rate 93% · categorias: sports
- lpcapital1 · PnL $41,871 · win rate 97% · categorias: sports, crypto
- 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 · PnL $113,146 · win rate 89% · categorias: sports, crypto, economy

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 679 registros 30d · ultimo dato 2026-10-21
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-21
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BPRE, BZH, CAMT, CIFR, FBK, GLD, IEF, LLY, NBIS, QQQ, SE, SPY, TALO, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
