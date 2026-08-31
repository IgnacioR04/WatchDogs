# WATCHDOG — Briefing diario para el LLM

_Generado 2026-08-31T14:05:32+00:00 · ventana señales 2026-08-01 -> 2026-08-31_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.4)
- Tendencia: `bull` (SPY 765.94 · MA50 754.34 · MA200 707.87 · dist MA200: 8.2%)
- Credito: `tight` (HY spread 2.63)
- Tipos: `flat` (curva 10y-2y 0.39)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.94 | -0.44% | 0.32% | 1.09% |
| QQQ | 12.0% | core | 714.57 | -0.26% | 1.17% | 2.07% |
| TLT | 12.0% | core | 82.23 | -0.78% | -0.4% | 0.05% |
| GLD | 9.3% | core | 405.37 | -0.86% | -5.0% | 9.06% |
| AAT | 7.7% | satellite | 22.27 | -0.69% | -3.15% | -6.68% |
| DGICA | 7.0% | satellite | 19.05 | -0.99% | 0.37% | -3.59% |
| RSG | 6.8% | satellite | 223.41 | 0.59% | 0.15% | 6.58% |
| IEF | 6.2% | core | 92.64 | -0.22% | -0.39% | -0.19% |
| MED | 5.2% | satellite | 12.24 | 0.49% | 2.0% | 25.67% |
| DKS | 4.0% | satellite | 138.09 | 2.22% | -23.0% | -31.24% |
| SUJA | 1.6% | satellite | 9.85 | 5.07% | 8.78% | -14.09% |
| CTEV | 1.1% | satellite | 39.89 | 1.27% | 9.05% | 64.22% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.5%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -1.9%
- Beta vs SPY: 0.445 · posiciones efectivas: 13.2 · HHI: 0.076

**Por que estos satellite (señales WATCHDOG):**

