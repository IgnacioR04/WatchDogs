# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-21T18:54:05+00:00 · ventana señales 2026-09-21 -> 2026-10-21_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.68)
- Tendencia: `bull` (SPY 773.26 · MA50 767.35 · MA200 723.24 · dist MA200: 6.92%)
- Credito: `normal` (HY spread 3.29)
- Tipos: `flat` (curva 10y-2y 0.33)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.26 | 0.55% | 0.48% | 0.71% |
| QQQ | 11.4% | core | 725.74 | 1.13% | -0.44% | -2.09% |
| TLT | 11.4% | core | 80.1 | -0.04% | 1.53% | -0.05% |
| GLD | 8.6% | core | 378.2 | 0.14% | 0.59% | -3.74% |
| DX | 7.5% | satellite | 11.09 | 1.14% | 2.26% | -5.5% |
| IEF | 5.7% | core | 90.17 | -0.09% | 0.51% | 0.32% |
| PAG | 4.3% | satellite | 212.21 | -0.02% | 8.94% | 1.22% |
| VEON | 4.1% | satellite | 82.67 | 2.78% | 2.74% | 17.49% |
| FSLR | 2.9% | satellite | 173.23 | -0.69% | -3.27% | -9.76% |
| SE | 2.9% | satellite | 77.07 | -4.18% | -19.14% | -25.38% |
| RSKD | 2.5% | satellite | 9.02 | 2.79% | 11.43% | 26.26% |
| NVAX | 2.0% | satellite | 11.16 | -2.32% | -11.67% | 5.83% |
| CAMT | 1.9% | satellite | 132.68 | 3.74% | -2.24% | -9.78% |
| SG | 1.8% | satellite | 10.23 | -4.11% | 0.9% | 32.7% |
| BMBL | 1.0% | satellite | 5.93 | -0.25% | -0.59% | 121.46% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.2%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -3.3%
- Beta vs SPY: 0.695 · posiciones efectivas: 15.7 · HHI: 0.0638

**Por que estos satellite (señales WATCHDOG):**

