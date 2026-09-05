# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-05T12:58:47+00:00 · ventana señales 2026-08-06 -> 2026-09-05_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.53)
- Tendencia: `bull` (SPY 770.19 · MA50 756.86 · MA200 709.87 · dist MA200: 8.5%)
- Credito: `tight` (HY spread 2.65)
- Tipos: `flat` (curva 10y-2y 0.41)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 770.19 | -0.39% | 0.11% | -0.4% |
| QQQ | 12.0% | core | 718.96 | 0.18% | 0.35% | -0.56% |
| TLT | 12.0% | core | 82.21 | 0.17% | -0.43% | -0.28% |
| GLD | 9.3% | core | 406.77 | -0.84% | -0.52% | 2.08% |
| IEF | 6.2% | core | 92.25 | -0.03% | -0.29% | -0.63% |
| MD | 6.0% | satellite | 27.03 | 0.56% | 1.58% | -0.18% |
| KIDS | 5.1% | satellite | 22.41 | -0.8% | -5.24% | -1.58% |
| ETOR | 4.3% | satellite | 32.47 | -0.85% | 4.64% | -7.86% |
| BILL | 4.1% | satellite | 49.16 | -3.34% | -2.29% | 2.44% |
| GAP | 4.1% | satellite | 22.43 | 0.49% | -4.47% | 9.57% |
| LILA | 3.7% | satellite | 8.52 | -2.85% | -0.47% | 0.12% |
| BRBR | 3.4% | satellite | 10.39 | -0.1% | -2.81% | -10.12% |
| ENOV | 2.7% | satellite | 18.56 | -4.33% | -25.46% | -30.25% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.9%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.3%
- Max drawdown historico: -2.7%
- Beta vs SPY: 0.563 · posiciones efectivas: 14.2 · HHI: 0.0705

**Por que estos satellite (señales WATCHDOG):**

- **ENOV** · score agregado 223.2 · 3 señales · fuentes: corporate_insider
- **MD** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **BRBR** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **GAP** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **LILA** · score agregado 188.8 · 3 señales · fuentes: corporate_insider
- **BILL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KIDS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **ETOR** · score agregado 67.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| ENOV | 78 | corporate_insider | McDonald Damien | 2 | $249,620 | cluster_buy |
| SMID | 75 | corporate_insider | SMITH ASHLEY B | 2 | $53,740 | cluster_buy |
| CSBB | 74 | corporate_insider | STEINER EDDIE L | 2 | $36,755 | cluster_buy |
| ENOV | 73 | corporate_insider | Engert Oliver | 2 | $100,024 | cluster_buy |
| BILL | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NPCE | 72 | large_holder | First Light Asset Managem |  | - | - |
| UEIC | 72 | large_holder | Ameriprise Financial, Inc |  | - | - |
| FRNM | 72 | large_holder | Roche Holdings, Inc. |  | - | - |
| ZNB | 72 | large_holder | L1 Capital Global Opportu |  | - | - |
| ENOV | 72 | corporate_insider | Engert Oliver | 2 | $49,947 | cluster_buy |
| SMID | 71 | corporate_insider | Smith Matthew I | 2 | $54,300 | cluster_buy |
| EROC | 70 | large_holder | McAndrew Walter Thomas Jr |  | - | - |
| MAC | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| TENB | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| SIG | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| CAI | 58 | corporate_insider | Spetzler David Baxley | $9,733,313 | - |
| NMIH | 58 | corporate_insider | Pollitzer Adam | $7,746,728 | - |
| DDOG | 57 | corporate_insider | Pomel Olivier | $5,605,978 | - |
| BILL | 57 | corporate_insider | Lacerte Rene A. | $4,902,228 | - |
| ILMN | 56 | corporate_insider | Meister Keith A. | $21,980,954 | - |
| PARR | 56 | corporate_insider | Monteleone William | $3,252,000 | - |
| CAI | 56 | corporate_insider | Spetzler David Baxley | $2,951,117 | - |
| RKLB | 56 | corporate_insider | Spice Adam C. | $4,590,542 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 770.19 (-0.39% / 0.11% / -0.4%) [2026-09-04]
- QQQ: 718.96 (0.18% / 0.35% / -0.56%) [2026-09-04]
- IWM: 296.01 (0.28% / 0.09% / -1.84%) [2026-09-04]
- DIA: 534.08 (-0.53% / -0.18% / -0.94%) [2026-09-04]
- TLT: 82.21 (0.17% / -0.43% / -0.28%) [2026-09-04]
- IEF: 92.25 (-0.03% / -0.29% / -0.63%) [2026-09-04]
- GLD: 406.77 (-0.84% / -0.52% / 2.08%) [2026-09-04]
- ^VIX: 14.53 (1.47% / 0.69% / -2.48%) [2026-09-04]
- BTC-USD: 79736.27 (0.08% / 1.51% / 26.93%) [2026-09-05]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.34 (delta 1m: 0.16) [2026-09-03]
- Treasury 10Y yield: 4.77 (delta 1m: 0.14) [2026-09-03]
- Curva 10Y-2Y: 0.41 (delta 1m: -0.03) [2026-09-04]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.65 (delta 1m: -0.1) [2026-09-03]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.35 (delta 1m: 0.09) [2026-09-04]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: legal (2), stock (1), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [FCF] First Commonwealth Financial ( NYSE : FCF ) CFO James Reske Sells 2 , 072 Shares of Stock (2026-09-05)
- [ADXN] Contrasting Addex Therapeutics ( NASDAQ : ADXN ) & BioAge Labs ( NASDAQ : BIOA ) (2026-09-05)
- [CRWD] Jim Cramer Explains Why CrowdStrike ( CRWD ) Upended the Tech Bear Thesis (2026-09-05)
- [CRWD] CrowdStrike Probes Falcon Zero - Day Exploit Code (2026-09-05)
- [CRWD] CrowdStrike Probes Falcon Zero - Day Exploit Code (2026-09-04)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Spetzler David Baxley vendio CAI por $9.7M el 2026-09-03.
- CEO Pollitzer Adam vendio NMIH por $7.7M el 2026-09-04.
- CEO Lacerte Rene A. vendio BILL por $4.9M el 2026-09-02 [senal en multiples fuentes].
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- HongYunX · PnL $24,268 · win rate 100% · categorias: sports
- 0b1 · PnL $60,289 · win rate 90% · categorias: sports, crypto
- Kosherlocks · PnL $18,939 · win rate 96% · categorias: sports, crypto
- MissingJoy · PnL $23,522 · win rate 87% · categorias: sports, crypto
- zofgkt1111 · PnL $21,464 · win rate 86% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 678 registros 30d · ultimo dato 2026-09-04
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-04
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BILL, BRBR, ENOV, ETOR, GAP, GLD, IEF, KIDS, LILA, MD, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
