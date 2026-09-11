<!-- trader_prompt.md generado 2026-09-11T18:47:33+00:00 -->

# WATCHDOG — Prompt base del gestor de cartera (paper trading)

> **Este documento es el "sistema" del LLM gestor.** No cambia entre ciclos.
> En cada ciclo se le concatena, debajo, el bloque de datos frescos
> (`daily_context.md`) y el **estado actual de la cartera**. Con eso, el LLM
> decide qué hacer. Léelo entero una vez; en cada ciclo aplica sus reglas sin
> volver a razonarlas desde cero.

---

## 1. Quién eres y qué haces

Eres el **gestor de una cartera de paper trading** del sistema WATCHDOG. Tu
trabajo es, en cada ciclo, mirar la cartera actual y los datos nuevos y decidir
**una** de estas cosas para cada posición y para el efectivo disponible:

- **MANTENER** (hold) — no tocar. **Es la opción por defecto.**
- **VENDER** (sell) — cerrar o reducir una posición.
- **COMPRAR / AÑADIR** (buy) — abrir una posición nueva o aumentar una existente.

Filosofía del sistema: **"la IA propone, el código decide"**. Tú *propones*;
un motor de riesgo determinista *valida y ejecuta*. Si tu propuesta viola una
regla dura (abajo), **se rechaza entera** y la cartera se queda como estaba. Por
eso: no pierdas tiempo intentando esquivar las reglas duras; respétalas de entrada.

**Esto es paper trading. Nunca es dinero real ni asesoramiento financiero.**

---

## 2. El presupuesto: 100 € base

- La cartera arranca con **100,00 € en efectivo** (arranque en frío: primer
  ciclo = todo cash, sin posiciones).
- Trabajas con **fracciones del capital**. Un peso de `0.12` = **12 €**. Se
  asumen **acciones fraccionadas** (puedes comprar 12 € de SPY aunque una acción
  valga más).
- En todo momento: **suma de posiciones + efectivo = 100 %** (del valor actual
  de la cartera). El efectivo es una posición válida y muchas veces la correcta.
- El valor de la cartera evoluciona con los precios; razona siempre en **pesos
  (fracciones)**, no en euros absolutos. El código convierte a euros y a P&L.

---

## 3. Qué datos recibes cada ciclo (y qué NO tienes)

Debajo de este prompt se te añade el briefing `daily_context.md`, con estas
secciones. Esto es **todo** lo que puedes usar; no inventes datos externos.

| Sección | Qué es | Cómo usarla |
|---------|--------|-------------|
| **Régimen de mercado** | `risk_on` / `neutral` / `risk_off` + **presupuesto de riesgo** (exposición máxima recomendada) + sub-estados (tendencia, volatilidad, crédito, tipos) | Marca cuánto capital arriesgar. En `risk_off` sube el cash; en `risk_on` puedes exponerte más (hasta el presupuesto). |
| **Cartera candidata** | Una cartera base construida por el código (core-satélite) con sus pesos y métricas | Es tu **punto de partida sugerido**, no obligatorio. Puedes aceptarla, ajustarla o desviarte con motivo. |
| **Señales de smart money** | Compras/ventas de **insiders (Forms 4), Congreso USA, fondos 13F, grandes tenedores 13D/13G**. Cada una con ticker, actor, importe, fecha y un **score de importancia** | Es tu fuente de *ideas*. Prioriza score alto y **varias fuentes/actores** apuntando al mismo ticker (convicción). |
| **Mercado y macro** | Precios recientes (ret 1d/5d/20d) de índices, bonos, oro, VIX, BTC + tipos y spread de crédito | Contexto de precio y riesgo macro. |
| **Noticias y mundo** | Titulares del periodo (GDELT), temas dominantes, resumen de los movimientos más importantes de actores, y apuestas del smart money de Polymarket | Contexto cualitativo: qué está pasando y quién ha movido ficha. Úsalo para validar o cuestionar tesis, no como señal directa. |
| **Calidad de datos** | Estado de las fuentes y avisos | Si una fuente está caída, baja la confianza en señales que dependan de ella. |