- **CAMT** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **DX** · score agregado 151.6 · 2 señales · fuentes: corporate_insider
- **SG** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **BMBL** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **NVAX** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **VEON** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **PAG** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **RSKD** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **FSLR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **SE** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| DX | 77 | corporate_insider | Popenoe Smriti Laxman | 2 | $106,200 | cluster_buy |
| DX | 75 | corporate_insider | Popenoe Smriti Laxman | 2 | $50,360 | cluster_buy |
| NVA | 72 | corporate_insider | Gerteisen Christopher | 2 | $14,183 | cluster_buy,small_amount |
| SE | 72 | large_holder | BAILLIE GIFFORD & CO |  | - | - |
| BZH | 72 | large_holder | Allan P. Merrill |  | - | - |
| LLY | 72 | large_holder | LILLY ENDOWMENT, INC. |  | - | - |
| WEAV | 72 | large_holder | Glazer Capital, LLC |  | - | - |
| NVA | 71 | corporate_insider | Gerteisen Christopher | 2 | $7,750 | cluster_buy,small_amount |
| DX | 71 | corporate_insider | Sartori Michael Andrew | 2 | $10,700 | cluster_buy,small_amount |
| YORW | 70 | corporate_insider | Velazquez David M | 2 | $40,000 | cluster_buy |
| IOND | 70 | large_holder | Sachem Head Capital Manag |  | - | - |
| SGRP | 70 | large_holder | Brown Rory William |  | - | - |
| XAIR | 70 | large_holder | Lin Yi-Chien |  | - | - |
| WTS | 70 | large_holder | Timothy P. Horne |  | - | - |
| IOT | 70 | large_holder | BAILLIE GIFFORD & CO |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MU | 57 | corporate_insider | Deboer Scott J | $25,599,600 | - |
| GOLF | 56 | corporate_insider | Misto Holdings Corp. | $52,501,033 | - |
| CRSP | 55 | corporate_insider | Kulkarni Samarth | $2,381,326 | - |
| GRND | 55 | corporate_insider | Zage George Raymond III | $4,979,800 | - |
| NZF | 54 | corporate_insider | Robert Young L | $17,631,183 | - |
| GWRE | 53 | corporate_insider | Mullen John P | $999,000 | - |
| UTHR | 53 | corporate_insider | ROTHBLATT MARTINE A | $973,133 | - |
| VG | 53 | corporate_insider | Thayer Jonathan W | $1,411,243 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.26 (0.55% / 0.48% / 0.71%) [2026-10-21]
- QQQ: 725.74 (1.13% / -0.44% / -2.09%) [2026-10-21]
- IWM: 276.75 (0.35% / 1.98% / -1.83%) [2026-10-21]
- DIA: 526.84 (0.47% / 2.2% / 2.46%) [2026-10-21]
- TLT: 80.1 (-0.04% / 1.53% / -0.05%) [2026-10-21]
- IEF: 90.17 (-0.09% / 0.51% / 0.32%) [2026-10-21]
- GLD: 378.2 (0.14% / 0.59% / -3.74%) [2026-10-21]
- ^VIX: 16.68 (-3.64% / -1.13% / 9.88%) [2026-10-21]
- BTC-USD: 84517.94 (1.9% / 3.7% / -0.39%) [2026-10-21]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.77 (delta 1m: 0.1) [2026-10-19]
- Treasury 10Y yield: 5.15 (delta 1m: 0.21) [2026-10-19]
- Curva 10Y-2Y: 0.33 (delta 1m: 0.08) [2026-10-20]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.29 (delta 1m: 0.61) [2026-10-19]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.35 (delta 1m: 0.02) [2026-10-20]
- Dolar broad index: 121.4048 (delta 1m: 2.484) [2026-10-16]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [UBER] Uber Technologies , Inc . $UBER Stock Sold by Prime Capital Investment Advisors LLC (2026-10-21)
- [UBER] Uber Technologies ( NYSE : UBER ) Stock Falls 1 . 5 % – Should You Sell ? (2026-10-20)
- [UBER] Uber Technologies ( UBER ) Is Generating Cash , but Can Robotaxi Spending Preserve Its Valuation ? (2026-10-20)
- [IAM] Iambic Therapeutics ( NASDAQ : IAM ) Director Purchases 718 , 750 Shares of Stock (2026-10-20)
- [JBL] Analyzing Yaskawa Electric ( OTCMKTS : YASKY ) and Jabil ( NYSE : JBL ) (2026-10-17)
- [JBL] Jabil , Inc . $JBL Stock : Triasima Portfolio Management inc . Grows Stake (2026-10-16)
- [IAM] Iambic Therapeutics ( IAM ) prices IPO at $16 , raising $150 million on Nasdaq (2026-10-15)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Zhang Jason Gechen compro APLD por $5.7M el 2026-10-16.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $12.1M el 2026-10-16.
- 10% owner Misto Holdings Corp. vendio GOLF por $52.5M el 2026-10-15.
- 10% owner Saba Capital Management, L.P. opero IAE por $10.2M el 2026-10-16 [senal en multiples fuentes].
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.

**Polymarket — smart money (traders con mejor track record):**

- OhWhenTheReds · PnL $71,931 · win rate 100% · categorias: sports
- EdZachary · PnL $163,723 · win rate 91% · categorias: sports, politics, economy
- taylorsversion · PnL $142,970 · win rate 91% · categorias: sports, crypto
- JnStrtPrdctnMrkts · PnL $106,594 · win rate 90% · categorias: crypto
- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $36,106 · win rate 95% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 587 registros 30d · ultimo dato 2026-10-20
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-21
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BMBL, CAMT, DX, FSLR, GLD, IEF, NVAX, PAG, QQQ, RSKD, SE, SG, SPY, TLT, VEON`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
