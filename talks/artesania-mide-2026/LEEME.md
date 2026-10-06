# Sobre artesanIA intelectual — deck completo en Quarto

64 slides. Portado desde el Beamer, con el tema "marino oscuro": tu paleta invertida
para pantalla.

---

## Archivos

| Archivo | Qué es |
|---|---|
| `artesania.qmd` | El deck. Markdown con divs de Quarto. Es lo que editas. |
| `theme-marino.scss` | El tema: paleta, tipografía y todos los componentes. |
| `fuentes.css` | Inter y JetBrains Mono incrustadas en base64. |
| `figuras/` | Las cuatro imágenes. Las que vienen son **placeholders**. |
| `artesania.html` + `artesania_files/` | El deck renderizado. Abre el `.html`. |
| `artesania-respaldo.pdf` | El PDF de respaldo, generado desde el HTML. |
| `pdf.js`, `shots.js` | Scripts de apoyo: exportar el PDF y capturar slides. |

### Las cuatro imágenes que hay que reemplazar

```
figuras/mills-libro.jpg     portada de La imaginación sociológica
figuras/becker-libro.jpg    portada del Manual de escritura
figuras/obsidian-logo.png   logo de Obsidian
figuras/grafo-vault.png     captura de la vista Graph de tu vault
```

Los archivos que vienen son cajas grises con el nombre adentro: sobrescríbelos
manteniendo el mismo nombre y extensión y listo.

---

## Cómo se compila

```bash
quarto render artesania.qmd     # produce artesania.html
quarto preview artesania.qmd    # recarga en vivo mientras editas
```

En RStudio: abrir el `.qmd` y apretar **Render**.

### El PDF de respaldo

Abre en Chrome `artesania.html?print-pdf`, después Imprimir → Guardar como PDF,
con márgenes en **Ninguno** y **Gráficos de fondo activados**. Los revelados
progresivos se aplanan: cada slide queda en una página con todo visible.

Automatizado, con `node pdf.js` (necesita `npm install playwright`), o bien:

```bash
npm install -g decktape
decktape reveal "artesania.html?print-pdf" artesania-respaldo.pdf
```

---

## El deck no depende de la red

Verificado: cero peticiones externas al abrirlo.

- Las fuentes van incrustadas en base64 dentro de `fuentes.css` (151 KB).
- `html-math-method: plain` desactiva MathJax, que se cargaba de un CDN. Las pocas
  letras matemáticas del deck son cursivas de markdown, y el `β₁` es un carácter
  Unicode. Si más adelante necesitas fórmulas de verdad, saca esa línea del YAML
  y MathJax vuelve (con dependencia de internet).

Para una sala de clases, esto vale más que los kilobytes que cuesta.

---

## Teclas durante la presentación

| Tecla | Qué hace |
|---|---|
| ← → | Avanzar y retroceder (navegación lineal por las 64 slides) |
| **S** | Vista de orador: notas, temporizador y siguiente slide |
| **B** | Pizarra: dibujar encima de la slide |
| **Esc** | Vista general de todas las slides |
| **M** | Menú con buscador |
| **F** | Pantalla completa |

Las notas de orador (`::: {.notes}`) están puestas en la portada y en la slide de
Mills y Becker. Agrega las que quieras: sólo se ven en la vista **S**.

---

## Componentes disponibles

### Bloques

```markdown
::: {.bloque}
[Título del bloque]{.t}
Texto del bloque.
:::
```

`.bloque` (dorado) · `.alerta` (azul acero) · `.ejemplo` (verde salvia) ·
`.falla` (rojo ladrillo). El `[…]{.t}` es el título, y es opcional.

### La franja de criterio

Se ancla sola al pie de la slide:

```markdown
::: {.franja}
::: {.d}
**Delego**
Lo mecánico y verificable contra el PDF.
:::
::: {.nd}
**No delego**
La idea central, la conexión y la objeción.
:::
::: {.v}
**Cómo verifico**
Leo la ficha seis meses después.
:::
:::
```

Está en nueve estaciones. Para mostrarla en medio de una slide en vez de al pie
(como en la slide que la explica), agrega
`{.franja style="position:relative; bottom:auto"}`.

### Énfasis en línea

`[texto]{.hl}` dorado · `[texto]{.hlr}` acero · `[texto]{.hld}` salvia ·
`[texto]{.hlx}` ladrillo · `[texto]{.tenue}` gris.

### Estructura

- `::: {.destacado}` — la caja centrada con borde dorado; `[…]{.grande}` adentro para la línea grande.
- `::: {.cajas}` con `[TEXTO]{.caja}` y `[TEXTO]{.caja .acento}` — la fila de cajas etiquetadas.
- `::: {.cols2}` `.cols3` `.cols-40-60` `.cols-60-40` `.cols-30-70` `.cols-img` — rejillas.
- `::: {.pasos}` — listas numeradas con aire, y `[…]{.glosa}` para la línea gris debajo de cada paso.
- `::: {.nota}` — el pie de página gris.
- `. . .` en una línea sola — un revelado progresivo (el `\pause` de Beamer).
- `## Título {.sintesis}` — las slides de síntesis (las que en Beamer eran fondo marino).
- `# Acto X {.divisoria}` — las portadillas de acto.

### Los diagramas

Once SVG inline, siempre dentro de un bloque raw:

````markdown
::: {.diagrama}
```{=html}
<svg viewBox="0 0 1200 195"> … </svg>
```
:::
````

**El bloque `{=html}` no es opcional.** Pandoc corta un bloque HTML crudo en la
primera línea en blanco, y un SVG con líneas en blanco adentro se desarma en texto
suelto.

Paleta de los diagramas, por si dibujas uno nuevo:

| Rol | Relleno | Borde | Texto |
|---|---|---|---|
| Caja normal | `#17243C` | `#3E5578` | `#E8E3D9` |
| Caja ancla (dorada) | `#2A2416` | `#C9A84C` | `#F0D588` |
| Caja azul (compuerta) | `#132A44` | `#4E7FB0` | `#BFD8F0` |
| Caja verde | `#1C2A18` | `#7E9C64` | `#BBD19E` |
| Caja de falla | `#2A1614` | `#E08C81` | `#EBB3AC` |
| Flechas | `#8FA3C0` · doradas `#D9BC66` · rojas `#E08C81` | | |

---

## Un detalle del tema, por si toca la tipografía

Un nombre de fuente con número (`Source Sans 3`) sin comillas invalida toda la
declaración `font-family` y el navegador cae a Times. Por eso la pila es
`Inter, Helvetica Neue, Arial, sans-serif`. Si agregas una fuente con número al
`$font-family-sans-serif`, va a romper el deck entero de una manera que no parece
tipográfica.

---

## Nota sobre `embed-resources`

No se puede tener un único archivo HTML autocontenido *y* la pizarra al mismo
tiempo: Quarto lo rechaza. El deck viene con pizarra, así que es una carpeta
(`artesania.html` + `artesania_files/`). Si prefieres un solo archivo para mandar
por correo, saca `chalkboard: true` y agrega `embed-resources: true`.
