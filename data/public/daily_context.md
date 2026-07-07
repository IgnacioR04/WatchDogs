# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-07T15:31:19+00:00 · ventana señales 2026-06-07 -> 2026-07-07_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.49)
- Tendencia: `bull` (SPY 746.1 · MA50 737.54 · MA200 689.7 · dist MA200: 8.18%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 746.1 | -0.69% | 0.69% | 1.42% |
| QQQ | 11.4% | core | 707.15 | -2.17% | -2.34% | 0.41% |
| TLT | 11.4% | core | 84.89 | -0.66% | -2.57% | 0.17% |
| GLD | 8.6% | core | 380.16 | -0.52% | 3.14% | -4.06% |
| CWK | 6.1% | satellite | 14.06 | 1.99% | 2.37% | 5.2% |
| IEF | 5.7% | core | 93.93 | -0.26% | -0.86% | 0.67% |
| PUBM | 5.1% | satellite | 13.38 | -1.07% | 2.33% | 15.9% |
| TOST | 4.6% | satellite | 29.67 | 0.64% | 5.36% | 20.41% |
| INTU | 3.8% | satellite | 281.71 | 3.52% | 5.75% | -5.07% |
| JOBY | 3.2% | satellite | 8.1 | -9.25% | -6.2% | -15.24% |
| GTM | 2.7% | satellite | 3.04 | 3.58% | 3.94% | 1.85% |
| CDLX | 2.4% | satellite | 4.09 | -6.29% | -15.91% | -31.52% |
| ARQQ | 1.7% | satellite | 19.79 | -10.57% | -27.54% | 63.01% |
| ZSPC | 0.8% | satellite | 0.17 | -5.56% | -10.53% | -11.46% |
| FIRY | 0.5% | satellite | 9.55 | 0.84% | -6.83% | 13.29% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 14.8%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -6.4%
- Beta vs SPY: 0.757 · posiciones efectivas: 15.7 · HHI: 0.0637

**Por que estos satellite (señales WATCHDOG):**

- **INTU** · score agregado 1514.2 · 25 señales · fuentes: corporate_insider
- **ARQQ** · score agregado 1360.6 · 23 señales · fuentes: corporate_insider
- **TOST** · score agregado 1226.4 · 20 señales · fuentes: corporate_insider
- **JOBY** · score agregado 1097.6 · 18 señales · fuentes: corporate_insider
- **GTM** · score agregado 1081.0 · 18 señales · fuentes: corporate_insider
- **PUBM** · score agregado 366.6 · 6 señales · fuentes: corporate_insider
- **CWK** · score agregado 358.0 · 6 señales · fuentes: corporate_insider
- **CDLX** · score agregado 340.4 · 6 señales · fuentes: corporate_insider
- **ZSPC** · score agregado 292.0 · 5 señales · fuentes: corporate_insider
- **FIRY** · score agregado 288.2 · 5 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| QNT | 72 | large_holder | Capital World Investors |  | - | - |
| TOFB | 72 | large_holder | LPL Financial LLC |  | - | - |
| GWRE | 72 | large_holder | BAMCO INC /NY/ |  | - | - |
| SVRE | 72 | corporate_insider | VisionWave Holdings, Inc. | 0 | $1,135,938,816 | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| QTTB | 70 | large_holder | The Carlyle Group Inc. |  | - | - |
| DYAI | 70 | large_holder | Francisco Trust under agr |  | - | - |
| TDIC | 70 | large_holder | IMPERIAL VISION FUND SPC  |  | - | - |
| MRTN | 70 | large_holder | Nuance Investments LLC |  | - | - |
| HAL | 70 | large_holder | Capital Research Global I |  | - | - |
| WOLF | 70 | large_holder | Capital Research Global I |  | - | - |
| LFVN | 70 | large_holder | The Capital Management Co |  | - | - |
| TSQ | 70 | large_holder | The Capital Management Co |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PUBM | 72 | corporate_insider | Goel Rajeev K. | $687,257 | cluster_buy |
| TOST | 71 | corporate_insider | Narang Aman | $414,416 | cluster_buy |
| TOST | 71 | corporate_insider | Gomez Elena | $334,793 | cluster_buy |
| TOST | 70 | corporate_insider | Fredette Stephen | $263,853 | cluster_buy |
| ARQQ | 70 | corporate_insider | Leaver Andrew | $249,329 | cluster_buy |
| PUBM | 70 | corporate_insider | Goel Rajeev K. | $238,990 | cluster_buy |
| PUBM | 70 | corporate_insider | Pantelick Steven | $321,395 | cluster_buy |
| JOBY | 69 | corporate_insider | Bevirt JoeBen | $140,829 | cluster_buy |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 746.1 (-0.69% / 0.69% / 1.42%) [2026-07-07]
- QQQ: 707.15 (-2.17% / -2.34% / 0.41%) [2026-07-07]
- IWM: 296.76 (-0.72% / -0.74% / 5.62%) [2026-07-07]
- DIA: 527.69 (-0.45% / 1.15% / 3.81%) [2026-07-07]
- TLT: 84.89 (-0.66% / -2.57% / 0.17%) [2026-07-07]
- IEF: 93.93 (-0.26% / -0.86% / 0.67%) [2026-07-07]
- GLD: 380.16 (-0.52% / 3.14% / -4.06%) [2026-07-07]
- ^VIX: 16.49 (5.91% / -6.57% / -23.34%) [2026-07-07]
- BTC-USD: 63630.85 (-0.57% / 3.49% / -1.22%) [2026-07-07]

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

**Temas dominantes**: stock (3)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ARQQ] Patrick Willcocks Sells 2 , 009 Shares of Arqit Quantum ( NASDAQ : ARQQ ) Stock (2026-07-07)
- [ARQQ] Arqit Quantum ( NASDAQ : ARQQ ) Director Garth Ritchie Sells 439 Shares of Stock (2026-07-07)
- [ACVA] ACV Auctions ( ACVA ) Fell Despite Positive Structural Advantages (2026-06-29)
- [ARQQ] Arqit Quantum ( NASDAQ : ARQQ ) CRO Sells $177 , 528 . 96 in Stock (2026-06-24)

**Actores que han movido ficha este mes (top movimientos):**

- Director VisionWave Holdings, Inc. compro SVRE por $1.1B el 2026-06-16.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $27.9B.
- Institutional manager Vanguard Group Inc compro ELI LILLY & CO por $23.6B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.
- Institutional manager Geode Capital Management LLC compro JPMORGAN CHASE & CO por $13.1B.

**Polymarket — smart money (traders con mejor track record):**

- CandleHammerDrums · PnL $1,342,823 · win rate 96% · categorias: sports
- Oneger · PnL $515,166 · win rate 98% · categorias: sports
- R88N · PnL $147,790 · win rate 98% · categorias: sports
- 0x5966Db1fE50763C9e3C014d756369BAd07E1F804-1777648534241 · PnL $107,000 · win rate 90% · categorias: sports, crypto
- Jsram · PnL $397,813 · win rate 75% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 806 registros 30d · ultimo dato 2026-07-06
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-07
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ARQQ, CDLX, CWK, FIRY, GLD, GTM, IEF, INTU, JOBY, PUBM, QQQ, SPY, TLT, TOST, ZSPC`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
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
