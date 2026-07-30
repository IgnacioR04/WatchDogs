# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-30T19:06:28+00:00 · ventana señales 2026-06-30 -> 2026-07-30_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.72)
- Tendencia: `neutral` (SPY 741.23 · MA50 743.91 · MA200 696.96 · dist MA200: 6.35%)
- Credito: `tight` (HY spread 2.87)
- Tipos: `flat` (curva 10y-2y 0.45)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 741.23 | 1.61% | 0.41% | -0.61% |
| QQQ | 9.8% | core | 682.78 | 3.18% | -1.33% | -5.85% |
| TLT | 9.8% | core | 82.81 | -0.05% | -0.44% | -3.17% |
| GLD | 7.3% | core | 376.41 | 1.44% | 1.32% | 1.57% |
| BEP | 7.0% | satellite | 32.67 | 3.22% | -1.21% | -4.95% |
| EQBK | 6.3% | satellite | 50.96 | 0.47% | 2.8% | 1.51% |
| ZTS | 5.6% | satellite | 76.1 | -2.35% | 2.05% | 5.77% |
| IEF | 4.9% | core | 93.24 | 0.08% | 0.42% | -0.84% |
| VSXY | 3.1% | satellite | 88.69 | -0.49% | 7.13% | 14.13% |
| REAL | 2.7% | satellite | 12.05 | 3.04% | 5.94% | -1.27% |
| SPCX | 1.5% | satellite | 111.94 | -0.54% | -5.33% | -28.94% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 7.8%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 0.8%
- Max drawdown historico: -2.8%
- Beta vs SPY: 0.466 · posiciones efectivas: 18.1 · HHI: 0.0552

**Por que estos satellite (señales WATCHDOG):**

- **SPCX** · score agregado 241.4 · 4 señales · fuentes: congress
- **ZTS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **REAL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **VSXY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress
- **EQBK** · score agregado 55.0 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| [NONE] | 84 | corporate_insider | VEP Group, LLC | 2 | $6,229,807 | cluster_buy |
| STRL | 72 | large_holder | BlackRock, Inc. |  | - | - |
| SMTC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| SRPT | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ZTS | 72 | large_holder | BlackRock, Inc. |  | - | - |
| WDAY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| VOYG | 72 | large_holder | BlackRock, Inc. |  | - | - |
| VLTO | 72 | large_holder | BlackRock, Inc. |  | - | - |
| REAL | 72 | large_holder | BlackRock, Inc. |  | - | - |
| VSXY | 72 | large_holder | BBFIT INVESTMENTS PTE LTD |  | - | - |
| PPIH | 72 | large_holder | BlackRock, Inc. |  | - | - |
| PEBK | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NPKI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| LHX | 72 | large_holder | BlackRock, Inc. |  | - | - |
| REKR | 70 | large_holder | Maybank Securities Pte. L |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| GOOGL | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CRDO | 62 | congress | Gilbert Cisneros | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 741.23 (1.61% / 0.41% / -0.61%) [2026-07-30]
- QQQ: 682.78 (3.18% / -1.33% / -5.85%) [2026-07-30]
- IWM: 292.05 (1.21% / -0.01% / -2.43%) [2026-07-30]
- DIA: 521.67 (1.21% / 1.05% / -0.11%) [2026-07-30]
- TLT: 82.81 (-0.05% / -0.44% / -3.17%) [2026-07-30]
- IEF: 93.24 (0.08% / 0.42% / -0.84%) [2026-07-30]
- GLD: 376.41 (1.44% / 1.32% / 1.57%) [2026-07-30]
- ^VIX: 17.72 (-14.23% / -5.24% / 6.81%) [2026-07-30]
- BTC-USD: 64700.25 (1.24% / 0.6% / 0.89%) [2026-07-30]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.26 (delta 1m: 0.19) [2026-07-28]
- Treasury 10Y yield: 4.61 (delta 1m: 0.23) [2026-07-28]
- Curva 10Y-2Y: 0.45 (delta 1m: 0.17) [2026-07-29]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.87 (delta 1m: 0.12) [2026-07-29]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.26 (delta 1m: 0.04) [2026-07-29]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: merger (3), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [GM] Ford deal sets stage for tougher talks with GM , Stellantis : Experts (2026-07-30)
- [CRWV] CoreWeave & Leidos are building a classified AI cloud for US spies (2026-07-30)
- [GM] Ford deal sets stage for tougher talks with GM , Stellantis : Experts (2026-07-30)
- [GM] Ford deal sets stage for tougher talks with GM , Stellantis : Experts (2026-07-30)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner BBRC INTERNATIONAL PTE LTD vendio VSXY por $64.0M el 2026-07-28 [senal en multiples fuentes].
- 10% owner Gebbia Joseph vendio ABNB por $175.2M el 2026-07-28.
- 10% owner ADVENT INTERNATIONAL, L.P. vendio LUNR por $147.6M el 2026-07-28.
- CEO Huang Jack Jiajia compro COE por $7.7M el 2026-07-27.
- 10% owner Abu Dhabi Investment Authority compro Overland Advantage por $22.9M el 2026-07-28.
- 10% owner VEP Group, LLC compro [NONE] por $6.2M el 2026-07-29.
- CEO Huang Jack Jiajia compro COE por $3.0M el 2026-07-24.
- CEO Barra Mary T vendio GM por $9.8M el 2026-07-28.

**Polymarket — smart money (traders con mejor track record):**

- 0xE16D3F2A5807999b358aFfD9445C3a09E45E5e30-1776429210592 · PnL $89,255 · win rate 96% · categorias: sports
- 111111111115 · PnL $77,372 · win rate 94% · categorias: sports
- 0xe11Ff8cd2718F51a4d9403D166c20eaAAbE253F4-1777047101622 · PnL $77,786 · win rate 89% · categorias: sports, crypto
- JnStTrdrBnusFnd · PnL $49,670 · win rate 91% · categorias: crypto
- 0x27c5C1EEE404a07F39FE70078AFf815E5a656D61-1763107503028 · PnL $80,189 · win rate 88% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 47 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 729 registros 30d · ultimo dato 2026-07-30
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-30
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, EQBK, GLD, IEF, QQQ, REAL, SPCX, SPY, TLT, VSXY, ZTS`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
