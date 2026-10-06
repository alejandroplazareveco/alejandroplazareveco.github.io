"""Todos los diagramas estáticos de la clase, como SVG."""
from svgkit import Diagram

D = {}

# --- ¿Qué significa medir? --------------------------------------------------
d = Diagram(420, 420, "Concepto, regla y número")
d.node("c", 210, 60, 280, 84, "Concepto\n«confianza»", "lat", 24)
d.node("r", 210, 210, 280, 84, "Regla\npregunta + escala", "obs", 24)
d.node("n", 210, 360, 280, 84, "Número\n1 · 2 · 3 · 4 · 5", "err", 24)
d.arrow("c", "r"); d.arrow("r", "n")
D["medir"] = d.svg()

# --- Asignar números ----------------------------------------------------------
d = Diagram(460, 420, "Categorías de respuesta y números")
for i, (t, n) in enumerate([("Nada", 1), ("Poca", 2), ("Algo", 3), ("Bastante", 4), ("Mucha", 5)]):
    y = 45 + i * 82
    d.node(f"c{i}", 120, y, 200, 58, t, "obs", 24)
    d.node(f"n{i}", 380, y, 70, 58, str(n), "lat", 26)
    d.arrow(f"c{i}", f"n{i}")
D["numeros"] = d.svg()

# --- Encuesta ≠ cuestionario --------------------------------------------------
d = Diagram(1200, 330, "Cuestionario, muestra y modo forman la encuesta")
d.node("q", 200, 70, 320, 110, "Cuestionario\n¿qué preguntamos y cómo?", "obs", 23, first_bold=True)
d.node("m", 600, 70, 320, 110, "Muestra\n¿a quiénes preguntamos?", "obs", 23, first_bold=True)
d.node("mo", 1000, 70, 320, 110, "Modo\n¿cómo llega la pregunta?", "obs", 23, first_bold=True)
d.node("e", 600, 270, 380, 80, "Encuesta", "err", 28)
for k in ("q", "m", "mo"):
    d.arrow(k, "e")
D["encuesta"] = d.svg()

# --- El tiro al blanco (una diana) -------------------------------------------
def diana(cx, cy, r=1.0):
    return (f'<circle cx="{cx}" cy="{cy}" r="{150*r}" fill="#17243C" stroke="#3E5578" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{105*r}" fill="#1F3152"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{60*r}" fill="#2B4268"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{20*r}" fill="#D9BC66"/>')

d = Diagram(520, 380, "Diana: el centro es el valor verdadero")
d.raw(diana(190, 200))
d.path("M420,70 C380,90 260,140 214,188", "a")
d.text(430, 52, "centro = valor verdadero", 22, "lbl oro", "middle", "600")
D["diana"] = d.svg()

# --- Dos tipos de error: cuatro dianas, con fragmentos -----------------------
import random
random.seed(4)
def disparos(cx, cy, bx, by, sd, n=7):
    out = ""
    for _ in range(n):
        x = cx + bx + random.gauss(0, sd); y = cy + by + random.gauss(0, sd)
        out += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#E8E3D9" stroke="#0F1A2E" stroke-width="2"/>'
    return out
casos = [("Preciso e insesgado", "el ideal", 0, 0, 8),
         ("Impreciso, insesgado", "error aleatorio", 0, 0, 48),
         ("Preciso, sesgado", "error sistemático", 60, -55, 9),
         ("Impreciso y sesgado", "lo peor", 55, -50, 42)]
d = Diagram(1400, 380, "Cuatro dianas: precisión y sesgo")
for i, (t1, t2, bx, by, sd) in enumerate(casos):
    cx = 175 + i * 350
    def dib(cx=cx, t1=t1, t2=t2, bx=bx, by=by, sd=sd):
        d.raw(diana(cx, 165, 0.95))
        d.raw(disparos(cx, 165, bx, by, sd))
        d.text(cx, 335, t1, 22, "lbl claro", "middle", "700")
        d.text(cx, 363, t2, 19, "lbl")
    if i == 0:
        dib()
    else:
        d.group(f"fragment\" data-fragment-index=\"{i}", dib)
D["dianas"] = d.svg()

