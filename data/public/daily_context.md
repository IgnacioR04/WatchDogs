# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-25T20:05:41+00:00 · ventana señales 2026-07-26 -> 2026-08-25_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.45)
- Tendencia: `bull` (SPY 765.85 · MA50 752.63 · MA200 705.92 · dist MA200: 8.49%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.85 | 0.31% | -0.21% | 3.37% |
| QQQ | 12.0% | core | 710.72 | 0.62% | -0.95% | 5.22% |
| TLT | 12.0% | core | 83.47 | 1.1% | 2.22% | -0.51% |
| DGICA | 11.8% | satellite | 19.13 | 0.79% | 2.79% | 0.62% |
| GLD | 9.3% | core | 428.1 | 0.33% | 7.41% | 15.9% |
| IEF | 6.2% | core | 93.51 | 0.54% | 0.62% | 0.29% |
| CHTR | 5.2% | satellite | 155.14 | 3.22% | 4.58% | 10.84% |
| AMR | 4.8% | satellite | 216.12 | 2.95% | 27.55% | 48.98% |
| GSHD | 4.3% | satellite | 72.33 | -0.92% | 11.65% | 5.1% |
| CLBT | 4.2% | satellite | 11.29 | -1.74% | 2.64% | -23.97% |
| PRE | 3.3% | satellite | 23.25 | 6.55% | 19.85% | 27.33% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.3%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -6.5%
- Beta vs SPY: 0.478 · posiciones efectivas: 12.6 · HHI: 0.0793

**Por que estos satellite (señales WATCHDOG):**

- **AMR** · score agregado 312.3 · 4 señales · fuentes: corporate_insider
- **CHTR** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **PRE** · score agregado 184.6 · 3 señales · fuentes: corporate_insider
- **DGICA** · score agregado 119.8 · 2 señales · fuentes: corporate_insider
- **CLBT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GSHD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| AMR | 81 | corporate_insider | Gorzynski Michael | 2 | $2,089,169 | cluster_buy |
| AMR | 79 | corporate_insider | Courtis Kenneth S. | 2 | $2,097,179 | cluster_buy |
| TISI | 77 | corporate_insider | Roeder Clinton William | 2 | $183,200 | cluster_buy |
| AMR | 77 | corporate_insider | Courtis Kenneth S. | 2 | $677,466 | cluster_buy |
| AMR | 75 | corporate_insider | Courtis Kenneth S. | 2 | $382,985 | cluster_buy |
| TISI | 72 | corporate_insider | Roeder Clinton William | 2 | $22,840 | cluster_buy,small_amount |
| GEVO | 72 | corporate_insider | Barber James J | 2 | $77,000 | cluster_buy |
| USIO | 72 | large_holder | TALL PINES CAPITAL, LLC |  | - | - |
| TG | 72 | large_holder | John D. Gottwald |  | - | - |
| GO | 72 | large_holder | Pertento Partners LLP |  | - | - |
| CLBT | 72 | large_holder | Voss Value Master Fund, L |  | - | - |
| TENX | 72 | large_holder | Millennium Management LLC |  | - | - |
| HKHC | 71 | corporate_insider | Rosenthal Brent D | 2 | $54,000 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $45,800 | cluster_buy |
| TISI | 71 | corporate_insider | Horton Anthony R | 2 | $46,300 | cluster_buy |

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

- SPY: 765.85 (0.31% / -0.21% / 3.37%) [2026-08-25]
- QQQ: 710.72 (0.62% / -0.95% / 5.22%) [2026-08-25]
- IWM: 299.28 (0.44% / -0.32% / 2.01%) [2026-08-25]
- DIA: 535.27 (0.3% / 0.53% / 1.67%) [2026-08-25]
- TLT: 83.47 (1.1% / 2.22% / -0.51%) [2026-08-25]
- IEF: 93.51 (0.54% / 0.62% / 0.29%) [2026-08-25]
- GLD: 428.1 (0.33% / 7.41% / 15.9%) [2026-08-25]
- ^VIX: 15.45 (-2.52% / -2.46% / -15.16%) [2026-08-25]
- BTC-USD: 78733.47 (-0.29% / 7.81% / 21.88%) [2026-08-25]

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

**Temas dominantes**: stock (3), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [ANET] Cisco Systems ( CSCO ) & Arista Networks ( ANET ): Cisco Just Beat Every Estimate . Why Did the Stock Still Drop 8 %? (2026-08-24)
- [ANET] Greenland Capital Management LP Purchases Shares of 4 , 085 Arista Networks , Inc . $ANET (2026-08-23)
- [PKOH] Head to Head Contrast : Park - Ohio ( NASDAQ : PKOH ) & Gold . com ( NYSE : GOLD ) (2026-08-22)
- [ANET] Korea Investment CORP Reduces Position in Arista Networks , Inc . $ANET (2026-08-22)
- [ANET] Arista Networks vs . Salesforce : Which Technology Stock Is a Better Buy in 2026 ? (2026-08-22)
- [LEG] Leggett & Platt shareholders approve merger with Somnigroup (2026-08-21)
- [ANET] Tom Lee Recommends Arista Networks ( ANET ) and JPMorgan ( JPM ), Analysts Weigh In (2026-08-20)

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

- comon119 · PnL $30,801 · win rate 97% · categorias: sports, crypto
- cruzzzz · PnL $24,940 · win rate 95% · categorias: sports, politics
- AV23IUa · PnL $286,370 · win rate 76% · categorias: sports, crypto
- JnStrtPrdctnMrkts · PnL $19,664 · win rate 89% · categorias: crypto
- thatguythatguy · PnL $24,097 · win rate 95% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 670 registros 30d · ultimo dato 2026-08-25
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
