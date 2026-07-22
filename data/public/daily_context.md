# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-22T14:37:38+00:00 · ventana señales 2026-06-22 -> 2026-07-22_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.96)
- Tendencia: `bull` (SPY 747.34 · MA50 744.04 · MA200 694.69 · dist MA200: 7.58%)
- Credito: `tight` (HY spread 2.69)
- Tipos: `flat` (curva 10y-2y 0.37)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 747.34 | -0.13% | -0.99% | 1.88% |
| QQQ | 12.0% | core | 707.25 | -0.24% | -1.46% | -0.9% |
| TLT | 12.0% | core | 83.53 | -0.16% | -0.84% | -2.74% |
| GLD | 9.3% | core | 380.77 | 1.59% | 2.26% | 0.91% |
| BEP | 7.8% | satellite | 32.4 | 0.67% | -0.38% | -8.59% |
| IEF | 6.2% | core | 93.11 | -0.21% | -0.71% | -0.75% |
| LLY | 5.3% | satellite | 1160.64 | -1.26% | 0.35% | 4.84% |
| ENR | 4.5% | satellite | 20.49 | 2.04% | -0.97% | -5.09% |
| CAG | 4.4% | satellite | 15.1 | 1.68% | 7.17% | 12.43% |
| UBER | 4.2% | satellite | 70.35 | -1.68% | -3.19% | 0.98% |
| TSM | 2.9% | satellite | 422.1 | -0.59% | 0.62% | -3.27% |
| VOR | 1.9% | satellite | 19.12 | -4.64% | 5.75% | 28.75% |
| QNT | 1.5% | satellite | 58.01 | -0.97% | -4.13% | -25.11% |
| BFLY | 0.9% | satellite | 6.39 | -6.23% | -12.4% | -16.62% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 13.0%
- VaR 95% 1d: 1.2% · CVaR 95% 1d: 1.6%
- Max drawdown historico: -3.2%
- Beta vs SPY: 0.659 · posiciones efectivas: 13.9 · HHI: 0.072

**Por que estos satellite (señales WATCHDOG):**

