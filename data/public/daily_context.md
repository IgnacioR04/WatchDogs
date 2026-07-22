# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-22T20:48:56+00:00 · ventana señales 2026-06-22 -> 2026-07-22_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.64)
- Tendencia: `bull` (SPY 747.41 · MA50 744.04 · MA200 694.69 · dist MA200: 7.59%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.37)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 747.41 | -0.12% | -0.98% | 1.89% |
| QQQ | 12.0% | core | 705.35 | -0.51% | -1.73% | -1.16% |
| TLT | 12.0% | core | 83.44 | -0.26% | -0.95% | -2.84% |
| GLD | 9.3% | core | 379.12 | 1.15% | 1.82% | 0.48% |
| BEP | 7.8% | satellite | 32.2 | 0.06% | -0.98% | -9.14% |
| IEF | 6.2% | core | 93.1 | -0.23% | -0.73% | -0.76% |
| LLY | 5.3% | satellite | 1163.01 | -1.05% | 0.55% | 5.05% |
| ENR | 4.5% | satellite | 20.5 | 2.09% | -0.92% | -5.05% |
| CAG | 4.4% | satellite | 14.83 | -0.13% | 5.25% | 10.42% |
| UBER | 4.2% | satellite | 70.33 | -1.71% | -3.22% | 0.95% |
| TSM | 2.9% | satellite | 421.21 | -0.8% | 0.41% | -3.48% |
| VOR | 1.9% | satellite | 19.51 | -2.69% | 7.91% | 31.38% |
| QNT | 1.5% | satellite | 54.88 | -6.32% | -9.3% | -29.15% |
| BFLY | 0.9% | satellite | 6.61 | -3.08% | -9.45% | -13.82% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.0%
- VaR 95% 1d: 1.2% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -3.2%
- Beta vs SPY: 0.659 · posiciones efectivas: 13.9 · HHI: 0.072

**Por que estos satellite (señales WATCHDOG):**

- **ENR** · score agregado 307.7 · 5 señales · fuentes: corporate_insider
- **TSM** · score agregado 282.0 · 5 señales · fuentes: corporate_insider
- **BFLY** · score agregado 142.0 · 2 señales · fuentes: large_holder
- **QNT** · score agregado 73.0 · 1 señales · fuentes: large_holder
- **VOR** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **UBER** · score agregado 68.5 · 1 señales · fuentes: congress
- **CAG** · score agregado 64.0 · 1 señales · fuentes: corporate_insider
- **LLY** · score agregado 63.5 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| CHCO | 73 | corporate_insider | FISHER ROBERT D | 4 | $20,990 | cluster_buy,small_amount |
| QNT | 73 | large_holder | BlackRock Portfolio Manag |  | - | - |
| CHCO | 72 | corporate_insider | STRONG-TREISTER DIANE W | 4 | $14,800 | cluster_buy,small_amount |
| CHCO | 72 | corporate_insider | Hoyer James A | 4 | $12,782 | cluster_buy,small_amount |
| INSM | 72 | large_holder | JPMORGAN CHASE & CO. |  | - | - |
| BFLY | 72 | large_holder | Rothberg Jonathan M. |  | - | - |
| HCAT | 72 | large_holder | Impax Asset Management Gr |  | - | - |
| CHCO | 72 | corporate_insider | Reyes Javier A | 4 | $11,168 | cluster_buy,small_amount |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| PAG | 70 | large_holder | Penske Corporation |  | - | - |
| PAG | 70 | large_holder | Mitsui & Co., Ltd. |  | - | - |
| NCO | 70 | large_holder | Space Summit Capital LLC |  | - | - |
| NVVE | 70 | large_holder | RainForest Partners, LLC |  | - | - |
| FLYW | 70 | large_holder | Temasek Holdings (Private |  | - | - |
| TTE | 70 | large_holder | AMUNDI |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| LLY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| HSY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CAG | 62 | congress | Gilbert Cisneros | $50,000 | - |

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
- ^VIX: 16.64 (-2.4% / 6.19% / -14.62%) [2026-07-22]
- BTC-USD: 65865.01 (-0.96% / 3.08% / 7.12%) [2026-07-22]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.26 (delta 1m: 0.07) [2026-07-21]
- Treasury 10Y yield: 4.63 (delta 1m: 0.17) [2026-07-21]
- Curva 10Y-2Y: 0.37 (delta 1m: 0.1) [2026-07-21]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.69 (delta 1m: 0.04) [2026-07-21]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.26 (delta 1m: 0.01) [2026-07-21]
- Dolar broad index: 120.5315 (delta 1m: 1.275) [2026-07-17]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (5), ai (4), earnings (3)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWD] CRWD Short Strangle Could Net $1 , 045 in a Few Weeks (2026-07-22)
- [CRWD] United Airlines says Homesite alone refused to pay its CrowdStrike claim (2026-07-22)
- [CAG] Conagra ( CAG ) Q4 2026 Earnings Call Transcript (2026-07-22)
- [CRWD] Jim Cramer Calls AI Cyberattacks a  Watershed Moment  for CrowdStrike (2026-07-22)
- [CRWD] Homesite seeks to dodge United Airline CrowdStrike outage claim (2026-07-22)
- [ANGO] AngioDynamics ( ANGO ) Q4 2026 Earnings Call Transcript (2026-07-21)
- [CAG] Conagra Brands Slashes Its 10 % Dividend Yield in Half Just 1 Month After Getting Kicked Out of the S & P 500 . Here Why the Stock Isnt Tanking . (2026-07-19)
- [CAG] SteelPeak Wealth LLC Makes New Investment in Conagra Brands $CAG (2026-07-19)
- [CAG] Conagra Brands Slashes Its 10 % Dividend Yield in Half Just 1 Month After Getting Kicked Out of the S & P 500 . Here Why the Stock Isnt Tanking . (2026-07-19)
- [ANGO] Zacks Research Downgrades AngioDynamics ( NASDAQ : ANGO ) to Strong Sell (2026-07-18)

**Actores que han movido ficha este mes (top movimientos):**

- CEO KIRBY J SCOTT vendio UAL por $18.8M el 2026-07-21.
- Officer Sutherland Vanessa Allen vendio PSX por $7.4B el 2026-07-21.
- 10% owner ABRY Partners VII, L.P. vendio KORE por $44.9M el 2026-07-21.
- CEO Clark Kevin Cronin vendio CCRN por $12.6M el 2026-07-21.
- 10% owner ROTHBERG JONATHAN M vendio BFLY por $7.8M el 2026-07-20 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.

**Polymarket — smart money (traders con mejor track record):**

- 111111111115 · PnL $175,302 · win rate 95% · categorias: sports
- Sassy-Bucket · PnL $170,616 · win rate 93% · categorias: sports
- esportGG · PnL $81,401 · win rate 94% · categorias: sports
- monkeymashingkeyboard · PnL $70,803 · win rate 92% · categorias: sports
- 0x5F659BcCBC353dBf7BcdffDEE73beE60bB482036-1780496231400 · PnL $45,429 · win rate 90% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 74 registros 30d · ultimo dato 2026-07-20
- **sec_insiders**: `ok` · 616 registros 30d · ultimo dato 2026-07-22
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-22
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BFLY, CAG, ENR, GLD, IEF, LLY, QNT, QQQ, SPY, TLT, TSM, UBER, VOR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
