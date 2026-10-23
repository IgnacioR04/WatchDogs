# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-23T18:38:21+00:00 · ventana señales 2026-09-23 -> 2026-10-23_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `neutral`  -> **presupuesto de riesgo recomendado: 60.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 19.88)
- Tendencia: `neutral` (SPY 760.74 · MA50 766.91 · MA200 724.01 · dist MA200: 5.07%)
- Credito: `normal` (HY spread 3.4)
- Tipos: `flat` (curva 10y-2y 0.31)
- Fed Funds: 3.75%

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **60.0%** · cash **40.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 760.74 | -0.42% | -0.33% | -1.38% |
| DOLE | 9.6% | satellite | 13.35 | -1.22% | 0.41% | 2.89% |
| QQQ | 8.1% | core | 705.6 | 0.16% | -0.59% | -5.22% |
| TLT | 8.1% | core | 81.49 | -0.31% | 1.79% | 3.14% |
| GLD | 6.1% | core | 366.54 | -0.67% | -4.05% | -6.83% |
| SE | 5.1% | satellite | 75.41 | -0.37% | -19.58% | -24.25% |
| IEF | 4.0% | core | 91.12 | -0.09% | 0.77% | 1.59% |
| CAMT | 2.6% | satellite | 121.92 | 2.04% | -5.84% | -17.09% |
| RAPP | 2.5% | satellite | 26.02 | -1.92% | -5.62% | -23.27% |
| CIFR | 1.5% | satellite | 8.04 | -3.37% | -10.47% | -54.65% |
| SRZN | 0.5% | satellite | 25.59 | -0.62% | 9.17% | -13.37% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 7.7%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -4.2%
- Beta vs SPY: 0.584 · posiciones efectivas: 21.7 · HHI: 0.0461

**Por que estos satellite (señales WATCHDOG):**

- **RAPP** · score agregado 386.6 · 5 señales · fuentes: corporate_insider
- **CIFR** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **CAMT** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **DOLE** · score agregado 194.9 · 3 señales · fuentes: corporate_insider
- **SE** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **SRZN** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| RAPP | 81 | corporate_insider | PAUL STEVEN M | 4 | $974,278 | cluster_buy |
| RAPP | 78 | corporate_insider | MARAGANORE JOHN | 4 | $217,344 | cluster_buy |
| LEO | 77 | corporate_insider | Saba Capital Management,  | 2 | $262,612 | cluster_buy |
| RAPP | 76 | corporate_insider | Silva Paul M | 4 | $99,636 | cluster_buy |
| RAPP | 76 | corporate_insider | Young Wendy B. | 4 | $99,992 | cluster_buy |
| DSM | 75 | corporate_insider | Saba Capital Management,  | 2 | $109,459 | cluster_buy |
| RAPP | 74 | corporate_insider | MARAGANORE JOHN | 4 | $31,547 | cluster_buy |
| DSM | 74 | corporate_insider | Saba Capital Management,  | 2 | $77,528 | cluster_buy |
| LEO | 73 | corporate_insider | Saba Capital Management,  | 2 | $44,181 | cluster_buy |
| SNES | 72 | large_holder | GLENBROOK CAPITAL MANAGEM |  | - | - |
| ACU | 72 | large_holder | The Capital Management Co |  | - | - |
| IOT | 72 | large_holder | BAILLIE GIFFORD & CO |  | - | - |
| SE | 72 | large_holder | BAILLIE GIFFORD & CO |  | - | - |
| HERZ | 72 | large_holder | CSS LLC/IL |  | - | - |
| GDTC | 70 | large_holder | mDR LTD |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| IHT | 63 | corporate_insider | WIRTH JAMES F | $2,011,316,976 | - |
| ROIV | 57 | corporate_insider | Venker Eric | $6,521,687 | - |
| SNOW | 56 | corporate_insider | Slootman Frank | $26,156,811 | - |
| ATKR | 56 | corporate_insider | Waltz William E Jr. | $18,204,152 | - |
| SNOW | 56 | corporate_insider | Slootman Frank | $21,628,970 | - |
| BRZE | 55 | corporate_insider | Hyman Jonathan | $12,919,050 | - |
| TRV | 55 | corporate_insider | Klein Michael Frederick | $2,411,493 | - |
| STT | 55 | corporate_insider | O HANLEY RONALD P | $2,395,588 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 760.74 (-0.42% / -0.33% / -1.38%) [2026-10-23]
- QQQ: 705.6 (0.16% / -0.59% / -5.22%) [2026-10-23]
- IWM: 275.69 (-0.35% / 1.94% / -2.23%) [2026-10-23]
- DIA: 522.16 (-1.08% / 0.59% / 0.93%) [2026-10-23]
- TLT: 81.49 (-0.31% / 1.79% / 3.14%) [2026-10-23]
- IEF: 91.12 (-0.09% / 0.77% / 1.59%) [2026-10-23]
- GLD: 366.54 (-0.67% / -4.05% / -6.83%) [2026-10-23]
- ^VIX: 19.88 (4.47% / -0.55% / 33.69%) [2026-10-23]
- BTC-USD: 81409.99 (0.12% / -0.74% / -3.96%) [2026-10-23]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.81 (delta 1m: 0.05) [2026-10-21]
- Treasury 10Y yield: 5.13 (delta 1m: 0.17) [2026-10-21]
- Curva 10Y-2Y: 0.31 (delta 1m: 0.06) [2026-10-22]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.4 (delta 1m: 0.67) [2026-10-22]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.32 (delta 1m: -0.01) [2026-10-22]
- Dolar broad index: 121.4048 (delta 1m: 2.484) [2026-10-16]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (1), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [UTHR] United Therapeutics Authorizes Additional $2 Billion Share Buyback Program (2026-10-22)
- [UTHR] United Therapeutics ( NASDAQ : UTHR ) Price Target Raised to $725 . 00 (2026-10-22)
- [DNA] Ginkgo Bioworks ( NYSE : DNA ) Major Shareholder Barry Canton Sells 22 , 369 Shares of Company Stock (2026-10-21)

**Actores que han movido ficha este mes (top movimientos):**

- CEO WIRTH JAMES F vendio IHT por $2.0B el 2026-10-20.
- CEO Feng Zhimin opero SE por $15.0M el 2026-10-21 [senal en multiples fuentes].
- 10% owner Pale Fire Capital SE compro DOLE por $5.8M el 2026-10-21.
- CEO Waltz William E Jr. vendio ATKR por $18.2M el 2026-10-19.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $6.8M el 2026-10-20.
- 10% owner Pale Fire Capital SE compro DOLE por $2.2M el 2026-10-22.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $1,546,607 · win rate 87% · categorias: sports, politics
- RJW1 · PnL $88,288 · win rate 98% · categorias: sports
- Jokerxing7 · PnL $56,583 · win rate 96% · categorias: sports
- lllllllIlll · PnL $69,011 · win rate 95% · categorias: sports
- CORGII · PnL $65,028 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 580 registros 30d · ultimo dato 2026-10-22
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-23
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`CAMT, CIFR, DOLE, GLD, IEF, QQQ, RAPP, SE, SPY, SRZN, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **60.0%** (el resto es cash). Estamos en regimen `neutral`.
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
