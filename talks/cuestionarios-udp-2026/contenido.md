---
pagetitle: "Encuestas, cuestionarios y medición"
format:
  revealjs:
    theme: [default, theme-marino.scss]
    css: [fuentes.css, interactivos.css]
    width: 1600
    height: 900
    margin: 0.055
    slide-number: c/t
    progress: true
    chalkboard: true
    menu: true
    transition: fade
    transition-speed: fast
    hash: true
    history: true
    navigation-mode: linear
    html-math-method: plain
---

## {.portada}

@@W:utils@@

::: {.regla-gruesa}
:::

::: {.titulo}
Encuestas, cuestionarios y medición
:::

::: {.subtitulo}
Del concepto al número: trabajar con el error
:::

::: {.regla-fina}
:::

::: {.pie}
[Alejandro Plaza Reveco · profesor invitado]{.nombre}
Lógica de la Investigación Social · Sociología, Universidad Diego Portales\
6 de octubre de 2026
:::

::: {.notes}
Tiempos sugeridos (80 min): Parte 1, 12 · Parte 2, 18 · Parte 3, 16 · Parte 4, 20 · Parte 5, 12 · cierre, 2.
Teclas: S vista de orador · B pizarra · Esc vista general · F pantalla completa.
:::

## Hoja de ruta

::: {.pasos}
1. **Medir y encuestar: lo básico**
   [variables, niveles de medición, cuestionarios]{.glosa}
2. **Obsesionarse con el error**
   [nos vamos a equivocar: ¿por cuánto?]{.glosa}
3. **Del concepto al número**
   [conceptos latentes y operacionalización]{.glosa}
4. **Tres casos reales: ELSOC**
   [autoeficacia política · autoritarismo · depresión]{.glosa}
5. **Innovaciones**
   [experimentos, modos de aplicación y datos vinculados]{.glosa}
:::

# Parte 1 --- Medir y encuestar {.divisoria}

::: {.bajada}
Lo básico: qué es medir, qué es una variable y qué es un cuestionario
:::

## ¿Qué significa medir?

::: {.cols-60-40}
::: {}
::: {.bloque}
[Definición clásica]{.t}
Medir es [asignar números a objetos o eventos según reglas]{.hl} (Stevens, 1946)
:::

- Medimos la estatura con una regla y la temperatura con un termómetro
- En sociología medimos edad, ingreso, confianza, autoritarismo…
- La pregunta de hoy: ¿con qué **regla** le asignamos un número a la confianza en las instituciones?
:::

@@D:medir@@
:::

## ¿Qué es una variable?

::: {.bloque}
[Definición]{.t}
Una [variable]{.hl} es una característica que **toma distintos valores** entre las unidades que estudiamos: personas, hogares, comunas…
:::

| Persona | Comuna | Nivel educacional | Confianza (1–5) | Edad |
|---|---|---|---|---|
| Ana | Maipú | Media completa | 2 | 34 |
| Benito | Ñuñoa | Universitaria | 4 | 51 |
| Carla | Temuco | Básica | 3 | 67 |
| Diego | Antofagasta | Técnica superior | 1 | 22 |
: {.grande}

- Cada fila es una **unidad**; cada columna, una **variable**
- ¿Las cuatro columnas son datos del mismo tipo?

## Niveles de medición

| Nivel | Qué nos dicen los valores | Ejemplos | Operaciones |
|---|---|---|---|
| **Nominal** | Solo categorías distintas, sin orden | Comuna, partido, sexo | Contar |
| **Ordinal** | Categorías con orden, pero distancias desconocidas | Nivel educacional, escala de acuerdo | Contar, ordenar |
| **Continua** | Distancias iguales: un año más es siempre un año más | Edad en años, ingreso, horas de trabajo | Contar, ordenar, sumar, promediar |
: {.grande}

. . .

::: {.alerta}
[Ojo]{.t}
El número que ponemos en la base **no cambia** el nivel de medición: codificar «Norte = 1, Centro = 2, Sur = 3» no convierte la zona en una variable numérica.
:::

## Asignar números a conceptos

::: {.cols-40-60}
@@D:numeros@@

::: {}
«¿Cuánto confía usted en el Congreso?»

- Los números respetan el **orden**: más número, más confianza
- Pero, ¿la distancia entre «Nada» y «Poca» es igual a la que hay entre «Bastante» y «Mucha»?
- Si lo es, podemos [promediar]{.hl}; si no, es una variable ordinal

::: {.ejemplo}
[Para pensar]{.t}
Un promedio de confianza de 2,4: ¿qué significa exactamente?
:::
:::
:::

## Ejercicio: ¿qué nivel de medición? {.ejercicio}

[Hagan clic en cada tarjeta para ver la respuesta]{.tenue}

@@W:niveles@@

::: {.nota}
Una decisión de diseño: la **misma** variable puede medirse a distintos niveles. Preguntar la edad en tramos pierde información.
:::

## Un cuestionario, según Asún

::: {.bloque}
[Definición]{.t}
«Un cuestionario es un dispositivo de investigación cuantitativa consistente en un conjunto de preguntas que deben ser aplicadas a un sujeto (usualmente individual) en un orden determinado y frente a las cuales este sujeto puede responder adecuando sus respuestas a un espacio restringido o a una serie de respuestas que el mismo cuestionario ofrece.»
:::

- Objetivo: [«medir» el grado o la forma]{.hl} en que las personas poseen determinadas variables
- Es una **conversación no horizontal**: uno pregunta con opciones preestablecidas, el otro elige

::: {.nota}
Asún (2006, p. 67).
:::

## Encuesta ≠ cuestionario

@@D:encuesta@@

- Un buen cuestionario aplicado a una mala muestra produce **malos datos**
- Una muestra perfecta con preguntas mal hechas, **también**
- Modos: cara a cara, teléfono, web, autoaplicado… o [mezclas]{.hl}

## ¿Qué se puede preguntar?

::: {.cols3}
::: {.bloque}
[Hechos]{.t}
Conductas o sucesos

[¿Votó en la última elección? ¿Con quién vive?]{.tenue}
:::

::: {.bloque}
[Conocimientos y habilidades]{.t}
Hay respuestas correctas e incorrectas

[Pruebas SIMCE o PAES, preguntas de conocimiento político]{.tenue}
:::

::: {.bloque}
[Opiniones y valores]{.t}
Lo que la persona piensa o siente

