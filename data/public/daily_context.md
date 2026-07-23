# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-23T17:03:43+00:00 · ventana señales 2026-06-23 -> 2026-07-23_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 19.32)
- Tendencia: `neutral` (SPY 738.62 · MA50 744.07 · MA200 695.07 · dist MA200: 6.27%)
- Credito: `tight` (HY spread 2.68)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 738.62 | -1.18% | -1.61% | 0.73% |
| QQQ | 9.8% | core | 692.76 | -1.78% | -1.87% | -2.51% |
| TLT | 9.8% | core | 83.12 | -0.38% | -1.29% | -4.52% |
| GLD | 7.3% | core | 371.7 | -1.96% | 1.85% | 1.58% |
| BEP | 5.8% | satellite | 32.91 | 2.2% | 3.49% | -6.82% |
| IEF | 4.9% | core | 92.85 | -0.27% | -0.93% | -1.67% |
| CLBK | 4.8% | satellite | 10.84 | -0.96% | 3.86% | 20.09% |
| NMM | 4.3% | satellite | 75.44 | 2.42% | 1.36% | 5.98% |
| LLY | 4.1% | satellite | 1180.99 | 1.55% | 1.01% | 5.7% |
| CAG | 3.2% | satellite | 14.28 | -3.67% | -1.28% | 4.96% |
| TSM | 2.2% | satellite | 417.87 | -0.79% | 1.98% | -5.21% |
| QNT | 1.1% | satellite | 56.81 | 3.52% | 0.51% | -20.1% |
| BFLY | 0.7% | satellite | 6.46 | -2.27% | -7.85% | -16.86% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.2%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -1.8%
- Beta vs SPY: None · posiciones efectivas: 19.2 · HHI: 0.0522

**Por que estos satellite (señales WATCHDOG):**

- **CLBK** · score agregado 1950.9 · 25 señales · fuentes: corporate_insider
- **TSM** · score agregado 434.6 · 6 señales · fuentes: corporate_insider
- **NMM** · score agregado 174.4 · 3 señales · fuentes: corporate_insider
- **BFLY** · score agregado 142.0 · 2 señales · fuentes: large_holder
- **LLY** · score agregado 135.3 · 2 señales · fuentes: congress, large_holder
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
| LLY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| HSY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CAG | 62 | congress | Gilbert Cisneros | $50,000 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 738.62 (-1.18% / -1.61% / 0.73%) [2026-07-23]
- QQQ: 692.76 (-1.78% / -1.87% / -2.51%) [2026-07-23]
- IWM: 291.69 (-0.71% / -1.32% / -1.69%) [2026-07-23]
- DIA: 516.8 (-0.9% / -1.5% / -0.3%) [2026-07-23]
- TLT: 83.12 (-0.38% / -1.29% / -4.52%) [2026-07-23]
- IEF: 92.85 (-0.27% / -0.93% / -1.67%) [2026-07-23]
- GLD: 371.7 (-1.96% / 1.85% / 1.58%) [2026-07-23]
- ^VIX: 19.32 (16.11% / 15.48% / 3.7%) [2026-07-23]
- BTC-USD: 64735.09 (-2.07% / -0.09% / 3.5%) [2026-07-23]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.26 (delta 1m: 0.07) [2026-07-21]
- Treasury 10Y yield: 4.63 (delta 1m: 0.17) [2026-07-21]
- Curva 10Y-2Y: 0.36 (delta 1m: 0.09) [2026-07-22]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.68 (delta 1m: -0.03) [2026-07-22]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.28 (delta 1m: 0.05) [2026-07-22]
- Dolar broad index: 120.5315 (delta 1m: 1.275) [2026-07-17]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (2), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWD] CrowdStrike Just Became Wall Street Newest Stock - Split Stock , but Something More  Magnificent  May Be Next (2026-07-23)
- [CRWV] CoreWeave ( NASDAQ : CRWV ) Upgraded by Robert W . Baird to  Strong - Buy  Rating (2026-07-23)
- [CRWD] CRWD Short Strangle Could Net $1 , 045 in a Few Weeks (2026-07-22)
- [CRWD] United Airlines says Homesite alone refused to pay its CrowdStrike claim (2026-07-22)
- [CAG] Conagra ( CAG ) Q4 2026 Earnings Call Transcript (2026-07-22)
- [CAG] Conagra Brands Slashes Its 10 % Dividend Yield in Half Just 1 Month After Getting Kicked Out of the S & P 500 . Here Why the Stock Isnt Tanking . (2026-07-19)

**Actores que han movido ficha este mes (top movimientos):**

- Officer Sutherland Vanessa Allen vendio PSX por $7.4B el 2026-07-21.
- CEO Chu Chinh opero VLOS por $14.2M el 2026-07-20.
- CEO OYLER JOHN vendio ONC por $6.3M el 2026-07-21.
- CEO Huang Jack Jiajia compro COE por $1.9M el 2026-07-20.
- CEO Huang Jack Jiajia compro COE por $1.9M el 2026-07-16.
- CEO Huang Jack Jiajia compro COE por $1.4M el 2026-07-17.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.

**Polymarket — smart money (traders con mejor track record):**

- 111111111115 · PnL $81,837 · win rate 95% · categorias: sports
- kekasaur · PnL $119,683 · win rate 92% · categorias: sports
- ExplosiveNinja · PnL $47,603 · win rate 97% · categorias: sports
- 0xe11Ff8cd2718F51a4d9403D166c20eaAAbE253F4-1777047101622 · PnL $89,488 · win rate 88% · categorias: sports
- venera1234 · PnL $32,261 · win rate 95% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 74 registros 30d · ultimo dato 2026-07-20
- **sec_insiders**: `ok` · 688 registros 30d · ultimo dato 2026-07-22
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-23
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BFLY, CAG, CLBK, GLD, IEF, LLY, NMM, QNT, QQQ, SPY, TLT, TSM`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
