# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-02T16:05:29+00:00 · ventana señales 2026-09-02 -> 2026-10-02_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.59)
- Tendencia: `bull` (SPY 769.36 · MA50 762.22 · MA200 717.04 · dist MA200: 7.3%)
- Credito: `normal` (HY spread 3.24)
- Tipos: `flat` (curva 10y-2y 0.46)
- Fed Funds: 3.75%
- Motivos: tendencia alcista (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 769.36 | 0.7% | -0.26% | -0.25% |
| QQQ | 11.4% | core | 750.33 | 1.12% | 0.78% | 4.66% |
| TLT | 11.4% | core | 77.54 | -0.23% | -1.86% | -5.15% |
| EVV | 9.2% | satellite | 8.49 | 0.24% | 0.83% | -5.34% |
| GLD | 8.6% | core | 378.62 | -1.08% | -3.76% | -7.7% |
| KTF | 6.8% | satellite | 8.14 | 0.49% | -1.09% | -5.43% |
| IEF | 5.7% | core | 89.12 | -0.2% | -0.63% | -3.09% |
| SPG | 5.4% | satellite | 201.74 | 0.46% | -1.5% | -3.6% |
| MTN | 2.2% | satellite | 141.27 | 1.64% | 3.79% | 3.83% |
| ADUR | 1.6% | satellite | 12.51 | 3.22% | -0.95% | -9.87% |
| GPI | 1.6% | satellite | 250.18 | -2.54% | -0.8% | -12.01% |
| TRMD | 1.6% | satellite | 39.42 | 1.59% | 14.85% | 23.82% |
| COUR | 1.5% | satellite | 5.07 | -0.2% | 0.4% | -15.64% |
| LFCR | 0.5% | satellite | 6.53 | 0.0% | 55.48% | 50.11% |
| SSTI | 0.5% | satellite | 8.32 | -1.36% | 47.61% | 36.92% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 6.8%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -3.5%
- Beta vs SPY: 0.603 · posiciones efectivas: 14.6 · HHI: 0.0687

**Por que estos satellite (señales WATCHDOG):**

- **SPG** · score agregado 150.4 · 2 señales · fuentes: corporate_insider
- **KTF** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **EVV** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **COUR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **ADUR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **TRMD** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **LFCR** · score agregado 139.5 · 2 señales · fuentes: large_holder
- **SSTI** · score agregado 138.0 · 2 señales · fuentes: large_holder
- **GPI** · score agregado 138.0 · 2 señales · fuentes: large_holder
- **MTN** · score agregado 138.0 · 2 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| SPG | 76 | corporate_insider | Smith Daniel C. | 5 | $70,973 | cluster_buy |
| SPG | 75 | corporate_insider | SELIG STEFAN M | 5 | $42,178 | cluster_buy |
| SPG | 73 | corporate_insider | Roe Peggy | 5 | $17,845 | cluster_buy,small_amount |
| PYXS | 72 | large_holder | GordonMD Global Investmen |  | - | - |
| DMRC | 72 | large_holder | Ocho Investments LLC |  | - | - |
| MRVI | 72 | large_holder | Millennium Management LLC |  | - | - |
| SPG | 71 | corporate_insider | Jones Nina P | 5 | $9,328 | cluster_buy,small_amount |
| CTM | 70 | corporate_insider | Ives Glen R | 4 | $910 | cluster_buy,small_amount |
| NSTS | 70 | large_holder | NORTH SHORE TRUST & SAVIN |  | - | - |
| BBSI | 70 | large_holder | Private Capital Managemen |  | - | - |
| MATW | 70 | large_holder | Private Capital Managemen |  | - | - |
| AN | 70 | large_holder | Brave Warrior Advisors, L |  | - | - |
| CISS | 70 | large_holder | TOWERVIEW LLC |  | - | - |
| EIKN | 70 | large_holder | Abu Dhabi Investment Auth |  | - | - |
| CPHC | 70 | large_holder | Gate City Capital Managem |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MEDP | 59 | corporate_insider | Troendle August J. | $16,581,855 | - |
| ACT | 59 | corporate_insider | Genworth Holdings, Inc. | $37,116,929 | - |
| MEDP | 59 | corporate_insider | Troendle August J. | $13,739,074 | - |
| CRWV | 58 | corporate_insider | Intrator Michael N | $7,670,355 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $6,412,376 | - |
| CRWV | 56 | corporate_insider | Intrator Michael N | $4,130,013 | - |
| IOT | 56 | corporate_insider | Biswas Sanjit | $3,841,838 | - |
| CRWV | 56 | corporate_insider | Intrator Michael N | $3,452,655 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 769.36 (0.7% / -0.26% / -0.25%) [2026-10-02]
- QQQ: 750.33 (1.12% / 0.78% / 4.66%) [2026-10-02]
- IWM: 281.54 (0.9% / -0.15% / -4.38%) [2026-10-02]
- DIA: 510.16 (0.3% / -1.42% / -4.77%) [2026-10-02]
- TLT: 77.54 (-0.23% / -1.86% / -5.15%) [2026-10-02]
- IEF: 89.12 (-0.2% / -0.63% / -3.09%) [2026-10-02]
- GLD: 378.62 (-1.08% / -3.76% / -7.7%) [2026-10-02]
- ^VIX: 15.59 (-4.88% / 4.84% / 7.3%) [2026-10-02]
- BTC-USD: 85436.33 (0.69% / 1.16% / 10.57%) [2026-10-02]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.88 (delta 1m: 0.54) [2026-09-30]
- Treasury 10Y yield: 5.29 (delta 1m: 0.54) [2026-09-30]
- Curva 10Y-2Y: 0.46 (delta 1m: 0.06) [2026-10-01]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.24 (delta 1m: 0.58) [2026-10-01]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.36 (delta 1m: 0.01) [2026-10-01]
- Dolar broad index: 120.33 (delta 1m: 1.884) [2026-09-25]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (3), leadership (1), ai (1), earnings (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRDO] Credo Technology CEO Sells Company Shares Worth $2 . 5 Million (2026-10-01)
- [CBRL] What Price Increases Mean For Your Cracker Barrel Bill (2026-09-29)
- [CBRL] What Price Increases Mean For Your Cracker Barrel Bill (2026-09-28)
- [CBRL] What Price Increases Mean For Your Cracker Barrel Bill (2026-09-28)
- [IOT] Webinar : Moving from reactive to preventative maintenance with Samsara (2026-09-24)
- [CBRL] Cracker Barrel ( CBRL ) Q4 2026 Earnings Call Transcript (2026-09-24)
- [CRDO] Credo Technology Group ( NASDAQ : CRDO ) Shares Up 6 . 5 % – Here What Happened (2026-09-21)
- [CRDO] Jim Cramer on Credo ( CRDO ):  I Think You Can Buy the Stock (2026-09-21)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner Manufacturers Life Reinsurance Ltd compro John Hancock GA Senior Loan Trust por $31.0M el 2026-09-30.
- 10% owner Manulife (International) Ltd compro John Hancock GA Mortgage Trust por $26.0M el 2026-09-30.
- CEO Troendle August J. vendio MEDP por $13.7M el 2026-09-30 [senal en multiples fuentes].
- 10% owner Manufacturers Life Insurance Co (Bermuda Branch) compro John Hancock GA Senior Loan Trust por $12.0M el 2026-09-30.
- CEO Troendle August J. vendio MEDP por $16.6M el 2026-09-29 [senal en multiples fuentes].
- 10% owner Genworth Holdings, Inc. vendio ACT por $37.1M el 2026-09-30.
- 10% owner SENEFF JAMES M JR compro CNL Strategic Residential Credit, Inc. por $5.0M el 2026-09-30.
- 10% owner Manulife (Singapore) Pte. Ltd. compro John Hancock GA Mortgage Trust por $4.0M el 2026-09-30.

**Polymarket — smart money (traders con mejor track record):**

- Diabolical-Prize · PnL $156,145 · win rate 94% · categorias: sports, economy
- monkeymashingkeyboard · PnL $29,405 · win rate 92% · categorias: sports
- taylorsversion · PnL $84,163 · win rate 84% · categorias: sports, crypto
- five5120 · PnL $20,908 · win rate 91% · categorias: sports
- JnStrtPrdctnMrkts · PnL $25,044 · win rate 89% · categorias: crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 534 registros 30d · ultimo dato 2026-10-01
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-02
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ADUR, COUR, EVV, GLD, GPI, IEF, KTF, LFCR, MTN, QQQ, SPG, SPY, SSTI, TLT, TRMD`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
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
