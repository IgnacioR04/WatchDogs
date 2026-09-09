<!-- trader_prompt.md generado 2026-09-09T21:58:38+00:00 -->

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

_Generado 2026-09-09T21:58:38+00:00 · ventana señales 2026-08-10 -> 2026-09-09_

Este documento contiene todo lo que necesitas para revisar la cartera. Lee de arriba abajo: regimen -> cartera propuesta -> señales -> mercado -> noticias/mundo -> calidad -> instrucciones. Responde segun la seccion 7.

---

## 1. Regimen de mercado

- **Estado de riesgo**: `risk_on`  -> **presupuesto de riesgo recomendado: 90.0%** (exposicion maxima a activos; el resto en cash)
- Volatilidad: `normal` (VIX 16.46)
- Tendencia: `bull` (SPY 762.4 · MA50 758.02 · MA200 710.95 · dist MA200: 7.24%)
- Credito: `tight` (HY spread 2.67)
- Tipos: `flat` (curva 10y-2y 0.4)
- Fed Funds: 3.63%
- Motivos: tendencia alcista (+); credito tenso/risk-on (+)

## 2. Cartera CANDIDATA (propuesta por el codigo)

Perfil **moderado** · exposicion total **85.0%** · cash **15.0%** · gate **PASS**

| Ticker | Peso | Bloque | Precio | Ret 1d | Ret 5d | Ret 20d |
|--------|-----:|--------|-------:|-------:|-------:|--------:|
| SPY | 12.0% | core | 762.4 | -0.46% | 0.08% | -1.06% |
| QQQ | 12.0% | core | 716.31 | -0.29% | 1.23% | -0.3% |
| TLT | 12.0% | core | 81.73 | -0.57% | -0.17% | -0.18% |
| GLD | 9.3% | core | 403.35 | 0.91% | 1.66% | 0.6% |
| CSQ | 9.0% | satellite | 20.85 | -0.62% | 0.58% | 0.5% |
| IEF | 6.2% | core | 91.89 | -0.29% | -0.22% | -0.69% |
| DGICA | 5.9% | satellite | 19.0 | 0.0% | -0.89% | 1.71% |
| BWFG | 5.3% | satellite | 66.71 | 0.83% | 1.91% | -1.88% |
| UBER | 3.3% | satellite | 71.08 | -2.8% | -5.53% | -9.5% |
| ZBIO | 2.4% | satellite | 32.29 | -2.3% | 0.97% | -0.46% |
| TENB | 1.7% | satellite | 33.67 | -0.09% | -5.07% | -11.02% |
| LEU | 1.7% | satellite | 181.49 | -2.18% | 7.83% | -4.07% |
| EAF | 1.4% | satellite | 6.17 | -2.06% | -13.22% | -22.0% |
| TWST | 1.4% | satellite | 125.52 | -1.98% | -4.95% | 1.95% |
| SEI | 1.4% | satellite | 67.67 | 5.8% | 36.32% | 15.1% |

**Metricas de riesgo de esta cartera:**

- Volatilidad anualizada: 9.9%
- VaR 95% 1d: 0.9% · CVaR 95% 1d: 1.0%
- Max drawdown historico: -2.3%
- Beta vs SPY: 0.706 · posiciones efectivas: 13.7 · HHI: 0.073

**Por que estos satellite (señales WATCHDOG):**

- **BWFG** · score agregado 459.8 · 6 señales · fuentes: corporate_insider
- **CSQ** · score agregado 211.5 · 3 señales · fuentes: large_holder
- **ZBIO** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **TWST** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **EAF** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **LEU** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **TENB** · score agregado 141.0 · 2 señales · fuentes: large_holder
- **UBER** · score agregado 124.5 · 2 señales · fuentes: corporate_insider
- **DGICA** · score agregado 118.9 · 2 señales · fuentes: corporate_insider
- **SEI** · score agregado 117.0 · 2 señales · fuentes: corporate_insider

## 3. Señales de smart money (30d)

### 3a. Compras (buy signals)

