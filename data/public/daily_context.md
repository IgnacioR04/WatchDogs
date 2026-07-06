# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-06T22:55:31+00:00 · ventana señales 2026-06-06 -> 2026-07-06_

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
| IEF | 5.7% | core | 94.18 | 0.06% | -0.57% | 0.39% |
| PUBM | 4.8% | satellite | 13.52 | -0.22% | 6.88% | 13.8% |
| VEEV | 4.7% | satellite | 192.01 | -0.38% | 12.05% | 7.51% |
| NXDR | 4.3% | satellite | 2.3 | 0.44% | 3.6% | 6.98% |
| INTU | 3.6% | satellite | 272.14 | -1.17% | 1.65% | -9.88% |
| W | 3.2% | satellite | 93.18 | -1.4% | -1.37% | 28.54% |
| JOBY | 3.1% | satellite | 8.92 | 5.06% | 1.02% | -19.93% |
| GTM | 2.5% | satellite | 2.93 | -2.01% | 1.38% | -3.3% |
| CIFR | 2.2% | satellite | 21.73 | 8.43% | -16.23% | -14.95% |
| ARQQ | 1.6% | satellite | 22.13 | -5.89% | -8.78% | 55.63% |
| ZSPC | 0.7% | satellite | 0.18 | -6.74% | 0.0% | -12.62% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 16.2%
- VaR 95% 1d: 1.6% · CVaR 95% 1d: 2.0%
- Max drawdown historico: -7.2%
- Beta vs SPY: 0.842 · posiciones efectivas: 16.1 · HHI: 0.0623

**Por que estos satellite (señales WATCHDOG):**

- **ARQQ** · score agregado 1360.6 · 23 señales · fuentes: corporate_insider
- **JOBY** · score agregado 1097.6 · 18 señales · fuentes: corporate_insider
- **GTM** · score agregado 1081.0 · 18 señales · fuentes: corporate_insider
- **W** · score agregado 541.2 · 9 señales · fuentes: corporate_insider
- **INTU** · score agregado 396.4 · 7 señales · fuentes: corporate_insider
- **PUBM** · score agregado 366.6 · 6 señales · fuentes: corporate_insider
- **CIFR** · score agregado 354.0 · 6 señales · fuentes: corporate_insider
- **VEEV** · score agregado 303.8 · 5 señales · fuentes: corporate_insider
- **NXDR** · score agregado 297.0 · 5 señales · fuentes: corporate_insider
- **ZSPC** · score agregado 292.0 · 5 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BBSI | 72 | large_holder | Private Capital Managemen |  | - | - |
| TOFB | 72 | large_holder | LPL Financial LLC |  | - | - |
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
| EVF | 70 | large_holder | Royal Bank of Canada |  | - | - |
| EVF | 70 | large_holder | Royal Bank of Canada |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PUBM | 72 | corporate_insider | Goel Rajeev K. | $687,257 | cluster_buy |
| INDI | 72 | corporate_insider | McClymont Donald | $563,072 | cluster_buy |
| ARQQ | 70 | corporate_insider | Leaver Andrew | $249,329 | cluster_buy |
| PUBM | 70 | corporate_insider | Goel Rajeev K. | $238,990 | cluster_buy |
| PUBM | 70 | corporate_insider | Pantelick Steven | $321,395 | cluster_buy |
| JOBY | 69 | corporate_insider | Bevirt JoeBen | $140,829 | cluster_buy |
| NUVL | 69 | corporate_insider | Balcom Alexandra | $1,412,519 | cluster_buy |
| PUBM | 69 | corporate_insider | Goel Rajeev K. | $118,150 | cluster_buy |

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
- BTC-USD: 64158.74 (0.96% / 6.92% / -2.2%) [2026-07-06]

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

**Temas dominantes**: regulatory (2), legal (1), ai (1), leadership (1), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [AVAV] AeroVironment , Inc . ( AVAV ) Shareholders Who Lost Money Have Opportunity to Lead Securities Fraud Lawsuit (2026-07-06)
- [AVAV] Lost Money on AeroVironment , Inc . ( AVAV )? Join Class Action Before ... (2026-07-05)
- [AVAV] Investors in AeroVironment , Inc . ( AVAV ): Protect Your Rights – Contact ... (2026-07-05)
- [AVAV] 2026 - 07 - 04 | AVAV DEADLINE ALERT : ROSEN , GLOBAL INVESTOR COUNSEL , Encourages AeroVironment , Inc . Investors With Losses in Excess of $100K to Secure Counsel Before Important Deadline in Securities Class Action - AVAV | NDAQ : AVAV (2026-07-05)
- [JOBY] Price Prediction : Joby Aviation High - Risk , High - Reward Path to 30 % Upside (2026-06-30)
- [JOBY] Joby & Toyota Launch Strategic Air Mobility Alliance (2026-06-30)
- [JOBY] Joby Aviation ( NYSE : JOBY ) vs . easyjet ( OTCMKTS : EJTTF ) Critical Comparison (2026-06-30)
- [PUBM] PubMatic ( NASDAQ : PUBM ) CEO Rajeev Goel Sells 43 , 077 Shares of Stock (2026-06-23)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Peter Warwick opero SCHL por $390.8M el 2026-07-01.
- CEO Gilboa David Abraham vendio WRBY por $7.2M el 2026-07-01.
- CEO Blumenthal Neil Harris vendio WRBY por $6.4M el 2026-07-01.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $27.9B.
- Institutional manager Vanguard Group Inc compro ELI LILLY & CO por $23.6B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.

**Polymarket — smart money (traders con mejor track record):**

- RJW1 · PnL $372,823 · win rate 99% · categorias: sports
- BreakTheBank · PnL $882,152 · win rate 88% · categorias: sports
- shijiebeifacai · PnL $160,312 · win rate 98% · categorias: sports
- Allezpapa · PnL $123,781 · win rate 99% · categorias: sports
- CandleHammerDrums · PnL $185,287 · win rate 96% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 673 registros 30d · ultimo dato 2026-07-06
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-06
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ARQQ, CIFR, GLD, GTM, IEF, INTU, JOBY, NXDR, PUBM, QQQ, SPY, TLT, VEEV, W, ZSPC`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
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
