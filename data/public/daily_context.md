# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-06T21:18:51+00:00 · ventana señales 2026-06-06 -> 2026-07-06_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.57)
- Tendencia: `bull` (SPY 751.28 · MA50 736.75 · MA200 689.23 · dist MA200: 9.0%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 751.28 | 0.87% | 3.06% | -0.51% |
| QQQ | 11.4% | core | 722.82 | 1.43% | 2.31% | -2.29% |
| TLT | 11.4% | core | 85.45 | -0.07% | -1.83% | 0.31% |
| GLD | 8.6% | core | 382.13 | 1.06% | 2.27% | -7.09% |
| MFG | 6.7% | satellite | 10.35 | 4.12% | 6.59% | 5.72% |
| BBSI | 5.9% | satellite | 37.61 | -0.79% | 4.3% | 15.72% |
| IEF | 5.7% | core | 94.18 | 0.06% | -0.57% | 0.39% |
| GH | 3.5% | satellite | 168.82 | 0.5% | 13.13% | 26.88% |
| NXDR | 3.4% | satellite | 2.3 | 0.44% | 3.6% | 6.98% |
| GTM | 3.3% | satellite | 2.93 | -2.01% | 1.38% | -3.3% |
| SMCI | 2.4% | satellite | 27.19 | -0.11% | -11.23% | -42.03% |
| CSIQ | 2.2% | satellite | 15.15 | 4.77% | -1.56% | -22.19% |
| ARQQ | 1.8% | satellite | 22.13 | -5.89% | -8.78% | 55.63% |
| INDP | 1.0% | satellite | 2.85 | -5.94% | -16.42% | -40.0% |
| ADTX | 0.6% | satellite | 0.0 | -12.0% | 120.0% | -94.29% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.6%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -12.6%
- Beta vs SPY: 0.828 · posiciones efectivas: 15.6 · HHI: 0.0642

**Por que estos satellite (señales WATCHDOG):**

- **GTM** · score agregado 1018.0 · 17 señales · fuentes: corporate_insider
- **GH** · score agregado 715.2 · 12 señales · fuentes: corporate_insider
- **MFG** · score agregado 583.0 · 10 señales · fuentes: corporate_insider
- **ARQQ** · score agregado 333.6 · 6 señales · fuentes: corporate_insider
- **NXDR** · score agregado 297.0 · 5 señales · fuentes: corporate_insider
- **ADTX** · score agregado 280.5 · 4 señales · fuentes: large_holder
- **SMCI** · score agregado 277.4 · 5 señales · fuentes: corporate_insider
- **INDP** · score agregado 276.0 · 4 señales · fuentes: large_holder
- **BBSI** · score agregado 248.8 · 4 señales · fuentes: corporate_insider, large_holder
- **CSIQ** · score agregado 236.0 · 4 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BBSI | 72 | large_holder | Private Capital Managemen |  | - | - |
| APPN | 72 | large_holder | Lead Edge Capital Managem |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| CTM | 70 | corporate_insider | Ives Glen R | 4 | $772 | cluster_buy,small_amount |
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

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MFG | 76 | corporate_insider | Take Hidekatsu | $336,166,416 | cluster_buy |
| MFG | 76 | corporate_insider | Kihara Masahiro | $3,230,401,438 | cluster_buy |
| MFG | 75 | corporate_insider | Sugawara Masayuki | $215,227,947 | cluster_buy |
| MFG | 75 | corporate_insider | Matsuura Shuji | $122,982,192 | cluster_buy |
| MFG | 75 | corporate_insider | Kaminoyama Nobuhiro | $282,512,034 | cluster_buy |
| MFG | 75 | corporate_insider | Inomata Naoshi | $302,206,732 | cluster_buy |
| MFG | 74 | corporate_insider | Yonezawa Takefumi | $72,624,878 | cluster_buy |
| MFG | 74 | corporate_insider | Yagi Minako | $72,624,878 | cluster_buy |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 751.28 (0.87% / 3.06% / -0.51%) [2026-07-06]
- QQQ: 722.82 (1.43% / 2.31% / -2.29%) [2026-07-06]
- IWM: 298.9 (0.44% / -0.31% / 2.6%) [2026-07-06]
- DIA: 530.09 (0.42% / 2.38% / 2.87%) [2026-07-06]
- TLT: 85.45 (-0.07% / -1.83% / 0.31%) [2026-07-06]
- IEF: 94.18 (0.06% / -0.57% / 0.39%) [2026-07-06]
- GLD: 382.13 (1.06% / 2.27% / -7.09%) [2026-07-06]
- ^VIX: 15.57 (-3.59% / -15.43% / 1.1%) [2026-07-06]
- BTC-USD: 64198.77 (1.02% / 6.99% / -2.14%) [2026-07-06]

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

**Temas dominantes**: stock (5), legal (4), ai (3), regulatory (3)

**Titulares recientes (GDELT, tickers con mas señales):**

- [GTM] 2026 - 06 - 30 | GTM Breaking News : ZoomInfo Technologies Inc . Sued for Securities Fraud after AI Integration Issues Lead to a 33 % Stock Drop - Investors Notified to Contact BFA Law | NDAQ : GTM (2026-06-30)
- [GTM] Bronstein , Gewirtz & Grossman LLC Urges ZoomInfo Technologies Inc . Investors to Act : Class Action Filed Alleging Investor Harm (2026-06-30)
- [GTM] GTM Stockholder Alert : Shareholder Rights Law Firm Robbins LLP Reminds Investors of the Securities Class Action Lawsuit Against ZoomInfo Technologies Inc . (2026-06-29)
- [GTM] GTM Stockholder Alert : Shareholder Rights Law Firm Robbins LLP Reminds Investors of the Securities Class Action Lawsuit Against ZoomInfo Technologies Inc . (2026-06-29)
- [ACVA] ACV Auctions ( ACVA ) Fell Despite Positive Structural Advantages (2026-06-29)
- [GTM] 2026 - 06 - 26 | Investor Notice : Robbins LLP Informs Investors of the ZoomInfo Technologies Inc . Class Action Lawsuit | NDAQ : GTM (2026-06-27)
- [GTM] ZoomInfo Technologies ( NASDAQ : GTM ) Shares Up 8 . 2 % – Time to Buy ? (2026-06-26)
- [GH] Insider Selling : Guardant Health ( NASDAQ : GH ) Director Sells $204 , 084 . 96 in Stock (2026-06-24)

**Actores que han movido ficha este mes (top movimientos):**

- Director Take Hidekatsu vendio MFG por $336.2M el 2026-07-01.
- Director Kihara Masahiro vendio MFG por $3.2B el 2026-07-01.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $27.9B.
- Institutional manager Vanguard Group Inc compro ELI LILLY & CO por $23.6B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $1,438,502 · win rate 88% · categorias: sports
- RJW1 · PnL $141,170 · win rate 99% · categorias: sports
- Sassy-Bucket · PnL $212,034 · win rate 91% · categorias: sports
- fgdfhr666 · PnL $89,884 · win rate 94% · categorias: sports
- 0x5966Db1fE50763C9e3C014d756369BAd07E1F804-1777648534241 · PnL $133,465 · win rate 90% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 562 registros 30d · ultimo dato 2026-07-06
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-06
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ADTX, ARQQ, BBSI, CSIQ, GH, GLD, GTM, IEF, INDP, MFG, NXDR, QQQ, SMCI, SPY, TLT`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
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