# --- ¿Qué es un DAG? ---------------------------------------------------------
d = Diagram(560, 330, "DAG: la lluvia causa paraguas y calle mojada")
d.node("ll", 280, 50, 200, 66, "Lluvia", "obs", 24)
d.node("pa", 110, 250, 200, 66, "Paraguas", "obs", 24)
d.node("ca", 450, 250, 200, 66, "Calle mojada", "obs", 24)
d.arrow("ll", "pa"); d.arrow("ll", "ca")
d.plain("M212,250 L348,250", "#9BA9BF", 2.5, dash=True)
d.text(280, 290, "andan juntos", 18, "lbl")
D["dag_lluvia"] = d.svg()

d = Diagram(560, 80, "Leyenda de colores")
d.node("a", 90, 40, 170, 56, "no observada", "lat", 19)
d.node("b", 280, 40, 170, 56, "observada", "obs", 19)
d.node("c", 470, 40, 170, 56, "error", "err", 19)
D["leyenda"] = d.svg()

# --- X = V + E -----------------------------------------------------------------
d = Diagram(600, 300, "X igual V más E")
d.node("V", 110, 210, 190, 90, "V\nvalor verdadero", "lat", 24)
d.node("X", 480, 210, 190, 90, "X\nrespuesta", "obs", 24)
d.node("E", 480, 55, 100, 70, "E", "err", 30)
d.arrow("V", "X"); d.arrow("E", "X", "a")
D["xve"] = d.svg()

# --- Barras CIS ----------------------------------------------------------------
d = Diagram(420, 400, "65 por ciento declarado versus 51 por ciento real")
d.raw('<rect x="60" y="80" width="120" height="260" fill="#4E7FB0" rx="3"/>'
      '<rect x="240" y="137" width="120" height="203" fill="#C9A84C" rx="3"/>'
      '<line x1="30" y1="340" x2="390" y2="340" stroke="#9BA9BF" stroke-width="2"/>')
d.text(120, 62, "65%", 30, "lbl claro", "middle", "700")
d.text(300, 119, "51%", 30, "lbl claro", "middle", "700")
d.text(120, 372, "declarado", 20); d.text(300, 372, "resultado real", 20)
D["cis"] = d.svg()

# --- Dos historias ------------------------------------------------------------
d = Diagram(560, 250, "Historia 1: deseabilidad social")
d.node("v", 110, 190, 190, 70, "Voto real", "lat", 22)
d.node("d", 440, 190, 190, 70, "Voto\ndeclarado", "obs", 22)
d.node("s", 440, 50, 250, 64, "Deseabilidad social", "err", 21)
d.arrow("v", "d"); d.arrow("s", "d", "a")
D["hist1"] = d.svg()

d = Diagram(560, 250, "Historia 2: quién acepta responder")
d.node("v", 110, 190, 190, 70, "Voto real", "lat", 22)
d.node("d", 440, 190, 190, 70, "Voto\ndeclarado", "obs", 22)
d.node("r", 110, 50, 220, 64, "Acepta responder", "err", 21)
d.arrow("v", "d"); d.arrow("v", "r", "a")
D["hist2"] = d.svg()

# --- Anillos del árbol ---------------------------------------------------------
d = Diagram(320, 330, "Anillos de un árbol")
d.raw("".join(f'<circle cx="160" cy="150" r="{r}" fill="none" stroke="#C9A84C" stroke-width="2.5"/>' for r in range(22, 145, 22)))
d.raw('<circle cx="160" cy="150" r="8" fill="#D9BC66"/>')
d.text(160, 315, "6 anillos ⇒ 6 años", 22, "lbl claro")
D["anillos"] = d.svg()

# --- Del concepto al número -----------------------------------------------------
d = Diagram(1400, 470, "Del concepto al índice")
d.node("c", 130, 190, 200, 100, "Concepto", "lat", 28)
ys = [70, 190, 310]
for i, y in enumerate(ys, 1):
    d.node(f"d{i}", 470, y, 230, 76, f"Dimensión {i}", "lat", 23)
    d.arrow("c", f"d{i}")
    for j, dy in enumerate((-24, 24)):
        d.node(f"p{i}{j}", 820, y + dy, 190, 40, "Pregunta", "obs", 18, bold=False)
        d.arrow(f"d{i}", f"p{i}{j}")
d.node("i", 1200, 190, 170, 120, "Índice\n45", "err", 28)
for i in (1, 2, 3):
    for j in (0, 1):
        d.arrow(f"p{i}{j}", "i")
d.plain("M30,400 L30,415 L590,415 L590,400", "#C9A84C", 2.5)
d.plain("M700,400 L700,415 L1300,415 L1300,400", "#C9A84C", 2.5)
d.text(310, 450, "Fase teórica", 24, "lbl oro", "middle", "700")
d.text(1000, 450, "Fase empírica", 24, "lbl oro", "middle", "700")
D["concepto_numero"] = d.svg()

