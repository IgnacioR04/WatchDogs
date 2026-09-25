# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-25T22:38:12+00:00 · ventana señales 2026-08-26 -> 2026-09-25_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 95.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `calm` (VIX 14.87)
- Tendencia: `bull` (SPY 771.35 · MA50 759.91 · MA200 714.84 · dist MA200: 7.91%)
- Credito: `tight` (HY spread 2.8)
- Tipos: `flat` (curva 10y-2y 0.36)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); VIX calmado (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 771.35 | 0.54% | 1.27% | 0.28% |
| QQQ | 12.0% | core | 744.5 | 0.46% | 3.3% | 3.35% |
| TLT | 12.0% | core | 79.32 | -0.13% | -2.38% | -4.22% |
| NAD | 10.7% | satellite | 10.1 | -0.2% | -4.99% | -13.48% |
| GLD | 9.3% | core | 393.41 | 0.44% | -1.93% | -6.91% |
| IEF | 6.2% | core | 90.0 | 0.35% | -0.88% | -3.12% |
| IEP | 5.5% | satellite | 6.96 | 0.14% | -0.14% | 3.42% |
| OPRA | 3.5% | satellite | 17.65 | -0.28% | -2.27% | -9.07% |
| TRMD | 3.1% | satellite | 34.32 | 0.06% | -10.23% | 15.88% |
| MGY | 3.1% | satellite | 24.11 | -2.55% | -4.25% | -9.53% |
| DT | 3.1% | satellite | 57.95 | -1.24% | 5.1% | 8.46% |
| DKS | 1.7% | satellite | 136.43 | 2.39% | 12.61% | 4.52% |
| TYRA | 1.5% | satellite | 21.76 | -2.9% | -15.43% | -16.72% |
| DFDV | 1.3% | satellite | 6.04 | 4.32% | -0.33% | 14.39% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.2%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -2.6%
- Beta vs SPY: 0.636 · posiciones efectivas: 13.3 · HHI: 0.0749

**Por que estos satellite (señales WATCHDOG):**

- **TRMD** · score agregado 284.0 · 4 señales · fuentes: large_holder
- **TYRA** · score agregado 210.0 · 3 señales · fuentes: large_holder
- **DKS** · score agregado 154.9 · 2 señales · fuentes: corporate_insider
- **DT** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **MGY** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **IEP** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **NAD** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **OPRA** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **DFDV** · score agregado 58.1 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| NYAX | 85 | corporate_insider | Nechmad Yair | 2 | $4,607,723 | cluster_buy |
| DKS | 80 | corporate_insider | Gupta Navdeep | 2 | $999,983 | cluster_buy |
| RGCO | 74 | corporate_insider | Nester Paul W | 3 | $6,324 | cluster_buy,small_amount |
| DKS | 74 | corporate_insider | Fitzgerald Larry Jr. | 2 | $244,906 | cluster_buy |
| RGCO | 73 | corporate_insider | JOHNSTON ROBERT B | 3 | $20,750 | cluster_buy,small_amount |
| RGCO | 73 | corporate_insider | WILLIAMSON JOHN B III | 3 | $21,190 | cluster_buy,small_amount |
| TRMD | 72 | large_holder | Hafnia Limited |  | - | - |
| TRMD | 72 | large_holder | OCM NJORD HOLDINGS S.A R. |  | - | - |
| CLPR | 72 | large_holder | Marc Bistricer |  | - | - |
| NYAX | 72 | large_holder | MEITAV INVESTMENT HOUSE L |  | - | - |
| MGY | 72 | large_holder | WildFire Energy I LLC |  | - | - |
| NYAX | 72 | corporate_insider | Ben-Avi David | 2 | $67,105 | cluster_buy |
| RGCO | 71 | corporate_insider | WILLIAMSON JOHN B III | 3 | $6,714 | cluster_buy,small_amount |
| DT | 70 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| ZJYL | 70 | large_holder | Erqi Wang |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| HOOD | 61 | corporate_insider | Tenev Vladimir | $30,020,114 | - |
| MEDP | 59 | corporate_insider | Troendle August J. | $17,293,478 | - |
| AVGO | 59 | corporate_insider | SAMUELI HENRY | $81,776,020 | - |
| AVGO | 58 | corporate_insider | SAMUELI HENRY | $66,263,020 | - |
| MEDP | 58 | corporate_insider | Troendle August J. | $10,110,417 | - |
| CRWV | 58 | corporate_insider | Intrator Michael N | $7,546,891 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $5,358,840 | - |
| AVGO | 57 | corporate_insider | SAMUELI HENRY | $30,388,104 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 771.35 (0.54% / 1.27% / 0.28%) [2026-09-25]
- QQQ: 744.5 (0.46% / 3.3% / 3.35%) [2026-09-25]
- IWM: 281.97 (0.11% / -0.75% / -5.7%) [2026-09-25]
- DIA: 517.49 (0.94% / 0.31% / -3.09%) [2026-09-25]
- TLT: 79.32 (-0.13% / -2.38% / -4.22%) [2026-09-25]
- IEF: 90.0 (0.35% / -0.88% / -3.12%) [2026-09-25]
- GLD: 393.41 (0.44% / -1.93% / -6.91%) [2026-09-25]
- ^VIX: 14.87 (-5.11% / 0.41% / 3.05%) [2026-09-25]
- BTC-USD: 84043.15 (-0.4% / 3.57% / 5.29%) [2026-09-25]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.87 (delta 1m: 0.7) [2026-09-24]
- Treasury 10Y yield: 5.18 (delta 1m: 0.54) [2026-09-24]
- Curva 10Y-2Y: 0.36 (delta 1m: -0.11) [2026-09-25]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.8 (delta 1m: 0.13) [2026-09-24]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.02) [2026-09-25]
- Dolar broad index: 119.5133 (delta 1m: 1.18) [2026-09-18]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (4), merger (2), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWV] CoreWeave ( NASDAQ : CRWV ) CFO Sells 55 , 764 Shares of Company Stock (2026-09-25)
- [CRWV] CoreWeave ( NASDAQ : CRWV ) Shares Climb 3 . 7 % Following Analyst Upgrade (2026-09-24)
- [UTHR] FinancialContent - Why United Therapeutics ( UTHR ) Shares Are Falling Today (2026-09-24)
- [CUEN] Cuentas Inc . to Present at the Financial Services Virtual Investor Conference September 24th (2026-09-24)
- [TBPH] Zymeworks Completes Acquisition of Theravance Biopharma (2026-09-23)
- [TBPH] Zymeworks Inc .: Zymeworks Completes Acquisition of Theravance Biopharma (2026-09-23)
- [UTHR] Insider Selling : United Therapeutics ( NASDAQ : UTHR ) CEO Sells $4 , 740 , 785 . 00 in Stock (2026-09-12)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Nechmad Yair compro NYAX por $4.6M el 2026-09-24 [senal en multiples fuentes].
- 10% owner ICAHN CARL C opero IEP por $284.2M el 2026-09-23 [senal en multiples fuentes].
- CEO Troendle August J. vendio MEDP por $17.3M el 2026-09-24.
- CEO Tenev Vladimir vendio HOOD por $30.0M el 2026-09-22.
- 10% owner Calamos Aksia Hedged Strategies Fund (Offshore), Ltd. compro Calamos Aksia Hedged Strategies Fund por $7.5M el 2026-09-23.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $7.5M el 2026-09-23.
- CEO Troendle August J. vendio MEDP por $10.1M el 2026-09-23.
- CEO Maner Tarkan vendio NTNX por $4.8M el 2026-09-24.

**Polymarket — smart money (traders con mejor track record):**

- 0x16bb9951a36fce71e2ef57890b786145e0ba8492 · PnL $127,789 · win rate 94% · categorias: sports
- us391 · PnL $59,895 · win rate 96% · categorias: sports
- monkeymashingkeyboard · PnL $98,792 · win rate 92% · categorias: sports
- primm · PnL $64,489 · win rate 94% · categorias: sports
- TAIWANNUMBERONE · PnL $65,652 · win rate 94% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 516 registros 30d · ultimo dato 2026-09-25
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-25
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`DFDV, DKS, DT, GLD, IEF, IEP, MGY, NAD, OPRA, QQQ, SPY, TLT, TRMD, TYRA`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
