# Encuestas, cuestionarios y medición: versión HTML (Quarto / reveal.js)

80 slides con el tema «marino oscuro» y **ocho laboratorios interactivos**. La versión
renderizada funciona sin internet: abre `clase_cuestionarios.html`.

---

## Archivos

| Archivo | Qué es |
|---|---|
| `clase_cuestionarios.html` + `clase_cuestionarios_files/` | El deck renderizado. Es lo que se proyecta. |
| `clase_cuestionarios-respaldo.pdf` | Respaldo en PDF (los laboratorios aparecen en su estado inicial). |
| `clase_cuestionarios.qmd` | El deck en Quarto, **generado** por `build.py`. |
| `contenido.md` | El texto de las slides, con marcadores `@@D:…@@` (diagramas) y `@@W:…@@` (laboratorios). |
| `diagramas.py` | Los 24 diagramas y DAG, dibujados como SVG. |
| `laboratorios.py` | Los 8 laboratorios (HTML + JavaScript, sin librerías externas). |
| `svgkit.py` | Funciones para dibujar nodos y flechas con la paleta del tema. |
| `theme-marino.scss`, `fuentes.css` | El tema y las fuentes de la clase anterior, sin cambios. |
| `interactivos.css` | Estilos de diagramas, laboratorios y tarjetas. |
| `figuras/` | Las imágenes. Las que vienen son **placeholders**. |
| `pdf.js`, `shots.js` | Exportar el PDF y capturar slides (necesitan `npm install playwright`). |

### Cómo se edita

Hay dos caminos:

- **Cambios de texto rápidos:** edita `clase_cuestionarios.qmd` y renderiza. Ojo: si después corres `build.py`, ese archivo se sobrescribe.
- **Cambios en diagramas o laboratorios (o si quieres mantener todo en orden):** edita `contenido.md`, `diagramas.py` o `laboratorios.py`, y luego corre:

```bash
python3 build.py                       # contenido.md + SVG + JS  →  clase_cuestionarios.qmd
quarto render clase_cuestionarios.qmd  # →  clase_cuestionarios.html
```

### Imágenes que hay que reemplazar

Sobrescribe estos archivos manteniendo el **mismo nombre y extensión**:

```
figuras/tse_groves.png        figura oficial del error total de encuesta (Groves et al. 2009)
figuras/mepco.jpg             foto asociada al MEPCO
figuras/sheldon_leonard.jpg   Sheldon y Leonard, The Big Bang Theory
figuras/higgs.jpg             Peter Higgs
figuras/cern_atlas.jpg        detector ATLAS del CERN
figuras/elsoc_terreno.jpg     ELSOC en terreno o logo COES-ELSOC
figuras/adorno.jpg            portada de The Authoritarian Personality o foto de Adorno
figuras/tablet.jpg            persona respondiendo sola en una tablet
figuras/gesis.png             pantallazo de las GESIS Survey Guidelines
```

---

## Los ocho laboratorios

Todos se manejan con el mouse desde el computador del profesor; no requieren que los
estudiantes usen celulares. Las notas de orador (tecla **S**) tienen el guion sugerido.

| Slide | Laboratorio | Qué muestra |
|---|---|---|
| 8 | **¿Qué nivel de medición?** | Tarjetas: clic para revelar nominal / ordinal / continua. |
| 16 | **¿Por cuánto nos equivocamos?** (MEPCO) | Cada clic es una encuesta con su intervalo de confianza. Slider de *n* y de sesgo de no respuesta: con sesgo, más casos no ayudan. |
| 20 | **El tiro al blanco** | Sliders de sesgo y dispersión; la cruz marca el promedio de los disparos. Botones con los cuatro casos. |
| 26 | **Explorar el mapa** (error total) | Clic en cada recuadro dorado: definición y ejemplo. |
| 38 | **¿Cuántas preguntas?** | Slider de 1 a 12 ítems: la correlación entre el puntaje y el valor verdadero sube. |
| 42 | **¿Qué tienen de malo estas preguntas?** | Tarjetas: clic para ver el problema y una versión corregida. |
| 57 | **Una relación fabricada** (aquiescencia) | Una escala en una sola dirección inventa una diferencia por educación; la escala balanceada la elimina. |
| 70 | **Conjoint en vivo** | El curso vota (a mano alzada) entre candidaturas con atributos al azar; se calcula cuánto gana cada atributo. |

Los números de slide pueden moverse si agregas o quitas slides.

---

## Teclas durante la presentación

| Tecla | Qué hace |
|---|---|
| ← → | Avanzar y retroceder |
| **S** | Vista de orador: notas, temporizador y siguiente slide |
| **B** | Pizarra |
| **Esc** | Vista general |
| **F** | Pantalla completa |

Las flechas del teclado no cambian de slide mientras el foco está en un slider. Haz clic
fuera del laboratorio para volver a navegar.

---

## PDF de respaldo

```bash
node pdf.js     # o: Chrome → clase_cuestionarios.html?print-pdf → Imprimir → Guardar como PDF
```

En el PDF, las tarjetas aparecen con las respuestas visibles y los laboratorios en su
estado inicial.
