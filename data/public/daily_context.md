# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-10T19:00:55+00:00 · ventana señales 2026-06-10 -> 2026-07-10_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.29)
- Tendencia: `bull` (SPY 754.52 · MA50 739.9 · MA200 691.09 · dist MA200: 9.18%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.38)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 754.52 | 0.37% | 1.31% | 4.28% |
| QQQ | 12.0% | core | 725.5 | 0.31% | 1.81% | 4.7% |
| TLT | 12.0% | core | 84.38 | -0.14% | -1.33% | -0.23% |
| GLD | 9.3% | core | 376.26 | -0.51% | -0.49% | 0.45% |
| BEP | 7.3% | satellite | 32.22 | -2.3% | -4.9% | -8.65% |
| IEF | 6.2% | core | 93.61 | -0.11% | -0.55% | 0.24% |
| NMM | 5.5% | satellite | 75.52 | 2.37% | 4.2% | 4.71% |
| AVO | 5.0% | satellite | 13.4 | 0.41% | 7.33% | 19.26% |
| ENR | 4.5% | satellite | 20.7 | 2.42% | -4.83% | 6.7% |
| GGAL | 3.8% | satellite | 53.56 | 8.43% | 6.32% | 7.93% |
| WRBY | 2.5% | satellite | 28.9 | -1.43% | -1.23% | 15.51% |
| NTSK | 2.5% | satellite | 12.19 | -1.81% | 4.14% | 43.98% |
| INTC | 2.3% | satellite | 109.93 | -2.32% | -8.66% | 2.7% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.1%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 1.7%
- Max drawdown historico: -7.1%
- Beta vs SPY: 0.761 · posiciones efectivas: 13.9 · HHI: 0.0719

**Por que estos satellite (señales WATCHDOG):**

