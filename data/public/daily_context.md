# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-23T09:53:53+00:00 · ventana señales 2026-06-23 -> 2026-07-23_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.66)
- Tendencia: `bull` (SPY 747.41 · MA50 744.04 · MA200 694.69 · dist MA200: 7.59%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 747.41 | -0.12% | -0.98% | 1.89% |
| QQQ | 12.0% | core | 705.35 | -0.51% | -1.73% | -1.16% |
| TLT | 12.0% | core | 83.44 | -0.26% | -0.95% | -2.84% |
| BEP | 9.8% | satellite | 32.2 | 0.06% | -0.98% | -9.14% |
| GLD | 9.3% | core | 379.12 | 1.15% | 1.82% | 0.48% |
| CLBK | 8.1% | satellite | 10.94 | -1.26% | 9.4% | 21.43% |
| NMM | 7.2% | satellite | 73.66 | -0.86% | -1.77% | 1.56% |
| IEF | 6.2% | core | 93.1 | -0.23% | -0.73% | -0.76% |
| CAG | 5.4% | satellite | 14.83 | -0.13% | 5.25% | 10.42% |
| QNT | 1.9% | satellite | 54.88 | -6.32% | -9.3% | -29.15% |
| BFLY | 1.1% | satellite | 6.61 | -3.08% | -9.45% | -13.82% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.7%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -2.0%
- Beta vs SPY: None · posiciones efectivas: 12.4 · HHI: 0.0805

**Por que estos satellite (señales WATCHDOG):**

- **CLBK** · score agregado 1950.9 · 25 señales · fuentes: corporate_insider
- **NMM** · score agregado 174.4 · 3 señales · fuentes: corporate_insider
- **BFLY** · score agregado 142.0 · 2 señales · fuentes: large_holder
- **QNT** · score agregado 73.0 · 1 señales · fuentes: large_holder
- **CAG** · score agregado 64.0 · 1 señales · fuentes: corporate_insider
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| CLBK | 84 | corporate_insider | Kemly Thomas J. | 16 | $400,000 | cluster_buy |
| CLBK | 83 | corporate_insider | Splaine Thomas Jr | 16 | $500,000 | cluster_buy |
| CLBK | 81 | corporate_insider | Kemly Thomas J. | 16 | $130,570 | cluster_buy |
| CLBK | 80 | corporate_insider | Schlesinger Allyson Katz | 16 | $444,000 | cluster_buy |
| CLBK | 80 | corporate_insider | Klein Steven M | 16 | $500,000 | cluster_buy |
| CLBK | 80 | corporate_insider | Klimowich John | 16 | $300,000 | cluster_buy |
| CLBK | 79 | corporate_insider | Randall Elizabeth E. | 16 | $272,000 | cluster_buy |
| CLBK | 78 | corporate_insider | Van Dyk Robert | 16 | $250,000 | cluster_buy |
| CLBK | 78 | corporate_insider | Gibney Dennis E. | 16 | $205,000 | cluster_buy |
| CLBK | 78 | corporate_insider | Prabhu Manesh Balachandra | 16 | $150,000 | cluster_buy |
| CLBK | 78 | corporate_insider | Sorrentini Lucy | 16 | $200,000 | cluster_buy |
| CLBK | 78 | corporate_insider | Lewis Oliver Edward Jr | 16 | $145,000 | cluster_buy |
| CLBK | 77 | corporate_insider | Massood Michael Jr. | 16 | $150,000 | cluster_buy |
| CLBK | 77 | corporate_insider | Gibney Dennis E. | 16 | $125,000 | cluster_buy |
| CLBK | 77 | corporate_insider | Rinaldi Mayra Liseth | 16 | $90,000 | cluster_buy |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 64 | congress | John McGuire | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| HSY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CAG | 62 | congress | Gilbert Cisneros | $50,000 | - |
| ADBE | 61 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 747.41 (-0.12% / -0.98% / 1.89%) [2026-07-22]
- QQQ: 705.35 (-0.51% / -1.73% / -1.16%) [2026-07-22]
- IWM: 293.79 (-0.93% / -0.67% / -0.52%) [2026-07-22]
- DIA: 521.47 (-0.01% / -0.82% / 0.97%) [2026-07-22]
- TLT: 83.44 (-0.26% / -0.95% / -2.84%) [2026-07-22]
- IEF: 93.1 (-0.23% / -0.73% / -0.76%) [2026-07-22]
- GLD: 379.12 (1.15% / 1.82% / 0.48%) [2026-07-22]
- ^VIX: 17.66 (6.13% / 5.56% / -5.21%) [2026-07-23]
- BTC-USD: 65645.23 (-0.69% / 1.31% / 4.96%) [2026-07-23]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.26 (delta 1m: 0.07) [2026-07-21]
- Treasury 10Y yield: 4.63 (delta 1m: 0.17) [2026-07-21]
- Curva 10Y-2Y: 0.36 (delta 1m: 0.09) [2026-07-22]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.69 (delta 1m: 0.04) [2026-07-21]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.28 (delta 1m: 0.05) [2026-07-22]
- Dolar broad index: 120.5315 (delta 1m: 1.275) [2026-07-17]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWV] CoreWeave ( NASDAQ : CRWV ) Shares Up 3 . 8 % – Still a Buy ? (2026-07-22)
- [CRWV] CoreWeave and Nebius Get Bullish Calls (2026-07-22)

**Actores que han movido ficha este mes (top movimientos):**

- Officer Sutherland Vanessa Allen vendio PSX por $7.4B el 2026-07-21.
- CEO Chu Chinh opero VLOS por $14.2M el 2026-07-20.
- CEO OYLER JOHN vendio ONC por $6.3M el 2026-07-21.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.
- Institutional manager Citadel Advisors LLC compro STATE STR SPDR S&P 500 ETF T por $16.0B.
- Institutional manager Geode Capital Management LLC compro JPMORGAN CHASE & CO por $13.1B.

**Polymarket — smart money (traders con mejor track record):**

- kekasaur · PnL $119,683 · win rate 92% · categorias: sports
- PleaseWinPlease · PnL $32,102 · win rate 90% · categorias: sports
- esportGG · PnL $12,592 · win rate 95% · categorias: sports
- kunkun168 · PnL $9,187 · win rate 90% · categorias: sports
- VD721lsj4938Dk388 · PnL $14,174 · win rate 85% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 74 registros 30d · ultimo dato 2026-07-20
- **sec_insiders**: `ok` · 693 registros 30d · ultimo dato 2026-07-22
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-22
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BFLY, CAG, CLBK, GLD, IEF, NMM, QNT, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
