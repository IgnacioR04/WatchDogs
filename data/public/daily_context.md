# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-02T22:13:44+00:00 · ventana señales 2026-08-03 -> 2026-09-02_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.2)
- Tendencia: `bull` (SPY 765.16 · MA50 755.34 · MA200 708.78 · dist MA200: 7.95%)
- Credito: `tight` (HY spread 2.65)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.16 | 0.44% | -0.12% | -0.6% |
| QQQ | 12.0% | core | 709.24 | 0.23% | -0.3% | -1.12% |
| TLT | 12.0% | core | 81.95 | 0.1% | -1.24% | -0.89% |
| ECAT | 12.0% | satellite | 15.24 | 0.4% | -1.99% | 0.02% |
| GLD | 9.4% | core | 402.78 | 1.52% | -4.4% | 3.37% |
| IEF | 6.3% | core | 92.18 | 0.09% | -0.87% | -0.86% |
| BPRE | 4.5% | satellite | 12.15 | 1.08% | 2.36% | -8.24% |
| KIDS | 4.4% | satellite | 22.8 | -0.87% | -5.12% | 2.2% |
| DT | 3.7% | satellite | 50.87 | -3.76% | -1.41% | 0.02% |
| PESI | 2.3% | satellite | 18.03 | 1.07% | -0.61% | 2.1% |
| KVYO | 2.1% | satellite | 19.31 | -6.44% | 8.54% | 0.05% |
| WIX | 2.0% | satellite | 86.69 | -1.91% | 5.35% | 34.26% |
| SUJA | 1.2% | satellite | 10.22 | -2.01% | 8.26% | 66.45% |
| FGL | 1.1% | satellite | 16.1 | -6.56% | -16.15% | -80.67% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.7%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.1%
- Max drawdown historico: -1.7%
- Beta vs SPY: 0.717 · posiciones efectivas: 12.9 · HHI: 0.0773

**Por que estos satellite (señales WATCHDOG):**

