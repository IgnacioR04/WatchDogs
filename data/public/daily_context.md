# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-06T19:21:58+00:00 · ventana señales 2026-06-06 -> 2026-07-06_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.67)
- Tendencia: `bull` (SPY 752.22 · MA50 736.77 · MA200 689.23 · dist MA200: 9.14%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 752.22 | 1.0% | 3.19% | -0.39% |
| QQQ | 11.4% | core | 724.85 | 1.72% | 2.59% | -2.02% |
| TLT | 11.4% | core | 85.36 | -0.17% | -1.92% | 0.21% |
| GLD | 8.6% | core | 381.98 | 1.02% | 2.23% | -7.12% |
| BBSI | 7.0% | satellite | 37.71 | -0.53% | 4.58% | 16.03% |
| MFG | 6.7% | satellite | 10.34 | 3.97% | 6.44% | 5.57% |
| IEF | 5.7% | core | 94.13 | 0.01% | -0.62% | 0.34% |
| BABA | 5.2% | satellite | 97.65 | 1.58% | 3.0% | -21.75% |
| SMCI | 2.7% | satellite | 26.93 | -1.07% | -12.08% | -42.58% |
| CSIQ | 2.4% | satellite | 15.19 | 5.01% | -1.33% | -22.01% |
| CRWV | 2.1% | satellite | 85.96 | 5.15% | -11.0% | -20.43% |
| CWBHF | 1.7% | satellite | 0.32 | -2.14% | 2.89% | -23.26% |
| INDP | 1.2% | satellite | 2.75 | -9.24% | -19.35% | -42.11% |
| RYDE | 1.1% | satellite | 0.62 | -11.34% | 1.57% | -32.54% |
| ADTX | 0.7% | satellite | 0.0 | -10.0% | 125.0% | -94.16% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 14.8%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 2.1%
- Max drawdown historico: -10.0%
- Beta vs SPY: 0.683 · posiciones efectivas: 15.2 · HHI: 0.0656

**Por que estos satellite (señales WATCHDOG):**

- **MFG** · score agregado 758.0 · 13 señales · fuentes: corporate_insider
- **BBSI** · score agregado 568.0 · 10 señales · fuentes: corporate_insider
- **CRWV** · score agregado 542.8 · 9 señales · fuentes: corporate_insider
- **SMCI** · score agregado 512.4 · 9 señales · fuentes: corporate_insider
- **INDP** · score agregado 276.0 · 4 señales · fuentes: large_holder
- **CWBHF** · score agregado 240.0 · 4 señales · fuentes: corporate_insider
- **CSIQ** · score agregado 236.0 · 4 señales · fuentes: corporate_insider
- **BABA** · score agregado 228.0 · 4 señales · fuentes: corporate_insider
- **RYDE** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **ADTX** · score agregado 210.0 · 3 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SVRE | 72 | corporate_insider | VisionWave Holdings, Inc. | 0 | $1,135,938,816 | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| DYAI | 70 | large_holder | Francisco Trust under agr |  | - | - |
| TDIC | 70 | large_holder | IMPERIAL VISION FUND SPC  |  | - | - |
| MRTN | 70 | large_holder | Nuance Investments LLC |  | - | - |
| HAL | 70 | large_holder | Capital Research Global I |  | - | - |
| WOLF | 70 | large_holder | Capital Research Global I |  | - | - |
| LFVN | 70 | large_holder | The Capital Management Co |  | - | - |
| TSQ | 70 | large_holder | The Capital Management Co |  | - | - |
| RAY | 70 | large_holder | HASH DIGITAL INVESTMENT L |  | - | - |
| RYDE | 70 | large_holder | HASH DIGITAL INVESTMENT L |  | - | - |
| RYDE | 70 | large_holder | HOYANG DEVELOPMENT LIMITE |  | - | - |
| TATT | 70 | large_holder | I.B.I. Investments House  |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| CRWV | 78 | corporate_insider | Intrator Michael N | $7,517,406 | cluster_buy |
| CRWV | 78 | corporate_insider | Intrator Michael N | $7,495,165 | cluster_buy |
| CRWV | 77 | corporate_insider | Intrator Michael N | $4,652,706 | cluster_buy |
| CRWV | 76 | corporate_insider | Intrator Michael N | $4,135,335 | cluster_buy |
| CRWV | 76 | corporate_insider | Intrator Michael N | $4,035,866 | cluster_buy |
| MFG | 76 | corporate_insider | Take Hidekatsu | $336,166,416 | cluster_buy |
| MFG | 76 | corporate_insider | Kihara Masahiro | $3,230,401,438 | cluster_buy |
| CRWV | 75 | corporate_insider | Intrator Michael N | $2,505,319 | cluster_buy |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 752.22 (1.0% / 3.19% / -0.39%) [2026-07-06]
- QQQ: 724.85 (1.72% / 2.59% / -2.02%) [2026-07-06]
- IWM: 299.29 (0.57% / -0.18% / 2.74%) [2026-07-06]
- DIA: 529.24 (0.26% / 2.22% / 2.71%) [2026-07-06]
- TLT: 85.36 (-0.17% / -1.92% / 0.21%) [2026-07-06]
- IEF: 94.13 (0.01% / -0.62% / 0.34%) [2026-07-06]
- GLD: 381.98 (1.02% / 2.23% / -7.12%) [2026-07-06]
- ^VIX: 15.67 (-2.97% / -14.88% / 1.75%) [2026-07-06]
- BTC-USD: 63803.29 (0.4% / 6.33% / -2.74%) [2026-07-06]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.17 (delta 1m: 0.12) [2026-07-01]
- Treasury 10Y yield: 4.48 (delta 1m: 0.01) [2026-07-01]
- Curva 10Y-2Y: 0.35 (delta 1m: -0.06) [2026-07-02]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.75 (delta 1m: 0.0) [2026-07-02]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.23 (delta 1m: -0.16) [2026-07-02]
- Dolar broad index: 120.8866 (delta 1m: 1.704) [2026-06-26]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWV] Should You Buy the Dip in CoreWeave Stock ? (2026-07-06)
- [CRWV] CoreWeave ( CRWV ) Launches AI - Enabled Research Agent , ARIA (2026-07-06)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Senior Loan Trust por $24.0M el 2026-06-30.
- CEO ARCHER TIMOTHY vendio LRCX por $11.7M el 2026-07-02 [senal en multiples fuentes].
- Director VisionWave Holdings, Inc. compro SVRE por $1.1B el 2026-06-16.
- CEO Volozh Arkadiy vendio NBIS por $11.0M el 2026-07-01.
- Director Take Hidekatsu vendio MFG por $336.2M el 2026-07-01.
- Director Kihara Masahiro vendio MFG por $3.2B el 2026-07-01.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $1,120,384 · win rate 88% · categorias: sports
- RJW1 · PnL $176,244 · win rate 99% · categorias: sports
- Sassy-Bucket · PnL $212,034 · win rate 91% · categorias: sports
- fgdfhr666 · PnL $76,458 · win rate 94% · categorias: sports
- 0x5966Db1fE50763C9e3C014d756369BAd07E1F804-1777648534241 · PnL $133,465 · win rate 90% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 468 registros 30d · ultimo dato 2026-07-06
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-06
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ADTX, BABA, BBSI, CRWV, CSIQ, CWBHF, GLD, IEF, INDP, MFG, QQQ, RYDE, SMCI, SPY, TLT`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
3. **Peso maximo por posicion**: <= **12.0%**.
4. **Sin apalancamiento y sin cortos**: todos los pesos >= 0, suma <= 1.
5. **Justifica cada cambio** con una razon concreta basada en los datos de este briefing (señal, regimen, riesgo, precio). Nada de datos externos.

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