| Ticker | Score | Fuente | Actor | Cluster | Importe | Flags |
|--------|------:|--------|-------|--------:|--------:|-------|
| BWFG | 79 | corporate_insider | SEIDMAN LAWRENCE B | 5 | $130,896 | cluster_buy |
| BWFG | 78 | corporate_insider | SEIDMAN LAWRENCE B | 5 | $87,264 | cluster_buy |
| BWFG | 76 | corporate_insider | SEIDMAN LAWRENCE B | 5 | $34,144 | cluster_buy |
| BWFG | 76 | corporate_insider | SEIDMAN LAWRENCE B | 5 | $34,474 | cluster_buy |
| BWFG | 76 | corporate_insider | SEIDMAN LAWRENCE B | 5 | $28,922 | cluster_buy |
| TSM | 76 | corporate_insider | Wei Che-Chia | 30 | $11,354 | cluster_buy,small_amount |
| BWFG | 75 | corporate_insider | SEIDMAN LAWRENCE B | 5 | $18,955 | cluster_buy,small_amount |
| BWFG | 75 | corporate_insider | SEIDMAN LAWRENCE B | 5 | $17,851 | cluster_buy,small_amount |
| BWFG | 74 | corporate_insider | Dale Eric J | 5 | $35,568 | cluster_buy |
| BWFG | 73 | corporate_insider | Porto Carl M | 5 | $21,945 | cluster_buy,small_amount |
| BWFG | 73 | corporate_insider | Dunne Jeffrey R | 5 | $17,516 | cluster_buy,small_amount |
| MFP | 72 | large_holder | T. Rowe Price Associates, |  | - | - |
| SUI | 72 | large_holder | BlackRock, Inc. |  | - | - |
| SMTC | 72 | large_holder | BlackRock, Inc. |  | - | - |
| TSM | 71 | corporate_insider | Huang Jen-Chau | 30 | $2,286 | cluster_buy,small_amount |

### 3b. Ventas (sell signals) — atencion si afectan a posiciones existentes

| Ticker | Score | Fuente | Actor | Importe | Flags |
|--------|------:|--------|-------|--------:|-------|
| BNTX | 57 | corporate_insider | Sahin Ugur | $4,628,232 | - |
| BNTX | 56 | corporate_insider | Sahin Ugur | $3,260,823 | - |
| ECAT | 53 | corporate_insider | Saba Capital Management,  | $2,555,739 | - |
| RLAY | 53 | corporate_insider | Patel Sanjiv | $912,889 | - |
| UTHR | 53 | corporate_insider | ROTHBLATT MARTINE A | $947,531 | - |
| PLPC | 53 | corporate_insider | RUHLMAN RANDALL M | $2,038,900 | - |
| AFL | 52 | corporate_insider | Japan Post Holdings Co.,  | $1,744,281 | - |
| IVZ | 52 | corporate_insider | DUKES LAURA ALLISON | $1,030,537 | - |

> **Cluster** = n de insiders distintos comprando el mismo ticker (señal de conviccion). **Score** = importancia individual de la señal.
> Los scores AGREGADOS por ticker (suma de todas sus señales) estan en la seccion 2 (satellite rationale). Un ticker con score agregado alto y multiples fuentes distintas tiene mayor conviccion.

## 4. Snapshot de mercado y macro

**Indices y activos de referencia:**

- SPY: 762.4 (-0.46% / 0.08% / -1.06%) [2026-09-09]
- QQQ: 716.31 (-0.29% / 1.23% / -0.3%) [2026-09-09]
- IWM: 290.64 (-1.37% / 0.02% / -3.44%) [2026-09-09]
- DIA: 524.07 (-0.75% / -0.7% / -2.38%) [2026-09-09]
- TLT: 81.73 (-0.57% / -0.17% / -0.18%) [2026-09-09]
- IEF: 91.89 (-0.29% / -0.22% / -0.69%) [2026-09-09]
- GLD: 403.35 (0.91% / 1.66% / 0.6%) [2026-09-09]
- ^VIX: 16.46 (4.71% / 8.29% / 13.13%) [2026-09-09]
- BTC-USD: 78091.85 (-0.44% / -1.98% / 6.93%) [2026-09-09]

**Macro (valor · cambio 1m):**

- Treasury 2Y yield: 4.39 (delta 1m: 0.2) [2026-09-08]
- Treasury 10Y yield: 4.8 (delta 1m: 0.15) [2026-09-08]
- Curva 10Y-2Y: 0.4 (delta 1m: -0.07) [2026-09-09]
- Fed Funds Rate: 3.63 (delta 1m: -1.01) [2026-08-01]
- High yield spread (OAS): 2.67 (delta 1m: -0.03) [2026-09-08]
- Tasa de paro: 4.1 (delta 1m: 0.0) [2026-08-01]
- Breakeven inflacion 10Y: 2.37 (delta 1m: 0.08) [2026-09-09]
- Dolar broad index: 118.0732 (delta 1m: -1.438) [2026-09-04]