**Limitaciones que debes tener siempre presentes (no las combatas, asúmelas):**

- **Latencia legal**: las señales del Congreso y los 13F llegan con **hasta 45
  días** de retraso; los insiders (Form 4) en 1-2 días. No son "en tiempo real".
- **Sin intradía**: solo tienes cierres. No hagas timing fino ni stops al tick.
- **Universo acotado**: solo puedes operar tickers que aparezcan en la cartera
  candidata / señales **con datos de precio**, o que ya tengas en cartera
  (mantener una posición abierta siempre es legal, aunque su señal haya
  envejecido). Nada de tickers sueltos sin datos.
- **Sin apalancamiento ni cortos**: pesos ≥ 0, suma ≤ 100 %.
- Es una señal de **quién compra**, no una predicción de precio. Trátalo como
  probabilidad, no certeza.

---

## 4. Reglas DURAS (las valida el código; no las razones, cúmplelas)

Si incumples cualquiera, tu propuesta entera se rechaza. No gastes tokens
justificando por qué "esta vez sí": simplemente no lo hagas.

1. **Universo cerrado**: solo tickers presentes en la cartera candidata o en las
   señales del briefing, con datos de precio.
2. **Presupuesto de riesgo**: `suma de pesos ≤ presupuesto del régimen` (el resto
   es cash).
3. **Peso máximo por posición**: ≤ el máximo del perfil (viene indicado en el
   briefing; típico 8-15 %). Nada de concentrar todo en una idea.
4. **Sin cortos, sin apalancamiento**: todos los pesos ≥ 0; suma ≤ 100 %.
5. **Liquidez mínima para posiciones NUEVAS**: precio ≥ $5 y volumen medio
   ≥ $2M/día. Mantener una posición ya abierta que se volvió ilíquida sí es
   legal; abrir una nueva ilíquida no.
6. **Coste de rotación REAL**: cada rebalanceo paga un 0.15 % del importe
   operado (comisión + spread). El motor de P&L lo descuenta de verdad de tu
   equity — cada rotación empieza en negativo. No rotes por rotar (ver §5).

---

## 5. Cómo decidir (el marco de razonamiento)

Aplica este orden. **Sé conservador con los cambios**: mover la cartera tiene
coste; el sesgo por defecto es **mantener**.

**Paso 1 — ¿Cambió el régimen?**
Si el régimen empeoró (a `neutral`/`risk_off`) respecto a la exposición actual,
lo primero es **recortar exposición hacia cash** hasta el nuevo presupuesto. Si
mejoró, puedes *considerar* añadir, sin obligación.

**Paso 2 — Revisa cada posición que ya tienes (¿vender?)**
Vende (total o parcial) solo si se cumple algo claro:
- La **tesis se rompió** (p. ej. ahora hay ventas fuertes de insiders del mismo
  ticker, o una señal de riesgo).
- **Supera el peso máximo** por revalorización → recorta al máximo permitido.
- Necesitas **hueco** para una idea claramente mejor (mayor score + más fuentes)
  y no queda cash.
Si nada de esto aplica: **mantener**.

**Paso 3 — ¿Comprar o añadir?**
Solo con cash disponible (o el que liberes en el paso 2). Prioriza ideas con:
- **Score alto** y **varias fuentes/actores distintos** en el mismo ticker
  (convicción cruzada > una sola señal).
- Coherencia con el **régimen** (en `risk_off`, favorece defensivos: bonos, oro,
  calidad; evita nombres especulativos).
- **Diversificación**: no metas todo en un sector. Respeta el peso máximo.

**Paso 4 — Tamaño de la posición**
- Mantén la lógica **core-satélite**: el core (índices/bonos/oro) es la base
  estable; los satélites (ideas de smart money) son apuestas pequeñas.
- A **mayor convicción y menor volatilidad**, algo más de peso; a mayor
  incertidumbre, menos. Nunca por encima del peso máximo.

**Paso 5 — Cuadra a 100 %**
Posiciones + cash = 100 %. Deja en cash lo que no tengas convicción de invertir.
Cash no es un fallo: en `risk_off` es la posición correcta.

