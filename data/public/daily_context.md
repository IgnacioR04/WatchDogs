# WATCHDOG — Briefing diario para el LLM

_Generado 2026-10-16T22:22:19+00:00 · ventana señales 2026-09-16 -> 2026-10-16_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `neutral`  -> **presupuesto de riesgo recomendado: 60.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 19.99)
- Tendencia: `neutral` (SPY 763.25 · MA50 767.4 · MA200 721.88 · dist MA200: 5.73%)
- Credito: `normal` (HY spread 3.23)
- Tipos: `flat` (curva 10y-2y 0.35)
- Fed Funds: 3.75%

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **60.0%** · cash **40.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 763.25 | -1.11% | -1.97% | 0.2% |
| QQQ | 8.1% | core | 709.8 | -2.5% | -5.52% | -1.51% |
| TLT | 8.1% | core | 80.05 | 0.1% | 2.65% | -1.08% |
| KTF | 6.5% | satellite | 8.17 | 0.37% | 1.24% | -2.49% |
| GLD | 6.1% | core | 382.01 | -0.18% | -0.67% | -4.78% |
| IEF | 4.0% | core | 90.42 | 0.08% | 1.14% | -0.08% |
| NAD | 3.9% | satellite | 10.36 | 0.39% | 2.29% | -1.85% |
| PEP | 3.0% | satellite | 131.49 | 2.42% | 4.38% | 1.34% |
| PAG | 2.1% | satellite | 212.42 | 0.2% | 8.29% | -0.09% |
| VEON | 1.3% | satellite | 83.2 | 0.47% | 8.32% | 21.23% |
| RSKD | 1.3% | satellite | 8.22 | -4.53% | -3.63% | 32.37% |
| FSLR | 1.2% | satellite | 172.64 | -3.45% | -2.91% | -11.9% |
| KLIC | 1.1% | satellite | 78.63 | -5.32% | -14.54% | -5.42% |
| NVAX | 0.9% | satellite | 11.26 | -12.17% | -11.69% | 11.37% |
| UTZ | 0.5% | satellite | 14.29 | -0.21% | -0.07% | 0.8% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 7.1%
- VaR 95% 1d: 0.7% · CVaR 95% 1d: 0.9%
- Max drawdown historico: -3.9%
- Beta vs SPY: 0.481 · posiciones efectivas: 24.7 · HHI: 0.0405

**Por que estos satellite (señales WATCHDOG):**