# --- Varias preguntas ---------------------------------------------------------
d = Diagram(560, 360, "Varios ítems con errores propios")
d.node("V", 280, 45, 220, 66, "Concepto", "lat", 24)
for i, x in enumerate([70, 210, 350, 490], 1):
    d.node(f"x{i}", x, 175, 110, 56, f"ítem {i}", "obs", 20)
    d.node(f"e{i}", x, 295, 80, 52, f"e{i}", "err", 20)
    d.arrow("V", f"x{i}"); d.arrow(f"e{i}", f"x{i}", "a")
D["items"] = d.svg()

# --- Reflectivo / formativo --------------------------------------------------------
d = Diagram(560, 280, "Modelo reflectivo")
d.node("A", 280, 50, 260, 70, "Autoritarismo", "lat", 23)
for i, x in enumerate([100, 280, 460], 1):
    d.node(f"a{i}", x, 220, 140, 56, f"ítem {i}", "obs", 20)
    d.arrow("A", f"a{i}")
D["reflectivo"] = d.svg()

d = Diagram(560, 280, "Modelo formativo")
d.node("C", 280, 50, 290, 70, "Calidad vivienda", "lat", 23)
for i, (x, t) in enumerate([(100, "material"), (280, "servicios"), (460, "entorno")], 1):
    d.node(f"m{i}", x, 220, 150, 56, t, "obs", 20)
    d.arrow(f"m{i}", "C")
D["formativo"] = d.svg()

# --- Tourangeau -------------------------------------------------------------------
d = Diagram(1400, 300, "Cuatro etapas de la respuesta")
pasos = [("1. Comprensión", "¿qué me preguntan?", "palabras difíciles\ndobles negaciones"),
         ("2. Recuperación", "¿qué recuerdo?", "periodos vagos\n«últimamente»"),
         ("3. Juicio", "¿qué pienso?", "cansancio\n«cualquier cosa»"),
         ("4. Respuesta", "¿qué alternativa elijo?", "deseabilidad social\naquiescencia")]
for i, (t, s, e) in enumerate(pasos):
    x = 175 + i * 350
    d.node(f"p{i}", x, 80, 290, 110, f"{t}\n{s}", "lat", 23)
    def frag(x=x, e=e):
        d.text(x, 220, e, 21, "lbl oro")
    d.group(f"fragment\" data-fragment-index=\"{i+1}", frag)
for i in range(3):
    d.arrow(f"p{i}", f"p{i+1}")
D["tourangeau"] = d.svg()

# --- Caso 1: teoría ------------------------------------------------------------
d = Diagram(500, 400, "Eficacia política interna y externa")
d.node("E", 250, 50, 300, 70, "Eficacia política", "lat", 24)
d.node("I", 120, 190, 180, 62, "Interna", "lat", 21)
d.node("X", 380, 190, 180, 62, "Externa", "lat", 21)
d.arrow("E", "I"); d.arrow("E", "X")
d.node("D", 250, 320, 230, 62, "Deber cívico", "obs", 21)
d.text(250, 375, "(concepto vecino)", 18)
D["eficacia"] = d.svg()

# --- Caso 1: facetas ----------------------------------------------------------------
d = Diagram(1400, 400, "Una escala corta con tres facetas")
d.node("A", 700, 50, 440, 70, "Relación con el voto", "lat", 25)
for k, x, t, it in [("DC", 230, "Deber cívico", "c10_01\nVotar es mi deber"),
                     ("EF", 700, "Eficacia del voto", "c10_02\nMi voto influye"),
                     ("EX", 1170, "Valor expresivo", "c10_03\nVotar expresa mis ideas")]:
    d.node(k, x, 185, 320, 66, t, "lat", 22)
    d.node("i" + k, x, 325, 360, 90, it, "obs", 21)
    d.arrow("A", k); d.arrow(k, "i" + k)
D["facetas"] = d.svg()

# --- Caso 1: voz política -----------------------------------------------------------
d = Diagram(560, 430, "Desigualdad social y participación")
d.node("N", 280, 50, 320, 76, "Nivel socioeconómico\ny educación", "obs", 21)
d.node("E", 120, 215, 190, 64, "Eficacia", "lat", 22)
d.node("R", 440, 215, 210, 76, "Recursos\n(tiempo, dinero)", "obs", 21)
d.node("P", 280, 375, 240, 64, "Participación", "err", 22)
d.arrow("N", "E"); d.arrow("N", "R"); d.arrow("E", "P"); d.arrow("R", "P")
D["voz"] = d.svg()

