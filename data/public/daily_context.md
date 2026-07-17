# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-17T21:26:13+00:00 · ventana señales 2026-06-17 -> 2026-07-17_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.77)
- Tendencia: `bull` (SPY 743.29 · MA50 743.23 · MA200 693.44 · dist MA200: 7.19%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.37)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 743.29 | -0.99% | -1.54% | 0.57% |
| QQQ | 12.0% | core | 695.33 | -1.5% | -4.16% | -3.66% |
| TLT | 12.0% | core | 84.52 | 0.37% | 0.06% | -1.74% |
| GLD | 9.3% | core | 368.41 | 0.95% | -2.28% | -5.2% |
| TYG | 9.1% | satellite | 43.6 | -0.48% | 0.53% | 3.07% |
| IEF | 6.2% | core | 93.84 | 0.13% | 0.22% | 0.14% |
| BEP | 5.9% | satellite | 31.76 | -0.13% | -1.76% | -7.24% |
| ELV | 4.5% | satellite | 373.11 | 0.07% | -10.36% | -4.64% |
| PNTG | 4.3% | satellite | 41.95 | 0.58% | 3.58% | 21.31% |
| MPWR | 3.4% | satellite | 1312.0 | 0.49% | -3.01% | -9.27% |
| ENR | 3.3% | satellite | 20.23 | -1.99% | -1.17% | 1.3% |
| NUVL | 3.0% | satellite | 123.96 | 0.05% | 0.19% | 0.41% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.1%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -6.3%
- Beta vs SPY: 0.598 · posiciones efectivas: 13.4 · HHI: 0.0745

**Por que estos satellite (señales WATCHDOG):**

- **ENR** · score agregado 246.4 · 4 señales · fuentes: corporate_insider
- **ELV** · score agregado 234.7 · 3 señales · fuentes: corporate_insider
- **TYG** · score agregado 141.8 · 2 señales · fuentes: corporate_insider
- **NUVL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PNTG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MPWR** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| ELV | 81 | corporate_insider | BOUDREAUX GAIL | 2 | $753,071 | cluster_buy |
| ELV | 78 | corporate_insider | BOUDREAUX GAIL | 2 | $249,159 | cluster_buy |
| ELV | 75 | corporate_insider | PERU RAMIRO G | 2 | $366,050 | cluster_buy |
| YORW | 73 | corporate_insider | Hand Joseph Thomas | 6 | $3,250 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Seger Andrew M | 5 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Ryan Christina M | 5 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | KELLY JASON M | 5 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Bawel Zachary W | 5 | $20,000 | cluster_buy,small_amount |
| GABC | 72 | corporate_insider | Stokes Ronnie R | 5 | $15,000 | cluster_buy,small_amount |
| KROS | 72 | large_holder | BlackRock Portfolio Manag |  | - | - |
| QNT | 72 | large_holder | BlackRock Portfolio Manag |  | - | - |
| NUVL | 72 | large_holder | Deerfield Management Comp |  | - | - |
| PNTG | 72 | large_holder | Wasatch Advisors LP |  | - | - |
| MPWR | 72 | large_holder | Invesco Ltd. |  | - | - |
| HQY | 72 | large_holder | Wasatch Advisors LP |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| ABT | 61 | congress | Rick Larsen | $15,000 | small_amount |
| SPGI | 61 | congress | Rick Larsen | $15,000 | small_amount |
| FLL | 61 | congress | Susie Lee | $15,000 | small_amount |
| BRCM | 61 | congress | Gilbert Cisneros | $15,000 | small_amount |
| CBZ | 61 | congress | Gilbert Cisneros | $15,000 | small_amount |
| CRDO | 61 | congress | Gilbert Cisneros | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 743.29 (-0.99% / -1.54% / 0.57%) [2026-07-17]
- QQQ: 695.33 (-1.5% / -4.16% / -3.66%) [2026-07-17]
- IWM: 294.04 (-0.52% / -0.66% / 1.44%) [2026-07-17]
- DIA: 520.81 (-0.77% / -0.95% / 1.15%) [2026-07-17]
- TLT: 84.52 (0.37% / 0.06% / -1.74%) [2026-07-17]
- IEF: 93.84 (0.13% / 0.22% / 0.14%) [2026-07-17]
- GLD: 368.41 (0.95% / -2.28% / -5.2%) [2026-07-17]
- ^VIX: 18.77 (12.19% / 24.88% / 1.79%) [2026-07-17]
- BTC-USD: 64125.13 (0.53% / 0.58% / 6.98%) [2026-07-17]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.16 (delta 1m: 0.09) [2026-07-16]
- Treasury 10Y yield: 4.57 (delta 1m: 0.1) [2026-07-16]
- Curva 10Y-2Y: 0.37 (delta 1m: -0.01) [2026-07-17]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.71 (delta 1m: 0.08) [2026-07-16]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.24 (delta 1m: -0.05) [2026-07-17]
- Dolar broad index: 120.5046 (delta 1m: 0.543) [2026-07-10]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [PAYX] Welch & Forbes LLC Cuts Stock Holdings in Paychex , Inc . $PAYX (2026-07-12)
- [PAYX] The Toughest Questions PAYX Faced On Its Latest Call (2026-07-10)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Decisive Point Group, LLC compro STDN por $19.1M el 2026-07-16.
- 10% owner Manufacturers Life Insurance Co (Bermuda Branch) compro John Hancock GA Mortgage Trust por $36.6M el 2026-07-15.
- Director SUMITOMO MITSUI FINANCIAL GROUP, INC. compro JEF por $318.7M el 2026-07-15.
- 10% owner PRUDENTIAL FINANCIAL INC compro TYG por $30.0M el 2026-07-15.
- 10% owner Flynn James E vendio NUVL por $1.0B el 2026-07-15 [senal en multiples fuentes].
- 10% owner Manulife (International) Ltd compro John Hancock GA Mortgage Trust por $22.0M el 2026-07-15.
- CEO MULLEE SPENCER EDWARD opero CSQR por $75.0M el 2026-07-15.
- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Mortgage Trust por $13.0M el 2026-07-15.

**Polymarket — smart money (traders con mejor track record):**

- 111111111115 · PnL $362,828 · win rate 96% · categorias: sports
- TAIWANNUMBERONE · PnL $246,173 · win rate 89% · categorias: sports, politics
- BreakTheBank · PnL $252,958 · win rate 86% · categorias: sports
- comon119 · PnL $29,337 · win rate 99% · categorias: sports, crypto, politics
- ExplosiveNinja · PnL $32,010 · win rate 97% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 40 registros 30d · ultimo dato 2026-07-08
- **sec_insiders**: `ok` · 597 registros 30d · ultimo dato 2026-07-17
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-17
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, ELV, ENR, GLD, IEF, MPWR, NUVL, PNTG, QQQ, SPY, TLT, TYG`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
