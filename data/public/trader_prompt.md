<!-- trader_prompt.md generado 2026-09-15T13:49:45+00:00 -->

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

_Generado 2026-09-15T13:49:45+00:00 · ventana señales 2026-08-16 -> 2026-09-15_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 17.12)
- Tendencia: `bull` (SPY 759.42 · MA50 759.1 · MA200 713.0 · dist MA200: 6.51%)
- Credito: `tight` (HY spread 2.65)
- Tipos: `flat` (curva 10y-2y 0.32)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 759.42 | -0.19% | -0.85% | -1.71% |
| QQQ | 12.0% | core | 709.03 | -0.02% | -1.3% | -2.86% |
| TLT | 12.0% | core | 80.59 | -0.42% | -1.96% | -0.55% |
| CSQ | 9.3% | satellite | 20.36 | -0.34% | -2.32% | -1.94% |
| GLD | 9.3% | core | 393.59 | 0.19% | -1.53% | -2.93% |
| AMH | 8.3% | satellite | 31.22 | -1.31% | -3.36% | -7.18% |
| ECL | 6.6% | satellite | 273.95 | -0.57% | -1.5% | -0.68% |
| IEF | 6.2% | core | 90.81 | -0.13% | -1.46% | -1.84% |
| MG | 3.1% | satellite | 19.57 | 0.18% | 0.75% | 7.86% |
| PMTS | 2.4% | satellite | 24.78 | 2.16% | -14.75% | -13.65% |
| SLGL | 2.2% | satellite | 65.49 | 0.48% | -5.59% | -21.11% |
| USAR | 1.7% | satellite | 15.52 | -1.21% | -12.12% | -19.54% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 10.6%
- VaR 95% 1d: 1.0% · CVaR 95% 1d: 1.4%
- Max drawdown historico: -3.6%
- Beta vs SPY: 0.701 · posiciones efectivas: 12.8 · HHI: 0.0779

**Por que estos satellite (señales WATCHDOG):**

