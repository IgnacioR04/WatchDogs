# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-23T20:37:31+00:00 · ventana señales 2026-06-23 -> 2026-07-23_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.7)
- Tendencia: `neutral` (SPY 738.18 · MA50 744.06 · MA200 695.06 · dist MA200: 6.2%)
- Credito: `tight` (HY spread 2.68)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 738.18 | -1.23% | -1.67% | 0.67% |
| QQQ | 9.8% | core | 691.96 | -1.9% | -1.98% | -2.63% |
| TLT | 9.8% | core | 83.17 | -0.32% | -1.24% | -4.47% |
| ECAT | 7.3% | satellite | 15.14 | -1.69% | -2.82% | 0.07% |
| GLD | 7.3% | core | 371.52 | -2.0% | 1.8% | 1.53% |
| BEP | 5.0% | satellite | 33.07 | 2.7% | 3.99% | -6.37% |
| IEF | 4.9% | core | 92.85 | -0.27% | -0.93% | -1.66% |
| CLBK | 4.1% | satellite | 11.01 | 0.64% | 5.54% | 22.03% |
| NMM | 3.7% | satellite | 76.82 | 4.29% | 3.21% | 7.91% |
| ENR | 2.8% | satellite | 20.65 | 0.73% | 0.05% | -8.3% |
| TSM | 1.9% | satellite | 415.58 | -1.34% | 1.43% | -5.73% |
| QNT | 0.9% | satellite | 56.46 | 2.88% | -0.11% | -20.59% |
| BFLY | 0.6% | satellite | 6.62 | 0.15% | -5.56% | -14.8% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.1%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -1.9%
- Beta vs SPY: None · posiciones efectivas: 18.8 · HHI: 0.0533

**Por que estos satellite (señales WATCHDOG):**

- **CLBK** · score agregado 1950.9 · 25 señales · fuentes: corporate_insider
- **TSM** · score agregado 434.6 · 6 señales · fuentes: corporate_insider
- **ENR** · score agregado 369.3 · 6 señales · fuentes: corporate_insider
- **NMM** · score agregado 174.4 · 3 señales · fuentes: corporate_insider
- **BFLY** · score agregado 142.0 · 2 señales · fuentes: large_holder
- **QNT** · score agregado 73.0 · 1 señales · fuentes: large_holder
- **ECAT** · score agregado 70.2 · 1 señales · fuentes: large_holder
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
| LLY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| HSY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CRDO | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 738.18 (-1.23% / -1.67% / 0.67%) [2026-07-23]
- QQQ: 691.96 (-1.9% / -1.98% / -2.63%) [2026-07-23]
- IWM: 292.09 (-0.58% / -1.18% / -1.55%) [2026-07-23]
- DIA: 516.26 (-1.0% / -1.6% / -0.41%) [2026-07-23]
- TLT: 83.17 (-0.32% / -1.24% / -4.47%) [2026-07-23]
- IEF: 92.85 (-0.27% / -0.93% / -1.66%) [2026-07-23]
- GLD: 371.52 (-2.0% / 1.8% / 1.53%) [2026-07-23]
- ^VIX: 18.7 (12.38% / 11.78% / 0.38%) [2026-07-23]
- BTC-USD: 65084.41 (-1.54% / 0.44% / 4.06%) [2026-07-23]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.31 (delta 1m: 0.07) [2026-07-22]
- Treasury 10Y yield: 4.67 (delta 1m: 0.16) [2026-07-22]
- Curva 10Y-2Y: 0.36 (delta 1m: 0.09) [2026-07-22]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.68 (delta 1m: -0.03) [2026-07-22]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.28 (delta 1m: 0.05) [2026-07-22]
- Dolar broad index: 120.5315 (delta 1m: 1.275) [2026-07-17]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (2), ai (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWV] High - Flying Tech Stocks NASDAQ : IONQ , NASDAQ : RKLB and NASDAQ : CRWV Down 60 % From Highs (2026-07-23)
- [CRWV] CoreWeave ( NASDAQ : CRWV ) Upgraded by Robert W . Baird to  Strong - Buy  Rating (2026-07-23)
- [NSA] National Storage Affiliates Trust ( NYSE : NSA ) Announces $0 . 03 Special Dividend (2026-07-19)
- [ONC] 2026 - 07 - 17 | BeOne Medicines to Announce Second Quarter 2026 Financial Results on August 5 | NDAQ : ONC (2026-07-17)
- [NSA] 2026 - 07 - 10 | National Storage Affiliates Trust Announces Anticipated Closing Date of Pending Transaction ; Declares Dividend in Connection with Pending Transaction | NYSE : NSA (2026-07-10)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Chu Chinh opero VLOS por $14.2M el 2026-07-20.
- CEO OYLER JOHN vendio ONC por $6.3M el 2026-07-21.
- CEO Huang Jack Jiajia compro COE por $1.9M el 2026-07-20.
- CEO Huang Jack Jiajia compro COE por $1.9M el 2026-07-16.
- CEO Huang Jack Jiajia compro COE por $1.4M el 2026-07-17.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.

**Polymarket — smart money (traders con mejor track record):**

- kekasaur · PnL $119,683 · win rate 92% · categorias: sports
- ExplosiveNinja · PnL $34,286 · win rate 97% · categorias: sports
- laozishudaosan · PnL $34,365 · win rate 95% · categorias: sports
- venera1234 · PnL $32,261 · win rate 95% · categorias: sports
- PleaseWinPlease · PnL $31,552 · win rate 90% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 74 registros 30d · ultimo dato 2026-07-20
- **sec_insiders**: `ok` · 690 registros 30d · ultimo dato 2026-07-23
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-23
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BFLY, CLBK, ECAT, ENR, GLD, IEF, NMM, QNT, QQQ, SPY, TLT, TSM`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **70.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
