# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-07T07:29:46+00:00 · ventana señales 2026-09-07 -> 2026-10-07_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.01)
- Tendencia: `bull` (SPY 779.09 · MA50 763.82 · MA200 718.13 · dist MA200: 8.49%)
- Credito: `normal` (HY spread 3.12)
- Tipos: `flat` (curva 10y-2y 0.48)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 779.09 | 0.55% | 1.95% | 1.97% |
| QQQ | 11.4% | core | 759.66 | 0.46% | 2.94% | 5.86% |
| TLT | 11.4% | core | 77.28 | 0.22% | -0.82% | -5.61% |
| GLD | 8.6% | core | 382.27 | 0.72% | -0.16% | -4.37% |
| PSUS | 8.3% | satellite | 37.74 | 1.04% | 3.0% | -0.87% |
| IEF | 5.7% | core | 89.13 | 0.24% | -0.01% | -2.95% |
| LWAY | 4.3% | satellite | 20.46 | -2.57% | -3.22% | -18.0% |
| TOST | 4.3% | satellite | 30.25 | 0.7% | -0.69% | -9.13% |
| SAH | 3.9% | satellite | 61.0 | -2.6% | 1.92% | -19.3% |
| AVR | 3.6% | satellite | 7.05 | -6.62% | -7.11% | -18.21% |
| ESTC | 3.3% | satellite | 94.6 | -0.33% | 6.53% | 6.99% |
| DKS | 3.2% | satellite | 134.88 | -1.64% | 0.13% | 2.86% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.1%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -5.8%
- Beta vs SPY: 0.651 · posiciones efectivas: 15.0 · HHI: 0.0666

**Por que estos satellite (señales WATCHDOG):**

- **PSUS** · score agregado 193.6 · 3 señales · fuentes: corporate_insider
- **LWAY** · score agregado 187.8 · 3 señales · fuentes: corporate_insider
- **AVR** · score agregado 131.7 · 2 señales · fuentes: corporate_insider
- **SAH** · score agregado 128.6 · 2 señales · fuentes: corporate_insider
- **ESTC** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **TOST** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **DKS** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| ESTC | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| TOST | 72 | large_holder | BlackRock, Inc. |  | - | - |
| DKS | 72 | large_holder | BlackRock, Inc. |  | - | - |
| EVGN | 70 | large_holder | L.I.A. Pure Capital Ltd. |  | - | - |
| AGMH | 70 | large_holder | Rui Zhang |  | - | - |
| IESC | 70 | large_holder | Tontine Capital Partners, |  | - | - |
| QRVO | 70 | large_holder | Starboard Value LP |  | - | - |
| ZCSH | 70 | large_holder | Karminski Michal Adam |  | - | - |
| HGTY | 70 | large_holder | Neuberger Berman Group LL |  | - | - |
| XPER | 70 | large_holder | Neuberger Berman Group LL |  | - | - |
| AWR | 70 | large_holder | Neuberger Berman Group LL |  | - | - |
| TTI | 70 | large_holder | Neuberger Berman Group LL |  | - | - |
| SWKS | 70 | large_holder | Capital World Investors |  | - | - |
| AUGO | 70 | large_holder | Capital World Investors |  | - | - |
| RCL | 70 | large_holder | Capital Research Global I |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MDLN | 61 | corporate_insider | GIC Private Ltd | $251,764,606 | - |
| MDLN | 61 | corporate_insider | GIC Private Ltd | $245,354,485 | - |
| RITE | 61 | corporate_insider | Hendricks Lloyd Bernard I | $106,724,935 | - |
| MDLN | 61 | corporate_insider | GIC Private Ltd | $90,884,815 | - |
| MDLN | 61 | corporate_insider | GIC Private Ltd | $73,218,994 | - |
| MDLN | 60 | corporate_insider | GIC Private Ltd | $60,421,328 | - |
| ESTC | 59 | corporate_insider | Schuurman Steven | $135,195,000 | - |
| S | 59 | corporate_insider | Weingarten Tomer | $13,323,531 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 779.09 (0.55% / 1.95% / 1.97%) [2026-10-06]
- QQQ: 759.66 (0.46% / 2.94% / 5.86%) [2026-10-06]
- IWM: 281.34 (-0.72% / 0.84% / -4.27%) [2026-10-06]
- DIA: 514.56 (0.48% / 0.33% / -2.33%) [2026-10-06]
- TLT: 77.28 (0.22% / -0.82% / -5.61%) [2026-10-06]
- IEF: 89.13 (0.24% / -0.01% / -2.95%) [2026-10-06]
- GLD: 382.27 (0.72% / -0.16% / -4.37%) [2026-10-06]
- ^VIX: 15.01 (-3.29% / -6.42% / -4.52%) [2026-10-06]
- BTC-USD: 84194.51 (-1.59% / -0.36% / 10.2%) [2026-10-07]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.84 (delta 1m: 0.5) [2026-10-05]
- Treasury 10Y yield: 5.31 (delta 1m: 0.54) [2026-10-05]
- Curva 10Y-2Y: 0.48 (delta 1m: 0.07) [2026-10-06]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.12 (delta 1m: 0.44) [2026-10-05]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.36 (delta 1m: 0.01) [2026-10-06]
- Dolar broad index: 121.3848 (delta 1m: 2.855) [2026-10-02]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (2), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [NBIS] Nebius Group ( NASDAQ : NBIS ) Stock : Insider John Wilson Iv Boynton Sells 50 Shares (2026-10-01)
- [ENS] Baystreet . ca - EnerSys Dips on Cordex Word (2026-09-29)
- [NBIS] Could Palantir ( PLTR ) Partnership with Nebius Group ( NBIS ) Accelerate its AI Growth ? (2026-09-24)
- [AMBQ] Alpha and Omega Semiconductor ( NASDAQ : AOSL ) vs . Ambiq Micro ( NYSE : AMBQ ) Head to Head Contrast (2026-09-24)
- [NBIS] Nebius Group ( NASDAQ : NBIS ) Trading Down 4 % – Here What Happened (2026-09-23)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner GIC Private Ltd vendio MDLN por $251.8M el 2026-10-06.
- 10% owner Hendricks Lloyd Bernard III opero RITE por $103.5M el 2026-09-30.
- 10% owner GIC Private Ltd vendio MDLN por $60.4M el 2026-10-05.
- 10% owner WOLTOSZ WALTER S vendio SLP por $59.2M el 2026-10-06.
- Director Schuurman Steven vendio ESTC por $135.2M el 2026-10-05 [senal en multiples fuentes].
- 10% owner GIC Private Ltd vendio MDLN por $245.4M el 2026-10-02.
- CEO Weingarten Tomer vendio S por $13.3M el 2026-10-05.
- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro Keenova Therapeutics plc por $42.1M el 2026-09-24.

**Polymarket — smart money (traders con mejor track record):**

- 0x16bb9951a36fce71e2ef57890b786145e0ba8492 · PnL $71,044 · win rate 95% · categorias: sports
- Kosherlocks · PnL $13,274 · win rate 96% · categorias: sports, crypto
- royalestake · PnL $11,331 · win rate 97% · categorias: sports, crypto
- OhWhenTheReds · PnL $100,629 · win rate 100% · categorias: sports
- 0xb4F978BE63cDF75554b0B46a4262a6dB597cc9A7-1779258330186 · PnL $37,828 · win rate 88% · categorias: sports, crypto, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 641 registros 30d · ultimo dato 2026-10-06
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-06
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AVR, DKS, ESTC, GLD, IEF, LWAY, PSUS, QQQ, SAH, SPY, TLT, TOST`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
