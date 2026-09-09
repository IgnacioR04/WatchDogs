# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-09T04:57:02+00:00 · ventana señales 2026-08-10 -> 2026-09-09_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.72)
- Tendencia: `bull` (SPY 765.96 · MA50 757.6 · MA200 710.43 · dist MA200: 7.82%)
- Credito: `tight` (HY spread 2.68)
- Tipos: `flat` (curva 10y-2y 0.41)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.96 | -0.55% | -0.14% | -0.91% |
| QQQ | 12.0% | core | 718.36 | -0.08% | 0.22% | -0.35% |
| TLT | 12.0% | core | 82.2 | -0.01% | -0.01% | 0.55% |
| GLD | 9.3% | core | 399.72 | -1.73% | -2.13% | -0.7% |
| CSQ | 8.7% | satellite | 20.98 | -0.52% | 0.19% | 0.45% |
| IEF | 6.2% | core | 92.16 | -0.1% | -0.27% | -0.29% |
| LTH | 4.3% | satellite | 42.47 | -1.76% | 1.07% | 0.02% |
| WTS | 4.2% | satellite | 360.98 | -0.59% | -1.13% | -5.86% |
| UBER | 3.6% | satellite | 73.13 | -3.47% | -3.33% | -6.28% |
| KMT | 3.5% | satellite | 30.47 | -1.77% | 3.85% | -2.93% |
| GOLD | 2.8% | satellite | 47.47 | 2.9% | 5.56% | 9.2% |
| AMR | 2.3% | satellite | 223.74 | -0.74% | -5.07% | 45.47% |
| INBX | 2.2% | satellite | 114.34 | -5.64% | -9.76% | 22.8% |
| TXG | 1.9% | satellite | 65.6 | 4.71% | 5.04% | 12.0% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.2%
- VaR 95% 1d: 1.1% · CVaR 95% 1d: 1.5%
- Max drawdown historico: -3.3%
- Beta vs SPY: 0.795 · posiciones efectivas: 14.0 · HHI: 0.0716

**Por que estos satellite (señales WATCHDOG):**

