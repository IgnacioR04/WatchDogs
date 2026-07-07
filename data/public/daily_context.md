# WATCHDOG — Briefing diario para el LLM

_Generado 2026-07-07T23:30:36+00:00 · ventana señales 2026-06-07 -> 2026-07-07_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 80.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.13)
- Tendencia: `bull` (SPY 747.71 · MA50 737.57 · MA200 689.71 · dist MA200: 8.41%)
- Credito: `unknown` (HY spread None)
- Tipos: `unknown` (curva 10y-2y None)
- Motivos: tendencia alcista (+)
- **AVISO**: sin datos de credit, rates (FRED API key no configurada). El presupuesto de riesgo puede ser impreciso.

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **80.0%** · cash **20.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 747.71 | -0.48% | 0.91% | 1.64% |
| QQQ | 12.0% | core | 709.43 | -1.85% | -2.02% | 0.73% |
| TLT | 12.0% | core | 84.55 | -1.05% | -2.96% | -0.23% |
| GLD | 12.0% | core | 377.49 | -1.21% | 2.42% | -4.73% |
| VFLEX | 12.0% | satellite | 27.67 | -0.43% | -0.36% | 0.44% |
| IEF | 10.4% | core | 93.7 | -0.51% | -1.11% | 0.42% |
| CWK | 1.8% | satellite | 13.81 | 0.15% | 0.51% | 3.29% |
| TOST | 1.6% | satellite | 29.61 | 0.44% | 5.15% | 20.17% |
| NWL | 1.4% | satellite | 5.54 | -0.54% | -8.58% | 48.92% |
| SSTK | 1.3% | satellite | 8.72 | -5.11% | -38.29% | -32.72% |
| GTM | 1.2% | satellite | 2.99 | 2.05% | 2.4% | 0.34% |
| ADPT | 1.1% | satellite | 20.82 | -3.16% | -2.71% | 23.2% |
| CWBHF | 0.5% | satellite | 0.31 | -6.28% | -3.06% | -28.19% |
| ZSPC | 0.4% | satellite | 0.19 | 5.56% | 0.0% | -1.04% |
| FIRY | 0.3% | satellite | 9.2 | -2.85% | -10.24% | 9.13% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 8.4%
- VaR 95% 1d: 0.8% · CVaR 95% 1d: 1.2%
- Max drawdown historico: -6.9%
- Beta vs SPY: 0.527 · posiciones efectivas: 11.9 · HHI: 0.0841

**Por que estos satellite (señales WATCHDOG):**