[¿Cuánto confía en el Congreso? ¿Qué es más importante: libertad o igualdad?]{.tenue}
:::
:::

. . .

::: {.alerta}
[Incluso los hechos pasan por la persona]{.t}
Lo que recibimos «no es el hecho», sino «la percepción, recuerdo o lo que nos desea transmitir el sujeto» (Asún, 2006, p. 78).
:::

## Síntesis {.sintesis}

- Medir es asignar números a conceptos según una regla explícita
- Las variables pueden ser nominales, ordinales o continuas: el nivel define qué operaciones tienen sentido
- El cuestionario es la regla de medición; la encuesta suma muestra y modo de aplicación

# Parte 2 --- Obsesionarse con el error {.divisoria}

::: {.bajada}
Nos vamos a equivocar. La pregunta es: ¿por cuánto?
:::

## {.portada}

::: {.destacado style="margin-top:1.4em"}
Trabajar con datos cuantitativos significa

[obsesionarse con el error]{.grande}
:::

. . .

::: {.pasos style="max-width:60%; margin:1em auto 0"}
1. ¿De dónde viene el error?
2. ¿Cómo lo evitamos o reducimos?
3. ¿Cómo le ponemos un [número]{.hl}?
:::

## No es si nos equivocamos, sino por cuánto

::: {.cols-60-40}
::: {}
Marzo de 2026: el debate sobre el MEPCO (Mecanismo de Estabilización de Precios de los Combustibles)

::: {.bloque}
[Mirada determinista]{.t}
«El 48% de los chilenos opina que el Gobierno debía endeudarse para mantener el subsidio del MEPCO»
:::

::: {.fragment}
::: {.ejemplo}
[Mirada probabilística]{.t}
«Entre **44% y 52%** lo opina, con 95% de confianza»\
[Ilustrativo: muestra de ≈700 casos, margen de ±3,7 puntos]{.tenue}
:::
:::
:::

![](figuras/mepco.jpg){.foto}
:::

::: {.nota}
Dato: Cadem, Plaza Pública (marzo 2026).
:::

## Laboratorio: ¿por cuánto nos equivocamos? {.lab-slide}

@@W:muestreo@@

::: {.notes}
1) Hacer 20 encuestas con n = 700: casi todas verdes (≈95%).
2) Bajar n a 100: intervalos anchos, pero siguen conteniendo el 48%.
3) Subir n a 3000 y agregar 4 puntos de sesgo de no respuesta: intervalos angostos y casi todos rojos.
Mensaje: más casos reducen el error aleatorio, no el sesgo. Y el margen de error publicado solo mide el muestral.
:::

## La pregunta científica

- No asumimos que la realidad social se puede capturar sin falla
- Asumimos que [nos vamos a equivocar siempre]{.hl}: por el muestreo, las preguntas, los encuestadores, el procesamiento
- La pregunta es: **¿por cuánto y en qué dirección?**

::: {.destacado style="margin-top:1em"}
*«Medir conceptos de ciencias sociales siempre incorpora un grado variable, pero frecuentemente importante, de error. Equivale a tratar de comprender una conversación escuchada en una radio con mucha estática y ruido de fondo.»*

[Asún (2006, p. 112)]{.tenue}
:::

## El tiro al blanco

::: {.cols-40-60}
@@D:diana@@

::: {style="padding-top:2.2em"}
- El [centro]{.hl} es lo que queremos conocer: el valor verdadero en la población
- Cada **disparo** es una medición: una encuesta, una muestra, una respuesta
- Nunca vemos el centro directamente: solo vemos dónde caen los disparos
:::
:::

## Dos tipos de error

@@D:dianas@@

::: {.fragment fragment-index=1}
- **Error aleatorio** (varianza): nos equivocamos para ambos lados; se reduce con más casos o más preguntas
:::
::: {.fragment fragment-index=2}
- [Error sistemático]{.hlr} (sesgo): nos equivocamos siempre hacia el mismo lado; más casos no lo arreglan
:::
::: {.fragment fragment-index=3}
- En la práctica, casi siempre tenemos un poco de ambos
:::

## Laboratorio: el tiro al blanco {.lab-slide}

@@W:tiro@@

::: {.notes}
Usar los cuatro botones de casos. Después: sesgo alto + dispersión alta, disparar muchas veces y mostrar que la cruz (el promedio) se queda lejos del centro.
:::

## ¿Qué es un DAG?

::: {.cols2}
::: {}
::: {.bloque}
[Grafo dirigido acíclico]{.t}
Un dibujo de **qué produce qué**

- **Nodos**: variables
- **Flechas**: una variable influye en otra
- **Acíclico**: no hay círculos; nada se causa a sí mismo
:::

La lluvia produce paraguas abiertos y calles mojadas. Paraguas y calles mojadas [andan juntos]{.hl}, aunque uno no cause al otro.
:::

::: {}
@@D:dag_lluvia@@

[Convención de colores en esta clase:]{.tenue style="font-size:.6em"}

@@D:leyenda@@
:::
:::

::: {.nota}
Pearl y Mackenzie (2018), *The Book of Why*.
:::

## La ecuación más importante de hoy

::: {.ecuacion}
X = V + E
:::

::: {.cols2}
::: {}
- *X*: lo que **observamos** (la respuesta)
- *V*: el [valor verdadero]{.hl} (lo que queremos conocer)
- *E*: el **error** de medición

[Teoría clásica de los tests: toda respuesta es verdad *más* ruido]{.tenue style="font-size:.7em"}
:::

@@D:xve@@
:::

## Un ejemplo con un hecho, no una opinión

::: {.cols-60-40}
::: {style="padding-top:1.5em"}
- En una encuesta del CIS (España) se preguntó por quién habían votado en la última elección
- Casi el [65%]{.hlr} declaró haber votado por el candidato ganador…
- …que en la realidad obtuvo poco más del [50%]{.hl}
:::

@@D:cis|dg-medio@@
:::

::: {.nota}
Ejemplo en Asún (2006, p. 103).
:::

## Dos historias para el mismo número

::: {.cols2}
::: {}
**Historia 1: la gente no dice la verdad**

@@D:hist1@@

[Declarar haber votado por el ganador «queda bien»: es un **error de medición**]{style="font-size:.7em"}
:::

::: {.fragment}
**Historia 2: responde otra gente**

