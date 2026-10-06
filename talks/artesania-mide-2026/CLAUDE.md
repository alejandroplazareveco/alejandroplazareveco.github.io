# CLAUDE.md — Contexto del vault de investigación
## Instrucción de uso
Lee este archivo al inicio de cada sesión antes de responder cualquier pregunta. Si el usuario no lo menciona, léelo igual — es tu contexto base. Este archivo es la fuente de verdad sobre quién soy, qué estoy haciendo, y cómo trabajar conmigo.

## Quién soy
Alejandro Plaza, sociólogo chileno. Doctoral researcher en la Humboldt-Universität zu Berlin. Magíster en Sociología PUC Chile, Licenciatura Universidad de Chile. Resido actualmente en Santiago.

Trabajo principalmente como investigador académico y consultor metodológico, con experiencia en diseño de encuestas, estudios longitudinales y análisis cuantitativo avanzado.

## Líneas de investigación
1. Desigualdad y estratificación social
2. Análisis de redes sociales (ERGM, SAOM, redes egocéntricas, position generator)
3. Estados de bienestar y preferencias redistributivas
4. Sociología política y formación de clivajes
5. Inferencia causal en ciencias sociales

## Argumento central de la tesis
El rol de las redes sociales en la producción y reproducción de la desigualdad. Tesis por artículos en curso.

## Estructura del vault
El vault está organizado en las siguientes carpetas principales:

- `00_META/` — sistema, templates, README, dashboards, scripts
- `10_TEORIA/` — fichas de lectura y literatura académica por subcarpetas temáticas
- `20_METODOS/` — inferencia causal, análisis longitudinal, análisis de redes, workshops
- `30_PAPERS/` — borradores, notas de trabajo y archivos de papers propios
- `40_CURSOS/` — notas de clases recibidas durante el doctorado
- `50_APLICADO/` — trabajo aplicado y consultorías
- `60_DESARROLLO_PROFESIONAL/` — carrera e investigación futura
- `70_DATASETS/` — información sobre bases de datos disponibles
- `80_TESIS/` — gestión general de la tesis, hipótesis compiladas, programa

## Perfil técnico y herramientas
### Dominio avanzado
- **R**: usuario avanzado. Manejo fluido de tidyverse, modelos longitudinales, modelos causales (diferencias en diferencias, variables instrumentales, propensity score), análisis de redes sociales (igraph, statnet, ERGM, RSiena). No necesitas explicar conceptos básicos de R ni de estadística.
- **Bases de datos longitudinales**: experiencia directa con diseño, gestión y análisis de paneles. Manejo de imputación múltiple, análisis de cambio, modelos de efectos fijos y aleatorios.
- **Análisis de redes sociales**: ERGM, SAOM/RSiena, redes egocéntricas, position generator, detección de comunidades, centralidades.
- **GitHub**: manejo básico-intermedio.

### En desarrollo activo
- **Python**: conocimientos básicos, interés fuerte en profundizar para ciencia de datos. Priorizar pandas, numpy, networkx, scikit-learn.
- **SQL**: interés en aprender para manejo de bases de datos relacionales.

### Idiomas
- Español: nativo
- Inglés: fluido. Puede trabajar en inglés sin problema.
- Alemán: nivel básico, en aprendizaje activo. No usar alemán salvo que lo pida.

## Convenciones del vault
- Fichas de lectura: `Apellido YYYY.md` (ej: `Mouw 2003.md`)
- Notas propias: prefijo `@` (ej: `@argumento-central-tesis.md`)
- Idioma: mixto — fichas en inglés cuando el paper es en inglés, notas propias y borradores en español o inglés según el contexto. Nunca mezclar idiomas dentro de una misma nota.
- Frontmatter YAML obligatorio en toda nota nueva:

```yaml
---
titulo:
autor:
anio:
tipo: articulo | paper | libro | capitulo | post
temas: []
modo: [investigacion]
estado: pendiente | procesado | integrado
fecha_lectura:
fecha_actualizacion:
---
```

## Cómo trabajar conmigo
- **Al inicio de cada sesión**: lee este archivo antes de responder cualquier pregunta.
- **Antes de responder**: si la pregunta involucra investigación, teoría o escritura, revisa primero si hay material relevante en el vault.
- **Referencias**: usa solo lo que encuentres en el vault. Nunca inventes fuentes ni atribuyas argumentos a autores sin haberlos leído en las notas.
- **Nivel técnico**: no explicar conceptos estadísticos básicos ni intermedios. Código R en estilo tidyverse por defecto. Cuando sea relevante, mostrar equivalente en Python o SQL.
- **Notas nuevas**: usar siempre frontmatter YAML completo y convención de nombres.
- **Reorganización de archivos**: confirmar siempre antes de ejecutar cualquier movimiento.
- **Gaps**: si no encuentras algo en el vault, decirlo explícitamente. No rellenar con conocimiento general sin avisar.