- **TOST** · score agregado 1226.4 · 20 señales · fuentes: corporate_insider
- **GTM** · score agregado 1018.0 · 17 señales · fuentes: corporate_insider
- **CWK** · score agregado 358.0 · 6 señales · fuentes: corporate_insider
- **ZSPC** · score agregado 292.0 · 5 señales · fuentes: corporate_insider
- **FIRY** · score agregado 288.2 · 5 señales · fuentes: corporate_insider
- **ADPT** · score agregado 273.8 · 7 señales · fuentes: corporate_insider
- **CWBHF** · score agregado 240.0 · 4 señales · fuentes: corporate_insider
- **NWL** · score agregado 192.3 · 3 señales · fuentes: corporate_insider
- **SSTK** · score agregado 176.0 · 3 señales · fuentes: corporate_insider
- **VFLEX** · score agregado 162.4 · 2 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| VFLEX | 85 | corporate_insider | PECK MICHAEL D | 2 | $4,999,988 | cluster_buy |
| VFLEX | 77 | corporate_insider | CHAD EISENBERG | 2 | $1,500,002 | cluster_buy |
| QNT | 72 | large_holder | Capital World Investors |  | - | - |
| BBSI | 72 | large_holder | Private Capital Managemen |  | - | - |
| TOFB | 72 | large_holder | LPL Financial LLC |  | - | - |
| ZBAO | 72 | large_holder | Ningbo Pangu Chuangfu Hef |  | - | - |
| MLP | 72 | large_holder | TSP Capital Management Gr |  | - | - |
| GWRE | 72 | large_holder | BAMCO INC /NY/ |  | - | - |
| SVRE | 72 | corporate_insider | VisionWave Holdings, Inc. | 0 | $1,135,938,816 | - |
| INTC | 71 | congress | Nancy Pelosi |  | $5,000,000 | - |
| OUT | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| TRNO | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| TDC | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| IVT | 70 | large_holder | Vanguard Portfolio Manage |  | - | - |
| EBRCZ | 70 | large_holder | Host-Plus Pty Ltd as trus |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| TOST | 71 | corporate_insider | Narang Aman | $414,416 | cluster_buy |
| TOST | 71 | corporate_insider | Gomez Elena | $334,793 | cluster_buy |
| TOST | 70 | corporate_insider | Fredette Stephen | $263,853 | cluster_buy |
| TOST | 66 | corporate_insider | Vassil Jonathan | $191,759 | cluster_buy |
| TPR | 65 | congress | Matthew Robert Van Epps | $50,000 | - |
| TOST | 65 | corporate_insider | Elworthy Brian R | $183,249 | cluster_buy |
| TCNNF | 64 | congress | Greg Stanton | $250,000 | - |
| AESI | 64 | congress | Chip Roy | $250,000 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 747.71 (-0.48% / 0.91% / 1.64%) [2026-07-07]
- QQQ: 709.43 (-1.85% / -2.02% / 0.73%) [2026-07-07]
- IWM: 296.19 (-0.91% / -0.93% / 5.41%) [2026-07-07]
- DIA: 528.45 (-0.31% / 1.3% / 3.96%) [2026-07-07]
- TLT: 84.55 (-1.05% / -2.96% / -0.23%) [2026-07-07]
- IEF: 93.7 (-0.51% / -1.11% / 0.42%) [2026-07-07]
- GLD: 377.49 (-1.21% / 2.42% / -4.73%) [2026-07-07]
- ^VIX: 16.13 (3.6% / -8.61% / -25.01%) [2026-07-07]
- BTC-USD: 63614.39 (-0.59% / 3.46% / -1.25%) [2026-07-07]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.17 (delta 1m: 0.12) [2026-07-01]
- Treasury 10Y yield: 4.48 (delta 1m: 0.01) [2026-07-01]
- Curva 10Y-2Y: 0.35 (delta 1m: -0.06) [2026-07-02]
- Fed Funds Rate: 3.63 (delta 1m: -1.5) [2026-06-01]
- High yield spread (OAS): 2.75 (delta 1m: 0.0) [2026-07-02]
- Tasa de paro: 4.2 (delta 1m: 0.0) [2026-06-01]
- Breakeven inflacion 10Y: 2.23 (delta 1m: -0.16) [2026-07-02]
- Dolar broad index: 120.8866 (delta 1m: 1.704) [2026-06-26]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (3), stock (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [WDAY] Fact check : Trump says stock market drove his 2025 income gains (2026-07-07)
- [MU] SEATTLE SET FOR HIGH - STAKES MUCKLESHOOT CASINO RESORT NHRA NORTHWEST NATIONALS (2026-07-07)
- [NET] Cloudflare Stock Tests 52 - Week High Zone : What Driving the Breakout ? - Cloudflare ( NYSE : NET ) (2026-07-07)
- [NET] AI meets Cryptography 1 : What AI Found in Cloudflare CIRCL (2026-07-07)
- [ADPT] BTIG Maintains a Buy Rating on Adaptive Biotechnologies ( ADPT ) (2026-06-28)
- [ADPT] Adaptive Biotechnologies ( NASDAQ : ADPT ) Trading Up 8 . 4 % – What Next ? (2026-06-24)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner ADVENT INTERNATIONAL, L.P. opero OLPX por $1.0B el 2026-07-07.
- 10% owner ADVENT INTERNATIONAL, L.P. opero OLPX por $1.0B el 2026-07-07.
- CEO PECK MICHAEL D compro VFLEX por $5.0M el 2026-07-02.
- Director Glynn Tricia vendio OLPX por $1.0B el 2026-07-07.
- Director VisionWave Holdings, Inc. compro SVRE por $1.1B el 2026-06-16.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager State Street Corp vendio MICROSOFT CORP por $34.5B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $27.9B.

**Polymarket — smart money (traders con mejor track record):**

- CandleHammerDrums · PnL $1,251,405 · win rate 96% · categorias: sports
- Oneger · PnL $493,621 · win rate 98% · categorias: sports
- HongYunX · PnL $148,288 · win rate 100% · categorias: sports
- Kch-Temp · PnL $185,900 · win rate 96% · categorias: sports
- BreakTheBank · PnL $524,962 · win rate 88% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `ok`
- **congress**: `ok` · 68 registros 30d · ultimo dato 2026-06-30
- **sec_insiders**: `ok` · 717 registros 30d · ultimo dato 2026-07-07
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-07-07
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`ADPT, CWBHF, CWK, FIRY, GLD, GTM, IEF, NWL, QQQ, SPY, SSTK, TLT, TOST, VFLEX, ZSPC`) o de las señales de la seccion 3, siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing.
2. **Presupuesto de riesgo**: la suma de todos los pesos <= **80.0%** (el resto es cash). Estamos en regimen `risk_on`.
3. **Peso maximo por posicion**: <= **12.0%**.
4. **Sin apalancamiento y sin cortos**: todos los pesos >= 0, suma <= 1.
5. **Justifica cada cambio** con una razon concreta basada en los datos de este briefing (señal, regimen, riesgo, precio). Nada de datos externos.

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