@@D:hist2@@

[Quienes votaron (y por el ganador) aceptan más responder: es un **error de representación**]{style="font-size:.7em"}
:::
:::

::: {.fragment}
::: {.bloque}
[La lección]{.t}
El mismo número equivocado puede venir de fuentes distintas. En EE.UU., buena parte de la sobreestimación de la participación se explica por la historia 2 (Jackman y Spahn, 2019).
:::
:::

## El mapa: error total de encuesta

![](figuras/tse_groves.png){style="height:650px; width:auto; display:block; margin:0 auto; background:#fff; padding:12px; border-radius:6px"}

::: {.nota}
Groves et al. (2009), *Survey Methodology*, cap. 2.
:::

## Explorar el mapa {.lab-slide}

@@W:tse@@

::: {.nota}
Los errores se **acumulan**: el estadístico final los hereda todos. El margen de error que publica la prensa mide **solo** el error muestral.
:::

## Un mismo tema, tres encuestas, tres números

¿Qué piensan los chilenos sobre el MEPCO? (marzo–abril de 2026)

| Encuesta | Lo que se preguntó (en síntesis) | Resultado |
|---|---|---|
| Cadem, Plaza Pública | El Gobierno debía endeudarse para mantener el subsidio | 48% de acuerdo |
| Pulso Ciudadano | Rechazo a la decisión de **no** aplicar el mecanismo | 57,2% rechaza |
| Métrica Pública | Rechazo a la eliminación o suspensión del MEPCO | 65,5% rechaza |
: {.grande}

. . .

::: {.alerta}
[Para discutir]{.t}
¿Estas encuestas se contradicen? ¿O cada una mide [una cosa distinta]{.hlr}: el endeudamiento, una decisión del Gobierno, la existencia del mecanismo?
:::

::: {.nota}
Cifras según reportes de prensa; verificar en los informes originales de cada encuesta.
:::

## Síntesis {.sintesis}

- Nos vamos a equivocar: la pregunta científica es por cuánto y en qué dirección
- El error aleatorio se compensa con más casos; el sistemático no
- Toda respuesta es verdad más error: X = V + E
- El error total viene de cómo preguntamos (medición) y de a quiénes (representación)

# Parte 3 --- Del concepto al número {.divisoria}

::: {.bajada}
Conceptos latentes y operacionalización
:::

## ¿Cómo se mide…?

::: {.cajas}
[el amor]{.caja} [la inteligencia]{.caja} [la confianza en los demás]{.caja}
:::

::: {.cajas}
[el autoritarismo]{.caja} [la depresión]{.caja} [la eficacia política]{.caja .acento}
:::

- Son conceptos [latentes]{.hl}: existen (o eso creemos), pero **no se observan directamente**
- No hay una regla para medir el autoritarismo como la hay para medir la estatura
- Solo observamos sus **manifestaciones**: lo que la gente dice, hace o responde

## Operacionalización

::: {.bloque}
[Asún (2006, p. 69)]{.t}
(a) Definir cuidadosamente un concepto no observable; (b) derivar consecuencias observables, los [indicadores]{.hl}; (c) medir los indicadores; (d) deducir de ellos el grado en que el objeto posee el concepto.
:::

::: {.cols-60-40}
::: {}
**Un ejemplo de otras ciencias**

- La **edad de un árbol** (latente) se mide contando los **anillos del tronco** (indicador)
- Funciona porque la relación es **directa y estable**
- En ciencias sociales esa relación casi nunca es tan limpia
:::

@@D:anillos|dg-chico@@
:::

## Dos roles en la ciencia: teoría y medición

::: {.cols2}
::: {}
![](figuras/sheldon_leonard.jpg){.foto style="max-height:290px"}

- **Sheldon**, físico **teórico**: trabaja con conceptos y ecuaciones
- **Leonard**, físico **experimental**: diseña instrumentos para medir
:::

::: {}
::: {.fila-fotos}
![](figuras/higgs.jpg){.foto style="max-height:290px"}

![](figuras/cern_atlas.jpg){.foto style="max-height:290px"}
:::

- 1964: Higgs propone una partícula **en teoría**
- 2012: el CERN logra **medirla**, 48 años después
:::
:::

. . .

::: {.bloque}
[En sociología]{.t}
Hay una [fase teórica]{.hl} (qué es el concepto) y una **fase empírica** (cómo se traduce en números). La operacionalización es el puente.
:::

## Del concepto al número

@@D:concepto_numero@@

Concepto → dimensiones → preguntas → categorías de respuesta → índice o escala

::: {.nota}
Adaptado de Asún (2006, p. 75).
:::

## Conceptos simples y conceptos complejos

::: {.cols2}
::: {.bloque}
[Concepto simple]{.t}
Las personas lo usan en su vida cotidiana **igual que el investigador**

[«¿Cuántos años tiene?» · «¿Se siente enamorado de su pareja actual?»]{.tenue}
:::

::: {.bloque}
[Concepto complejo]{.t}
El habla cotidiana **no lo usa**, o lo usa distinto

[No podemos preguntar «¿cuán individuado está usted?»]{.tenue}
:::
:::

- Operacionalizar un concepto complejo es un proceso de [traducción]{.hl}: del lenguaje del investigador al habla de las personas
- Hay que **desagregarlo** en dimensiones hasta llegar a algo que la gente pueda responder

::: {.nota}
Asún (2006, pp. 71–73).
:::

## Un ejemplo chileno: individuación (PNUD, 2002)

| Dimensión | Pregunta |
|---|---|
| Disposición a romper normas sociales | ¿Seguiría adelante con una idea aunque vaya en contra de la opinión de sus padres? ¿De su pareja? ¿De la Iglesia? |
| Deberes morales que restringen la conducta | ¿Cómo le gustaría ser recordado? (a) alguien que se entregó a los demás; (b) alguien que salió adelante contra viento y marea; (c) **alguien fiel a sus sueños**; (d) alguien que cumplió su deber |
| Biografía como decisión personal | ¿Cuál frase lo representa mejor? (a) **Yo analizo mi vida y veo qué hacer**; (b) En la vida uno tiene que hacer lo que hay que hacer |

Un punto por cada respuesta «individualizada» ⇒ [índice de 0 a 5]{.hl}

::: {.nota}
Ejemplo desarrollado en Asún (2006, pp. 73–75).
:::