- **CSQ** · score agregado 282.0 · 4 señales · fuentes: large_holder
- **PMTS** · score agregado 233.9 · 3 señales · fuentes: corporate_insider
- **USAR** · score agregado 207.0 · 3 señales · fuentes: large_holder
- **ECL** · score agregado 117.5 · 2 señales · fuentes: corporate_insider
- **SLGL** · score agregado 117.2 · 2 señales · fuentes: corporate_insider
- **AMH** · score agregado 111.7 · 2 señales · fuentes: corporate_insider
- **MG** · score agregado 70.2 · 1 señales · fuentes: large_holder

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| GREE | 80 | corporate_insider | Kovler Jordan | 3 | $99,999 | cluster_buy |
| GREE | 80 | corporate_insider | Irwin Dale | 3 | $99,999 | cluster_buy |
| GREE | 80 | corporate_insider | Mulvihill Christian | 3 | $99,999 | cluster_buy |
| PMTS | 79 | corporate_insider | Riley H Sanford | 4 | $299,990 | cluster_buy |
| PMTS | 78 | corporate_insider | Peters Nicholas | 4 | $250,002 | cluster_buy |
| MAIA | 76 | corporate_insider | Vitoc Vlad | 2 | $100,010 | cluster_buy |
| PMTS | 76 | corporate_insider | SHEINBAUM MARC | 4 | $99,996 | cluster_buy |
| OFLX | 74 | corporate_insider | Unger Matthew Francis | 2 | $25,420 | cluster_buy |
| PMTS | 73 | corporate_insider | Mallela Ravi | 4 | $21,500 | cluster_buy,small_amount |
| OFLX | 73 | corporate_insider | Moran Edwin B. | 2 | $20,090 | cluster_buy,small_amount |
| GLOO | 72 | large_holder | Grace & Mercy Foundation, |  | - | - |
| ANIX | 71 | corporate_insider | KUMAR AMIT | 2 | $8,250 | cluster_buy,small_amount |
| MAIA | 71 | corporate_insider | Guerrero Ramiro | 2 | $49,516 | cluster_buy |
| HEPS | 70 | large_holder | Joint Stock Company Kaspi |  | - | - |
| SPAI | 70 | large_holder | Phillip Frost, M.D. |  | - | - |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| PMTS | 60 | corporate_insider | Parallel49 Equity, ULC | $54,900,786 | - |
| GMRS | 60 | corporate_insider | Loporcaro Nicola | $17,776,644 | - |
| DBX | 58 | corporate_insider | Houston Andrew | $11,350,091 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $4,362,021 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $4,077,315 | - |
| P | 56 | corporate_insider | Giancarlo Charles H | $3,883,237 | - |
| GMRS | 56 | corporate_insider | Van Horne Edward | $3,199,792 | - |
| RYTM | 56 | corporate_insider | Meeker David P | $3,146,761 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 759.42 (-0.19% / -0.85% / -1.71%) [2026-09-15]
- QQQ: 709.03 (-0.02% / -1.3% / -2.86%) [2026-09-15]
- IWM: 285.43 (-0.86% / -3.14% / -6.13%) [2026-09-15]
- DIA: 521.23 (-0.62% / -1.29% / -2.34%) [2026-09-15]
- TLT: 80.59 (-0.42% / -1.96% / -0.55%) [2026-09-15]
- IEF: 90.81 (-0.13% / -1.46% / -1.84%) [2026-09-15]
- GLD: 393.59 (0.19% / -1.53% / -2.93%) [2026-09-15]
- ^VIX: 17.12 (0.12% / 8.91% / 8.08%) [2026-09-15]
- BTC-USD: 76278.98 (-2.41% / -0.38% / -3.48%) [2026-09-15]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.63 (delta 1m: 0.43) [2026-09-11]
- Treasury 10Y yield: 4.96 (delta 1m: 0.28) [2026-09-11]
- Curva 10Y-2Y: 0.32 (delta 1m: -0.16) [2026-09-14]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.65 (delta 1m: -0.06) [2026-09-11]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.37 (delta 1m: 0.13) [2026-09-14]
- Dolar broad index: 118.2126 (delta 1m: -0.905) [2026-09-11]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (2), regulatory (2), earnings (2), merger (1), stock (1)

**Titulares recientes (GDELT, tickers con mas señales):**

- [HII] Sequoia Financial Advisors LLC Acquires 4 , 748 Shares of Huntington Ingalls Industries , Inc . $HII (2026-09-12)
- [NTSK] Netskope ( NTSK ) Rides AI Security Wave to 29 % Topline Growth (2026-09-11)
- [NTSK] Netskope ( NTSK ) Q2 2027 Earnings Call Transcript (2026-09-10)
- [NTSK] Netskope ( NTSK ) Q2 2027 Earnings Call Transcript (2026-09-10)
- [NTSK] Netskope ( NTSK ) Rides AI Security Wave to 29 % Topline Growth (2026-09-09)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Loporcaro Nicola vendio GMRS por $17.8M el 2026-09-14.
- 10% owner Parallel49 Equity, ULC vendio PMTS por $54.9M el 2026-09-14.
- CEO Houston Andrew vendio DBX por $11.4M el 2026-09-10.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.

**Polymarket — smart money (traders con mejor track record):**

- Kch-Temp · PnL $138,459 · win rate 90% · categorias: sports
- lllllllIlll · PnL $39,595 · win rate 94% · categorias: sports
- RJW1 · PnL $11,043 · win rate 98% · categorias: sports
- five5120 · PnL $19,041 · win rate 90% · categorias: sports
- 0xbbf379252411511ADAb081F016Dc991aA6bbAA3A-1768154730738 · PnL $14,326 · win rate 85% · categorias: sports, crypto

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 463 registros 30d · ultimo dato 2026-09-15
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-15
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`AMH, CSQ, ECL, GLD, IEF, MG, PMTS, QQQ, SLGL, SPY, TLT, USAR`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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