- **GGAL** · score agregado 236.8 · 4 señales · fuentes: corporate_insider
- **AVO** · score agregado 206.1 · 3 señales · fuentes: corporate_insider, large_holder
- **NMM** · score agregado 174.2 · 3 señales · fuentes: corporate_insider
- **ENR** · score agregado 126.1 · 2 señales · fuentes: corporate_insider
- **WRBY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **NTSK** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **INTC** · score agregado 70.7 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| EWSB | 84 | corporate_insider | Schmalz Charles D | 5 | $591,410 | cluster_buy |
| UUUU | 81 | corporate_insider | Bhappu Ross R. | 2 | $967,920 | cluster_buy |
| BBASX | 81 | corporate_insider | AMG New York Holdings Cor | 2 | $1,826,012 | cluster_buy |
| EWSB | 80 | corporate_insider | Schmalz Charles D | 5 | $85,000 | cluster_buy |
| EWSB | 80 | corporate_insider | Mangold James E | 5 | $399,500 | cluster_buy |
| EWSB | 80 | corporate_insider | Schneider Kory J | 5 | $328,600 | cluster_buy |
| WRAP | 78 | corporate_insider | Cohen Scot | 2 | $230,288 | cluster_buy |
| EWSB | 78 | corporate_insider | Schneider Kory J | 5 | $150,400 | cluster_buy |
| BBASX | 78 | corporate_insider | BROWN BROTHERS HARRIMAN C | 2 | $456,503 | cluster_buy |
| EWSB | 76 | corporate_insider | Vander Loop Kailee | 5 | $76,400 | cluster_buy |
| EWSB | 76 | corporate_insider | Vander Loop Kailee | 5 | $60,400 | cluster_buy |
| TSM | 76 | corporate_insider | Wei Che-Chia | 31 | $11,187 | cluster_buy,small_amount |
| WRAP | 73 | corporate_insider | Cohen Scot | 2 | $23,914 | cluster_buy,small_amount |
| EWSB | 73 | corporate_insider | Vander Loop Kailee | 5 | $15,000 | cluster_buy,small_amount |
| WRAP | 73 | corporate_insider | SHULMAN JOHN D | 2 | $110,000 | cluster_buy |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AMZN | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| AAPL | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| XOM | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |
| GE | 63 | congress | Matthew Robert Van Epps | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 754.52 (0.37% / 1.31% / 4.28%) [2026-07-10]
- QQQ: 725.5 (0.31% / 1.81% / 4.7%) [2026-07-10]
- IWM: 295.89 (-0.45% / -0.57% / 5.16%) [2026-07-10]
- DIA: 526.1 (0.37% / -0.34% / 5.46%) [2026-07-10]
- TLT: 84.38 (-0.14% / -1.33% / -0.23%) [2026-07-10]
- IEF: 93.61 (-0.11% / -0.55% / 0.24%) [2026-07-10]
- GLD: 376.26 (-0.51% / -0.49% / 0.45%) [2026-07-10]
- ^VIX: 15.29 (-3.47% / -5.33% / -31.19%) [2026-07-10]
- BTC-USD: 63756.97 (0.89% / 0.33% / -0.75%) [2026-07-10]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.21 (delta 1m: 0.04) [2026-07-08]
- Treasury 10Y yield: 4.56 (delta 1m: 0.01) [2026-07-08]
- Curva 10Y-2Y: 0.38 (delta 1m: -0.03) [2026-07-09]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.08) [2026-07-08]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.23 (delta 1m: -0.12) [2026-07-09]
- Dolar broad index: 120.6902 (delta 1m: 1.654) [2026-07-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (8), merger (5), regulatory (4), ai (3), leadership (1), legal (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TBRG] IKS Health Buys TruBridge (2026-07-10)
- [UTHR] Bank of America Issues Pessimistic Forecast for United Therapeutics ( NASDAQ : UTHR ) Stock Price (2026-07-10)
- [TSM] A Potential New Rival Wants to Undercut TSMC . Here What Investors Need to Know . (2026-07-10)
- [CRCL] Circle Internet Group shares rise as company receives approval to establish national trust bank (2026-07-10)
- [TBRG] IKS Health Completes Acquisition of TruBridge - The HinduBusinessLine (2026-07-10)
- [TBRG] IKS Health Completes Acquisition of TruBridge (2026-07-10)
- [IOT] Samsara ( NYSE : IOT ) Insider John Bicket Sells 17 , 975 Shares of Stock (2026-07-10)
- [TBRG] IKS Health Completes Acquisition of TruBridge (2026-07-10)
- [RKLB] Rocket Lab Bull - Case Target Set at $293 by Morgan Stanley (2026-07-10)
- [UTHR] Martine Rothblatt Sells 9 , 500 Shares of United Therapeutics ( NASDAQ : UTHR ) Stock (2026-07-09)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Beck Peter vendio RKLB por $38.7M el 2026-07-07.
- 10% owner Globalharvest Holdings Venture Ltd compro AVO por $9.2M el 2026-07-08 [senal en multiples fuentes].
- CEO Beck Peter vendio RKLB por $29.2M el 2026-07-08.
- 10% owner Globalharvest Holdings Venture Ltd compro AVO por $6.6M el 2026-07-07 [senal en multiples fuentes].
- CEO Beck Peter vendio RKLB por $19.8M el 2026-07-06.
- CEO Wohlin Hakan compro VII por $3.0M el 2026-07-06.
- CEO Tenev Vladimir vendio HOOD por $13.6M el 2026-07-06.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- Sassy-Bucket · PnL $392,530 · win rate 92% · categorias: sports
- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $182,923 · win rate 97% · categorias: sports
- 0x30353403430dadnm76fes8ma3 · PnL $33,751 · win rate 90% · categorias: sports
- waterx- · PnL $25,405 · win rate 91% · categorias: crypto, sports
- MeiGuNiuBi · PnL $121,335 · win rate 80% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 91 registros 30d · ultimo dato 2026-07-07
- **sec_insiders**: `ok` · 846 registros 30d · ultimo dato 2026-07-10
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-10
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AVO, BEP, ENR, GGAL, GLD, IEF, INTC, NMM, NTSK, QQQ, SPY, TLT, WRBY`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