## Operacionalizar siempre tiene un costo

::: {.destacado style="margin-top:1em"}
*«El proceso de operacionalización siempre implica un grado de distorsión o mutilación del sentido teórico de un concepto. […] Nunca logramos medir totalmente el concepto que buscamos, sólo obtenemos mejores o peores interpretaciones empíricas.»*

[Asún (2006, p. 77)]{.tenue}
:::

. . .

::: {.bloque}
[Pregunta al curso]{.t}
¿Las cinco preguntas del PNUD capturan todo lo que un sociólogo entiende por «individuación»? ¿Qué quedó fuera?
:::

## Por qué usamos varias preguntas

::: {.cols-60-40}
::: {}
- Cada pregunta trae su propio error: el fraseo, las palabras, el orden de las alternativas
- Si una pregunta empuja hacia arriba y otra hacia abajo, [el promedio se acerca a la verdad]{.hl}
- Es la lógica de «más casos», aplicada a **más ítems**

::: {.ejemplo}
[Asún (2006, p. 91)]{.t}
Si en una prueba de 60 preguntas un alumno capaz se confunde con una, su puntaje total igual reflejará su conocimiento.
:::
:::

@@D:items@@
:::

## Laboratorio: ¿cuántas preguntas? {.lab-slide}

@@W:items@@

::: {.notes}
Partir con 1 pregunta (r ≈ 0,6). Subir a 4 y a 12. La nube se alinea con la diagonal dorada.
Conectar con X = V + E: al promediar, el E de cada ítem se compensa.
:::

## Validez y confiabilidad

::: {.cols2}
::: {.bloque}
[Confiabilidad]{.t}
¿El instrumento entrega **el mismo resultado** si lo aplicamos dos veces a alguien que no ha cambiado?

[Una regla que hoy dice 15 cm y en cinco minutos dice 20 cm no sirve]{.tenue}
:::

::: {.bloque}
[Validez]{.t}
¿El instrumento mide **lo que dice medir**?

[Si digo que mido autoritarismo, que sea autoritarismo y no otra cosa]{.tenue}
:::
:::

::: {.destacado}
Vuelvan al tiro al blanco: un instrumento [preciso pero sesgado]{.hl} es **confiable pero no válido**. Siempre mide lo mismo… pero no lo que queríamos.
:::

::: {.nota}
Asún (2006, pp. 101–102).
:::

## Dos maneras de relacionar concepto e indicadores

::: {.cols2}
::: {}
**Reflectivo**

@@D:reflectivo@@

[El concepto **causa** las respuestas: si alguien es autoritario, tenderá a estar de acuerdo con todos los ítems. Los ítems **deben correlacionar**.]{style="font-size:.68em"}
:::

::: {}
**Formativo**

@@D:formativo@@

[Los indicadores **componen** el concepto: una casa puede tener buen material y mal entorno. **No tienen por qué correlacionar**.]{style="font-size:.68em"}
:::
:::

::: {.alerta}
[¿Por qué importa?]{.t}
En un modelo formativo, eliminar el indicador «que no correlaciona» significa [amputar una parte del concepto]{.hlr}.
:::

## ¿Qué hace una persona cuando responde?

@@D:tourangeau@@

::: {.fragment fragment-index=5}
- En **cada etapa** algo puede salir mal (en dorado)
- Las reglas de redacción no son manías: cada una protege una etapa
- Si la tarea es difícil y la motivación baja, la gente responde «lo suficiente» (*satisficing*, Krosnick, 1991)
:::

::: {.nota}
Tourangeau, Rips y Rasinski (2000).
:::

## Ejercicio: ¿qué tienen de malo estas preguntas? {.ejercicio}

[En parejas, 2 minutos. Después, clic en cada tarjeta para ver el problema y una mejor versión]{.tenue}

@@W:malas@@

::: {.nota}
Lenzner y Menold (2016), *GESIS Survey Guidelines: Question Wording*; Asún (2006, pp. 80–90).
:::

## Preguntar también produce la opinión

::: {.cols-60-40}
::: {}
- Asún lo llama [cristalización]{.hl}: preguntar hace que la persona se sitúe donde antes no se había situado
- «Cuando aplicamos un cuestionario estamos *produciendo* información y no sólo *recogiendo* información» (p. 72)

::: {.fragment}
::: {.ejemplo}
[Una ley que no existía]{.t}
En EE.UU. se preguntó si había que derogar la *Public Affairs Act of 1975*, una ley **inventada**. Cerca de **un tercio** dio su opinión igual.
:::
:::
:::

::: {.bloque}
[Implicancias]{.t}

- Ofrecer la opción «no sabe»
- Preguntar primero si conoce el tema
- Desconfiar de opiniones sobre temas poco conocidos
:::
:::

::: {.nota}
Bishop, Oldendick, Tuchfarber y Bennett (1980), *Public Opinion Quarterly*, 44(2).
:::

::: {.notes}
Cincinnati, fines de los 70. Sin filtro, ~1/3 opinó sobre la ley ficticia; con un filtro («¿o no ha pensado mucho en este tema?») cayó a un dígito. La gente no responde al azar: infiere de qué se trata y responde a esa interpretación.
:::

## Síntesis {.sintesis}

- Los conceptos sociológicos son latentes: solo vemos sus manifestaciones
- Operacionalizar es traducir: concepto, dimensiones, preguntas, categorías, índice
- Varias preguntas por concepto reducen el error aleatorio
- Cada etapa de la respuesta puede fallar: las reglas de redacción la protegen

# Parte 4 --- Tres casos reales: ELSOC {.divisoria}

::: {.bajada}
Autoeficacia política · autoritarismo · depresión
:::

## ELSOC: Estudio Longitudinal Social de Chile

