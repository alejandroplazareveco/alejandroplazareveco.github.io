"""Genera clase_cuestionarios.qmd a partir de la plantilla de texto,
insertando diagramas SVG (@@D:clave@@) y laboratorios (@@W:clave@@)."""
import re
from diagramas import D
from laboratorios import W
from svgkit import raw_html, rawblock

src = open("contenido.md", encoding="utf-8").read()

def sub(m):
    kind, key, extra = m.group(1), m.group(2), m.group(3)
    if kind == "D":
        cls = "diagrama" + (" " + extra if extra else "")
        return f'::: {{.{cls.replace(" ", " .")}}}\n```{{=html}}\n{D[key]}\n```\n:::\n'
    return rawblock(W[key])

out = re.sub(r"@@([DW]):([a-z_0-9]+)(?:\|([a-z\-]+))?@@", sub, src)
open("clase_cuestionarios.qmd", "w", encoding="utf-8").write(out)
print("ok", len(out))
