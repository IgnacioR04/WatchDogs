# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-29T17:57:20+00:00 · ventana señales 2026-06-29 -> 2026-07-29_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 19.54)
- Tendencia: `neutral` (SPY 735.86 · MA50 743.95 · MA200 696.52 · dist MA200: 5.65%)
- Credito: `tight` (HY spread 2.84)
- Tipos: `flat` (curva 10y-2y 0.35)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 735.86 | -0.67% | -1.55% | -1.46% |
| QQQ | 9.8% | core | 670.19 | -0.78% | -4.98% | -8.99% |
| TLT | 9.8% | core | 83.91 | -0.39% | 0.56% | -2.55% |
| BEP | 9.5% | satellite | 31.72 | -0.84% | -1.49% | -8.67% |
| KRNY | 7.3% | satellite | 9.55 | -1.04% | 0.74% | 0.95% |
| GLD | 7.3% | core | 370.91 | 0.42% | -2.17% | 0.69% |
| IEF | 4.9% | core | 93.32 | -0.25% | 0.24% | -0.99% |
| GSHD | 2.9% | satellite | 70.17 | 1.97% | 36.53% | 44.69% |
| HTFL | 2.5% | satellite | 25.22 | -1.45% | 4.09% | -14.04% |
| MSTR | 2.2% | satellite | 97.24 | 1.12% | -2.77% | 11.86% |
| SPCX | 1.8% | satellite | 116.45 | 0.03% | 1.03% | -31.84% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.3%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -2.2%
- Beta vs SPY: None · posiciones efectivas: 17.3 · HHI: 0.0579

**Por que estos satellite (señales WATCHDOG):**

- **GSHD** · score agregado 443.4 · 7 señales · fuentes: corporate_insider
- **SPCX** · score agregado 241.4 · 4 señales · fuentes: congress
- **KRNY** · score agregado 182.4 · 3 señales · fuentes: corporate_insider, large_holder
- **HTFL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MSTR** · score agregado 62.0 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NNOX | 78 | corporate_insider | Meltzer Erez | 3 | $33,480 | cluster_buy |
| NNOX | 74 | corporate_insider | Kainan Noga | 3 | $29,700 | cluster_buy |
| NNOX | 73 | corporate_insider | Suesskind Dan S | 3 | $23,500 | cluster_buy,small_amount |
| NNOX | 73 | corporate_insider | Suesskind Dan S | 3 | $23,000 | cluster_buy,small_amount |
| JKHY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| GDDY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| FMC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ENVX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| KRNY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| HTFL | 72 | large_holder | BlackRock, Inc. |  | - | - |
| FUNC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CEPV | 70 | large_holder | RP Investment Advisors LP |  | - | - |
| PRQR | 70 | large_holder | Aberdeen Group plc |  | - | - |
| MWC | 70 | large_holder | Honda Motor Co., Ltd. |  | - | - |
| HUIZ | 70 | large_holder | Cunjun Ma |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| FMC | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 735.86 (-0.67% / -1.55% / -1.46%) [2026-07-29]
- QQQ: 670.19 (-0.78% / -4.98% / -8.99%) [2026-07-29]
- IWM: 290.19 (-1.08% / -1.23% / -3.41%) [2026-07-29]
- DIA: 519.06 (-1.49% / -0.46% / -0.61%) [2026-07-29]
- TLT: 83.91 (-0.39% / 0.56% / -2.55%) [2026-07-29]
- IEF: 93.32 (-0.25% / 0.24% / -0.99%) [2026-07-29]
- GLD: 370.91 (0.42% / -2.17% / 0.69%) [2026-07-29]
- ^VIX: 19.54 (7.3% / 17.43% / 18.78%) [2026-07-29]
- BTC-USD: 64115.41 (0.38% / 0.03% / 1.46%) [2026-07-29]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.31 (delta 1m: 0.22) [2026-07-27]
- Treasury 10Y yield: 4.65 (delta 1m: 0.25) [2026-07-27]
- Curva 10Y-2Y: 0.35 (delta 1m: 0.04) [2026-07-28]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.84 (delta 1m: 0.04) [2026-07-28]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.2 (delta 1m: 0.0) [2026-07-28]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: leadership (4), stock (4), regulatory (1), earnings (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [MU] For India to become truly wealthy , people in Tier - 3 to Tier - 6 towns must get benefits of multi - sectoral growth : NCDEX CEO (2026-07-29)
- [MU] Most undervalued U . S . consumer discretionary stocks during Q2 earnings season ( XLY : NYSEARCA ) (2026-07-29)
- [CRWD] CrowdStrike ( CRWD ) Rides the AI Threat Wave , But Can It Lead the Pack ? (2026-07-29)
- [UTHR] United Therapeutics CEO Sells $5 Million of Shares . What Does This Mean for Investors ? (2026-07-28)
- [UTHR] United Therapeutics CEO Sells $5 Million of Shares . What Does This Mean for Investors ? (2026-07-28)
- [UTHR] Insider Selling : United Therapeutics ( NASDAQ : UTHR ) CEO Sells $5 , 038 , 990 . 00 in Stock (2026-07-28)
- [UTHR] Ardelyx ( NASDAQ : ARDX ) vs . United Therapeutics ( NASDAQ : UTHR ) Financial Survey (2026-07-27)
- [KMT] Kennametal Unveils Next Level Shop Experience for IMTS 2026 (2026-07-20)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner MSD CAPITAL, L.P. compro 5C Lending Partners Corp. por $31.0M el 2026-07-24.
- CEO Pacitti David vendio AVNS por $11.1M el 2026-07-27.
- 10% owner Market Technology Acquisition Sponsor LLC compro MTAK por $4.5M el 2026-07-27.
- 10% owner LIBERTY MUTUAL HOLDING Co INC. compro 5C Lending Partners Corp. por $8.2M el 2026-07-24.
- CFO ZHANG PINGTING compro STFS por $2.6M el 2026-07-22.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.

**Polymarket — smart money (traders con mejor track record):**

- MoistLotion · PnL $23,496 · win rate 98% · categorias: crypto, sports, economy
- esportGG · PnL $26,360 · win rate 95% · categorias: sports
- 0xE30E74595517de48f1FB19f4553dd3d9F1E96B87-1772612985000 · PnL $221,163 · win rate 83% · categorias: sports
- monkeymashingkeyboard · PnL $38,912 · win rate 92% · categorias: sports
- 0x5F659BcCBC353dBf7BcdffDEE73beE60bB482036-1780496231400 · PnL $36,406 · win rate 91% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 65 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 584 registros 30d · ultimo dato 2026-07-29
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-29
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, GLD, GSHD, HTFL, IEF, KRNY, MSTR, QQQ, SPCX, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **70.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
