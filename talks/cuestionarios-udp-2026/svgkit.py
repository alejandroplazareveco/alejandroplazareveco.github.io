"""Pequeño kit para dibujar los diagramas (DAG y flujos) como SVG inline
con la paleta del tema 'marino oscuro'. Cada SVG lleva sus propios
marcadores de flecha con ids únicos (evita problemas con slides ocultas)."""
import itertools, math

_ids = itertools.count(1)

class Diagram:
    def __init__(self, w, h, label=""):
        self.w, self.h, self.label = w, h, label
        self.uid = next(_ids)
        self.nodes = {}
        self.parts = []

    # --- nodos -----------------------------------------------------------
    def node(self, key, cx, cy, w, h, text, kind="obs", size=22, bold=None, cls="", first_bold=False):
        """kind: obs (observada), lat (no observada), err (error/dorada),
        ok (verde), bad (rojo), sol (relleno sólido marino)."""
        self.nodes[key] = (cx, cy, w / 2, h / 2)
        lines = text.split("\n")
        weight = "700" if (bold if bold is not None else kind in ("lat", "err")) else "500"
        lh = size * 1.18
        y0 = cy - lh * (len(lines) - 1) / 2
        tsp = "".join(
            (f'<tspan x="{cx}" y="{y0 + i*lh:.1f}" font-weight="700">{l}</tspan>' if (first_bold and i == 0)
             else f'<tspan x="{cx}" y="{y0 + i*lh:.1f}">{l}</tspan>') for i, l in enumerate(lines)
        )
        extra = f' {cls}' if cls else ''
        self.parts.append(
            f'<g class="nd {kind}{extra}" data-k="{key}"><rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="8"/>'
            f'<text font-size="{size}" font-weight="{weight}">{tsp}</text></g>'
        )

    def _edge(self, key, tx, ty, gap=4):
        cx, cy, hw, hh = self.nodes[key]
        dx, dy = tx - cx, ty - cy
        if dx == 0 and dy == 0:
            return cx, cy
        t = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
        L = math.hypot(dx, dy)
        return cx + dx * t + dx / L * gap, cy + dy * t + dy / L * gap

    # --- flechas ---------------------------------------------------------
    def arrow(self, a, b, kind="g", dash=False, label=None, lpos=0.5, loff=(0, -14),
              lsize=18, both=False, cls=""):
        ax, ay = self.nodes[a][:2]
        bx, by = self.nodes[b][:2]
        x1, y1 = self._edge(a, bx, by)
        x2, y2 = self._edge(b, ax, ay, gap=6)
        self.line(x1, y1, x2, y2, kind, dash, both=both, cls=cls)
        if label:
            lx = x1 + (x2 - x1) * lpos + loff[0]
            ly = y1 + (y2 - y1) * lpos + loff[1]
            self.text(lx, ly, label, size=lsize, cls="lbl" + (" " + cls if cls else ""))

    def line(self, x1, y1, x2, y2, kind="g", dash=False, both=False, cls=""):
        d = " dash" if dash else ""
        ms = f' marker-start="url(#s{kind}{self.uid})"' if both else ""
        c = f" {cls}" if cls else ""
        self.parts.append(
            f'<line class="ar {kind}{d}{c}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'marker-end="url(#m{kind}{self.uid})"{ms}/>'
        )

    def path(self, d, kind="g", dash=False, cls=""):
        dd = " dash" if dash else ""
        c = f" {cls}" if cls else ""
        self.parts.append(f'<path class="ar {kind}{dd}{c}" d="{d}" marker-end="url(#m{kind}{self.uid})"/>')

    def plain(self, d, color="#8FA3C0", width=2.5, dash=False):
        da = ' stroke-dasharray="8 6"' if dash else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da}/>')

    def text(self, x, y, s, size=20, cls="lbl", anchor="middle", weight="500"):
        lines = s.split("\n")
        lh = size * 1.2
        y0 = y - lh * (len(lines) - 1) / 2
        tsp = "".join(f'<tspan x="{x}" y="{y0+i*lh:.1f}">{l}</tspan>' for i, l in enumerate(lines))
        self.parts.append(f'<text class="{cls}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{tsp}</text>')

    def raw(self, s):
        self.parts.append(s)

    def group(self, cls, fn):
        """Agrupa lo que dibuje fn() dentro de <g class=cls> (para fragmentos)."""
        start = len(self.parts)
        fn()
        inner = "".join(self.parts[start:])
        del self.parts[start:]
        self.parts.append(f'<g class="{cls}">{inner}</g>')

    def svg(self):
        u = self.uid
        cols = {"g": "#8FA3C0", "a": "#D9BC66", "r": "#E08C81", "v": "#A3BE86"}
        defs = "".join(
            f'<marker id="m{k}{u}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="userSpaceOnUse">'
            f'<path d="M0,0 L10,5 L0,10 Z" fill="{c}"/></marker>'
            f'<marker id="s{k}{u}" markerWidth="10" markerHeight="10" refX="1" refY="5" orient="auto" markerUnits="userSpaceOnUse">'
            f'<path d="M10,0 L0,5 L10,10 Z" fill="{c}"/></marker>'
            for k, c in cols.items()
        )
        body = "".join(self.parts)
        return (f'<svg class="dg" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{self.label}">'
                f'<defs>{defs}</defs>{body}</svg>')


def raw_html(s, cls="diagrama", style=""):
    st = f' style="{style}"' if style else ""
    return f'::: {{.{cls}{st}}}\n```{{=html}}\n{s}\n```\n:::\n'


def rawblock(s):
    return f'```{{=html}}\n{s}\n```\n'