::: {.cols-60-40}
::: {}
- Encuesta [panel]{.hl} del Centro de Estudios de Conflicto y Cohesión Social (COES)
- Sigue a **las mismas personas** año a año desde 2016
- Población urbana adulta de Chile
- Módulos: ciudadanía, desigualdad, redes, salud y bienestar, territorio, conflicto
- Cuestionarios, bases y documentación son **públicos**
- Sitio del estudio: [ELSOC – COES](https://coes.cl/elsoc/)
:::

![](figuras/elsoc_terreno.jpg){.foto}
:::

## La operacionalización, en una planilla

El *Listado de Variables* de ELSOC documenta, para cada ítem, su concepto y su pregunta:

| Código | Concepto general | Concepto específico | Fraseo del ítem | Tipo |
|---|---|---|---|---|
| `c10_02` | Autoeficacia política | Autoeficacia política | Mi voto influye en el resultado de la elección | Ordinal |
| `c18_06` | Autoritarismo | Autoritarismo 1 | La obediencia y el respeto por la autoridad son los valores más importantes que los niños debieran aprender | Ordinal |
| `s11_02` | Estado de ánimo | Sintomatología depresiva | Decaimiento, pesadez o desesperanza | Ordinal |

Concepto → dimensión → pregunta → categorías: el diagrama de Asún, [hecho planilla]{.hl}

::: {.nota}
ELSOC, Listado de Variables Global v2023.
:::

## Caso 1. Autoeficacia política: la teoría

::: {.cols-60-40}
::: {}
- **Eficacia política**: la sensación de que uno **puede** influir en la política (Campbell et al., 1954)
- Dos dimensiones clásicas:
  - [Interna]{.hl}: «entiendo la política y puedo participar»
  - **Externa**: «el sistema responde a gente como yo»
- Un concepto vecino: el **deber cívico**, la sensación de que *hay que* participar
:::

@@D:eficacia@@
:::

::: {.nota}
Campbell, Gurin y Miller (1954); Niemi, Craig y Mattei (1991).
:::

## Caso 1. Autoeficacia política en ELSOC

«¿En qué medida se encuentra usted de acuerdo o en desacuerdo con cada una de las siguientes afirmaciones?»

| Código | Ítem |
|---|---|
| `c10_01` | Votar es mi deber como ciudadano |
| `c10_02` | Mi voto influye en el resultado de la elección |
| `c10_03` | Votar permite expresar mis ideas |
: {.grande}

[Totalmente en desacuerdo — En desacuerdo — Ni de acuerdo ni en desacuerdo — De acuerdo — Totalmente de acuerdo]{.tenue style="font-size:.6em"}

::: {.bloque}
[Pregunta al curso]{.t}
¿Qué **faceta** de la relación con el voto captura cada ítem?
:::

## Caso 1. Una escala corta, varias facetas

@@D:facetas@@

- Una encuesta panel cubre **muchos** temas: cada concepto recibe pocas preguntas
- Asún: el mínimo es una o dos preguntas por subconcepto; el resto se «invierte» en los conceptos centrales del estudio (p. 92)
- Cada ítem aporta [una faceta]{.hl}: quien analiza los datos decide cuáles usar según su pregunta

## Caso 1. Leer la documentación antes de analizar

::: {.cols2}
::: {}
::: {.ejemplo}
[Lo que permite una buena documentación]{.t}

- Ver el fraseo exacto de cada ítem
- Elegir los ítems que calzan con **mi** concepto
- Saber en qué olas se preguntó cada uno
:::

::: {.bloque}
[Ejemplo]{.t}
Si me interesa la eficacia **externa**, `c10_02` es mi mejor candidato; si me interesa la cultura cívica, `c10_01`.
:::
:::

::: {}
::: {.alerta}
[La lección]{.t}
La [etiqueta]{.hlr} de una variable es un punto de partida, no una garantía. La validez se juzga **en relación con la pregunta de investigación** de quien usa los datos.
:::

Que ELSOC publique el concepto, el fraseo y las olas de cada ítem es justamente lo que hace posible esta discusión.
:::
:::

## Caso 1. ¿Por qué importa medirlo bien?

::: {.cols-60-40}
::: {}
- Verba, Schlozman y Brady (1995): no todos tienen la misma [voz política]{.hl}
- Participar requiere **recursos** (tiempo, dinero, habilidades), **compromiso** (interés, eficacia) y **redes** que te recluten
- La eficacia es parte del mecanismo por el cual la **desigualdad social se vuelve desigualdad política**
:::

@@D:voz@@
:::

::: {.alerta}
[Medir no es solo un problema técnico]{.t}
Cómo medimos la eficacia define qué podemos decir sobre **un mecanismo de la desigualdad**.
:::

## Caso 2. Autoritarismo: una larga historia

::: {.cols-60-40}
::: {}
- Adorno, Frenkel-Brunswik, Levinson y Sanford (1950), *The Authoritarian Personality*
- La pregunta tras el nazismo: ¿por qué personas comunes apoyan regímenes autoritarios?
- Construyeron la [escala F]{.hl} (de «fascismo»): obediencia, convencionalismo, agresión hacia los desviados
- Incluía preguntas sobre la relación con los padres, justificadas desde la **teoría psicoanalítica** (Asún, 2006, p. 112)
:::

![](figuras/adorno.jpg){.foto}
:::

## Caso 2. Autoritarismo en ELSOC

«¿En qué medida se encuentra usted de acuerdo o en desacuerdo con cada una de las siguientes afirmaciones?»

| Código | Ítem |
|---|---|
| `c18_04` | En vez de tanta preocupación por los derechos de las personas, lo que este país necesita es un gobierno firme |
| `c18_05` | Lo que nuestro país necesita es un mandatario/a fuerte con la determinación para llevarnos por el camino correcto |
| `c18_06` | La obediencia y el respeto por la autoridad son los valores más importantes que los niños debieran aprender |
| `c18_07` | Las verdaderas claves para tener una buena vida son la obediencia y la disciplina |

::: {.bloque}
[Miren con atención]{.t}
¿Qué significa responder «de acuerdo» en **las cuatro** afirmaciones?
:::

## Caso 2. Un desafío de toda escala de acuerdo / desacuerdo

- En los cuatro ítems, **estar de acuerdo = más autoritario**
- Es el formato estándar de muchas escalas, desde la escala F hasta encuestas internacionales actuales
- Su riesgo: la [aquiescencia]{.hl}, la tendencia a responder «de acuerdo» **independientemente del contenido**

::: {.cols2}
::: {.bloque}
[¿Por qué ocurre?]{.t}

- Cortesía con el encuestador
- Deferencia hacia quien pregunta
- Menor esfuerzo: es más fácil buscar razones para estar de acuerdo (Krosnick, 1991)
:::

::: {.alerta}
[Consecuencia]{.t}
Una persona aquiescente puede aparecer como **más autoritaria** de lo que es: un [error sistemático]{.hlr}.
:::
:::

::: {.nota}
Bogner y Landrock (2016), *GESIS Survey Guidelines: Response Biases in Standardised Surveys*, sección 2.2.
:::

## Caso 2. El DAG del problema

@@D:aquiescencia@@

- Si las personas con menos educación aparecen «más autoritarias», ¿cuánto es autoritarismo y cuánto es **forma de responder**?
- El error de medición puede [fabricar o inflar relaciones]{.hl} entre variables

## Laboratorio: una relación fabricada {.lab-slide}

@@W:aquiescencia@@

::: {.notes}
Con aquiescencia 6 y la escala en una sola dirección: aparece una diferencia de ~0,2–0,3 puntos que NO existe. Subir a 10: crece. Cambiar a escala balanceada: la diferencia vuelve a ≈ 0.
:::

## Caso 2. ¿Cómo se enfrenta?

::: {.cols3}
::: {.bloque}
[1. Escalas balanceadas]{.t}
Mitad de los ítems en un sentido y mitad en el otro: la aquiescencia se cancela

[Ej.: escala RWA de Altemeyer]{.tenue}
:::

::: {.bloque}
[2. Categorías propias]{.t}
Reemplazar «de acuerdo / en desacuerdo» por alternativas del ítem

[«¿Cuánto influye su voto?» Nada — Poco — Algo — Mucho]{.tenue}
:::

::: {.bloque}
[3. Medición indirecta]{.t}
Preguntar por otra cosa que revela el concepto

[¿Qué es más importante que aprenda un niño: **obediencia** o **independencia**? (Feldman y Stenner, 1997)]{.tenue}
:::
:::

- La opción 3 elige entre dos cosas **deseables**: no hay un «de acuerdo» fácil
- Medir bien exige [creatividad conceptual]{.hl}, no solo técnica

## Caso 3. Depresión: un instrumento clínico en una encuesta

«¿Cuántas veces durante las **últimas dos semanas** ha sentido alguna de las siguientes molestias?»

::: {.cols-60-40}
| Código | Síntoma |
|---|---|
| `s11_01` | Poco interés o alegría para realizar sus actividades |
| `s11_02` | Decaimiento, pesadez o desesperanza |
| `s11_03` | Dificultad para dormir, o exceso de sueño |
| `s11_04` | Cansancio o falta de energía |
| `s11_05` | Apetito disminuido o aumentado |
| `s11_06` | Dificultad para concentrarse |
| `s11_07` | Mala opinión de sí mismo |
| `s11_08` | Movimientos o lenguaje enlentecidos |
| `s11_09` | Pensamientos de muerte o de hacerse daño |

::: {.bloque}
[PHQ-9]{.t}

- *Patient Health Questionnaire*: instrumento clínico validado
- Nueve síntomas, periodo de referencia preciso
- Asún: [no inventar todo]{.hl}, usar instrumentos probados (p. 108)
:::
:::

## Caso 3. Adaptar tiene costos

::: {.cols2}
::: {.bloque}
[PHQ-9 original · 4 categorías]{.t}
0 Nunca · 1 Varios días · 2 Más de la mitad de los días · 3 Casi todos los días
:::

::: {.bloque}
[ELSOC · 5 categorías]{.t}
1 Nunca · 2 Algunos días · 3 Más de la mitad de los días · 4 Casi todos los días · [5 Todos los días]{.hl}
:::
:::

- El PHQ-9 tiene **puntajes de corte** (5, 10, 15, 20) para la escala 0–27
- Con otra escala de respuesta, esos cortes no se aplican directamente
- Toda adaptación es una decisión con costos y beneficios de [comparabilidad]{.hl}

## Caso 3. El problema de tener a alguien enfrente

::: {.cols-60-40}
::: {}
- Responder sobre el propio ánimo frente a un **desconocido** no es neutral
- [Deseabilidad social]{.hl}: responder lo que «queda bien»
- **Efecto encuestador**: las respuestas cambian según quién pregunta
- **Presencia de terceros**: la pareja o los hijos en la sala
:::

::: {}
@@D:encuestador@@

[Ambos empujan **hacia abajo**: subreporte]{.tenue style="font-size:.66em"}
:::
:::

::: {.nota}
Bogner y Landrock (2016), secciones 2.1, 3.1 y 3.2.
:::

## Caso 3. La solución de ELSOC: pasar la tablet

::: {.cols-60-40}
::: {}
- En este módulo el encuestador **entrega la tablet** y la persona responde sola
- ELSOC lo registra: `s11_10` indica si la persona contestó directamente en la tablet
- Lo mismo con el **voto**: «PREGUNTA AUTOADMINISTRADA. ENTREVISTADO DEBE RESPONDER DIRECTAMENTE EN LA TABLET»

::: {.ejemplo}
[Asún ya lo anticipaba (p. 108)]{.t}
Aumentar la confidencialidad «dejando que parte del instrumento lo responda secretamente (sin mediación del encuestador)».
:::
:::

![](figuras/tablet.jpg){.foto}
:::

## Caso 3. Una pregunta abierta: ¿qué es la depresión?

::: {.cols2}
::: {}
**Causa común**

@@D:causa_comun@@

[La depresión es una condición latente que **produce** los síntomas: sumarlos tiene sentido]{style="font-size:.68em"}
:::

::: {.fragment}
**Red de síntomas**

@@D:red@@

[Los síntomas **se causan entre sí**: la depresión *es* la red. Ojo: este dibujo **no es un DAG**, porque tiene un ciclo]{style="font-size:.68em"}
:::
:::

::: {.bloque}
[La lección]{.t}
Incluso en instrumentos clínicos, [¿qué es el concepto?]{.hl} sigue siendo una pregunta abierta. Operacionalizar es tomar posición teórica.
:::

::: {.nota}
Borsboom y Cramer (2013); Fried y Nesse (2015).
:::

## Caso 3. Medir también tiene consecuencias éticas

- El ítem `s11_09` pregunta por **pensamientos de muerte o de hacerse daño**
- Una encuesta que pregunta esto debe estar preparada para lo que puede escuchar: protocolos de [derivación]{.hl} a apoyo profesional, encuestadores capacitados y aprobación de un **comité de ética**

| Caso | Pregunta | Fuente de error |
|---|---|---|
| Autoeficacia | ¿qué faceta mide cada ítem? | validez |
| Autoritarismo | ¿el formato empuja? | sesgo de respuesta |
| Depresión | ¿la situación empuja? | efecto encuestador y modo |
: {.grande}

## Síntesis {.sintesis}

- Una buena documentación permite discutir la validez de cada ítem
- El formato de acuerdo / desacuerdo puede introducir error sistemático
- La situación de entrevista cambia las respuestas: la autoaplicación protege los temas sensibles
- Toda medición es también una posición teórica y una responsabilidad ética

# Parte 5 --- Innovaciones {.divisoria}

::: {.bajada}
Experimentos, modos de aplicación y datos vinculados
:::

## Experimentos dentro de encuestas

::: {.cols-60-40}
::: {}
- Se asigna [al azar]{.hl} a cada persona una versión distinta del cuestionario
- Como el azar decide, los grupos son **comparables en todo lo demás**
- Cualquier diferencia en las respuestas se debe a **la versión**
- Combina **muestras representativas** con **inferencia causal**
:::

::: {}
@@D:experimento@@

[El azar **corta** la flecha entre las características de las personas y la versión que reciben]{.tenue style="font-size:.64em"}
:::
:::

::: {.nota}
Mutz (2011), *Population-Based Survey Experiments*.
:::

## Dos experimentos clásicos de fraseo

::: {.cols2}
::: {.ejemplo}
[Prohibir vs. permitir (Rugg, 1941)]{.t}
«¿Debería EE.UU. **prohibir** los discursos públicos contra la democracia?» → 54% sí

«¿Debería **permitir**…?» → 75% no

Misma idea, **21 puntos** de diferencia
:::

::: {.ejemplo}
[Rangos de respuesta (Schwarz et al., 1985)]{.t}
Horas diarias de televisión:

Rangos **bajos** → 16% dice más de 2½ horas\
Rangos **altos** → 38% dice más de 2½ horas

Las alternativas sugieren qué es «normal»
:::
:::

- Ambos son *split-ballot*: dos versiones asignadas al azar
- El primero muestra error en una **opinión**; el segundo, en un [hecho]{.hl}

## Tipos de experimentos en encuestas

| Diseño | En qué consiste | Sirve para |
|---|---|---|
| *Split-ballot* | Dos redacciones de la misma pregunta | Efectos de fraseo, orden, escalas |
| Viñetas | Historias breves con atributos que varían (sexo, clase, nacionalidad…) | Juicios de justicia, discriminación, merecimiento |
| *Conjoint* | Elegir entre perfiles que combinan varios atributos | Preferencias por candidatos, políticas, inmigrantes |
| Lista | Contar cuántas afirmaciones de una lista son ciertas; un grupo tiene una extra, sensible | Temas sensibles: compra de votos, discriminación |
: {.grande}

::: {.nota}
Auspurg y Hinz (2015); Hainmueller, Hopkins y Yamamoto (2014); Blair e Imai (2012).
:::

## Conjoint en vivo: el curso vota {.lab-slide}

@@W:conjoint@@

::: {.notes}
Hacer 6 a 8 rondas. En cada una: «¿quiénes votarían por A?», contar manos y anotar; lo mismo con B; Enter o «Registrar ronda». Los atributos se sortean de nuevo. Después preguntar: ¿alguien diría en voz alta que vota por género o por edad? El conjoint lo detecta sin preguntarlo directamente.
:::

## Modos de aplicación y *mixed-mode*

::: {.cols-60-40}
::: {}
- El **mismo cuestionario no mide igual** cara a cara, por teléfono o por web
- Teléfono: preguntas cortas, pocas alternativas, sin tarjetas
- Web o autoaplicado: más reporte de temas sensibles, pero nadie aclara dudas
- [Mixed-mode]{.hl}: combinar modos para reducir costos o no respuesta, a riesgo de mezclar **efectos de modo**
:::

::: {}
::: {.ejemplo}
[Caso chileno: CASEN 2020]{.t}
Por la pandemia, se aplicó mayoritariamente por **teléfono**, con un cuestionario reducido. El Ministerio advirtió cautela al comparar con años anteriores.
:::

[La tablet de ELSOC es un **cambio de modo dentro de la misma entrevista**]{style="font-size:.7em"}
:::
:::

::: {.nota}
de Leeuw (2005); Kreuter, Presser y Tourangeau (2008).
:::

## Más allá del cuestionario: vincular datos

@@D:vincular@@

- La encuesta deja de ser la única fuente: se [conecta]{.hl} con otros datos sobre la misma persona
- Permite medir hechos sin depender del recuerdo y combinar métodos cuantitativos y cualitativos

## Un ejemplo real: ELSOC pide el RUT

::: {.cols-60-40}
::: {}
::: {.ejemplo}
[Pregunta m66_01 (cuestionario 2022)]{.t}
«Con el objetivo de potenciar el desarrollo de estudios y políticas públicas basadas en evidencia […] queremos consultarle sobre la posibilidad de contar con su RUT, de manera de poder **vincular sus respuestas** en esta encuesta con datos administrativos […] ¿Compartiría usted su RUT para fines de este estudio?»
:::

La pregunta recuerda los protocolos de confidencialidad y la aprobación del **comité de ética**.
:::

::: {}
::: {.alerta}
[Condiciones éticas]{.t}

- Consentimiento [específico]{.hlr} para cada vínculo
- Derecho a decir que no, sin consecuencias
- Datos seudonimizados y resguardados
- Aprobación de un comité de ética
:::

[Quienes aceptan vincular sus datos pueden ser distintos de quienes no: otra fuente de error de representación]{.tenue style="font-size:.64em"}
:::
:::

::: {.nota}
ELSOC, cuestionario maestro 2022; Sakshaug y Kreuter (2012); Boeschoten et al. (2022).
:::

## Síntesis {.sintesis}

- Los experimentos en encuestas combinan muestras representativas con inferencia causal
- *Split-ballot*, viñetas, *conjoint* y listas permiten estudiar el fraseo y los temas sensibles
- El modo de aplicación también es parte de la medición
- Vincular encuestas con registros, entrevistas y datos digitales exige consentimiento y resguardo ético

## Recomendaciones para construir un cuestionario

::: {.cols2}
::: {.pasos}
1. **No inventar todo**: revisar instrumentos existentes (ELSOC, CEP, CASEN, ISSP)
2. **Varias preguntas** por concepto importante
3. Seguir las **reglas de redacción**
4. Pensar el **orden**: de lo simple a lo complejo, lo sensible al final
:::

::: {.pasos}
5. Temas sensibles: **autoaplicación** y confidencialidad
6. **Pretest**: probar con personas reales y preguntar cómo entendieron
7. Trabajar en **equipo**
8. [No esperar perfección]{.hl}: «en toda encuesta siempre hay preguntas que no funcionan» (Asún, p. 67)
:::
:::

::: {.nota}
Asún (2006, pp. 66–67, 98–100, 108–109).
:::

## Un recurso para seguir: GESIS Survey Guidelines

::: {.cols-60-40}
![](figuras/gesis.png){.foto}

::: {}
- Guías breves del instituto alemán GESIS, con **revisión de pares**
- De [acceso libre]{.hl} (licencia CC BY-NC)
- Una guía para cada decisión: redacción de preguntas, diseño de escalas, sesgos de respuesta, pretest cognitivo, modos de aplicación
:::
:::

## Para llevarse {.sintesis}

- Trabajar con datos es obsesionarse con el error: nos vamos a equivocar, la pregunta es por cuánto
- El error viene de a quiénes preguntamos y de cómo preguntamos
- Los conceptos sociológicos son latentes: medirlos exige traducirlos con cuidado
- Operacionalizar es una decisión teórica, no solo técnica
- El fraseo, el formato y la situación de entrevista cambian las respuestas, y podemos estudiarlo

## Referencias

::: {.refs}
Adorno, T. W., Frenkel-Brunswik, E., Levinson, D. y Sanford, N. (1950). *The Authoritarian Personality*. Harper.

Asún, R. (2006). Construcción de cuestionarios y escalas: el proceso de la producción de información cuantitativa. En M. Canales (Ed.), *Metodologías de investigación social* (pp. 63–114). LOM.

Auspurg, K. y Hinz, T. (2015). *Factorial Survey Experiments*. Sage.

Bishop, G., Oldendick, R., Tuchfarber, A. y Bennett, S. (1980). Pseudo-opinions on public affairs. *Public Opinion Quarterly*, 44(2), 198–209.

Blair, G. e Imai, K. (2012). Statistical analysis of list experiments. *Political Analysis*, 20(1), 47–77.

Boeschoten, L., Ausloos, J., Möller, J., Araujo, T. y Oberski, D. (2022). A framework for privacy preserving digital trace data collection through data donation. *Computational Communication Research*, 4(2), 388–423.

Bogner, K. y Landrock, U. (2016). *Response Biases in Standardised Surveys*. GESIS Survey Guidelines.

Bollen, K. y Lennox, R. (1991). Conventional wisdom on measurement: A structural equation perspective. *Psychological Bulletin*, 110(2), 305–314.

Borsboom, D. y Cramer, A. (2013). Network analysis: An integrative approach to the structure of psychopathology. *Annual Review of Clinical Psychology*, 9, 91–121.

Campbell, A., Gurin, G. y Miller, W. (1954). *The Voter Decides*. Row, Peterson.

de Leeuw, E. (2005). To mix or not to mix data collection modes in surveys. *Journal of Official Statistics*, 21(2), 233–255.

Feldman, S. y Stenner, K. (1997). Perceived threat and authoritarianism. *Political Psychology*, 18(4), 741–770.

Fried, E. y Nesse, R. (2015). Depression sum-scores don't add up. *BMC Medicine*, 13, 72.

Groves, R., Fowler, F., Couper, M., Lepkowski, J., Singer, E. y Tourangeau, R. (2009). *Survey Methodology* (2.ª ed.). Wiley.

Hainmueller, J., Hopkins, D. y Yamamoto, T. (2014). Causal inference in conjoint analysis. *Political Analysis*, 22(1), 1–30.
:::

## Referencias (continuación)

::: {.refs}
Jackman, S. y Spahn, B. (2019). Why does the ANES overestimate voter turnout? *Political Analysis*, 27(2), 193–207.

Kreuter, F., Presser, S. y Tourangeau, R. (2008). Social desirability bias in CATI, IVR, and Web surveys. *Public Opinion Quarterly*, 72(5), 847–865.

Krosnick, J. (1991). Response strategies for coping with the cognitive demands of attitude measures in surveys. *Applied Cognitive Psychology*, 5(3), 213–236.

Lenzner, T. y Menold, N. (2016). *Question Wording*. GESIS Survey Guidelines.

Mutz, D. (2011). *Population-Based Survey Experiments*. Princeton University Press.

Niemi, R., Craig, S. y Mattei, F. (1991). Measuring internal political efficacy in the 1988 National Election Study. *American Political Science Review*, 85(4), 1407–1413.

Pearl, J. y Mackenzie, D. (2018). *The Book of Why*. Basic Books.

Rugg, D. (1941). Experiments in wording questions: II. *Public Opinion Quarterly*, 5(1), 91–92.

Sakshaug, J. y Kreuter, F. (2012). Assessing the magnitude of non-consent biases in linked survey and administrative data. *Survey Research Methods*, 6(2), 113–122.

Saris, W., Revilla, M., Krosnick, J. y Shaeffer, E. (2010). Comparing questions with agree/disagree response options to questions with item-specific response options. *Survey Research Methods*, 4(1), 61–79.

Schwarz, N., Hippler, H.-J., Deutsch, B. y Strack, F. (1985). Response scales: Effects of category range on reported behavior and comparative judgments. *Public Opinion Quarterly*, 49(3), 388–395.

Stevens, S. S. (1946). On the theory of scales of measurement. *Science*, 103(2684), 677–680.

Tourangeau, R., Rips, L. y Rasinski, K. (2000). *The Psychology of Survey Response*. Cambridge University Press.

Verba, S., Schlozman, K. y Brady, H. (1995). *Voice and Equality: Civic Voluntarism in American Politics*. Harvard University Press.
:::

## {.portada}

::: {.regla-gruesa}
:::

::: {.titulo}
¡Gracias!
:::

::: {.subtitulo}
Encuestas, cuestionarios y medición
:::

::: {.regla-fina}
:::

::: {.pie}
[Alejandro Plaza Reveco]{.nombre}
aplazareveco@gmail.com\
[alejandroplazareveco.github.io](https://alejandroplazareveco.github.io/)
:::