## 5. Noticias y contexto del mundo (30d)

**Temas dominantes**: ai (3), regulatory (3), stock (2)

**Titulares recientes (GDELT, tickers con mas señales):**

- [TSM] TSMC market share edges higher - Taipei Times (2026-09-09)
- [TSM] TSMC to use ASML next - gen machines for high - volume chip manufacturing (2026-09-09)
- [BWFG] Carl Porto Buys 327 Shares of Bankwell Financial Group ( NASDAQ : BWFG ) Stock (2026-09-09)
- [TSM] Cidel Asset Management Inc . Grows Position in Taiwan Semiconductor Manufacturing Company Ltd . $TSM (2026-09-09)
- [SBSI] Southside Bancshares ( NYSE : SBSI ) versus China Minsheng ( OTCMKTS : CMAKY ) Financial Comparison (2026-09-07)
- [UTHR] Reviewing United Therapeutics ( NASDAQ : UTHR ) and Zenas BioPharma ( NASDAQ : ZBIO ) (2026-09-07)
- [UTHR] Former Anheuser - Busch plant sold to United Therapeutics (2026-09-03)
- [UTHR] Anheuser - Busch plant in Merrimack sold to United Therapeutics for $47 . 5M (2026-09-02)
- [UTHR] United Therapeutics Announces FDA Acceptance Of SNDA For Nebulized Tyvaso In IPF (2026-09-02)

**Actores que han movido ficha este mes (top movimientos):**

- CEO Barry John F compro PSEC por $2.7M el 2026-09-04.
- Institutional manager State Street Corp compro MICRON TECHNOLOGY INC por $40.1B.
- Institutional manager Vanguard Group Inc compro ALPHABET INC por $35.5B.
- Institutional manager Invesco Ltd compro MICRON TECHNOLOGY INC por $31.4B.
- Institutional manager JPMorgan Chase & Co compro MICRON TECHNOLOGY INC por $16.1B.
- Institutional manager Citadel Advisors LLC compro MICRON TECHNOLOGY INC por $14.9B.
- Institutional manager Geode Capital Management LLC vendio ELI LILLY & CO por $13.2B.

**Polymarket — smart money (traders con mejor track record):**

- Diabolical-Prize · PnL $433,449 · win rate 95% · categorias: sports
- mmklop · PnL $111,877 · win rate 96% · categorias: sports
- Di88medes · PnL $78,733 · win rate 100% · categorias: sports
- CORGI8 · PnL $58,927 · win rate 92% · categorias: sports
- gransaaa · PnL $101,677 · win rate 88% · categorias: sports

> Polymarket refleja en que eventos del mundo (politica, macro, deportes) esta apostando el dinero con mejor historial. Usalo como termometro de contexto, no como señal directa de cartera.

## 6. Calidad de los datos

- Estado global: `error`
- **congress**: `error` · 0 registros 30d · ultimo dato ? — no_valid_tx_dates
- **sec_insiders**: `ok` · 430 registros 30d · ultimo dato 2026-09-09
- **sec_13d_13g**: `ok` · 250 registros 30d · ultimo dato 2026-09-09
- **institutional_13f**: `ok` · ? registros 30d · ultimo dato ? — stale_manager_report_date
- **polymarket**: `ok` · ? registros 30d · ultimo dato ?
- **Fuentes con problemas**: congress

> Congreso y 13F tienen retraso legal de hasta ~45 dias. Senate no disponible en vivo (portal eFD bloqueado); House si. Insiders (Form 4) llegan en 1-2 dias.

## 7. Instrucciones para ti (LLM)

Eres un **analista de carteras**, no un asesor financiero. El codigo ya ha construido la cartera candidata de la seccion 2 a partir de reglas deterministas. Tu trabajo es **revisarla y proponer AJUSTES** razonados. El codigo tendra la ultima palabra: validara tu propuesta contra el risk gate y rechazara cualquier cosa que viole las restricciones.

### Restricciones DURAS (si las violas, tu propuesta se rechaza entera)

1. **Universo permitido**: tickers de la cartera candidata (`BWFG, CSQ, DGICA, EAF, GLD, IEF, LEU, QQQ, SEI, SPY, TENB, TLT, TWST, UBER, ZBIO`), de las señales de la seccion 3, o posiciones que ya tengas abiertas (mantener siempre es legal), siempre que tengan datos de precio. No inventes tickers que no aparezcan en este briefing ni en tu cartera.
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