- **WIX** · score agregado 302.4 · 4 señales · fuentes: corporate_insider
- **SUJA** · score agregado 208.5 · 3 señales · fuentes: large_holder
- **PESI** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **BPRE** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **DT** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **FGL** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **ECAT** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **KIDS** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **KVYO** · score agregado 67.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| WIX | 78 | corporate_insider | Abrahami Avishai | 6 | $39,168 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 6 | $22,519 | cluster_buy,small_amount |
| JUSH | 77 | corporate_insider | Cacioppo James | 2 | $128,712 | cluster_buy |
| WIX | 77 | corporate_insider | Shemesh Lior | 6 | $27,310 | cluster_buy |
| WIX | 77 | corporate_insider | Zohar Nir | 6 | $16,230 | cluster_buy,small_amount |
| OPAL | 76 | corporate_insider | Comora Adam | 2 | $96,500 | cluster_buy |
| WIX | 74 | corporate_insider | Meyer Shelly B | 6 | $28,687 | cluster_buy |
| JUSH | 74 | corporate_insider | Cacioppo James | 2 | $36,560 | cluster_buy |
| RGCO | 73 | corporate_insider | WILLIAMSON JOHN B III | 3 | $21,300 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Abrahami Avishai | 6 | $3,294 | cluster_buy,small_amount |
| WIX | 73 | corporate_insider | Shai Omer | 6 | $29,346 | cluster_buy |
| WIX | 72 | corporate_insider | Even-Haim Yaniv | 6 | $19,165 | cluster_buy,small_amount |
| DT | 72 | large_holder | PICTET ASSET MANAGEMENT S |  | - | - |
| ZNB | 72 | large_holder | L1 Capital Global Opportu |  | - | - |
| EMPD | 72 | large_holder | Streeterville Capital LLC |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| ACT | 59 | corporate_insider | Genworth Holdings, Inc. | $33,953,773 | - |
| WHD | 58 | corporate_insider | Bender Joel | $7,037,200 | - |
| WHD | 58 | corporate_insider | Bender Scott | $7,037,200 | - |
| KIDS | 56 | corporate_insider | Pelizzon David R | $7,527,168 | - |
| AMBQ | 56 | corporate_insider | Esaka Fumihide | $2,761,534 | - |
| IRM | 55 | corporate_insider | Meaney William L | $2,391,461 | - |
| V | 55 | corporate_insider | MCINERNEY RYAN | $2,230,444 | - |
| MRVL | 55 | corporate_insider | Koopmans Chris | $2,032,700 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.16 (0.44% / -0.12% / -0.6%) [2026-09-02]
- QQQ: 709.24 (0.23% / -0.3% / -1.12%) [2026-09-02]
- IWM: 294.01 (1.18% / -1.65% / -1.92%) [2026-09-02]
- DIA: 530.62 (0.54% / -0.68% / -2.16%) [2026-09-02]
- TLT: 81.95 (0.1% / -1.24% / -0.89%) [2026-09-02]
- IEF: 92.18 (0.09% / -0.87% / -0.86%) [2026-09-02]
- GLD: 402.78 (1.52% / -4.4% / 3.37%) [2026-09-02]
- ^VIX: 15.2 (-6.98% / -0.07% / -3.86%) [2026-09-02]
- BTC-USD: 77149.72 (-0.33% / -0.87% / 21.68%) [2026-09-02]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.39 (delta 1m: 0.14) [2026-09-01]
- Treasury 10Y yield: 4.79 (delta 1m: 0.09) [2026-09-01]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.03) [2026-09-02]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.65 (delta 1m: -0.13) [2026-09-01]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.34 (delta 1m: 0.11) [2026-09-02]
- Dolar broad index: 118.7479 (delta 1m: -0.927) [2026-08-28]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (6), ai (4), legal (2), regulatory (1), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CNO] CNO Financial Group ( NYSE : CNO ) Insider Sells $360 , 734 . 40 in Stock (2026-09-02)
- [CNO] CNO Financial Group ( NYSE : CNO ) Insider Karen Detoro Sells 9 , 336 Shares of Stock (2026-09-02)
- [WIX] Bragar Eagel & Squire , P . C . Urges Wix . com Ltd . Investors to Contact the Firm Regarding ... (2026-09-01)
- [WIX] Wix . com Ltd . ( WIX ) Shareholders Who Lost Money Have Opportunity to Lead Securities Fraud Lawsuit (2026-09-01)
- [WIX] INVESTOR DEADLINE : Wix . com Ltd . ( WIX ) Investors with Substantial Losses Have Opportunity to Lead the Wix Class Action Lawsuit (2026-09-01)
- [WIX] Wix . com Ltd . ( NASDAQ : WIX ) Sees Significant Drop in Short Interest (2026-09-01)
- [WIX] Wix . com Director Ron Gutler Sells 5 , 718 Shares for $488 , 432 (2026-09-01)
- [WIX] Recover Investment Losses : Class Action Initiated Against Wix . com Ltd . ... (2026-09-01)
- [PEGA] Could Pegasystems ( PEGA ) Stock Win as Enterprises Rethink How they Deploy AI ? (2026-08-30)
- [PEGA] Coforge - Pega deal sends stock surging 3 . 4 % as IT partnership deepens (2026-08-28)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Genworth Holdings, Inc. vendio ACT por $34.0M el 2026-08-31.
- CEO Williams Charles Alan compro NPB por $1.4M el 2026-09-01.
- CEO Bender Joel vendio WHD por $7.0M el 2026-09-01.
- 10% owner Empery Asset Management, LP compro EMPD por $1.8M el 2026-09-01 [senal en multiples fuentes].
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.

**Polymarket — smart money (traders con mejor track record):**

- 0xd9670ea74384c1e1b9dc1e4267ffadaf4cdd140 · PnL $159,850 · win rate 97% · categorias: sports, crypto
- ExplosiveNinja · PnL $30,739 · win rate 97% · categorias: sports
- 0xDECfFdA0cA685646001e7f2f525F39de905f4dAF-1787058581228 · PnL $36,228 · win rate 91% · categorias: sports, politics, crypto
- dad168168 · PnL $22,713 · win rate 94% · categorias: sports
- Jan777 · PnL $28,703 · win rate 91% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 552 registros 30d · ultimo dato 2026-09-02
- **sec_13d_13g**: `ok` · 236 registros 30d · ultimo dato 2026-09-02
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BPRE, DT, ECAT, FGL, GLD, IEF, KIDS, KVYO, PESI, QQQ, SPY, SUJA, TLT, WIX`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