- **INBX** · score agregado 655.0 · 8 señales · fuentes: corporate_insider
- **AMR** · score agregado 296.3 · 5 señales · fuentes: corporate_insider
- **CSQ** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **GOLD** · score agregado 136.7 · 2 señales · fuentes: corporate_insider, large_holder
- **UBER** · score agregado 124.5 · 2 señales · fuentes: corporate_insider
- **TXG** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **WTS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **LTH** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KMT** · score agregado 57.4 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| INBX | 86 | corporate_insider | Lappe Mark | 3 | $1,087,001 | cluster_buy |
| INBX | 85 | corporate_insider | Lappe Mark | 3 | $664,719 | cluster_buy |
| INBX | 84 | corporate_insider | Lappe Mark | 3 | $585,343 | cluster_buy |
| GPUS | 81 | corporate_insider | AULT MILTON C III | 4 | $361,496 | cluster_buy |
| INBX | 81 | corporate_insider | Lappe Mark | 3 | $136,382 | cluster_buy |
| INBX | 81 | corporate_insider | Lappe Mark | 3 | $117,836 | cluster_buy |
| INBX | 80 | corporate_insider | Kayyem Jon Faiz | 3 | $567,580 | cluster_buy |
| INBX | 79 | corporate_insider | Lappe Mark | 3 | $54,118 | cluster_buy |
| GPUS | 79 | corporate_insider | Nisser Henry Carl | 4 | $46,775 | cluster_buy |
| INBX | 79 | corporate_insider | FORSYTH DOUGLAS | 3 | $286,617 | cluster_buy |
| GPUS | 77 | corporate_insider | Horne William B. | 4 | $20,000 | cluster_buy,small_amount |
| GPUS | 76 | corporate_insider | AULT MILTON C III | 4 | $37,904 | cluster_buy |
| GPUS | 76 | corporate_insider | CRAGUN KENNETH S | 4 | $18,650 | cluster_buy,small_amount |
| GPUS | 76 | corporate_insider | Horne William B. | 4 | $11,220 | cluster_buy,small_amount |
| GPUS | 73 | corporate_insider | AULT MILTON C III | 4 | $7,117 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PAMT | 59 | corporate_insider | MOROUN MATTHEW T | $31,225,740 | - |
| NVDA | 58 | corporate_insider | STEVENS MARK A | $54,976,302 | - |
| NVDA | 58 | corporate_insider | STEVENS MARK A | $45,974,100 | - |
| NVDA | 58 | corporate_insider | STEVENS MARK A | $45,431,041 | - |
| NVDA | 58 | corporate_insider | STEVENS MARK A | $45,244,670 | - |
| NVDA | 57 | corporate_insider | STEVENS MARK A | $42,636,607 | - |
| NET | 57 | corporate_insider | Zatlyn Michelle | $4,962,814 | - |
| BNTX | 57 | corporate_insider | Sahin Ugur | $4,628,232 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.96 (-0.55% / -0.14% / -0.91%) [2026-09-08]
- QQQ: 718.36 (-0.08% / 0.22% / -0.35%) [2026-09-08]
- IWM: 294.67 (-0.45% / 0.25% / -1.77%) [2026-09-08]
- DIA: 528.03 (-1.13% / -0.67% / -1.95%) [2026-09-08]
- TLT: 82.2 (-0.01% / -0.01% / 0.55%) [2026-09-08]
- IEF: 92.16 (-0.1% / -0.27% / -0.29%) [2026-09-08]
- GLD: 399.72 (-1.73% / -2.13% / -0.7%) [2026-09-08]
- ^VIX: 15.72 (2.75% / -3.79% / 2.88%) [2026-09-08]
- BTC-USD: 79174.13 (0.07% / -2.58% / 14.3%) [2026-09-09]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.37 (delta 1m: 0.12) [2026-09-04]
- Treasury 10Y yield: 4.78 (delta 1m: 0.09) [2026-09-04]
- Curva 10Y-2Y: 0.41 (delta 1m: -0.05) [2026-09-08]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.68 (delta 1m: -0.02) [2026-09-07]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.37 (delta 1m: 0.12) [2026-09-08]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (8), ai (1), regulatory (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DELL] Insider Selling : Dell Technologies ( NYSE : DELL ) Director Sells $38 , 215 , 418 . 85 in Stock (2026-09-09)
- [DELL] Silver Lake Partners Iv , L . P . Sells 75 , 285 Shares of Dell Technologies ( NYSE : DELL ) Stock (2026-09-09)
- [NET] Michelle Zatlyn Sells 33 , 003 Shares of Cloudflare ( NYSE : NET ) Stock (2026-09-09)
- [NET] Cloudflare ( NYSE : NET ) Insider Sells 33 , 003 Shares of Stock (2026-09-09)
- [NET] Michelle Zatlyn Sells 33 , 003 Shares of Cloudflare ( NYSE : NET ) Stock (2026-09-09)
- [DELL] Dell vs . HPE : Which Top AI Server Stock Is the Better Buy ? (2026-09-09)
- [CWT] California Water Service Kicks Off Back - to - School Season With 13th Year of Tap Into Learning Program (2026-09-09)
- [NET] MazeBolt Integrates with Cloudflare CDN Edge for Continuous DDoS Validation (2026-09-08)
- [SBSI] Southside Bancshares ( NYSE : SBSI ) versus China Minsheng ( OTCMKTS : CMAKY ) Financial Comparison (2026-09-07)
- [CWT] Lester Snow Sells 500 Shares of California Water Service Group ( NYSE : CWT ) Stock (2026-09-01)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner MOROUN MATTHEW T compro PAMT por $31.2M el 2026-09-03 [senal en multiples fuentes].
- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro QVCG por $11.8M el 2026-09-03 [senal en multiples fuentes].
- 10% owner Tether Global Investments Fund, S.I.C.A.F., S.A. compro GOLD por $3.9M el 2026-09-03 [senal en multiples fuentes].
- CEO Lappe Mark compro INBX por $1.1M el 2026-09-08.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.

**Polymarket — smart money (traders con mejor track record):**

- SDTrading · PnL $32,853 · win rate 94% · categorias: sports
- torta.tech · PnL $23,956 · win rate 95% · categorias: sports
- jarosbill · PnL $15,952 · win rate 87% · categorias: sports
- 0xheavy888 · PnL $25,020 · win rate 84% · categorias: sports
- JnStrtPrdctnMrkts · PnL $8,905 · win rate 91% · categorias: crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 746 registros 30d · ultimo dato 2026-09-08
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-08
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMR, CSQ, GLD, GOLD, IEF, INBX, KMT, LTH, QQQ, SPY, TLT, TXG, UBER, WTS`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
