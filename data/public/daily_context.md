# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-25T19:17:21+00:00 · ventana señales 2026-07-26 -> 2026-08-25_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.44)
- Tendencia: `bull` (SPY 765.11 · MA50 752.62 · MA200 705.92 · dist MA200: 8.39%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.11 | 0.21% | -0.3% | 3.27% |
| QQQ | 12.0% | core | 709.67 | 0.47% | -1.09% | 5.06% |
| TLT | 12.0% | core | 83.38 | 0.99% | 2.11% | -0.62% |
| DGICA | 11.8% | satellite | 19.06 | 0.42% | 2.42% | 0.25% |
| GLD | 9.3% | core | 427.8 | 0.26% | 7.34% | 15.82% |
| IEF | 6.2% | core | 93.45 | 0.47% | 0.56% | 0.23% |
| CHTR | 5.2% | satellite | 155.5 | 3.46% | 4.82% | 11.1% |
| AMR | 4.8% | satellite | 209.23 | -0.33% | 23.48% | 44.23% |
| GSHD | 4.3% | satellite | 72.19 | -1.11% | 11.44% | 4.9% |
| CLBT | 4.2% | satellite | 11.28 | -1.83% | 2.55% | -24.04% |
| PRE | 3.3% | satellite | 22.97 | 5.27% | 18.4% | 25.79% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.3%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -6.5%
- Beta vs SPY: 0.478 · posiciones efectivas: 12.6 · HHI: 0.0793

**Por que estos satellite (señales WATCHDOG):**

- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **PRE** · score agregado 184.6 · 3 señales · fuentes: corporate_insider
- **AMR** · score agregado 183.2 · 3 señales · fuentes: corporate_insider
- **DGICA** · score agregado 119.8 · 2 señales · fuentes: corporate_insider
- **CLBT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GSHD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| TISI | 77 | corporate_insider | Roeder Clinton William | 2 | $183,200 | cluster_buy |
| TISI | 72 | corporate_insider | Roeder Clinton William | 2 | $22,840 | cluster_buy,small_amount |
| GEVO | 72 | corporate_insider | Barber James J | 2 | $77,000 | cluster_buy |
| GO | 72 | large_holder | Pertento Partners LLP |  | - | - |
| CLBT | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| TENX | 72 | large_holder | Millennium Management LLC |  | - | - |
| HKHC | 71 | corporate_insider | Rosenthal Brent D | 2 | $54,000 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $45,800 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $46,300 | cluster_buy |
| CINT | 70 | large_holder | Swedbank Robur Fonder AB |  | - | - |
| USIO | 70 | large_holder | TALL PINES CAPITAL, LLC |  | - | - |
| NIXX | 70 | large_holder | NexGenAI Holding Group, I |  | - | - |
| XXII | 70 | large_holder | Iroquois Capital Manageme |  | - | - |
| SBDS | 70 | large_holder | Vanguard Charitable Endow |  | - | - |
| SBDS | 70 | large_holder | Vanguard Charitable Endow |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ALH | 61 | corporate_insider | BDT CAPITAL PARTNERS, LLC | $589,606,506 | - |
| PLTR | 58 | corporate_insider | Karp Alexander C. | $53,597,839 | - |
| DASH | 56 | corporate_insider | Adarkar Prabir | $3,778,407 | - |
| GH | 56 | corporate_insider | Talasaz AmirAli | $3,533,452 | - |
| PACS | 56 | corporate_insider | Murray Jason Hulse | $3,389,088 | - |
| DASH | 55 | corporate_insider | Inukonda Ravi | $4,303,271 | - |
| CRCL | 55 | corporate_insider | Fox-Geen Jeremy | $4,050,000 | - |
| DASH | 55 | corporate_insider | Tang Stanley | $16,294,516 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.11 (0.21% / -0.3% / 3.27%) [2026-08-25]
- QQQ: 709.67 (0.47% / -1.09% / 5.06%) [2026-08-25]
- IWM: 298.64 (0.23% / -0.53% / 1.8%) [2026-08-25]
- DIA: 534.92 (0.24% / 0.46% / 1.61%) [2026-08-25]
- TLT: 83.38 (0.99% / 2.11% / -0.62%) [2026-08-25]
- IEF: 93.45 (0.47% / 0.56% / 0.23%) [2026-08-25]
- GLD: 427.8 (0.26% / 7.34% / 15.82%) [2026-08-25]
- ^VIX: 15.44 (-2.59% / -2.53% / -15.21%) [2026-08-25]
- BTC-USD: 79161.9 (0.25% / 8.39% / 22.55%) [2026-08-25]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.24 (delta 1m: -0.13) [2026-08-21]
- Treasury 10Y yield: 4.74 (delta 1m: 0.03) [2026-08-21]
- Curva 10Y-2Y: 0.46 (delta 1m: 0.1) [2026-08-24]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.69 (delta 1m: -0.1) [2026-08-24]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.32 (delta 1m: 0.06) [2026-08-24]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), regulatory (2), earnings (2), merger (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ANET] Cisco Systems ( CSCO ) & Arista Networks ( ANET ): Cisco Just Beat Every Estimate . Why Did the Stock Still Drop 8 %? (2026-08-24)
- [ANET] Greenland Capital Management LP Purchases Shares of 4 , 085 Arista Networks , Inc . $ANET (2026-08-23)
- [ANET] Korea Investment CORP Reduces Position in Arista Networks , Inc . $ANET (2026-08-22)
- [ANET] Arista Networks vs . Salesforce : Which Technology Stock Is a Better Buy in 2026 ? (2026-08-22)
- [LEG] Leggett & Platt shareholders approve merger with Somnigroup (2026-08-21)
- [FMCB] Farmers & Merchants Bank of Long Beach ( OTCMKTS : FMBL ) Reaches New 1 - Year High – Here What Happened (2026-08-21)
- [AXON] Axon Enterprise vs . Celsius : Comparing Steady Incremental Gains and Historical Volatility in Quarterly Revenue Trends (2026-08-21)
- [ANET] Tom Lee Recommends Arista Networks ( ANET ) and JPMorgan ( JPM ), Analysts Weigh In (2026-08-20)
- [FMCB] Farmers & Merchants Bancorp ( OTCMKTS : FMCB ) Short Interest Down 50 . 0 % in July (2026-08-16)
- [BLND] Cango ( NYSE : CANG ) & Blend Labs ( NYSE : BLND ) Critical Analysis (2026-08-14)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Host-Plus Pty Ltd as trustee for the HOSTPLUS Pooled Superannuation Trust compro EBR Systems, Inc. por $20.8M el 2026-08-21.
- 10% owner BDT CAPITAL PARTNERS, LLC vendio ALH por $589.6M el 2026-08-20.
- Director Tsai Joseph C compro BABA por $10.4M el 2026-08-25.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- cruzzzz · PnL $24,904 · win rate 95% · categorias: sports, politics
- 123412341234 · PnL $13,705 · win rate 99% · categorias: sports
- AV23IUa · PnL $277,362 · win rate 76% · categorias: sports, crypto
- JnStrtPrdctnMrkts · PnL $22,441 · win rate 89% · categorias: crypto
- thatguythatguy · PnL $29,506 · win rate 95% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 656 registros 30d · ultimo dato 2026-08-25
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-25
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMR, CHTR, CLBT, DGICA, GLD, GSHD, IEF, PRE, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
