# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-19T04:15:27+00:00 · ventana señales 2026-07-20 -> 2026-08-19_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.84)
- Tendencia: `bull` (SPY 772.67 · MA50 748.9 · MA200 703.21 · dist MA200: 9.88%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `steep` (curva 10y-2y 0.52)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 772.67 | -0.47% | -0.05% | 4.12% |
| QQQ | 12.0% | core | 729.87 | -0.16% | 1.25% | 4.86% |
| TLT | 12.0% | core | 81.66 | 0.38% | -0.64% | -2.0% |
| FWONK | 11.4% | satellite | 101.98 | -1.85% | -0.73% | 1.98% |
| GLD | 9.3% | core | 405.49 | 1.0% | 0.73% | 10.31% |
| LTH | 8.9% | satellite | 45.34 | 0.18% | 6.78% | 7.95% |
| IEF | 6.2% | core | 92.84 | -0.21% | 0.09% | -0.73% |
| CHRW | 5.9% | satellite | 144.78 | -2.55% | -2.37% | -26.69% |
| MANE | 3.8% | satellite | 108.22 | -3.98% | -2.28% | -12.51% |
| AMBQ | 3.4% | satellite | 63.01 | -7.15% | -3.49% | -19.36% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.3%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -4.0%
- Beta vs SPY: 0.638 · posiciones efectivas: 12.1 · HHI: 0.0828

**Por que estos satellite (señales WATCHDOG):**

- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **AMBQ** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MANE** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| VRCA | 76 | corporate_insider | Rieger Jayson | 2 | $101,200 | cluster_buy |
| VRCA | 74 | corporate_insider | Rieger Jayson | 2 | $24,550 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Seger Andrew M | 4 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Ryan Christina M | 4 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Bawel Zachary W | 4 | $20,000 | cluster_buy,small_amount |
| EVLV | 72 | corporate_insider | Kuhl Henrik | 2 | $85,950 | cluster_buy |
| MLPT | 72 | corporate_insider | Catalyst4, Inc. | 0 | $50,072,000 | - |
| ELF | 72 | large_holder | Fenelon Opportunity Fund  |  | - | - |
| AMBQ | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| QDEL | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| EVLV | 71 | corporate_insider | Glat Neil | 2 | $48,790 | cluster_buy |
| VRCA | 70 | corporate_insider | Zawitz David | 2 | $29,880 | cluster_buy |
| PPC | 70 | large_holder | Wesley Mendonca Batista |  | - | - |
| BIRK | 70 | large_holder | CB Beteiligungs GmbH & Co |  | - | - |
| MEGI | 70 | large_holder | Saba Capital Management,  |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PINS | 65 | congress | Christian D. Menefee | $50,000 | - |
| TSCO | 64 | congress | April McClain Delaney | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| CCI | 63 | congress | Michael Rulli | $15,000 | small_amount |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| WAB | 62 | congress | April McClain Delaney | $15,000 | small_amount |
| WAB | 62 | congress | April McClain Delaney | $50,000 | - |
| OGN | 61 | congress | Kevin Hern | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 772.67 (-0.47% / -0.05% / 4.12%) [2026-08-17]
- QQQ: 729.87 (-0.16% / 1.25% / 4.86%) [2026-08-17]
- IWM: 304.06 (-0.34% / 1.36% / 4.02%) [2026-08-17]
- DIA: 532.91 (-0.24% / -0.81% / 2.19%) [2026-08-18]
- TLT: 81.66 (0.38% / -0.64% / -2.0%) [2026-08-18]
- IEF: 92.84 (-0.21% / 0.09% / -0.73%) [2026-08-17]
- GLD: 405.49 (1.0% / 0.73% / 10.31%) [2026-08-17]
- ^VIX: 15.84 (4.28% / 3.66% / -7.1%) [2026-08-18]
- BTC-USD: 64258.2 (-0.38% / 1.35% / 0.55%) [2026-08-19]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.19 (delta 1m: 0.01) [2026-08-17]
- Treasury 10Y yield: 4.72 (delta 1m: 0.17) [2026-08-17]
- Curva 10Y-2Y: 0.52 (delta 1m: 0.13) [2026-08-18]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.03) [2026-08-17]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.3 (delta 1m: 0.05) [2026-08-18]
- Dolar broad index: 118.9028 (delta 1m: -1.428) [2026-08-14]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (4), legal (3), leadership (1), stock (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [RDDT] Reddit tests AI - powered conversations (2026-08-19)
- [HIMS] Kessler Topaz Meltzer & Check , LLP Encourages Hims & Hers Health , Inc . ( NYSE : HIMS ) Investors to Contact the Firm (2026-08-19)
- [HIMS] Kessler Topaz Meltzer & Check , LLP Encourages Hims & Hers Health , Inc . ( NYSE : HIMS ) Investors to Contact the Firm (2026-08-19)
- [HIMS] Why Is Hims & Hers Health ( HIMS ) Facing A New Privacy Lawsuit ? (2026-08-18)
- [UBER] Zipline and Uber Eats aiming to reach one million drone deliveries per day by the end of 2029 (2026-08-18)
- [HIMS] Hims & Hers CEO Andrew Dudum talks FTC lawsuit , GLP - 1s , AI (2026-08-18)
- [UBER] Uber Eyes 1 Million Daily Drone Deliveries With Zipline Partnership (2026-08-18)
- [UBER] Uber and Zipline partner on drone delivery (2026-08-18)
- [UBER] NY Judge Delivers Blow to Uber Injury Lawsuit (2026-08-18)
- [UBER] Uber Technologies ( NYSE : UBER ) Shares Down 1 . 5 % – Here Why (2026-08-17)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Catalyst4, Inc. compro MLPT por $50.1M el 2026-08-14.
- CEO Jonsson Patrik vendio LLY por $7.6M el 2026-08-17 [senal en multiples fuentes].
- CEO Waldman Reid Alexander vendio MANE por $3.0M el 2026-08-17 [senal en multiples fuentes].
- CEO Hollar Jason M. opero CAH por $24.3M el 2026-08-15.
- CEO Bevirt JoeBen vendio JOBY por $4.7M el 2026-08-17.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- torta.tech · PnL $14,911 · win rate 94% · categorias: sports
- QuentinChen · PnL $11,620 · win rate 96% · categorias: sports
- ic4cream · PnL $27,225 · win rate 90% · categorias: sports
- CHACHA125655 · PnL $8,278 · win rate 91% · categorias: sports
- jarosbill · PnL $9,872 · win rate 87% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 103 registros 30d · ultimo dato 2026-08-07 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 873 registros 30d · ultimo dato 2026-08-18
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-18
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMBQ, CHRW, FWONK, GLD, IEF, LTH, MANE, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