# --- Caso 2: DAG aquiescencia ---------------------------------------------------------
d = Diagram(1100, 330, "La aquiescencia puede fabricar una relación")
d.node("Ed", 160, 60, 250, 70, "Educación", "obs", 23)
d.node("Q", 900, 60, 270, 70, "Aquiescencia", "err", 23)
d.node("A", 160, 260, 250, 70, "Autoritarismo", "lat", 23)
d.node("R", 900, 260, 270, 80, "Puntaje en\nla escala", "obs", 22)
d.arrow("A", "R"); d.arrow("Q", "R", "a")
d.arrow("Ed", "Q", "a", dash=True, label="menos educación, más aquiescencia", loff=(0, 28), lsize=19)
d.arrow("Ed", "A", label="?", loff=(-22, 0), lsize=26)
D["aquiescencia"] = d.svg()

# --- Caso 3: encuestador ------------------------------------------------------------------
d = Diagram(560, 330, "Presencia del encuestador y de terceros")
d.node("D", 110, 260, 190, 80, "Síntomas\nreales", "lat", 21)
d.node("R", 450, 260, 200, 80, "Síntomas\ndeclarados", "obs", 21)
d.node("Enc", 450, 60, 200, 76, "Encuestador\npresente", "err", 20)
d.node("Ter", 140, 60, 200, 76, "Terceros\npresentes", "err", 20)
d.arrow("D", "R"); d.arrow("Enc", "R", "a"); d.arrow("Ter", "R", "a")
D["encuestador"] = d.svg()

# --- Caso 3: causa común vs red -------------------------------------------------------------
d = Diagram(560, 270, "Modelo de causa común")
d.node("D", 280, 45, 220, 64, "Depresión", "lat", 23)
for i, (x, t) in enumerate([(70, "ánimo"), (210, "sueño"), (350, "energía"), (490, "concentr.")], 1):
    d.node(f"s{i}", x, 210, 120, 54, t, "obs", 18)
    d.arrow("D", f"s{i}")
D["causa_comun"] = d.svg()

d = Diagram(560, 270, "Red de síntomas")
d.node("s", 120, 50, 150, 56, "sueño", "obs", 20)
d.node("e", 440, 50, 150, 56, "energía", "obs", 20)
d.node("c", 440, 215, 150, 56, "concentr.", "obs", 20)
d.node("a", 120, 215, 150, 56, "ánimo", "obs", 20)
d.arrow("s", "e"); d.arrow("e", "c"); d.arrow("c", "a"); d.arrow("a", "s")
D["red"] = d.svg()

# --- Experimento ------------------------------------------------------------------------------
d = Diagram(560, 330, "El azar corta la confusión")
d.node("Z", 110, 50, 170, 64, "Azar", "err", 23)
d.node("V", 110, 255, 170, 80, "Versión\nA / B", "obs", 21)
d.node("Y", 440, 255, 190, 70, "Respuesta", "obs", 21)
d.node("U", 440, 55, 210, 80, "Edad, educación,\nideología…", "obs", 18)
d.arrow("Z", "V", "a"); d.arrow("V", "Y"); d.arrow("U", "Y")
d.arrow("U", "V", "r", dash=True)
d.text(268, 160, "✕", 44, "lbl rojo", "middle", "700")
D["experimento"] = d.svg()

# --- Vincular datos -----------------------------------------------------------------------------
d = Diagram(1400, 430, "La encuesta conectada con otras fuentes")
d.node("E", 700, 215, 300, 110, "Respuestas de\nla encuesta", "err", 25)
for k, x, y, t in [("A", 230, 80, "Registros administrativos\nMINEDUC · Registro Social de Hogares"),
                   ("Q", 1170, 80, "Seguimiento cualitativo\n¿acepta una entrevista en profundidad?"),
                   ("Dn", 230, 350, "Donación de datos\nhistorial de Instagram o LinkedIn"),
                   ("P", 1170, 350, "Paradatos\ntiempos de respuesta, dispositivo")]:
    d.node(k, x, y, 430, 100, t, "obs", 21, first_bold=True)
    d.arrow(k, "E", both=True)
D["vincular"] = d.svg()
