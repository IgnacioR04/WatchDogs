# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-03T19:01:44+00:00 · ventana señales 2026-08-04 -> 2026-09-03_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.49)
- Tendencia: `bull` (SPY 773.53 · MA50 756.15 · MA200 709.32 · dist MA200: 9.05%)
- Credito: `tight` (HY spread 2.66)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.53 | 1.09% | 0.32% | 0.65% |
| QQQ | 12.0% | core | 718.45 | 1.3% | -0.37% | 0.53% |
| TLT | 12.0% | core | 82.18 | 0.29% | -0.76% | -0.02% |
| ECAT | 10.8% | satellite | 15.3 | 0.36% | -0.81% | 0.25% |
| GLD | 9.3% | core | 410.17 | 1.83% | -2.94% | 5.26% |
| IEF | 6.2% | core | 92.33 | 0.17% | -0.6% | -0.3% |
| AMRZ | 4.2% | satellite | 43.81 | 1.95% | -1.08% | -14.26% |
| STRT | 3.3% | satellite | 75.21 | 2.93% | 7.0% | -13.37% |
| MAX | 3.2% | satellite | 12.16 | -2.95% | -3.26% | -1.46% |
| DT | 3.2% | satellite | 52.95 | 4.09% | -0.9% | 8.35% |
| BRBR | 3.0% | satellite | 10.53 | -1.78% | 2.62% | -13.06% |
| GLOB | 2.8% | satellite | 40.54 | 4.27% | 0.92% | 8.83% |
| VICR | 1.9% | satellite | 179.52 | -1.14% | -11.84% | -17.92% |
| SUJA | 1.1% | satellite | 10.7 | 4.7% | 18.89% | 68.5% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.6%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 1.0%
- Max drawdown historico: -2.1%
- Beta vs SPY: 0.641 · posiciones efectivas: 13.4 · HHI: 0.0745

**Por que estos satellite (señales WATCHDOG):**

- **AMRZ** · score agregado 306.9 · 5 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **BRBR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **VICR** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **DT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GLOB** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MAX** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **ECAT** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **STRT** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GROV | 76 | corporate_insider | Yurcisin Jeffrey Michael | 2 | $94,689 | cluster_buy |
| OPAL | 76 | corporate_insider | Comora Adam | 2 | $96,500 | cluster_buy |
| VICR | 72 | large_holder | JPMORGAN CHASE & CO. |  | - | - |
| DT | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| GLOB | 72 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |
| EMPD | 72 | large_holder | Streeterville Capital LLC |  | - | - |
| CLST | 72 | large_holder | Stilwell Activist Fund, L |  | - | - |
| TENX | 72 | large_holder | Sphera Funds Management L |  | - | - |
| TENX | 72 | large_holder | ING Groep N.V. |  | - | - |
| MAX | 72 | large_holder | Eugene Nonko |  | - | - |
| GROV | 71 | corporate_insider | Karp Jason H. | 2 | $56,529 | cluster_buy |
| BRBR | 70 | large_holder | Vanguard Capital Manageme |  | - | - |
| CINT | 70 | large_holder | Swedbank Robur Fonder AB |  | - | - |
| CRMT | 70 | large_holder | Magnolia Capital Fund, LP |  | - | - |
| CISS | 70 | large_holder | HORNE TIMOTHY P |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| WHD | 58 | corporate_insider | Bender Joel | $7,037,200 | - |
| WHD | 58 | corporate_insider | Bender Scott | $7,037,200 | - |
| AMBQ | 56 | corporate_insider | Esaka Fumihide | $2,761,534 | - |
| WAY | 55 | corporate_insider | Hawkins Matthew J. | $2,142,583 | - |
| MRVL | 55 | corporate_insider | Koopmans Chris | $2,032,700 | - |
| OKLO | 54 | corporate_insider | DeWitte Jacob | $1,536,000 | - |
| OKLO | 54 | corporate_insider | DeWitte Jacob | $1,546,400 | - |
| RDDT | 54 | corporate_insider | Huffman Steve Ladd | $1,506,132 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.53 (1.09% / 0.32% / 0.65%) [2026-09-03]
- QQQ: 718.45 (1.3% / -0.37% / 0.53%) [2026-09-03]
- IWM: 294.94 (0.32% / -1.62% / -1.11%) [2026-09-03]
- DIA: 536.79 (1.16% / 0.29% / -0.18%) [2026-09-03]
- TLT: 82.18 (0.29% / -0.76% / -0.02%) [2026-09-03]
- IEF: 92.33 (0.17% / -0.6% / -0.3%) [2026-09-03]
- GLD: 410.17 (1.83% / -2.94% / 5.26%) [2026-09-03]
- ^VIX: 14.49 (-4.67% / -0.14% / -4.36%) [2026-09-03]
- BTC-USD: 81275.18 (5.14% / 3.87% / 29.06%) [2026-09-03]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.39 (delta 1m: 0.14) [2026-09-01]
- Treasury 10Y yield: 4.79 (delta 1m: 0.09) [2026-09-01]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.03) [2026-09-02]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.66 (delta 1m: -0.07) [2026-09-02]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.11) [2026-09-02]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (1), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TDUP] Contrasting ThredUp ( NASDAQ : TDUP ) and Chow Tai Fook ( OTCMKTS : CJEWY ) (2026-09-03)
- [IVZ] Invesco Ltd . - Invesco Ltd : Form 8 . 3 - Bodycote PLC ; Public dealing disclosure (2026-09-03)
- [CNO] CNO Financial Group ( NYSE : CNO ) Insider Sells $360 , 734 . 40 in Stock (2026-09-02)
- [CNO] CNO Financial Group ( NYSE : CNO ) Insider Karen Detoro Sells 9 , 336 Shares of Stock (2026-09-02)
- [MBGL] Mobility Global ( NYSE : MBGL ) Stock Sold Rep . Kelly Morrison (2026-08-27)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Williams Charles Alan compro NPB por $1.4M el 2026-09-01.
- CEO Bender Joel vendio WHD por $7.0M el 2026-09-01.
- 10% owner Empery Asset Management, LP compro EMPD por $1.8M el 2026-09-01 [senal en multiples fuentes].
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- kekasaur · PnL $71,779 · win rate 94% · categorias: sports
- ExplosiveNinja · PnL $47,848 · win rate 97% · categorias: sports
- theowalcott · PnL $29,710 · win rate 100% · categorias: sports
- JnStrtPrdctnMrkts · PnL $129,519 · win rate 90% · categorias: crypto
- 0xa68c732b · PnL $28,993 · win rate 99% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 591 registros 30d · ultimo dato 2026-09-03
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-03
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMRZ, BRBR, DT, ECAT, GLD, GLOB, IEF, MAX, QQQ, SPY, STRT, SUJA, TLT, VICR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **95.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