- **PEP** · score agregado 259.3 · 4 señales · fuentes: corporate_insider
- **NVAX** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **VEON** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **PAG** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **RSKD** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **FSLR** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **NAD** · score agregado 106.3 · 2 señales · fuentes: corporate_insider
- **KTF** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **KLIC** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **UTZ** · score agregado 71.8 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BORR | 79 | corporate_insider | Troim Tor Olav | 2 | $2,299,150 | cluster_buy |
| BORR | 79 | corporate_insider | Snowling Harvey Edward | 2 | $1,473,000 | cluster_buy |
| SAFX | 74 | corporate_insider | EEME Energy SPV I, LLC | 0 | $142,083,451 | - |
| GABC | 73 | corporate_insider | Bawel Zachary W | 3 | $17,100 | cluster_buy,small_amount |
| SAFX | 72 | large_holder | EEME Energy SPV I, LLC |  | - | - |
| KTF | 72 | large_holder | JPMorgan Chase Bank, Nati |  | - | - |
| KLIC | 72 | large_holder | JPMORGAN CHASE & CO. |  | - | - |
| UTZ | 72 | large_holder | Glazer Capital, LLC |  | - | - |
| PAM | 71 | corporate_insider | Mindlin Marcos Marcelo | 0 | $35,139,300 | - |
| NVAX | 70 | large_holder | Shah Capital Management |  | - | - |
| VEON | 70 | large_holder | Shah Capital Management |  | - | - |
| OZ | 70 | large_holder | Donnalley David James |  | - | - |
| FIVN | 70 | large_holder | Voss Value Master Fund, L |  | - | - |
| COSM | 70 | large_holder | Bovopoulos Andreas |  | - | - |
| BLND | 70 | large_holder | Capricorn Fund Managers L |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| MRNA | 58 | corporate_insider | Hoge Stephen | $8,640,084 | - |
| MRNA | 58 | corporate_insider | Hoge Stephen | $8,277,086 | - |
| SNPS | 57 | corporate_insider | Ghazi Sassine | $6,759,359 | - |
| NUAI | 57 | corporate_insider | MCCARTHY KENT C | $14,765,718 | - |
| MDT | 57 | corporate_insider | Martha Geoffrey | $4,750,000 | - |
| INSW | 57 | corporate_insider | Famatown Finance Ltd | $11,496,700 | - |
| INSW | 56 | corporate_insider | Famatown Finance Ltd | $11,405,875 | - |
| INSW | 56 | corporate_insider | Famatown Finance Ltd | $11,108,800 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 763.25 (-1.11% / -1.97% / 0.2%) [2026-10-16]
- QQQ: 709.8 (-2.5% / -5.52% / -1.51%) [2026-10-16]
- IWM: 270.44 (-1.69% / -3.05% / -4.81%) [2026-10-16]
- DIA: 519.1 (-0.4% / 0.58% / 0.62%) [2026-10-16]
- TLT: 80.05 (0.1% / 2.65% / -1.08%) [2026-10-16]
- IEF: 90.42 (0.08% / 1.14% / -0.08%) [2026-10-16]
- GLD: 382.01 (-0.18% / -0.67% / -4.78%) [2026-10-16]
- ^VIX: 19.99 (21.45% / 34.7% / 34.98%) [2026-10-16]
- BTC-USD: 81681.85 (-0.56% / -2.39% / -3.23%) [2026-10-16]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.77 (delta 1m: 0.1) [2026-10-15]
- Treasury 10Y yield: 5.1 (delta 1m: 0.1) [2026-10-15]
- Curva 10Y-2Y: 0.35 (delta 1m: 0.08) [2026-10-16]
- Fed Funds Rate: 3.75 (delta 1m: -0.73) [2026-09-01]
- High yield spread (OAS): 3.23 (delta 1m: 0.53) [2026-10-15]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-09-01]
- Breakeven inflacion 10Y: 2.35 (delta 1m: 0.02) [2026-10-16]
- Dolar broad index: 121.6023 (delta 1m: 3.524) [2026-10-09]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [MRVL] TB Alternative Assets Ltd . Makes New $30 . 68 Million Investment in Marvell Technology , Inc . $MRVL (2026-10-16)
- [TDG] AIRO Group ( NASDAQ : AIRO ) versus Transdigm Group ( NYSE : TDG ) Financial Comparison (2026-10-16)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner EEME Energy SPV I, LLC compro SAFX por $142.1M el 2026-10-16 [senal en multiples fuentes].
- 10% owner Mindlin Marcos Marcelo compro PAM por $35.1M el 2026-10-15.
- 10% owner NIPPON LIFE INSURANCE CO compro CRBG por $20.5M el 2026-10-14.
- 10% owner Yoon Keun Chang Kevin vendio GOLF por $52.5M el 2026-10-15.
- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro Keenova Therapeutics plc por $12.3M el 2026-10-14.
- CEO Hoge Stephen vendio MRNA por $8.6M el 2026-10-15.
- CEO Ghazi Sassine vendio SNPS por $6.8M el 2026-10-15.
- CEO Martha Geoffrey vendio MDT por $4.8M el 2026-10-15.

**Polymarket — smart money (traders con mejor track record):**

- BreakTheBank · PnL $1,082,933 · win rate 86% · categorias: sports, politics
- theowalcott · PnL $99,711 · win rate 100% · categorias: sports
- fantasy7788 · PnL $43,809 · win rate 99% · categorias: sports, crypto
- lllllllIlll · PnL $68,228 · win rate 94% · categorias: sports
- Siddhartha1 · PnL $79,486 · win rate 89% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 637 registros 30d · ultimo dato 2026-10-16
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-10-16
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`FSLR, GLD, IEF, KLIC, KTF, NAD, NVAX, PAG, PEP, QQQ, RSKD, SPY, TLT, UTZ, VEON`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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