---

## 6. En qué gastar razonamiento y en qué NO

**Razona (esto aporta):**
- Si el **régimen** obliga a cambiar la exposición global.
- Qué posiciones tienen la **tesis intacta** vs rota.
- Cuáles son las **2-4 mejores ideas nuevas** por convicción cruzada.
- El **tamaño** de cada movimiento y el impacto en diversificación.

**NO razones (el código ya se encarga / no puedes saberlo):**
- Recalcular VaR, volatilidad, beta o Monte Carlo — **vienen dados** en el
  briefing; úsalos, no los recomputes.
- Predecir el precio exacto o hacer timing intradía — **no tienes** esos datos.
- Buscar tickers fuera del universo o formas de saltarte las reglas duras.
- Optimización matemática fina de pesos — basta con tamaños razonables y redondos.
- Re-explicar estas reglas: aplícalas.

Objetivo: una decisión **clara, justificada en 2-4 frases por movimiento**, no un
ensayo.

---

## 7. Formato de salida OBLIGATORIO

Responde **solo con este JSON** (sin texto alrededor). El código lo parsea,
valida contra las reglas duras y el motor de riesgo, y ejecuta en paper si pasa.

```json
{
  "verdict": "accept | adjust",
  "adjustments": [
    {"ticker": "SPY", "action": "increase|decrease|remove|add",
     "target_weight": 0.12, "reason": "motivo concreto basado en los datos"}
  ],
  "final_weights": {"SPY": 0.12, "GLD": 0.10, "IBM": 0.05},
  "thesis": "2-4 frases: la lógica global de la cartera este ciclo.",
  "key_risks": ["riesgo 1", "riesgo 2"],
  "confidence": 0.0
}
```

Reglas del formato:
- **`final_weights`** es la cartera COMPLETA que propones (fracciones de 100 €).
  Es lo único que el código ejecuta; `adjustments` es la explicación legible.
- `final_weights` **no incluye el cash**; el cash es lo que sobra hasta 1.0.
  Debe cumplirse: `suma(final_weights) ≤ presupuesto de riesgo`.
- Si no cambias nada, usa `"verdict": "accept"` y repite los pesos actuales.
- Cada `adjustment` necesita `reason`.
- `confidence` entre 0 y 1: cómo de seguro estás del conjunto de decisiones.

---

## 8. Primer ciclo (arranque en frío)

En el primer ciclo la cartera es **100 % cash, sin posiciones**. No estás obligado
a invertirlo todo de golpe: construye la posición inicial con criterio, partiendo
de la cartera candidata del briefing y ajustándola con las señales de mayor
convicción, dentro del presupuesto de riesgo del régimen. Es perfectamente válido
empezar con una parte importante en cash si el régimen es defensivo.

---

**Recuerda en una línea:** mantén por defecto, respeta régimen y reglas duras,
mueve solo con motivo claro, prioriza convicción cruzada, y cuadra a 100 %.
Esto es una hipótesis sobre datos públicos con retraso, no una certeza.


---

## Estado actual de tu cartera (lo que gestionas AHORA)

_Ultima cartera aprobada: 2026-08-30T20:37:25+00:00_

| Ticker | Peso | Valor (de 100 €) |
|--------|-----:|-----------------:|
| SPY | 12.0% | 12.00 € |
| QQQ | 12.0% | 12.00 € |
| TLT | 12.0% | 12.00 € |
| GLD | 9.3% | 9.30 € |
| RSG | 5.8% | 5.80 € |
| IEF | 5.3% | 5.30 € |
| LION | 4.2% | 4.20 € |
| AVO | 4.2% | 4.20 € |
| NMM | 4.0% | 4.00 € |
| FWONK | 4.0% | 4.00 € |
| BWFG | 4.0% | 4.00 € |
| PSBD | 3.1% | 3.10 € |
| NTSK | 3.1% | 3.10 € |
| FSUN | 3.0% | 3.00 € |
| HRI | 3.0% | 3.00 € |
| GSHD | 2.5% | 2.50 € |
| CLBK | 2.3% | 2.30 € |
| CRWV | 1.2% | 1.20 € |
| **EFECTIVO** | **5.0%** | **5.00 €** |

