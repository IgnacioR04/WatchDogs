# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-19T13:27:28+00:00 · ventana señales 2026-07-20 -> 2026-08-19_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.44)
- Tendencia: `bull` (SPY 767.45 · MA50 749.53 · MA200 703.64 · dist MA200: 9.07%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `steep` (curva 10y-2y 0.52)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 767.45 | -0.68% | -0.4% | 2.56% |
| QQQ | 12.0% | core | 717.51 | -1.69% | -0.13% | 1.2% |
| TLT | 12.0% | core | 81.66 | 0.38% | -0.64% | -2.0% |
| FWONK | 10.0% | satellite | 102.02 | 0.04% | -0.69% | 2.84% |
| GLD | 9.3% | core | 398.55 | -1.71% | -0.6% | 6.33% |
| LTH | 7.7% | satellite | 45.4 | 0.13% | 3.63% | 7.38% |
| IEF | 6.2% | core | 92.93 | 0.1% | 0.06% | -0.07% |
| CHRW | 5.1% | satellite | 144.67 | -0.08% | -0.3% | -30.92% |
| NVRI | 4.4% | satellite | 19.66 | -5.98% | -2.38% | -10.11% |
| MANE | 3.3% | satellite | 111.31 | 2.86% | 0.51% | 4.97% |
| AMBQ | 2.9% | satellite | 63.01 | -7.15% | -3.49% | -19.36% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.1%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -3.2%
- Beta vs SPY: 0.631 · posiciones efectivas: 12.8 · HHI: 0.0782

**Por que estos satellite (señales WATCHDOG):**

- **FWONK** · score agregado 248.8 · 4 señales · fuentes: congress
- **NVRI** · score agregado 147.5 · 2 señales · fuentes: corporate_insider
- **CHRW** · score agregado 127.4 · 2 señales · fuentes: congress
- **LTH** · score agregado 124.4 · 2 señales · fuentes: congress
- **AMBQ** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MANE** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| CCHH | 82 | corporate_insider | Goh Kok E | 2 | $1,440,720 | cluster_buy |
| VRCA | 76 | corporate_insider | Rieger Jayson | 2 | $101,200 | cluster_buy |
| NVRI | 75 | corporate_insider | Minan Peter Francis | 2 | $49,829 | cluster_buy |
| VRCA | 74 | corporate_insider | Rieger Jayson | 2 | $24,550 | cluster_buy,small_amount |
| CCHH | 73 | corporate_insider | Ng Yah Ling | 2 | $129,716 | cluster_buy |
| GABC | 73 | corporate_insider | Seger Andrew M | 4 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Ryan Christina M | 4 | $20,000 | cluster_buy,small_amount |
| GABC | 73 | corporate_insider | Bawel Zachary W | 4 | $20,000 | cluster_buy,small_amount |
| NVRI | 72 | corporate_insider | HAZNEDAR CAROLANN I | 2 | $99,747 | cluster_buy |
| ACON | 72 | corporate_insider | Gould Gregory A | 2 | $24,500 | cluster_buy,small_amount |
| EVLV | 72 | corporate_insider | Kuhl Henrik | 2 | $85,950 | cluster_buy |
| MLPT | 72 | corporate_insider | Catalyst4, Inc. | 0 | $50,072,000 | - |
| ELF | 72 | large_holder | Fenelon Opportunity Fund  |  | - | - |
| AMBQ | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| QDEL | 72 | large_holder | T. Rowe Price Investment  |  | - | - |

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

- SPY: 767.45 (-0.68% / -0.4% / 2.56%) [2026-08-18]
- QQQ: 717.51 (-1.69% / -0.13% / 1.2%) [2026-08-18]
- IWM: 300.23 (-1.26% / -0.25% / 1.24%) [2026-08-18]
- DIA: 532.91 (-0.24% / -0.81% / 2.19%) [2026-08-18]
- TLT: 81.66 (0.38% / -0.64% / -2.0%) [2026-08-18]
- IEF: 92.93 (0.1% / 0.06% / -0.07%) [2026-08-18]
- GLD: 398.55 (-1.71% / -0.6% / 6.33%) [2026-08-18]
- ^VIX: 15.44 (-2.53% / 6.12% / -7.21%) [2026-08-19]
- BTC-USD: 64888.15 (0.32% / 3.04% / 0.25%) [2026-08-19]

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

**Temas dominantes**: ai (2), leadership (2), legal (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [HIMS] Hims & Hers CEO on How Firms With Large Datasets Can Cut AI Costs (2026-08-19)
- [HIMS] Kessler Topaz Meltzer & Check , LLP Encourages Hims & Hers Health , Inc . ( NYSE : HIMS ) Investors to Contact the Firm (2026-08-19)
- [HIMS] Kessler Topaz Meltzer & Check , LLP Encourages Hims & Hers Health , Inc . ( NYSE : HIMS ) Investors to Contact the Firm (2026-08-19)
- [HIMS] Why Is Hims & Hers Health ( HIMS ) Facing A New Privacy Lawsuit ? (2026-08-18)
- [HIMS] Hims & Hers CEO Andrew Dudum talks FTC lawsuit , GLP - 1s , AI (2026-08-18)

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

- BOOMBOYS.Kiritych · PnL $22,036 · win rate 92% · categorias: sports
- torta.tech · PnL $13,986 · win rate 94% · categorias: sports
- ic4cream · PnL $27,884 · win rate 90% · categorias: sports
- jarosbill · PnL $22,706 · win rate 87% · categorias: sports
- BBQChickenisthebesttt · PnL $23,811 · win rate 83% · categorias: sports, crypto, economy

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `warning`
- **congress**: `warning` · 103 registros 30d · ultimo dato 2026-08-07 — invalid_tickers_present:A
- **sec_insiders**: `ok` · 867 registros 30d · ultimo dato 2026-08-18
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-18
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMBQ, CHRW, FWONK, GLD, IEF, LTH, MANE, NVRI, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
