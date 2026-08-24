# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-24T07:36:23+00:00 · ventana señales 2026-07-25 -> 2026-08-24_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.91)
- Tendencia: `bull` (SPY 765.72 · MA50 751.56 · MA200 704.98 · dist MA200: 8.62%)
- Credito: `tight` (HY spread 2.75)
- Tipos: `steep` (curva 10y-2y 0.5)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.72 | 0.41% | -1.37% | 3.63% |
| QQQ | 12.0% | core | 713.44 | 0.35% | -2.41% | 4.27% |
| TLT | 12.0% | core | 82.05 | -0.35% | 0.01% | -1.04% |
| GLD | 9.3% | core | 423.36 | 1.95% | 5.45% | 13.84% |
| MED | 7.6% | satellite | 11.95 | 2.84% | 4.46% | 23.45% |
| GRNT | 7.0% | satellite | 5.11 | -1.35% | 0.0% | 5.36% |
| CART | 6.9% | satellite | 49.83 | -2.43% | 1.94% | 18.05% |
| IEF | 6.2% | core | 92.82 | -0.19% | -0.24% | 0.12% |
| CHTR | 5.2% | satellite | 150.17 | 1.63% | -2.66% | 21.78% |
| ELF | 4.7% | satellite | 101.94 | 3.53% | 11.48% | 31.77% |
| CBRS | 2.0% | satellite | 196.13 | -6.54% | -10.43% | -1.5% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.9%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.5%
- Max drawdown historico: -3.1%
- Beta vs SPY: 0.556 · posiciones efectivas: 13.1 · HHI: 0.0766

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 213.8 · 3 señales · fuentes: large_holder
- **MED** · score agregado 190.8 · 3 señales · fuentes: corporate_insider, large_holder
- **ELF** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GRNT** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **CBRS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **CART** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GWRS | 81 | corporate_insider | Levine Jonathan L | 2 | $5,766,819 | cluster_buy |
| INV | 80 | corporate_insider | Haskell Gregory W | 4 | $75,600 | cluster_buy |
| INV | 79 | corporate_insider | Otworth Michael | 4 | $349,295 | cluster_buy |
| INV | 79 | corporate_insider | Donnally James O | 4 | $337,500 | cluster_buy |
| GWRS | 78 | corporate_insider | Cohn Andrew M. | 2 | $1,233,186 | cluster_buy |
| IDAI | 78 | corporate_insider | Genner Gareth Neville | 3 | $28,558 | cluster_buy |
| INV | 75 | corporate_insider | Brown Bruce | 4 | $45,399 | cluster_buy |
| JCTC | 72 | large_holder | AJB Investment Fund II, L |  | - | - |
| MED | 72 | large_holder | Steamboat Capital Partner |  | - | - |
| CHTR | 72 | large_holder | Advance/Newhouse Partners |  | - | - |
| CHTR | 72 | large_holder | Ronald A. Duncan |  | - | - |
| GO | 72 | large_holder | Pertento Partners LLP |  | - | - |
| ELF | 72 | large_holder | Fenelon Opportunity Fund  |  | - | - |
| IDAI | 71 | corporate_insider | Genner Gareth Neville | 3 | $1,545 | cluster_buy,small_amount |
| IDAI | 71 | corporate_insider | Francis Andrew Scott | 3 | $4,960 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MDLZ | 58 | corporate_insider | Van de Put Dirk | $8,559,806 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $27,432,882 | - |
| HCC | 57 | corporate_insider | SCHELLER WALTER J | $5,250,000 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $24,899,013 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $24,128,863 | - |
| ILMN | 57 | corporate_insider | Meister Keith A. | $29,245,694 | - |
| CBRS | 57 | corporate_insider | Lie Sean | $22,534,734 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $4,491,084 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.72 (0.41% / -1.37% / 3.63%) [2026-08-21]
- QQQ: 713.44 (0.35% / -2.41% / 4.27%) [2026-08-21]
- IWM: 299.96 (0.77% / -1.68% / 3.02%) [2026-08-21]
- DIA: 532.22 (0.98% / -0.77% / 2.68%) [2026-08-21]
- TLT: 82.05 (-0.35% / 0.01% / -1.04%) [2026-08-21]
- IEF: 92.82 (-0.19% / -0.24% / 0.12%) [2026-08-21]
- GLD: 423.36 (1.95% / 5.45% / 13.84%) [2026-08-21]
- ^VIX: 15.91 (5.16% / 4.74% / -14.78%) [2026-08-24]
- BTC-USD: 77457.27 (-0.38% / 11.83% / 20.92%) [2026-08-24]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: -0.12) [2026-08-20]
- Treasury 10Y yield: 4.69 (delta 1m: 0.02) [2026-08-20]
- Curva 10Y-2Y: 0.5 (delta 1m: 0.16) [2026-08-21]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.75 (delta 1m: 0.07) [2026-08-20]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.06) [2026-08-21]
- Dolar broad index: 118.9028 (delta 1m: -1.428) [2026-08-14]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (9), leadership (2), regulatory (2), merger (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWV] Two Seas Capital LP Makes New Investment in CoreWeave Inc . $CRWV (2026-08-23)
- [ILMN] Evolve Private Wealth LLC Takes $1 . 86 Million Position in Illumina , Inc . $ILMN (2026-08-23)
- [CRWV] BCA Research Sees a Dangerous Risk in CoreWeave ( CRWV ) and Nebius ( NBIS ) (2026-08-23)
- [CRWV] CoreWeave CEO Michael Intrator Sold Over 13 , 000 Shares for $1 . 2 Million . What Does This Mean for Investors ? (2026-08-22)
- [LIFE] Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Major Shareholder Us ( Ttgp ) Ltd . Sc Sells 107 , 795 Shares of Stock (2026-08-22)
- [CBRS] Cerebras System ( CBRS ) Buy Rating Reiterated at Needham & Company LLC (2026-08-22)
- [LIFE] Lingke Wang Sells 118 , 333 Shares of Ethos Technologies Inc . Class A Common Stock ( NASDAQ : LIFE ) Stock (2026-08-21)
- [CBRS] Cerebras Systems ( NASDAQ : CBRS ) COO Dhiraj Mallick Sells 38 , 889 Shares of Stock (2026-08-21)
- [WBS] Deutsche Bank AG Buys Shares of 759 , 307 Webster Financial Corporation $WBS (2026-08-21)
- [ILMN] Christensen Jakob Wedel Sells 1 , 033 Shares of Illumina ( NASDAQ : ILMN ) Stock (2026-08-20)

**Actores que han movido ficha este mes (top movimientos):**

- Officer Lie Sean vendio CBRS por $27.4M el 2026-08-20 [senal en multiples fuentes].
- CEO MINICUCCI BENITO compro ALK por $1.0M el 2026-08-20.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.
- Institutional manager Geode Capital Management LLC vendio ELI LILLY & CO por $13.2B.

**Polymarket — smart money (traders con mejor track record):**

- SPCEXBUYER · PnL $46,574 · win rate 92% · categorias: sports
- rollobravado · PnL $13,472 · win rate 99% · categorias: sports, politics
- WhattDoyoumean · PnL $16,007 · win rate 93% · categorias: sports
- Donghui · PnL $12,036 · win rate 93% · categorias: sports
- torta.tech · PnL $7,356 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 679 registros 30d · ultimo dato 2026-08-21
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-21
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CART, CBRS, CHTR, ELF, GLD, GRNT, IEF, MED, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