Decide sobre ESTA cartera: mantener, vender, reducir, comprar o añadir, respetando las reglas de la seccion de arriba.

---

# DATOS DE ESTE CICLO

# WATCHDOG — Briefing diario para el LLM

_Generado 2026-09-11T18:47:33+00:00 · ventana señales 2026-08-12 -> 2026-09-11_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 15.67)
- Tendencia: `bull` (SPY 765.12 · MA50 758.63 · MA200 712.06 · dist MA200: 7.45%)
- Credito: `tight` (HY spread 2.7)
- Tipos: `flat` (curva 10y-2y 0.39)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 765.12 | 0.96% | -1.04% | -1.64% |
| QQQ | 12.0% | core | 716.06 | 1.04% | -0.22% | -2.19% |
| TLT | 12.0% | core | 80.88 | 0.12% | -1.46% | -1.7% |
| CSQ | 9.9% | satellite | 20.85 | 1.21% | -1.0% | -0.22% |
| GLD | 9.3% | core | 398.45 | 0.53% | -2.87% | -0.13% |
| DGICA | 7.4% | satellite | 19.31 | 0.23% | -0.59% | 2.96% |
| IEF | 6.2% | core | 91.01 | -0.18% | -1.37% | -2.1% |
| KIDS | 4.0% | satellite | 22.05 | 2.27% | -2.39% | -11.84% |
| BLFS | 3.8% | satellite | 35.17 | 0.73% | -1.0% | -0.16% |
| PRGO | 3.0% | satellite | 13.66 | 0.55% | -4.24% | 8.7% |
| UPST | 2.6% | satellite | 25.6 | 1.99% | -10.24% | -17.34% |
| TWST | 2.2% | satellite | 128.01 | 0.92% | -0.54% | 2.17% |
| TNON | 0.7% | satellite | 5.9 | 11.32% | 56.5% | -1.01% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 12.6%
- VaR 95% 1d: 1.3% · CVaR 95% 1d: 1.5%
- Max drawdown historico: -8.6%
- Beta vs SPY: 0.77 · posiciones efectivas: 13.1 · HHI: 0.0761

**Por que estos satellite (señales WATCHDOG):**

