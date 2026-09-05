# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-05T00:20:27+00:00 · ventana señales 2026-08-06 -> 2026-09-05_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.53)
- Tendencia: `bull` (SPY 773.17 · MA50 756.14 · MA200 709.32 · dist MA200: 9.0%)
- Credito: `tight` (HY spread 2.65)
- Tipos: `flat` (curva 10y-2y 0.41)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 773.17 | 1.05% | 0.27% | 0.6% |
| QQQ | 12.0% | core | 717.67 | 1.19% | -0.48% | 0.42% |
| TLT | 12.0% | core | 82.07 | 0.15% | -0.9% | -0.16% |
| GLD | 9.3% | core | 410.22 | 1.85% | -2.93% | 5.27% |
| DGICA | 8.0% | satellite | 19.42 | 0.36% | 2.32% | -0.56% |
| IEF | 6.2% | core | 92.28 | 0.11% | -0.66% | -0.36% |
| MD | 4.9% | satellite | 26.88 | 0.07% | 0.3% | 1.4% |
| KIDS | 4.2% | satellite | 22.59 | -0.92% | -3.13% | -1.05% |
| ETOR | 3.5% | satellite | 32.75 | 2.83% | 1.55% | -7.69% |
| BILL | 3.4% | satellite | 50.86 | 4.31% | 4.07% | 8.21% |
| GAP | 3.3% | satellite | 22.32 | 1.18% | 7.36% | 8.77% |
| FRNM | 3.3% | satellite | 16.9 | 5.96% | 21.23% | 54.9% |
| BRBR | 2.8% | satellite | 10.4 | -2.99% | 1.36% | -14.12% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.1%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -2.3%
- Beta vs SPY: 0.519 · posiciones efectivas: 13.9 · HHI: 0.0717

**Por que estos satellite (señales WATCHDOG):**

- **MD** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **BRBR** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **GAP** · score agregado 210.6 · 3 señales · fuentes: large_holder
- **DGICA** · score agregado 119.8 · 2 señales · fuentes: corporate_insider
- **BILL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **FRNM** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KIDS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **ETOR** · score agregado 67.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SMID | 75 | corporate_insider | SMITH ASHLEY B | 2 | $53,740 | cluster_buy |
| CSBB | 74 | corporate_insider | STEINER EDDIE L | 2 | $36,755 | cluster_buy |
| BILL | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NPCE | 72 | large_holder | First Light Asset Managem |  | - | - |
| UEIC | 72 | large_holder | Ameriprise Financial, Inc |  | - | - |
| FRNM | 72 | large_holder | Roche Holdings, Inc. |  | - | - |
| ZNB | 72 | large_holder | L1 Capital Global Opportu |  | - | - |
| SMID | 71 | corporate_insider | Smith Matthew I | 2 | $54,300 | cluster_buy |
| EROC | 70 | large_holder | McAndrew Walter Thomas Jr |  | - | - |
| MAC | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| TENB | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| SIG | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| GAU | 70 | large_holder | BlackRock Portfolio Manag |  | - | - |
| MYGN | 70 | large_holder | BlackRock Portfolio Manag |  | - | - |
| ADIG | 70 | large_holder | BlackRock, Inc. |  | - | - |

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

- SPY: 773.17 (1.05% / 0.27% / 0.6%) [2026-09-03]
- QQQ: 717.67 (1.19% / -0.48% / 0.42%) [2026-09-03]
- IWM: 295.19 (0.4% / -1.54% / -1.03%) [2026-09-03]
- DIA: 536.93 (1.19% / 0.32% / -0.15%) [2026-09-03]
- TLT: 82.07 (0.15% / -0.9% / -0.16%) [2026-09-03]
- IEF: 92.28 (0.11% / -0.66% / -0.36%) [2026-09-03]
- GLD: 410.22 (1.85% / -2.93% / 5.27%) [2026-09-03]
- ^VIX: 14.53 (1.47% / 0.69% / -2.48%) [2026-09-04]
- BTC-USD: 79637.62 (-2.01% / 2.54% / 26.36%) [2026-09-05]

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

**Temas dominantes**: stock (3), leadership (2), regulatory (2), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [HOOD] Robinhood Rallies 11 % on Price Target Hikes , Webull Climbs 7 %, Interactive Brokers Gains 4 % (2026-09-04)
- [HOOD] Why Robinhood Stock Is Falling Today (2026-09-04)
- [HOOD] AMC Rises 6 % as CEO Blasts Tokenized Shares , Robinhood Slips (2026-09-04)
- [HOOD] AMC Rises 6 % as CEO Blasts Tokenized Shares , Robinhood Slips (2026-09-04)
- [UTHR] Former Anheuser - Busch plant sold to United Therapeutics (2026-09-03)
- [UTHR] Anheuser - Busch plant in Merrimack sold to United Therapeutics for $47 . 5M (2026-09-02)
- [UTHR] United Therapeutics Announces FDA Acceptance Of SNDA For Nebulized Tyvaso In IPF (2026-09-02)
- [UTHR] Anheuser - Busch plant in Merrimack sold to United Therapeutics for $47 . 5M (2026-09-02)
- [UTHR] United Therapeutics highlights new data supporting two FDA filings ( UTHR : NASDAQ ) (2026-08-31)
- [KRYS] OMERS ADMINISTRATION Corp Takes $1 . 44 Million Position in Krystal Biotech , Inc . $KRYS (2026-08-27)

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

- HongYunX · PnL $44,524 · win rate 100% · categorias: sports
- ExplosiveNinja · PnL $46,124 · win rate 97% · categorias: sports
- TheyAreTakingTheHobitsToIsengard · PnL $38,420 · win rate 98% · categorias: sports
- salahmh · PnL $40,474 · win rate 93% · categorias: sports
- sbimbg · PnL $38,085 · win rate 92% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 676 registros 30d · ultimo dato 2026-09-04
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-04
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BILL, BRBR, DGICA, ETOR, FRNM, GAP, GLD, IEF, KIDS, MD, QQQ, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
