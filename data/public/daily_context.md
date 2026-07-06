# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-06T16:47:05+00:00 · ventana señales 2026-06-06 -> 2026-07-06_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.91)
- Tendencia: `bull` (SPY 750.58 · MA50 736.73 · MA200 689.22 · dist MA200: 8.9%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 750.58 | 0.78% | 2.96% | -0.6% |
| QQQ | 11.4% | core | 724.01 | 1.6% | 2.48% | -2.13% |
| TLT | 11.4% | core | 85.3 | -0.25% | -2.0% | 0.13% |
| GLD | 8.6% | core | 380.77 | 0.7% | 1.91% | -7.42% |
| MFG | 7.8% | satellite | 10.3 | 3.58% | 6.03% | 5.16% |
| IEF | 5.7% | core | 94.09 | -0.03% | -0.66% | 0.3% |
| BABA | 5.5% | satellite | 97.48 | 1.39% | 2.82% | -21.89% |
| GH | 4.1% | satellite | 171.69 | 2.21% | 15.06% | 29.03% |
| NXDR | 3.9% | satellite | 2.34 | 2.18% | 5.41% | 8.84% |
| SMCI | 2.8% | satellite | 27.27 | 0.18% | -10.97% | -41.86% |
| CIFR | 2.2% | satellite | 22.25 | 11.03% | -14.23% | -12.92% |
| CALC | 1.7% | satellite | 0.92 | -4.88% | 12.49% | 7.86% |
| INDP | 1.2% | satellite | 2.72 | -10.23% | -20.23% | -42.74% |
| RYDE | 1.1% | satellite | 0.66 | -5.47% | 8.3% | -28.08% |
| ADTX | 0.7% | satellite | 0.0 | -18.0% | 105.0% | -94.68% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.7%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.9%
- Max drawdown historico: -13.0%
- Beta vs SPY: 0.856 · posiciones efectivas: 15.3 · HHI: 0.0653

**Por que estos satellite (señales WATCHDOG):**

- **MFG** · score agregado 758.0 · 13 señales · fuentes: corporate_insider
- **GH** · score agregado 715.2 · 12 señales · fuentes: corporate_insider
- **CIFR** · score agregado 629.0 · 10 señales · fuentes: corporate_insider
- **NXDR** · score agregado 297.0 · 5 señales · fuentes: corporate_insider
- **ADTX** · score agregado 280.5 · 4 señales · fuentes: large_holder
- **SMCI** · score agregado 277.4 · 5 señales · fuentes: corporate_insider
- **INDP** · score agregado 276.0 · 4 señales · fuentes: large_holder
- **BABA** · score agregado 228.0 · 4 señales · fuentes: corporate_insider
- **RYDE** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **CALC** · score agregado 208.5 · 3 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| APPN | 72 | large_holder | Lead Edge Capital Managem |  | - | - |
| SVRE | 72 | corporate_insider | VisionWave Holdings, Inc. | 0 | $1,135,938,816 | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| CTM | 70 | corporate_insider | Ives Glen R | 4 | $772 | cluster_buy,small_amount |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| DYAI | 70 | large_holder | Francisco Trust under agr |  | - | - |
| TDIC | 70 | large_holder | IMPERIAL VISION FUND SPC  |  | - | - |
| RAY | 70 | large_holder | HASH DIGITAL INVESTMENT L |  | - | - |
| RYDE | 70 | large_holder | HASH DIGITAL INVESTMENT L |  | - | - |
| RYDE | 70 | large_holder | HOYANG DEVELOPMENT LIMITE |  | - | - |
| TATT | 70 | large_holder | I.B.I. Investments House  |  | - | - |
| WILC | 70 | large_holder | MEITAV INVESTMENT HOUSE L |  | - | - |
| NINE | 70 | large_holder | Algebris Investments (US) |  | - | - |
| ALMR | 70 | large_holder | SHERPA HEALTHCARE FUND II |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MFG | 76 | corporate_insider | Take Hidekatsu | $336,166,416 | cluster_buy |
| MFG | 76 | corporate_insider | Kihara Masahiro | $3,230,401,438 | cluster_buy |
| MFG | 75 | corporate_insider | Akita Natsumi | $156,907,278 | cluster_buy |
| MFG | 75 | corporate_insider | Sugawara Masayuki | $215,227,947 | cluster_buy |
| MFG | 75 | corporate_insider | Matsuura Shuji | $122,982,192 | cluster_buy |
| MFG | 75 | corporate_insider | Kaminoyama Nobuhiro | $282,512,034 | cluster_buy |
| MFG | 75 | corporate_insider | Inomata Naoshi | $302,206,732 | cluster_buy |
| MFG | 74 | corporate_insider | Yonezawa Takefumi | $72,624,878 | cluster_buy |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 750.58 (0.78% / 2.96% / -0.6%) [2026-07-06]
- QQQ: 724.01 (1.6% / 2.48% / -2.13%) [2026-07-06]
- IWM: 300.18 (0.87% / 0.12% / 3.04%) [2026-07-06]
- DIA: 528.35 (0.09% / 2.05% / 2.53%) [2026-07-06]
- TLT: 85.3 (-0.25% / -2.0% / 0.13%) [2026-07-06]
- IEF: 94.09 (-0.03% / -0.66% / 0.3%) [2026-07-06]
- GLD: 380.77 (0.7% / 1.91% / -7.42%) [2026-07-06]
- ^VIX: 15.91 (-1.49% / -13.58% / 3.31%) [2026-07-06]
- BTC-USD: 63693.7 (0.23% / 6.15% / -2.91%) [2026-07-06]

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

_(sin noticias este ciclo — GDELT no disponible)_

**Actores que han movido ficha este mes (top movimientos):**

- Director VisionWave Holdings, Inc. compro SVRE por $1.1B el 2026-06-16.
- CEO Gilboa David Abraham vendio WRBY por $7.2M el 2026-07-01.
- CEO Blumenthal Neil Harris vendio WRBY por $6.4M el 2026-07-01.
- Director Take Hidekatsu vendio MFG por $336.2M el 2026-07-01.
- Director Kihara Masahiro vendio MFG por $3.2B el 2026-07-01.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $27.9B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $1,112,997 · win rate 88% · categorias: sports
- RJW1 · PnL $182,416 · win rate 99% · categorias: sports
- Sassy-Bucket · PnL $212,034 · win rate 91% · categorias: sports
- fgdfhr666 · PnL $74,132 · win rate 94% · categorias: sports
- 0x5966Db1fE50763C9e3C014d756369BAd07E1F804-1777648534241 · PnL $133,465 · win rate 90% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 389 registros 30d · ultimo dato 2026-07-03
- **sec_13d_13g**: `ok` · 247 registros 30d · ultimo dato 2026-07-06
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ADTX, BABA, CALC, CIFR, GH, GLD, IEF, INDP, MFG, NXDR, QQQ, RYDE, SMCI, SPY, TLT`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
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