- **RSG** · score agregado 407.4 · 6 señales · fuentes: corporate_insider
- **DKS** · score agregado 399.1 · 5 señales · fuentes: corporate_insider
- **SUJA** · score agregado 337.1 · 5 señales · fuentes: corporate_insider, large_holder
- **AAT** · score agregado 199.4 · 3 señales · fuentes: corporate_insider, large_holder
- **MED** · score agregado 131.9 · 2 señales · fuentes: corporate_insider, large_holder
- **CTEV** · score agregado 121.6 · 2 señales · fuentes: corporate_insider
- **DGICA** · score agregado 119.8 · 2 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| DKS | 83 | corporate_insider | Barrenechea Mark J | 4 | $2,222,240 | cluster_buy |
| ATTO | 82 | corporate_insider | WALSH COLIN | 2 | $8,500,000 | cluster_buy |
| ATTO | 81 | corporate_insider | GOLDMAN SACHS GROUP INC | 2 | $8,500,000 | cluster_buy |
| DKS | 80 | corporate_insider | COLOMBO WILLIAM J | 4 | $643,600 | cluster_buy |
| DKS | 80 | corporate_insider | Eddy Robert W. | 4 | $514,780 | cluster_buy |
| ATTO | 79 | corporate_insider | WALSH COLIN | 2 | $1,785,000 | cluster_buy |
| JUSH | 78 | corporate_insider | Cacioppo James | 2 | $247,000 | cluster_buy |
| JUSH | 78 | corporate_insider | Cacioppo James | 2 | $245,000 | cluster_buy |
| BIVI | 78 | corporate_insider | DO CUONG V | 4 | $31,637 | cluster_buy |
| DKS | 78 | corporate_insider | MATHRANI SANDEEP | 4 | $199,783 | cluster_buy |
| ATTO | 78 | corporate_insider | GOLDMAN SACHS GROUP INC | 2 | $1,785,000 | cluster_buy |
| DKS | 77 | corporate_insider | COLOMBO WILLIAM J | 4 | $141,900 | cluster_buy |
| MTDR | 76 | corporate_insider | Calvert Christopher P | 2 | $141,600 | cluster_buy |
| MTDR | 74 | corporate_insider | Foran Joseph Wm | 2 | $30,242 | cluster_buy |
| BIVI | 73 | corporate_insider | KIM JOANNE WENDY | 4 | $5,450 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| IHT | 63 | corporate_insider | WIRTH JAMES F | $825,000,000 | - |
| RLAY | 61 | corporate_insider | SVF Pauling (Cayman) Ltd | $116,400,000 | - |
| LTH | 59 | corporate_insider | DANHAKL JOHN G | $126,106,945 | - |
| LTH | 59 | corporate_insider | Green LTF Holdings II LP | $123,807,314 | - |
| LTH | 59 | corporate_insider | Galashan John Kristofer | $126,106,945 | - |
| CHYM | 58 | corporate_insider | DST Global Advisors Ltd | $17,674,301 | - |
| CHYM | 58 | corporate_insider | DST Global Advisors Ltd | $17,674,301 | - |
| IBM | 57 | corporate_insider | Thomas Robert David | $5,758,088 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.94 (-0.44% / 0.32% / 1.09%) [2026-08-31]
- QQQ: 714.57 (-0.26% / 1.17% / 2.07%) [2026-08-31]
- IWM: 293.32 (-0.82% / -1.56% / -0.98%) [2026-08-31]
- DIA: 531.78 (-0.61% / -0.35% / 0.19%) [2026-08-31]
- TLT: 82.23 (-0.78% / -0.4% / 0.05%) [2026-08-31]
- IEF: 92.64 (-0.22% / -0.39% / -0.19%) [2026-08-31]
- GLD: 405.37 (-0.86% / -5.0% / 9.06%) [2026-08-31]
- ^VIX: 15.4 (6.72% / -2.84% / -2.9%) [2026-08-31]
- BTC-USD: 78008.39 (0.23% / -1.21% / 20.3%) [2026-08-31]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.2 (delta 1m: -0.02) [2026-08-27]
- Treasury 10Y yield: 4.67 (delta 1m: 0.0) [2026-08-27]
- Curva 10Y-2Y: 0.39 (delta 1m: -0.06) [2026-08-28]
- Fed Funds Rate: 3.63 (delta 1m: -1.2) [2026-07-01]
- High yield spread (OAS): 2.63 (delta 1m: -0.24) [2026-08-27]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-07-01]
- Breakeven inflacion 10Y: 2.31 (delta 1m: 0.04) [2026-08-28]
- Dolar broad index: 118.0628 (delta 1m: -2.845) [2026-08-21]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (3), regulatory (2), stock (2), leadership (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [UTHR] United Therapeutics highlights new data supporting two FDA filings ( UTHR : NASDAQ ) (2026-08-31)
- [AMCR] Amcor to Unveil Food & Beverage Solutions at Empack (2026-08-27)
- [CHYM] Chime Financial ( NASDAQ : CHYM ) Major Shareholder Sells $15 , 494 , 530 . 74 in Stock (2026-08-27)
- [BLLN] Billiontoone ( BLLN ) & The Competition Head to Head Review (2026-08-26)
- [AMCR] Amcor , Tiptree Forge RecyClass - Certified Film Pact (2026-08-25)
- [UTHR] Hudson Portfolio Management LLC Purchases Shares of 1 , 365 United Therapeutics Corporation $UTHR (2026-08-23)
- [MNPR] Monopar Therapeutics ( NASDAQ : MNPR ) Trading Down 3 . 9 % – Time to Sell ? (2026-08-21)
- [AMCR] Amcor Marks 20 Years in FTSE4Good Index Series (2026-08-21)
- [AMCR] Amcor garners two AmeriStar awards (2026-08-20)
- [UP] Head to Head Analysis : Wheels Up Experience ( NYSE : UP ) vs . Japan Airlines ( OTCMKTS : JAPSY ) (2026-08-20)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $51.8M el 2026-08-27.
- CEO WIRTH JAMES F vendio IHT por $825.0M el 2026-08-26.
- 10% owner CASCADE INVESTMENT, L.L.C. compro RSG por $46.7M el 2026-08-26.
- CEO Siemiatkowski Sebastian compro KLAR por $9.9M el 2026-08-26.
- 10% owner SVF Pauling (Cayman) Ltd vendio RLAY por $116.4M el 2026-08-25.
- CEO Patel Viral compro Blackstone Private Equity Strategies Fund L.P. por $2.0M el 2026-08-28.
- 10% owner PAINE SCHWARTZ FOOD CHAIN FUND V GP, LTD. compro SUJA por $2.1M el 2026-08-27 [senal en multiples fuentes].
- 10% owner PAINE SCHWARTZ FOOD CHAIN FUND V GP, LTD. compro SUJA por $1.7M el 2026-08-28 [senal en multiples fuentes].

**Polymarket — smart money (traders con mejor track record):**

- kekasaur · PnL $152,374 · win rate 94% · categorias: sports
- NiNo999 · PnL $137,386 · win rate 90% · categorias: sports
- monkeymashingkeyboard · PnL $79,563 · win rate 91% · categorias: sports
- 0x6982049c65e98606f65A0CE71fDb9b61296dA165-1777135114945 · PnL $12,078 · win rate 98% · categorias: sports, crypto
- gregbeast · PnL $15,446 · win rate 95% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 627 registros 30d · ultimo dato 2026-08-30
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-08-28
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AAT, CTEV, DGICA, DKS, GLD, IEF, MED, QQQ, RSG, SPY, SUJA, TLT`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
