# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-25T08:04:52+00:00 · ventana señales 2026-08-26 -> 2026-09-25_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.6)
- Tendencia: `bull` (SPY 767.18 · MA50 759.46 · MA200 714.36 · dist MA200: 7.39%)
- Credito: `tight` (HY spread 2.73)
- Tipos: `flat` (curva 10y-2y 0.31)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 767.18 | -0.08% | 0.85% | 0.39% |
| QQQ | 12.0% | core | 741.1 | -0.01% | 3.48% | 4.29% |
| TLT | 12.0% | core | 79.42 | -1.29% | -2.89% | -4.29% |
| KNTK | 9.6% | satellite | 52.54 | -0.72% | -2.41% | -3.12% |
| GLD | 9.3% | core | 391.69 | -0.3% | -1.67% | -7.03% |
| TRMD | 6.3% | satellite | 34.3 | -0.35% | -6.28% | 17.03% |
| IEF | 6.2% | core | 89.69 | -0.55% | -1.15% | -3.74% |
| MEOH | 6.0% | satellite | 59.77 | 1.05% | -2.83% | 5.01% |
| MG | 5.5% | satellite | 21.38 | 2.1% | 10.43% | 12.59% |
| TYRA | 3.2% | satellite | 22.41 | -3.53% | -7.97% | -16.04% |
| SEZL | 2.8% | satellite | 109.78 | 2.7% | -6.43% | -11.52% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.3%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -2.5%
- Beta vs SPY: 0.383 · posiciones efectivas: 12.9 · HHI: 0.0775

**Por que estos satellite (señales WATCHDOG):**

