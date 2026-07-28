# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-28T14:57:26+00:00 · ventana señales 2026-06-28 -> 2026-07-28_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 18.6)
- Tendencia: `neutral` (SPY 739.41 · MA50 743.95 · MA200 696.17 · dist MA200: 6.21%)
- Credito: `tight` (HY spread 2.81)
- Tipos: `flat` (curva 10y-2y 0.34)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 739.41 | 0.04% | -1.19% | -0.21% |
| QQQ | 9.8% | core | 673.77 | -1.22% | -4.96% | -6.95% |
| TLT | 9.8% | core | 83.96 | 0.26% | 0.36% | -3.63% |
| GLD | 7.3% | core | 369.37 | -1.4% | -1.45% | 0.21% |
| BEP | 6.4% | satellite | 31.55 | -1.81% | -1.96% | -9.6% |
| IEF | 4.9% | core | 93.45 | 0.18% | 0.15% | -1.37% |
| NMM | 4.3% | satellite | 78.56 | 1.09% | 5.73% | 13.04% |
| BSY | 3.8% | satellite | 35.72 | 5.95% | 14.25% | 20.17% |
| FIS | 3.7% | satellite | 44.32 | 2.69% | 6.59% | 14.55% |
| ENR | 3.2% | satellite | 21.92 | 4.18% | 9.16% | 1.15% |
| BTDR | 1.5% | satellite | 10.32 | -9.03% | -17.27% | -34.9% |
| GLSI | 1.2% | satellite | 13.26 | -1.34% | -9.49% | -42.97% |
| SPCX | 1.2% | satellite | 113.74 | 0.21% | -7.93% | -30.73% |
| PENG | 0.9% | satellite | 47.12 | -10.24% | -18.91% | -30.65% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.7%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.0%
- Max drawdown historico: -3.0%
- Beta vs SPY: None · posiciones efectivas: 19.4 · HHI: 0.0516

**Por que estos satellite (señales WATCHDOG):**

- **ENR** · score agregado 369.3 · 6 señales · fuentes: corporate_insider
- **SPCX** · score agregado 241.4 · 4 señales · fuentes: congress
- **NMM** · score agregado 189.8 · 3 señales · fuentes: corporate_insider
- **BTDR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **PENG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BSY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **FIS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress
- **GLSI** · score agregado 58.1 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NMM | 74 | corporate_insider | Frangou Angeliki | 0 | $846,122,589 | - |
| SCTX | 72 | corporate_insider | Parrot David | 2 | $19,995 | cluster_buy,small_amount |
| SCTX | 72 | corporate_insider | Parrot David | 2 | $19,995 | cluster_buy,small_amount |
| PENG | 72 | large_holder | SK Telecom Co., Ltd. |  | - | - |
| CRAI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| BSY | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ADBE | 72 | large_holder | BlackRock, Inc. |  | - | - |
| ACHC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| CRDO | 72 | large_holder | BlackRock, Inc. |  | - | - |
| NCO | 72 | large_holder | Feis Equities LLC |  | - | - |
| FIS | 72 | large_holder | JPMORGAN CHASE & CO. |  | - | - |
| SCTX | 71 | corporate_insider | Lucas Svetlana | 2 | $45,000 | cluster_buy |
| ELLO | 70 | large_holder | MENORA MIVTACHIM HOLDINGS |  | - | - |
| TATT | 70 | large_holder | Y.D. More Investments Ltd |  | - | - |
| ODYS | 70 | large_holder | Y.D. More Investments Ltd |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| NVDA | 64 | congress | Sam T. Liccardo | $50,000 | - |
| ARCC | 63 | congress | Pete Sessions | $15,000 | small_amount |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| ADBE | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CSX | 62 | congress | Dan Newhouse | $15,000 | small_amount |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 739.41 (0.04% / -1.19% / -0.21%) [2026-07-28]
- QQQ: 673.77 (-1.22% / -4.96% / -6.95%) [2026-07-28]
- IWM: 291.91 (-0.34% / -1.56% / -2.36%) [2026-07-28]
- DIA: 525.82 (0.87% / 0.83% / 0.82%) [2026-07-28]
- TLT: 83.96 (0.26% / 0.36% / -3.63%) [2026-07-28]
- IEF: 93.45 (0.18% / 0.15% / -1.37%) [2026-07-28]
- GLD: 369.37 (-1.4% / -1.45% / 0.21%) [2026-07-28]
- ^VIX: 18.6 (-0.37% / 9.09% / 5.38%) [2026-07-28]
- BTC-USD: 63387.53 (-0.53% / -2.55% / 1.81%) [2026-07-28]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.33 (delta 1m: 0.22) [2026-07-24]
- Treasury 10Y yield: 4.69 (delta 1m: 0.28) [2026-07-24]
- Curva 10Y-2Y: 0.34 (delta 1m: 0.03) [2026-07-27]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.81 (delta 1m: -0.02) [2026-07-27]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.21 (delta 1m: 0.0) [2026-07-27]
- Dolar broad index: 120.7105 (delta 1m: -0.702) [2026-07-24]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), ai (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [UTHR] Ardelyx ( NASDAQ : ARDX ) vs . United Therapeutics ( NASDAQ : UTHR ) Financial Survey (2026-07-27)
- [SYM] Why Symbotic Stock Dropped 24 % in the First Half of 2026 And Is a Screaming Buy Now (2026-07-23)
- [SYM] Is Symbotic ( SYM ) One Of The Best Low - Priced AI Stocks To Buy Right Now ? (2026-07-16)
- [SYM] Is Symbotic ( SYM ) One Of The Best Low - Priced AI Stocks To Buy Right Now ? (2026-07-14)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Frangou Angeliki compro NMM por $846.1M el 2026-07-23.
- CEO Huang Jack Jiajia compro COE por $8.3M el 2026-07-21.
- 10% owner Abu Dhabi Investment Authority compro Jefferies Credit Partners BDC Inc. por $25.0M el 2026-07-23.
- CEO Huang Jack Jiajia compro COE por $4.8M el 2026-07-23.
- CEO Palmer Sheryl vendio TMHC por $19.4M el 2026-07-24.
- CEO Huang Jack Jiajia compro COE por $2.0M el 2026-07-22.
- CEO Griffith Susan Patricia opero PGR por $12.5M el 2026-07-24 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- monkeymashingkeyboard · PnL $125,962 · win rate 91% · categorias: sports
- 0x27c5C1EEE404a07F39FE70078AFf815E5a656D61-1763107503028 · PnL $143,250 · win rate 88% · categorias: sports, crypto
- MoistLotion · PnL $17,156 · win rate 98% · categorias: crypto, sports, economy
- comon119 · PnL $13,696 · win rate 98% · categorias: sports, crypto, politics
- TAIWANNUMBERONE · PnL $37,753 · win rate 90% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 71 registros 30d · ultimo dato 2026-07-24
- **sec_insiders**: `ok` · 518 registros 30d · ultimo dato 2026-07-27
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-28
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BSY, BTDR, ENR, FIS, GLD, GLSI, IEF, NMM, PENG, QQQ, SPCX, SPY, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
