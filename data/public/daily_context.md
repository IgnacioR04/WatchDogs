# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-06T13:17:23+00:00 · ventana señales 2026-06-06 -> 2026-07-06_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.37)
- Tendencia: `bull` (SPY 744.78 · MA50 735.91 · MA200 688.74 · dist MA200: 8.14%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 744.78 | -0.13% | 1.43% | -1.0% |
| QQQ | 11.4% | core | 712.6 | -1.73% | -0.53% | -4.14% |
| TLT | 11.4% | core | 85.51 | -0.01% | -1.74% | 0.6% |
| GLD | 8.6% | core | 378.13 | 2.03% | 2.35% | -7.29% |
| BBSI | 6.8% | satellite | 37.91 | 0.48% | 11.47% | 17.26% |
| IBM | 6.0% | satellite | 289.52 | 1.14% | 12.1% | -5.27% |
| IEF | 5.7% | core | 94.12 | 0.1% | -0.38% | 0.46% |
| GH | 4.1% | satellite | 167.98 | -1.63% | 17.52% | 32.24% |
| NXDR | 4.0% | satellite | 2.29 | -1.72% | 8.02% | 13.37% |
| SMCI | 2.8% | satellite | 27.22 | -1.56% | -14.08% | -42.6% |
| CIFR | 2.2% | satellite | 20.04 | -12.26% | -21.96% | -23.63% |
| FEAM | 2.1% | satellite | 1.37 | -4.86% | 4.58% | -21.71% |
| INDP | 1.2% | satellite | 3.03 | 3.06% | -7.06% | 37.1% |
| RYDE | 1.1% | satellite | 0.7 | 7.53% | 6.06% | -11.5% |
| ADTX | 0.7% | satellite | 0.0 | 0.0% | 150.0% | -94.74% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.3%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 1.8%
- Max drawdown historico: -12.7%
- Beta vs SPY: 0.815 · posiciones efectivas: 15.5 · HHI: 0.0647

**Por que estos satellite (señales WATCHDOG):**

- **GH** · score agregado 715.2 · 12 señales · fuentes: corporate_insider
- **FEAM** · score agregado 708.0 · 12 señales · fuentes: corporate_insider
- **CIFR** · score agregado 629.0 · 10 señales · fuentes: corporate_insider
- **SMCI** · score agregado 415.4 · 7 señales · fuentes: corporate_insider
- **NXDR** · score agregado 297.0 · 5 señales · fuentes: corporate_insider
- **ADTX** · score agregado 280.5 · 4 señales · fuentes: large_holder
- **INDP** · score agregado 276.0 · 4 señales · fuentes: large_holder
- **BBSI** · score agregado 236.0 · 4 señales · fuentes: corporate_insider
- **RYDE** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **IBM** · score agregado 210.0 · 4 señales · fuentes: congress, corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| APPN | 72 | large_holder | Lead Edge Capital Managem |  | - | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| CTM | 70 | corporate_insider | Ives Glen R | 4 | $772 | cluster_buy,small_amount |
| DYAI | 70 | large_holder | Francisco Trust under agr |  | - | - |
| TDIC | 70 | large_holder | IMPERIAL VISION FUND SPC  |  | - | - |
| RAY | 70 | large_holder | HASH DIGITAL INVESTMENT L |  | - | - |
| RYDE | 70 | large_holder | HASH DIGITAL INVESTMENT L |  | - | - |
| RYDE | 70 | large_holder | HOYANG DEVELOPMENT LIMITE |  | - | - |
| WILC | 70 | large_holder | MEITAV INVESTMENT HOUSE L |  | - | - |
| NINE | 70 | large_holder | Algebris Investments (US) |  | - | - |
| ALMR | 70 | large_holder | SHERPA HEALTHCARE FUND II |  | - | - |
| PSBD | 70 | large_holder | Alaris Master Fund LP |  | - | - |
| SUNE | 70 | large_holder | JANE STREET GROUP, LLC |  | - | - |
| MSGM | 70 | large_holder | Red Oak Partners, LLC |  | - | - |
| ZBAO | 70 | large_holder | Ningbo Pangu Chuangfu Hef |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| STEM | 64 | corporate_insider | Narayanan Arun | $15,669 | cluster_buy,small_amount |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| AESI | 64 | congress | Chip Roy | $250,000 | - |
| IBM | 64 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| STEM | 63 | corporate_insider | Carlson Michael James | $10,574 | cluster_buy,small_amount |
| STEM | 63 | corporate_insider | Tappin Matthew | $7,819 | cluster_buy,small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 744.78 (-0.13% / 1.43% / -1.0%) [2026-07-02]
- QQQ: 712.6 (-1.73% / -0.53% / -4.14%) [2026-07-02]
- IWM: 297.58 (-0.58% / -0.44% / 3.69%) [2026-07-02]
- DIA: 527.88 (1.05% / 1.66% / 4.14%) [2026-07-02]
- TLT: 85.51 (-0.01% / -1.74% / 0.6%) [2026-07-02]
- IEF: 94.12 (0.1% / -0.38% / 0.46%) [2026-07-02]
- GLD: 378.13 (2.03% / 2.35% / -7.29%) [2026-07-02]
- ^VIX: 16.37 (1.36% / -11.08% / 6.3%) [2026-07-06]
- BTC-USD: 61524.83 (-3.18% / 2.53% / -6.21%) [2026-07-06]

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

**Temas dominantes**: ai (1), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [BLK] Standard Chartered , BlackRock launch Asia Pacific - focused multi - asset fund (2026-07-06)
- [BLK] AI Biggest Challenge Is Power , Says BlackRock CEO Larry Fink (2026-07-06)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Gilboa David Abraham vendio WRBY por $7.2M el 2026-07-01.
- CEO Blumenthal Neil Harris vendio WRBY por $6.4M el 2026-07-01.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $27.9B.
- Institutional manager Vanguard Group Inc compro ELI LILLY & CO por $23.6B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $1,082,997 · win rate 88% · categorias: sports
- RJW1 · PnL $169,889 · win rate 99% · categorias: sports
- Sassy-Bucket · PnL $212,034 · win rate 91% · categorias: sports
- 0x5966Db1fE50763C9e3C014d756369BAd07E1F804-1777648534241 · PnL $133,465 · win rate 90% · categorias: sports, crypto
- fgdfhr666 · PnL $73,187 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 401 registros 30d · ultimo dato 2026-07-02
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-06
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ADTX, BBSI, CIFR, FEAM, GH, GLD, IBM, IEF, INDP, NXDR, QQQ, RYDE, SMCI, SPY, TLT`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
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