- **TRMD** · score agregado 212.2 · 3 señales · fuentes: large_holder
- **TYRA** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **MEOH** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **MG** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **KNTK** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **SEZL** · score agregado 67.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NYAX | 85 | corporate_insider | Nechmad Yair | 2 | $4,607,723 | cluster_buy |
| DKS | 80 | corporate_insider | Gupta Navdeep | 2 | $999,983 | cluster_buy |
| HHH | 78 | corporate_insider | GRANDISSON MARC | 2 | $1,602,938 | cluster_buy |
| DKS | 74 | corporate_insider | Fitzgerald Larry Jr. | 2 | $244,906 | cluster_buy |
| GAM | 73 | corporate_insider | Stark Eugene S | 2 | $113,750 | cluster_buy |
| GAM | 73 | corporate_insider | DAVIDSON SPENCER | 2 | $227,500 | cluster_buy |
| HHH | 72 | corporate_insider | Davis Andrew D. | 2 | $64,490 | cluster_buy |
| ASPN | 72 | large_holder | Wood River Capital, LLC |  | - | - |
| TRMD | 72 | large_holder | OCM NJORD HOLDINGS S.A R. |  | - | - |
| YI | 72 | large_holder | Gang Yu |  | - | - |
| NYAX | 72 | large_holder | MEITAV INVESTMENT HOUSE L |  | - | - |
| NYAX | 72 | corporate_insider | Ben-Avi David | 2 | $67,105 | cluster_buy |
| VMD | 70 | large_holder | Michael Moore |  | - | - |
| TROO | 70 | large_holder | WANG & LEE Holdings, Inc. |  | - | - |
| TROO | 70 | large_holder | Lianteng Limited |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| HOOD | 61 | corporate_insider | Tenev Vladimir | $31,154,170 | - |
| HOOD | 61 | corporate_insider | Tenev Vladimir | $30,020,114 | - |
| SPCX | 60 | corporate_insider | Shotwell Gwynne | $23,376,095 | - |
| SPCX | 60 | corporate_insider | Shotwell Gwynne | $22,348,568 | - |
| MS | 58 | corporate_insider | MITSUBISHI UFJ FINANCIAL  | $284,950,638 | - |
| CRWV | 58 | corporate_insider | Intrator Michael N | $7,546,891 | - |
| CLS | 58 | corporate_insider | Cooper Todd C | $7,242,480 | - |
| TEM | 57 | corporate_insider | LEFKOFSKY ERIC P | $6,125,928 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 767.18 (-0.08% / 0.85% / 0.39%) [2026-09-24]
- QQQ: 741.1 (-0.01% / 3.48% / 4.29%) [2026-09-24]
- IWM: 281.66 (-0.09% / -1.32% / -5.53%) [2026-09-24]
- DIA: 512.68 (-0.31% / -0.26% / -3.99%) [2026-09-24]
- TLT: 79.42 (-1.29% / -2.89% / -4.29%) [2026-09-24]
- IEF: 89.69 (-0.55% / -1.15% / -3.74%) [2026-09-24]
- GLD: 391.69 (-0.3% / -1.67% / -7.03%) [2026-09-24]
- ^VIX: 15.6 (-0.45% / 1.04% / 7.51%) [2026-09-25]
- BTC-USD: 84113.66 (-0.31% / 3.66% / 5.37%) [2026-09-25]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.85 (delta 1m: 0.61) [2026-09-23]
- Treasury 10Y yield: 5.11 (delta 1m: 0.41) [2026-09-23]
- Curva 10Y-2Y: 0.31 (delta 1m: -0.16) [2026-09-24]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.73 (delta 1m: 0.03) [2026-09-23]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.33 (delta 1m: 0.01) [2026-09-24]
- Dolar broad index: 119.5133 (delta 1m: 1.18) [2026-09-18]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (5), merger (2), regulatory (1), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [UNH] UnitedHealth , CVS , and Kaiser Oppose Medicare Remote Monitoring Vendor Ban While Humana and Blue Cross Back It (2026-09-25)
- [UNH] Minnesota - based UnitedHealthcare overbilled Medicare by $47 million : HHS (2026-09-25)
- [TEM] Tempus AI ( NASDAQ : TEM ) Trading 6 . 1 % Higher – Time to Buy ? (2026-09-24)
- [TEM] Tempus AI Chief Accounting Officer Sells $529 , 650 of Stock (2026-09-24)
- [TEM] Tempus AI ( TEM ) Has a $75 Goldman Sachs Target , But Its Data Business Faces a Bigger Test (2026-09-24)
- [TEM] The True Origins of China  Social Credit System  Part I – The Greanville Post (2026-09-24)
- [TBPH] Zymeworks Completes Acquisition of Theravance Biopharma (2026-09-23)
- [TBPH] Zymeworks Inc .: Zymeworks Completes Acquisition of Theravance Biopharma (2026-09-23)
- [TEM] Tempus AI ( TEM ) Has a $75 Goldman Sachs Target , But Its Data Business Faces a Bigger Test (2026-09-22)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Nechmad Yair compro NYAX por $4.6M el 2026-09-24 [senal en multiples fuentes].
- CEO Tenev Vladimir vendio HOOD por $31.2M el 2026-09-21.
- 10% owner MITSUBISHI UFJ FINANCIAL GROUP INC vendio MS por $285.0M el 2026-09-22.
- CEO Tenev Vladimir vendio HOOD por $30.0M el 2026-09-22.
- CEO Shotwell Gwynne vendio SPCX por $23.4M el 2026-09-22.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $10.2M el 2026-09-22.
- 10% owner Blackstone Holdings IV L.P. compro Blackstone Private Real Estate Credit & Income Fund por $5.0M el 2026-09-23.
- 10% owner Durable Capital Partners LP compro GSHD por $7.1M el 2026-09-22.

**Polymarket — smart money (traders con mejor track record):**

- 0x16bb9951a36fce71e2ef57890b786145e0ba8492 · PnL $94,777 · win rate 94% · categorias: sports
- TAIWANNUMBERONE · PnL $67,152 · win rate 94% · categorias: sports
- 0xb4F978BE63cDF75554b0B46a4262a6dB597cc9A7-1779258330186 · PnL $78,111 · win rate 88% · categorias: sports, crypto, politics
- 0x9f15613ebf1f36d4bc679e1211d1fc567cf9bdb3 · PnL $37,059 · win rate 90% · categorias: sports, economy
- Kev69 · PnL $65,050 · win rate 82% · categorias: sports, crypto, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 614 registros 30d · ultimo dato 2026-09-24
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-24
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`GLD, IEF, KNTK, MEOH, MG, QQQ, SEZL, SPY, TLT, TRMD, TYRA`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
