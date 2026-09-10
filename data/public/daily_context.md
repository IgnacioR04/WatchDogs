# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-10T05:02:04+00:00 · ventana señales 2026-08-11 -> 2026-09-10_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.46)
- Tendencia: `bull` (SPY 762.4 · MA50 758.02 · MA200 710.95 · dist MA200: 7.24%)
- Credito: `tight` (HY spread 2.67)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 762.4 | -0.46% | 0.08% | -1.06% |
| QQQ | 12.0% | core | 716.31 | -0.29% | 1.23% | -0.3% |
| TLT | 12.0% | core | 81.73 | -0.57% | -0.17% | -0.18% |
| CSQ | 11.5% | satellite | 20.85 | -0.62% | 0.58% | 0.5% |
| GLD | 9.3% | core | 403.35 | 0.91% | 1.66% | 0.6% |
| BWFG | 6.9% | satellite | 66.71 | 0.83% | 1.91% | -1.88% |
| IEF | 6.2% | core | 91.9 | -0.28% | -0.22% | -0.69% |
| DT | 3.7% | satellite | 50.6 | 0.62% | -4.28% | 1.89% |
| GOLD | 3.0% | satellite | 49.33 | 3.92% | 14.3% | 13.56% |
| WDAY | 2.4% | satellite | 186.05 | -0.12% | -6.22% | 2.64% |
| SLGL | 2.2% | satellite | 69.18 | -0.27% | -0.49% | -11.22% |
| SMTC | 1.7% | satellite | 163.94 | 0.81% | 23.94% | 24.97% |
| ALMS | 1.1% | satellite | 9.8 | -7.37% | 3.48% | -61.37% |
| MFP | 1.0% | satellite | 42.75 | -0.37% | -3.28% | -4.89% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.4%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -2.5%
- Beta vs SPY: 0.702 · posiciones efectivas: 12.9 · HHI: 0.0776

**Por que estos satellite (señales WATCHDOG):**

- **SLGL** · score agregado 293.3 · 5 señales · fuentes: corporate_insider
- **ALMS** · score agregado 254.6 · 4 señales · fuentes: corporate_insider
- **CSQ** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **BWFG** · score agregado 74.3 · 1 señales · fuentes: corporate_insider
- **DT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **MFP** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **SMTC** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WDAY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **GOLD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| PRTS | 83 | corporate_insider | Meniane David | 3 | $353,239 | cluster_buy |
| PRTS | 82 | corporate_insider | Meniane David | 3 | $203,288 | cluster_buy |
| PRTS | 82 | corporate_insider | Meniane David | 3 | $192,713 | cluster_buy |
| PRTS | 78 | corporate_insider | Huffaker Michael | 3 | $352,631 | cluster_buy |
| PRTS | 77 | corporate_insider | Huffaker Michael | 3 | $203,063 | cluster_buy |
| PRTS | 77 | corporate_insider | Huffaker Michael | 3 | $192,768 | cluster_buy |
| PRTS | 76 | corporate_insider | PHELPS BARRY | 3 | $64,152 | cluster_buy |
| BWFG | 74 | corporate_insider | Dale Eric J | 4 | $35,568 | cluster_buy |
| BWFG | 73 | corporate_insider | Porto Carl M | 4 | $21,945 | cluster_buy,small_amount |
| BWFG | 73 | corporate_insider | Dunne Jeffrey R | 4 | $17,516 | cluster_buy,small_amount |
| DT | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| MFP | 72 | large_holder | T. Rowe Price Associates, |  | - | - |
| MAC | 72 | large_holder | Vanguard Portfolio Manage |  | - | - |
| SMTC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| WDAY | 72 | large_holder | BlackRock, Inc. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| SBRA | 56 | corporate_insider | MATROS RICHARD K | $4,166,000 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $3,670,518 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $3,520,145 | - |
| VG | 56 | corporate_insider | Larson Keith D | $28,692,319 | - |
| SNOW | 56 | corporate_insider | GARRETT MARK | $17,500,000 | - |
| DELL | 55 | corporate_insider | Saavedra Jennifer D. | $13,130,520 | - |
| BLTE | 55 | corporate_insider | Lin Yu-Hsin | $2,117,909 | - |
| DELL | 55 | corporate_insider | Silver Lake Partners IV,  | $5,218,094 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 762.4 (-0.46% / 0.08% / -1.06%) [2026-09-09]
- QQQ: 716.31 (-0.29% / 1.23% / -0.3%) [2026-09-09]
- IWM: 290.64 (-1.37% / 0.02% / -3.44%) [2026-09-09]
- DIA: 524.07 (-0.75% / -0.7% / -2.38%) [2026-09-09]
- TLT: 81.73 (-0.57% / -0.17% / -0.18%) [2026-09-09]
- IEF: 91.9 (-0.28% / -0.22% / -0.69%) [2026-09-09]
- GLD: 403.35 (0.91% / 1.66% / 0.6%) [2026-09-09]
- ^VIX: 16.46 (4.71% / 8.29% / 13.13%) [2026-09-09]
- BTC-USD: 78368.63 (-0.09% / -1.64% / 7.31%) [2026-09-10]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.39 (delta 1m: 0.2) [2026-09-08]
- Treasury 10Y yield: 4.8 (delta 1m: 0.15) [2026-09-08]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.07) [2026-09-09]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.67 (delta 1m: -0.03) [2026-09-08]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.37 (delta 1m: 0.08) [2026-09-09]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (2), leadership (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [BLTE] Belite Bio ( NASDAQ : BLTE ) CFO Hao - Yuan Chuang Sells 17 , 962 Shares (2026-09-10)
- [BLTE] Belite Bio ( NASDAQ : BLTE ) CEO Sells 26 , 000 Shares of Stock (2026-09-10)
- [UTHR] Reviewing United Therapeutics ( NASDAQ : UTHR ) and Zenas BioPharma ( NASDAQ : ZBIO ) (2026-09-07)
- [UTHR] Former Anheuser - Busch plant sold to United Therapeutics (2026-09-03)
- [UTHR] Anheuser - Busch plant in Merrimack sold to United Therapeutics for $47 . 5M (2026-09-02)
- [UTHR] United Therapeutics Announces FDA Acceptance Of SNDA For Nebulized Tyvaso In IPF (2026-09-02)

**Actores que han movido ficha este mes (top movimientos):**

- CEO RESSLER RICHARD S compro CIM GROUP, INC. por $2.7M el 2026-09-04.
- CEO Barry John F compro PSEC por $2.7M el 2026-09-04.
- CEO Meeks Danny compro GWAV por $8.0M el 2026-08-27.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- theowalcott · PnL $185,347 · win rate 100% · categorias: sports
- Kch-Temp · PnL $155,386 · win rate 88% · categorias: sports
- BreakTheBank · PnL $121,653 · win rate 85% · categorias: sports
- 0xb4F978BE63cDF75554b0B46a4262a6dB597cc9A7-1779258330186 · PnL $41,147 · win rate 91% · categorias: sports, crypto, politics
- pltrkr111 · PnL $12,108 · win rate 98% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 819 registros 30d · ultimo dato 2026-09-09
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-09
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ALMS, BWFG, CSQ, DT, GLD, GOLD, IEF, MFP, QQQ, SLGL, SMTC, SPY, TLT, WDAY`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
