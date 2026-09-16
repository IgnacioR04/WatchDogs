# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-16T11:44:56+00:00 · ventana señales 2026-08-17 -> 2026-09-16_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 70.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.89)
- Tendencia: `neutral` (SPY 757.39 · MA50 759.06 · MA200 712.99 · dist MA200: 6.23%)
- Credito: `tight` (HY spread 2.71)
- Tipos: `flat` (curva 10y-2y 0.33)
- Fed Funds: 3.63%
- Motivos: credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **70.0%** · cash **30.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 757.39 | -0.46% | -1.12% | -1.98% |
| QQQ | 9.8% | core | 704.54 | -0.65% | -1.92% | -3.47% |
| TLT | 9.8% | core | 80.71 | -0.27% | -1.81% | -0.41% |
| CSQ | 8.2% | satellite | 20.28 | -0.73% | -2.71% | -2.33% |
| EVRG | 7.9% | satellite | 80.2 | -0.82% | -2.48% | -3.65% |
| GLD | 7.3% | core | 394.15 | 0.33% | -1.39% | -2.8% |
| IEF | 4.9% | core | 90.82 | -0.12% | -1.45% | -1.82% |
| COO | 3.2% | satellite | 53.27 | -1.75% | -21.3% | -29.07% |
| GOLD | 2.5% | satellite | 47.8 | 1.01% | 0.7% | 5.31% |
| DBI | 1.7% | satellite | 6.25 | -4.29% | 20.19% | 7.57% |
| USAR | 1.5% | satellite | 15.4 | -1.97% | -12.8% | -20.17% |
| DELL | 1.3% | satellite | 543.51 | 1.73% | 1.8% | 13.28% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.9%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -3.7%
- Beta vs SPY: 0.621 · posiciones efectivas: 17.7 · HHI: 0.0565

**Por que estos satellite (señales WATCHDOG):**

- **COO** · score agregado 315.7 · 4 señales · fuentes: corporate_insider
- **CSQ** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **EVRG** · score agregado 107.4 · 2 señales · fuentes: corporate_insider
- **DBI** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **DELL** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **GOLD** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NTHI | 81 | corporate_insider | Heshmatpour Amir F | 3 | $115,395 | cluster_buy |
| COO | 80 | corporate_insider | Kurzius Lawrence Erik | 3 | $539,150 | cluster_buy |
| NTHI | 79 | corporate_insider | Heshmatpour Amir F | 3 | $59,400 | cluster_buy |
| COO | 79 | corporate_insider | Rosebrough Walter M Jr | 3 | $378,770 | cluster_buy |
| VENU | 79 | corporate_insider | ROTH JAY W | 2 | $350,000 | cluster_buy |
| COO | 78 | corporate_insider | Keel Paul A | 3 | $250,000 | cluster_buy |
| COO | 78 | corporate_insider | Rosebrough Walter M Jr | 3 | $162,870 | cluster_buy |
| NTHI | 77 | corporate_insider | CHEN THOMAS C | 3 | $19,998 | cluster_buy,small_amount |
| NTHI | 77 | corporate_insider | CHEN THOMAS C | 3 | $20,002 | cluster_buy,small_amount |
| RWT | 76 | corporate_insider | Carillo Brooke | 2 | $100,238 | cluster_buy |
| VENU | 75 | corporate_insider | Finke Thomas M | 2 | $350,000 | cluster_buy |
| RWT | 74 | corporate_insider | KUBICEK GREG H | 2 | $192,560 | cluster_buy |
| TENX | 72 | corporate_insider | Giordano Christopher Thom | 2 | $11,250 | cluster_buy,small_amount |
| DBI | 72 | large_holder | Stone House Capital Manag |  | - | - |
| TENX | 72 | large_holder | ING Groep N.V. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| LFST | 61 | corporate_insider | TPG GP A, LLC | $226,255,274 | - |
| DELL | 60 | corporate_insider | Trizzino Peter | $21,137,638 | - |
| HPE | 59 | corporate_insider | Neri Antonio F | $15,110,500 | - |
| ROST | 58 | corporate_insider | Conroy James Grant | $11,291,775 | - |
| PBF | 57 | corporate_insider | Control Empresarial de Ca | $12,089,970 | - |
| HSTM | 56 | corporate_insider | FRIST ROBERT A JR | $4,250,006 | - |
| CRVL | 56 | corporate_insider | CORSTAR HOLDINGS INC | $8,968,055 | - |
| CRWV | 56 | corporate_insider | Agrawal Nitin | $5,303,445 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 757.39 (-0.46% / -1.12% / -1.98%) [2026-09-15]
- QQQ: 704.54 (-0.65% / -1.92% / -3.47%) [2026-09-15]
- IWM: 285.14 (-0.7% / -2.98% / -5.98%) [2026-09-15]
- DIA: 521.23 (-0.62% / -1.29% / -2.35%) [2026-09-15]
- TLT: 80.71 (-0.27% / -1.81% / -0.41%) [2026-09-15]
- IEF: 90.82 (-0.12% / -1.45% / -1.82%) [2026-09-15]
- GLD: 394.15 (0.33% / -1.39% / -2.8%) [2026-09-15]
- ^VIX: 16.89 (-1.8% / 2.61% / 13.43%) [2026-09-16]
- BTC-USD: 76147.25 (0.71% / -1.33% / -5.12%) [2026-09-16]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.65 (delta 1m: 0.5) [2026-09-14]
- Treasury 10Y yield: 4.97 (delta 1m: 0.34) [2026-09-14]
- Curva 10Y-2Y: 0.33 (delta 1m: -0.18) [2026-09-15]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.71 (delta 1m: 0.04) [2026-09-14]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.38 (delta 1m: 0.11) [2026-09-15]
- Dolar broad index: 118.2126 (delta 1m: -0.905) [2026-09-11]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (2), ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DELL] Dell Technologies Sees AI Boom Building as $95B Server Backlog Signals Demand (2026-09-12)
- [DELL] Jim Cramer Compares Dell ( DELL ) to Dallas Cowboys Star CeeDee Lamb (2026-09-12)
- [CHYM] Chime Financial ( CHYM ) versus The Competition Head to Head Survey (2026-09-12)
- [CL] Talon Private Wealth LLC Sells 10 , 006 Shares of Colgate - Palmolive Company $CL (2026-09-12)
- [CHYM] Insider Selling : Chime Financial ( NASDAQ : CHYM ) CAO Sells $642 , 494 . 70 in Stock (2026-09-12)
- [CHYM] Corpay ( NYSE : CPAY ) vs . Chime Financial ( NASDAQ : CHYM ) Head to Head Analysis (2026-09-11)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Trizzino Peter vendio DELL por $21.1M el 2026-09-11 [senal en multiples fuentes].
- 10% owner TPG GP A, LLC vendio LFST por $226.3M el 2026-09-11.
- CEO Conroy James Grant vendio ROST por $11.3M el 2026-09-14.
- CEO Neri Antonio F vendio HPE por $15.1M el 2026-09-11.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $5.9M el 2026-09-11.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- ethanaz · PnL $277,825 · win rate 89% · categorias: sports, crypto
- SDTrading · PnL $47,065 · win rate 94% · categorias: sports
- dontworrybaseball · PnL $11,739 · win rate 100% · categorias: sports
- BrotherObama · PnL $81,866 · win rate 84% · categorias: sports
- DimSumConnoisseur. · PnL $44,100 · win rate 91% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 773 registros 30d · ultimo dato 2026-09-15
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-16
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`COO, CSQ, DBI, DELL, EVRG, GLD, GOLD, IEF, QQQ, SPY, TLT, USAR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
