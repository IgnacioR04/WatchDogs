# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-03T21:59:51+00:00 · ventana señales 2026-08-04 -> 2026-09-03_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.32)
- Tendencia: `bull` (SPY 773.17 · MA50 756.14 · MA200 709.32 · dist MA200: 9.0%)
- Credito: `tight` (HY spread 2.66)
- Tipos: `flat` (curva 10y-2y 0.43)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.17 | 1.05% | 0.27% | 0.6% |
| QQQ | 12.0% | core | 717.67 | 1.19% | -0.48% | 0.42% |
| TLT | 12.0% | core | 82.07 | 0.15% | -0.9% | -0.16% |
| ECAT | 12.0% | satellite | 15.29 | 0.33% | -0.84% | 0.22% |
| GLD | 9.9% | core | 410.22 | 1.85% | -2.93% | 5.27% |
| IEF | 6.6% | core | 92.28 | 0.11% | -0.66% | -0.36% |
| MD | 5.8% | satellite | 26.88 | 0.07% | 0.3% | 1.4% |
| AMRZ | 5.4% | satellite | 44.01 | 2.42% | -0.63% | -13.87% |
| STRT | 4.3% | satellite | 74.42 | 1.85% | 5.88% | -14.28% |
| BRBR | 2.5% | satellite | 10.4 | -2.99% | 1.36% | -14.12% |
| EQPT | 2.5% | satellite | 18.14 | 1.85% | -0.87% | -9.84% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.6%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -3.1%
- Beta vs SPY: 0.683 · posiciones efectivas: 12.3 · HHI: 0.0811

**Por que estos satellite (señales WATCHDOG):**

- **AMRZ** · score agregado 306.9 · 5 señales · fuentes: corporate_insider
- **MD** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **BRBR** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **EQPT** · score agregado 124.2 · 2 señales · fuentes: corporate_insider
- **ECAT** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **STRT** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GLOB | 72 | large_holder | PZENA INVESTMENT MANAGEME |  | - | - |
| AUTL | 72 | large_holder | Renata Kellnerova |  | - | - |
| APGE | 70 | large_holder | Fairmount Funds Managemen |  | - | - |
| MD | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| CALM | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| BRBR | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| MD | 70 | large_holder | Vanguard Capital Manageme |  | - | - |
| BRBR | 70 | large_holder | Vanguard Capital Manageme |  | - | - |
| VVOS | 70 | large_holder | Streeterville Capital LLC |  | - | - |
| XTIA | 70 | large_holder | Patrick Green Harrington |  | - | - |
| CINT | 70 | large_holder | Swedbank Robur Fonder AB |  | - | - |
| CRMT | 70 | large_holder | Magnolia Capital Fund, LP |  | - | - |
| JTTT | 70 | large_holder | RA Capital Management, L. |  | - | - |
| CISS | 70 | large_holder | HORNE TIMOTHY P |  | - | - |
| MOH | 70 | large_holder | Giovanni Agnelli B.V. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| LRCX | 58 | corporate_insider | Varadarajan Seshasayee | $8,005,474 | - |
| LRCX | 57 | corporate_insider | Varadarajan Seshasayee | $5,826,400 | - |
| NNE | 57 | corporate_insider | Yu Jiang | $5,801,799 | - |
| DASH | 56 | corporate_insider | Xu Tony | $3,833,443 | - |
| LRCX | 56 | corporate_insider | Varadarajan Seshasayee | $3,574,496 | - |
| FROG | 56 | corporate_insider | Shlomi Ben Haim | $3,369,868 | - |
| NNE | 55 | corporate_insider | Yu Jiang | $2,481,649 | - |
| DGX | 55 | corporate_insider | Davis J. E. | $2,427,200 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 773.17 (1.05% / 0.27% / 0.6%) [2026-09-03]
- QQQ: 717.67 (1.19% / -0.48% / 0.42%) [2026-09-03]
- IWM: 295.19 (0.4% / -1.54% / -1.03%) [2026-09-03]
- DIA: 536.93 (1.19% / 0.32% / -0.15%) [2026-09-03]
- TLT: 82.07 (0.15% / -0.9% / -0.16%) [2026-09-03]
- IEF: 92.28 (0.11% / -0.66% / -0.36%) [2026-09-03]
- GLD: 410.22 (1.85% / -2.93% / 5.27%) [2026-09-03]
- ^VIX: 14.32 (-5.79% / -1.31% / -5.48%) [2026-09-03]
- BTC-USD: 81567.6 (5.52% / 4.25% / 29.52%) [2026-09-03]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.39 (delta 1m: 0.19) [2026-09-02]
- Treasury 10Y yield: 4.79 (delta 1m: 0.16) [2026-09-02]
- Curva 10Y-2Y: 0.43 (delta 1m: -0.02) [2026-09-03]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.66 (delta 1m: -0.07) [2026-09-02]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.35 (delta 1m: 0.13) [2026-09-03]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (3), leadership (1), stock (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TDOC] Teladoc Health Appoints Michael Grasher As Chief Financial Officer ; Stock Down (2026-08-31)
- [LTRX] Lantronix Q4 Earnings Call Highlights (2026-08-28)
- [TDOC] INVESTOR ALERT : Pomerantz Law Firm Investigates Claims On Behalf of Investors of Teladoc Health , Inc . (2026-08-27)
- [TDOC] INVESTOR ALERT : Pomerantz Law Firm Investigates Claims On Behalf of Investors of Teladoc Health , Inc . (2026-08-27)
- [LTRX] Lantronix , Inc . ( NASDAQ : LTRX ) Receives $10 . 40 Consensus Price Target from Brokerages (2026-08-27)
- [LTRX] Contrasting China Techfaith Wireless Communication Technology ( OTCMKTS : CNTFY ) and Lantronix ( NASDAQ : LTRX ) (2026-08-21)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Varadarajan Seshasayee vendio LRCX por $8.0M el 2026-09-02.
- CEO Barber James J. compro VSTS por $1.0M el 2026-09-02.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.
- Institutional manager Geode Capital Management LLC vendio ELI LILLY & CO por $13.2B.

**Polymarket — smart money (traders con mejor track record):**

- ExplosiveNinja · PnL $73,029 · win rate 97% · categorias: sports
- JnStrtPrdctnMrkts · PnL $133,495 · win rate 90% · categorias: crypto
- kekasaur · PnL $71,779 · win rate 94% · categorias: sports
- theowalcott · PnL $29,710 · win rate 100% · categorias: sports
- 0xa68c732b · PnL $29,737 · win rate 99% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 742 registros 30d · ultimo dato 2026-09-03
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-03
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMRZ, BRBR, ECAT, EQPT, GLD, IEF, MD, QQQ, SPY, STRT, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