- **ENR** · score agregado 307.7 · 5 señales · fuentes: corporate_insider
- **TSM** · score agregado 282.0 · 5 señales · fuentes: corporate_insider
- **BFLY** · score agregado 142.0 · 2 señales · fuentes: large_holder
- **QNT** · score agregado 73.0 · 1 señales · fuentes: large_holder
- **VOR** · score agregado 70.2 · 1 señales · fuentes: large_holder
- **UBER** · score agregado 68.5 · 1 señales · fuentes: congress
- **CAG** · score agregado 64.0 · 1 señales · fuentes: corporate_insider
- **LLY** · score agregado 63.5 · 1 señales · fuentes: congress
- **BEP** · score agregado 58.5 · 1 señales · fuentes: congress

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| CHCO | 73 | corporate_insider | FISHER ROBERT D | 4 | $20,990 | cluster_buy,small_amount |
| QNT | 73 | large_holder | BlackRock Portfolio Manag |  | - | - |
| CHCO | 72 | corporate_insider | STRONG-TREISTER DIANE W | 4 | $14,800 | cluster_buy,small_amount |
| CHCO | 72 | corporate_insider | Hoyer James A | 4 | $12,782 | cluster_buy,small_amount |
| BFLY | 72 | large_holder | Rothberg Jonathan M. |  | - | - |
| HCAT | 72 | large_holder | Impax Asset Management Gr |  | - | - |
| CHCO | 72 | corporate_insider | Reyes Javier A | 4 | $11,168 | cluster_buy,small_amount |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| PAG | 70 | large_holder | Penske Corporation |  | - | - |
| PAG | 70 | large_holder | Mitsui & Co., Ltd. |  | - | - |
| FLYW | 70 | large_holder | Temasek Holdings (Private |  | - | - |
| TTE | 70 | large_holder | AMUNDI |  | - | - |
| ERII | 70 | large_holder | AMUNDI |  | - | - |
| CWT | 70 | large_holder | AMUNDI |  | - | - |
| ZSTK | 70 | large_holder | Reis-Faria Daniel |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| XOM | 65 | congress | James A. Himes | $50,000 | - |
| HD | 65 | congress | James A. Himes | $50,000 | - |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| BAC | 63 | congress | James A. Himes | $15,000 | small_amount |
| BLK | 63 | congress | John McGuire | $15,000 | small_amount |
| LLY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| HSY | 62 | congress | Dan Newhouse | $15,000 | small_amount |
| CAG | 62 | congress | Gilbert Cisneros | $50,000 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 747.34 (-0.13% / -0.99% / 1.88%) [2026-07-22]
- QQQ: 707.25 (-0.24% / -1.46% / -0.9%) [2026-07-22]
- IWM: 294.89 (-0.55% / -0.3% / -0.14%) [2026-07-22]
- DIA: 522.15 (0.12% / -0.69% / 1.1%) [2026-07-22]
- TLT: 83.53 (-0.16% / -0.84% / -2.74%) [2026-07-22]
- IEF: 93.11 (-0.21% / -0.71% / -0.75%) [2026-07-22]
- GLD: 380.77 (1.59% / 2.26% / 0.91%) [2026-07-22]
- ^VIX: 16.96 (-0.53% / 8.23% / -12.98%) [2026-07-22]
- BTC-USD: 65810.13 (-1.05% / 2.99% / 7.03%) [2026-07-22]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.21 (delta 1m: 0.01) [2026-07-20]
- Treasury 10Y yield: 4.6 (delta 1m: 0.11) [2026-07-20]
- Curva 10Y-2Y: 0.37 (delta 1m: 0.1) [2026-07-21]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.69 (delta 1m: 0.04) [2026-07-21]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.26 (delta 1m: 0.01) [2026-07-21]
- Dolar broad index: 120.5315 (delta 1m: 1.275) [2026-07-17]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: stock (5), ai (2), merger (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [CRWD] CrowdStrike and Cerebras Partner to Power AI Detection and Response on the World Fastest Inference (2026-07-22)
- [TDG] A $4 . 2M Sale , 46 % Stake Cut : What TransDigm Co - COO Joel Reiss Latest Transaction Means for Investors (2026-07-22)
- [CRWD] Is CrowdStrike Holdings ( CRWD ) Cheap On Its Schwarz Digits Partnership And Pullback ? (2026-07-22)
- [CRWD] CrowdStrike warns of malware targeting AI coding tools (2026-07-22)
- [CAG] Conagra Brands Slashes Its 10 % Dividend Yield in Half Just 1 Month After Getting Kicked Out of the S & P 500 . Here Why the Stock Isnt Tanking . (2026-07-19)
- [CAG] SteelPeak Wealth LLC Makes New Investment in Conagra Brands $CAG (2026-07-19)
- [CAG] Conagra Brands Slashes Its 10 % Dividend Yield in Half Just 1 Month After Getting Kicked Out of the S & P 500 . Here Why the Stock Isnt Tanking . (2026-07-19)
- [CCRN] Cross Country Healthcare Clears Key Hurdle as Stockholders Approve Merger (2026-07-17)
- [CCRN] $HAREHOLDER ALERT : The M & A Class Action Firm Encourages $hareholders to Act Before the Vote -- CCRN , EQH , AXTA , and CZNL (2026-07-15)
- [APPF] Maurice Duca Sells 7 , 200 Shares of AppFolio ( NASDAQ : APPF ) Stock (2026-07-15)

**Actores que han movido ficha este mes (top movimientos):**

- CEO KIRBY J SCOTT vendio UAL por $18.8M el 2026-07-21.
- Officer Sutherland Vanessa Allen vendio PSX por $7.4B el 2026-07-21.
- 10% owner ABRY Partners VII, L.P. vendio KORE por $44.9M el 2026-07-21.
- CEO Clark Kevin Cronin vendio CCRN por $12.6M el 2026-07-21.
- 10% owner ROTHBERG JONATHAN M vendio BFLY por $7.8M el 2026-07-20 [senal en multiples fuentes].
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Nomura Holdings Inc vendio ECHOSTAR CORP por $19.2B.

**Polymarket — smart money (traders con mejor track record):**

- 111111111115 · PnL $108,517 · win rate 95% · categorias: sports
- esportGG · PnL $65,583 · win rate 94% · categorias: sports
- Sassy-Bucket · PnL $59,041 · win rate 93% · categorias: sports
- monkeymashingkeyboard · PnL $52,388 · win rate 92% · categorias: sports
- Themsnw · PnL $49,935 · win rate 83% · categorias: sports, politics

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 74 registros 30d · ultimo dato 2026-07-20
- **sec_insiders**: `ok` · 676 registros 30d · ultimo dato 2026-07-21
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-22
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BEP, BFLY, CAG, ENR, GLD, IEF, LLY, QNT, QQQ, SPY, TLT, TSM, UBER, VOR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
