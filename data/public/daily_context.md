# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-07T17:44:51+00:00 · ventana señales 2026-06-07 -> 2026-07-07_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.66)
- Tendencia: `bull` (SPY 749.09 · MA50 737.6 · MA200 689.71 · dist MA200: 8.61%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 749.09 | -0.29% | 1.09% | 1.83% |
| QQQ | 11.4% | core | 713.37 | -1.31% | -1.48% | 1.29% |
| TLT | 11.4% | core | 84.79 | -0.77% | -2.68% | 0.06% |
| GLD | 8.6% | core | 380.55 | -0.41% | 3.25% | -3.96% |
| CWK | 6.1% | satellite | 14.01 | 1.6% | 1.97% | 4.79% |
| IEF | 5.7% | core | 93.88 | -0.32% | -0.92% | 0.6% |
| PUBM | 5.1% | satellite | 13.5 | -0.18% | 3.25% | 16.94% |
| TOST | 4.6% | satellite | 29.95 | 1.59% | 6.36% | 21.55% |
| INTU | 3.8% | satellite | 282.58 | 3.84% | 6.07% | -4.78% |
| JOBY | 3.2% | satellite | 8.22 | -7.9% | -4.81% | -13.98% |
| GTM | 2.7% | satellite | 3.05 | 3.92% | 4.28% | 2.18% |
| CDLX | 2.4% | satellite | 4.31 | -1.37% | -11.5% | -27.93% |
| ARQQ | 1.7% | satellite | 20.31 | -8.22% | -25.63% | 67.3% |
| ZSPC | 0.8% | satellite | 0.17 | -5.5% | -10.47% | -11.41% |
| FIRY | 0.5% | satellite | 9.69 | 2.32% | -5.46% | 14.95% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 14.7%
- VaR 95% 1d: 1.4% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -6.4%
- Beta vs SPY: 0.756 · posiciones efectivas: 15.7 · HHI: 0.0637

**Por que estos satellite (señales WATCHDOG):**

- **ARQQ** · score agregado 1360.6 · 23 señales · fuentes: corporate_insider
- **TOST** · score agregado 1226.4 · 20 señales · fuentes: corporate_insider
- **JOBY** · score agregado 1097.6 · 18 señales · fuentes: corporate_insider
- **GTM** · score agregado 1081.0 · 18 señales · fuentes: corporate_insider
- **INTU** · score agregado 851.4 · 14 señales · fuentes: corporate_insider
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
| LIME | 70 | large_holder | Lunate Capital Limited |  | - | - |
| PBH | 70 | large_holder | Ariel Investments, LLC |  | - | - |
| HRI | 70 | large_holder | Invesco Ltd. |  | - | - |
| SKYQ | 70 | large_holder | JPMORGAN CHASE & CO |  | - | - |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| ARTW | 70 | large_holder | Walther Larry M |  | - | - |
| QTTB | 70 | large_holder | The Carlyle Group Inc. |  | - | - |
| DYAI | 70 | large_holder | Francisco Trust under agr |  | - | - |
| TDIC | 70 | large_holder | IMPERIAL VISION FUND SPC  |  | - | - |
| MRTN | 70 | large_holder | Nuance Investments LLC |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PUBM | 72 | corporate_insider | Goel Rajeev K. | $687,257 | cluster_buy |
| INDI | 72 | corporate_insider | McClymont Donald | $563,072 | cluster_buy |
| TOST | 71 | corporate_insider | Narang Aman | $414,416 | cluster_buy |
| TOST | 71 | corporate_insider | Gomez Elena | $334,793 | cluster_buy |
| TOST | 70 | corporate_insider | Fredette Stephen | $263,853 | cluster_buy |
| ARQQ | 70 | corporate_insider | Leaver Andrew | $249,329 | cluster_buy |
| PUBM | 70 | corporate_insider | Goel Rajeev K. | $238,990 | cluster_buy |
| PUBM | 70 | corporate_insider | Pantelick Steven | $321,395 | cluster_buy |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 749.09 (-0.29% / 1.09% / 1.83%) [2026-07-07]
- QQQ: 713.37 (-1.31% / -1.48% / 1.29%) [2026-07-07]
- IWM: 297.52 (-0.46% / -0.49% / 5.89%) [2026-07-07]
- DIA: 528.69 (-0.26% / 1.34% / 4.01%) [2026-07-07]
- TLT: 84.79 (-0.77% / -2.68% / 0.06%) [2026-07-07]
- IEF: 93.88 (-0.32% / -0.92% / 0.6%) [2026-07-07]
- GLD: 380.55 (-0.41% / 3.25% / -3.96%) [2026-07-07]
- ^VIX: 15.66 (0.58% / -11.27% / -27.2%) [2026-07-07]
- BTC-USD: 64144.45 (0.23% / 4.32% / -0.43%) [2026-07-07]

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

**Temas dominantes**: stock (10), regulatory (2), legal (2), ai (1), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [JOBY] Joby and Archer trade - secret battle inches along in federal court (2026-07-07)
- [JOBY] Joby Aviation Stock : Is It More Likely to Hit $15 or $5 This Year ? (2026-07-07)
- [AVAV] AeroVironment , Inc .: AV Awarded $30 Million Contract to Provide Puma Systems Stack for Germany LARUS Program (2026-07-07)
- [JOBY] Joby Aviation Stock : Is It More Likely to Hit $15 or $5 This Year ? (2026-07-07)
- [AVAV] Securities Fraud Class Action Filed Against AeroVironment , Inc . ( AVAV ) ... (2026-07-07)
- [AVAV] AVAV Class Action Reminder - Robbins LLP Is Investigating AeroVironment , Inc . Involvement in the U . S . Space Force SCAR Program (2026-07-07)
- [JOBY] Joby Aviation ( NYSE : JOBY ) Insider Sells 9 , 575 Shares of Stock (2026-07-07)
- [ARQQ] Patrick Willcocks Sells 2 , 009 Shares of Arqit Quantum ( NASDAQ : ARQQ ) Stock (2026-07-07)
- [JOBY] Insider Selling : Joby Aviation ( NYSE : JOBY ) Insider Sells 7 , 832 Shares (2026-07-07)
- [ARQQ] Arqit Quantum ( NASDAQ : ARQQ ) Director Garth Ritchie Sells 439 Shares of Stock (2026-07-07)

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

- CandleHammerDrums · PnL $1,216,245 · win rate 96% · categorias: sports
- Oneger · PnL $506,496 · win rate 98% · categorias: sports
- RJW1 · PnL $126,687 · win rate 99% · categorias: sports
- R88N · PnL $152,830 · win rate 98% · categorias: sports
- 0x5966Db1fE50763C9e3C014d756369BAd07E1F804-1777648534241 · PnL $107,000 · win rate 90% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 72 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 789 registros 30d · ultimo dato 2026-07-06
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