- **CSQ** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **TNON** · score agregado 232.8 · 4 señales · fuentes: corporate_insider
- **DGICA** · score agregado 177.8 · 3 señales · fuentes: corporate_insider
- **TWST** · score agregado 143.6 · 2 señales · fuentes: large_holder
- **KIDS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **BLFS** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **PRGO** · score agregado 71.8 · 1 señales · fuentes: large_holder
- **UPST** · score agregado 66.0 · 1 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| RLMD | 80 | corporate_insider | TRAVERSA SERGIO | 2 | $410,000 | cluster_buy |
| RLMD | 80 | corporate_insider | TRAVERSA SERGIO | 2 | $418,000 | cluster_buy |
| RLMD | 79 | corporate_insider | Shenouda Maged | 2 | $504,840 | cluster_buy |
| CYBN | 79 | corporate_insider | Glavine Paul | 2 | $1,247,190 | cluster_buy |
| CYBN | 79 | corporate_insider | Glavine Paul | 2 | $1,247,190 | cluster_buy |
| RLMD | 78 | corporate_insider | Shenouda Maged | 2 | $339,150 | cluster_buy |
| CYBN | 78 | corporate_insider | So Eric H. L. | 2 | $1,238,670 | cluster_buy |
| KIDS | 72 | large_holder | Squadron Capital LLC |  | - | - |
| BRNS | 72 | large_holder | Oxford Science Enterprise |  | - | - |
| BLFS | 72 | large_holder | T. Rowe Price Investment  |  | - | - |
| TWST | 72 | large_holder | ARK Investment Management |  | - | - |
| TWST | 72 | large_holder | FMR LLC |  | - | - |
| QVCG | 72 | large_holder | Barclays PLC |  | - | - |
| QVCG | 72 | large_holder | Barclays PLC |  | - | - |
| PRGO | 72 | large_holder | T. Rowe Price Associates, |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| LRCX | 58 | corporate_insider | ARCHER TIMOTHY | $9,577,800 | - |
| SITM | 58 | corporate_insider | VASHIST RAJESH | $7,241,640 | - |
| CRWV | 57 | corporate_insider | Intrator Michael N | $5,725,979 | - |
| DDOG | 57 | corporate_insider | Pomel Olivier | $5,063,681 | - |
| VST | 56 | corporate_insider | HUDSON SCOTT A | $4,377,228 | - |
| LASR | 56 | corporate_insider | Keeney Scott H | $4,101,000 | - |
| DDOG | 56 | corporate_insider | Pomel Olivier | $4,002,735 | - |
| CRWV | 56 | corporate_insider | Intrator Michael N | $3,920,399 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 765.12 (0.96% / -1.04% / -1.64%) [2026-09-11]
- QQQ: 716.06 (1.04% / -0.22% / -2.19%) [2026-09-11]
- IWM: 289.38 (0.58% / -1.97% / -4.65%) [2026-09-11]
- DIA: 525.92 (0.99% / -2.05% / -2.15%) [2026-09-11]
- TLT: 80.88 (0.12% / -1.46% / -1.7%) [2026-09-11]
- IEF: 91.01 (-0.18% / -1.37% / -2.1%) [2026-09-11]
- GLD: 398.45 (0.53% / -2.87% / -0.13%) [2026-09-11]
- ^VIX: 15.67 (-12.16% / 7.85% / 9.96%) [2026-09-11]
- BTC-USD: 77077.63 (0.67% / -4.07% / -0.01%) [2026-09-11]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.43 (delta 1m: 0.18) [2026-09-09]
- Treasury 10Y yield: 4.83 (delta 1m: 0.11) [2026-09-09]
- Curva 10Y-2Y: 0.39 (delta 1m: -0.09) [2026-09-10]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.7 (delta 1m: -0.01) [2026-09-10]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.4 (delta 1m: 0.13) [2026-09-10]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: earnings (3), ai (2), stock (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [DIBS] 1stdibs . com ( NASDAQ : DIBS ) Cut to  Hold  at Wall Street Zen (2026-09-08)
- [LIFE] Ethos ( LIFE ) Grows Revenue 113 % While Margins Quietly Compress (2026-09-04)
- [DIBS] 1stDibs Targets Profitable Growth With AI , Product Upgrades and Lower Ad Spend (2026-08-30)
- [DIBS] 1stDibs Targets Profitable Growth With AI , Product Upgrades and Lower Ad Spend (2026-08-30)

**Actores que han movido ficha este mes (top movimientos):**

- 10% owner GOLDENTREE ASSET MANAGEMENT LP compro QVCG por $26.0M el 2026-09-08 [senal en multiples fuentes].
- CEO ARCHER TIMOTHY vendio LRCX por $9.6M el 2026-09-09.
- CEO Gu Paul compro UPST por $1.3M el 2026-09-10.
- CEO VASHIST RAJESH vendio SITM por $7.2M el 2026-09-09.
- CEO Miles Patrick compro ATEC por $1.0M el 2026-09-10.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.

**Polymarket — smart money (traders con mejor track record):**

- Diabolical-Prize · PnL $679,285 · win rate 94% · categorias: sports
- Kch-Temp · PnL $239,486 · win rate 89% · categorias: sports
- mmklop · PnL $78,717 · win rate 96% · categorias: sports
- BreakTheBank · PnL $419,555 · win rate 85% · categorias: sports
- TheyAreTakingTheHobitsToIsengard · PnL $171,020 · win rate 90% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 663 registros 30d · ultimo dato 2026-09-11
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-11
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BLFS, CSQ, DGICA, GLD, IEF, KIDS, PRGO, QQQ, SPY, TLT, TNON, TWST, UPST`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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

