#!/usr/bin/env python3
"""Esquemas del recorrido conceptual. Se puede volver a ejecutar."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "modulos-conceptuales" / "img"

FONT = "Segoe UI, Helvetica Neue, Arial, sans-serif"


def svg(w, h, title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<title>{title}</title>
<rect width="100%" height="100%" fill="#f3efe6"/>
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="8.2" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
    <path d="M 0 1.1 L 8.6 5 L 0 8.9 Z" fill="#1e3a5f"/>
  </marker>
  <marker id="arrSoft" viewBox="0 0 10 10" refX="8.2" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
    <path d="M 0 1.1 L 8.6 5 L 0 8.9 Z" fill="#5c6b7a"/>
  </marker>
  <marker id="arrCoral" viewBox="0 0 10 10" refX="8.2" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
    <path d="M 0 1.1 L 8.6 5 L 0 8.9 Z" fill="#9a4638"/>
  </marker>
</defs>
{body}
</svg>
"""


def save(name, content):
    (OUT / name).write_text(content, encoding="utf-8")


def t(x, y, text, size=16, fill="#1e2430", anchor="start", weight="400"):
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}">{text}</text>'
    )


def rrect(x, y, w, h, fill, stroke, sw=2, rx=12):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def arrow(x1, y1, x2, y2, color="#1e3a5f", soft=False):
    marker = "arrSoft" if soft else ("arrCoral" if color == "#9a4638" else "arr")
    if soft and color == "#1e3a5f":
        color = "#5c6b7a"
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
        f'stroke-width="2.2" marker-end="url(#{marker})"/>'
    )


def pill(x, y, w, h, label, sub, fill, stroke):
    return (
        rrect(x, y, w, h, fill, stroke, 2, 10)
        + t(x + 16, y + 28, label, 15, "#1e2430", weight="700")
        + t(x + 16, y + 50, sub, 13, "#3d4654")
    )


# --- evolución ---------------------------------------------------------------

def evolucion():
    cols = [
        (28, "1", "Documentos enlazados", "Cada dirección\nes una hoja."),
        (310, "2", "El servidor escribe", "Cada acción pide\notra página completa."),
        (592, "3", "La página se queda", "Llega un dato\ny cambia un trozo."),
    ]
    body = []
    for x, n, title, _cap in cols:
        body.append(rrect(x, 28, 260, 390, "#fffdf8", "#e2dcd0", 1.5, 16))
        body.append(f'<circle cx="{x+28}" cy="58" r="14" fill="#1e3a5f"/>')
        body.append(t(x + 28, 63, n, 14, "#fffdf8", "middle", "700"))
        body.append(t(x + 52, 63, title, 16, "#1e2430", weight="700"))
    # col 1: two linked pages
    body.append(rrect(52, 96, 150, 92, "#fff", "#2c333d", 2, 8))
    body.append(t(68, 128, "Horarios", 16, weight="700"))
    body.append(t(68, 154, "L1 · L2 · B12", 14, "#5c6570"))
    body.append(rrect(118, 214, 150, 92, "#fff", "#2c333d", 2, 8))
    body.append(t(134, 246, "Línea L2", 16, weight="700"))
    body.append(t(134, 272, "otra hoja", 14, "#5c6570"))
    body.append(arrow(128, 188, 168, 210))
    body.append(t(158, 360, "Un enlace abre", 15, "#3d4654", "middle"))
    body.append(t(158, 382, "un documento nuevo.", 15, "#3d4654", "middle"))
    # col 2: server
    body.append(rrect(334, 110, 88, 64, "#e7e2d8", "#6f675c", 2, 8))
    body.append(t(378, 138, "Servidor", 13, "#1e2430", "middle", "700"))
    body.append(t(378, 156, "escribe HTML", 12, "#3d4654", "middle"))
    body.append(arrow(422, 142, 468, 142))
    body.append(rrect(472, 100, 74, 86, "#fff", "#2c333d", 2, 6))
    body.append(t(509, 132, "Página", 13, "#1e2430", "middle", "700"))
    body.append(t(509, 152, "entera", 13, "#1e2430", "middle"))
    body.append(t(440, 250, "Pulsar «buscar»", 15, "#3d4654", "middle"))
    body.append(t(440, 272, "sustituye todo", 15, "#3d4654", "middle"))
    body.append(t(440, 294, "lo que había.", 15, "#3d4654", "middle"))
    body.append(t(440, 360, "El navegador espera", 15, "#3d4654", "middle"))
    body.append(t(440, 382, "un documento.", 15, "#3d4654", "middle"))
    # col 3: stable chrome + one row
    body.append(rrect(616, 100, 212, 176, "#fff", "#2c333d", 2, 10))
    body.append(f'<rect x="616" y="100" width="212" height="28" rx="10" fill="#e7e2d8"/>')
    body.append(f'<rect x="616" y="118" width="212" height="12" fill="#e7e2d8"/>')
    body.append(t(722, 119, "Panel", 12, "#1e2430", "middle", "700"))
    body.append(rrect(630, 140, 184, 28, "#fff", "#c9c1b4", 1.5, 6))
    body.append(t(642, 159, "Buscar…", 13, "#8a8175"))
    body.append(rrect(630, 178, 184, 36, "#f8e6b0", "#8d6a12", 2, 6))
    body.append(t(642, 201, "L2  ·  retraso leve", 13, "#1e2430", weight="700"))
    body.append(rrect(630, 222, 184, 28, "#fff", "#e2dcd0", 1.5, 6))
    body.append(t(642, 241, "B12  ·  en servicio", 13, "#5c6570"))
    body.append(t(722, 330, "El menú sigue.", 15, "#3d4654", "middle"))
    body.append(t(722, 352, "Cambia la fila", 15, "#3d4654", "middle"))
    body.append(t(722, 374, "cuyo dato cambió.", 15, "#3d4654", "middle"))
    body.append(t(460, 450, "React organiza esta tercera forma. No inventa la web: ordena cómo se describe la pantalla.", 15, "#3d4654", "middle"))
    return svg(880, 480, "Tres momentos de la web: documentos, páginas escritas por el servidor y una página que se queda mientras cambia un trozo.", "\n".join(body))


def spa():
    body = []
    body.append(rrect(24, 24, 406, 470, "#fffdf8", "#e2dcd0", 1.5, 16))
    body.append(rrect(450, 24, 406, 470, "#fffdf8", "#e2dcd0", 1.5, 16))
    body.append(t(227, 62, "Página tradicional", 20, "#1e2430", "middle", "700"))
    body.append(t(653, 62, "Aplicación de una página", 20, "#1e2430", "middle", "700"))
    steps_l = [
        (96, "1", "La persona pulsa «L2»."),
        (168, "2", "El navegador pide otra dirección."),
        (240, "3", "El servidor envía un documento entero."),
        (312, "4", "La pantalla anterior desaparece."),
    ]
    steps_r = [
        (96, "1", "La persona pulsa «L2»."),
        (168, "2", "La página que ya está se queda."),
        (240, "3", "Se pide un dato, o ya estaba."),
        (312, "4", "Se vuelve a describir solo el detalle."),
    ]
    for y, n, label in steps_l:
        body.append(f'<circle cx="62" cy="{y-6}" r="14" fill="#9a4638"/>')
        body.append(t(62, y - 1, n, 14, "#fff", "middle", "700"))
        body.append(t(88, y, label, 16, "#1e2430"))
    for y, n, label in steps_r:
        body.append(f'<circle cx="488" cy="{y-6}" r="14" fill="#2f6b3a"/>')
        body.append(t(488, y - 1, n, 14, "#fff", "middle", "700"))
        body.append(t(514, y, label, 16, "#1e2430"))
    body.append(t(227, 400, "Tiene sentido cuando cada paso", 15, "#3d4654", "middle"))
    body.append(t(227, 422, "es un documento distinto.", 15, "#3d4654", "middle"))
    body.append(t(653, 400, "Tiene sentido cuando la persona", 15, "#3d4654", "middle"))
    body.append(t(653, 422, "trabaja un rato en la misma vista.", 15, "#3d4654", "middle"))
    body.append(t(440, 524, "Las dos viven en el navegador. Las dos hablan con un servidor. Cambia quién fabrica la siguiente vista.", 15, "#3d4654", "middle"))
    return svg(880, 552, "Comparación de un clic: la página tradicional sustituye el documento; la SPA mantiene la página y actualiza una región.", "\n".join(body))


def mapa():
    body = []
    body.append(pill(36, 150, 200, 78, "Datos", "líneas, estados, alarmas", "#fffdf8", "#6f675c"))
    body.append(arrow(246, 189, 300, 189))
    body.append(rrect(308, 118, 250, 142, "#d5e4f7", "#2c5f94", 2.5, 16))
    body.append(t(433, 168, "React", 26, "#1e2430", "middle", "700"))
    body.append(t(433, 196, "piezas que describen", 15, "#1e3a5f", "middle"))
    body.append(t(433, 216, "la pantalla", 15, "#1e3a5f", "middle"))
    body.append(arrow(568, 189, 622, 189))
    body.append(pill(630, 150, 214, 78, "Pantalla", "lo que la persona ve", "#f8e6b0", "#8d6a12"))
    body.append(rrect(36, 330, 808, 110, "#fffdf8", "#e2dcd0", 1.5, 14))
    body.append(t(56, 368, "Alrededor, sin ser React", 16, "#1e2430", weight="700"))
    body.append(t(56, 398, "Node y NPM preparan los archivos. El servidor web los entrega. La base de datos guarda la verdad.", 15, "#3d4654"))
    body.append(t(56, 422, "Angular y Vue ocupan el mismo hueco: describir la interfaz. Un marco (Next, Gatsby, Remix) decide dónde nace el HTML.", 15, "#3d4654"))
    body.append(t(440, 78, "React es la pieza del medio", 22, "#1e2430", "middle", "700"))
    body.append(t(440, 106, "De los datos sale la pantalla. La pantalla no es un segundo original.", 15, "#3d4654", "middle"))
    return svg(880, 468, "React en el centro: los datos entran, la pantalla sale. Node, el servidor y la base de datos quedan alrededor.", "\n".join(body))


def cuando():
    body = []
    body.append(rrect(24, 24, 406, 400, "#fffdf8", "#2f6b3a", 2, 16))
    body.append(rrect(450, 24, 406, 400, "#fffdf8", "#9a4638", 2, 16))
    body.append(t(227, 64, "React encaja", 22, "#2f6b3a", "middle", "700"))
    body.append(t(653, 64, "Suele sobrar", 22, "#9a4638", "middle", "700"))
    yes = [
        "Un panel cuyo estado cambia a menudo",
        "La misma ficha en lista y en detalle",
        "Filtros, alarmas, colas de trabajo",
        "Varias personas mantienen la interfaz",
    ]
    no = [
        "Una hoja que se lee y casi no cambia",
        "Un formulario que envía y recarga",
        "Un PDF o un correo",
        "La primera necesidad es solo el texto público",
    ]
    y = 110
    for item in yes:
        body.append(f'<circle cx="52" cy="{y-5}" r="5" fill="#2f6b3a"/>')
        body.append(t(70, y, item, 16))
        y += 52
    y = 110
    for item in no:
        body.append(f'<circle cx="478" cy="{y-5}" r="5" fill="#9a4638"/>')
        body.append(t(496, y, item, 16))
        y += 52
    body.append(t(440, 460, "Encajar no obliga a usarlo. Sobrar no lo prohíbe. La pregunta es si la pantalla depende de datos que cambian.", 15, "#3d4654", "middle"))
    return svg(880, 490, "Situaciones en las que un panel React compensa y situaciones en las que una página simple suele bastar.", "\n".join(body))


def bibliotecas():
    cards = [
        (28, "#e7e2d8", "#6f675c", "Angular", "Marco completo", "Trae routing, formularios", "y bastante opinión de serie."),
        (310, "#d5e4f7", "#2c5f94", "React", "Biblioteca de interfaz", "Trae componentes y estado.", "El marco se añade aparte."),
        (592, "#d5ead6", "#2f6b3a", "Vue", "Biblioteca y plantilla", "Misma idea de piezas.", "La plantilla se parece al HTML."),
    ]
    body = [t(440, 48, "Tres herramientas, un mismo trabajo", 22, "#1e2430", "middle", "700")]
    for x, fill, stroke, name, role, l1, l2 in cards:
        body.append(rrect(x, 78, 260, 250, fill, stroke, 2, 16))
        body.append(t(x + 130, 130, name, 26, "#1e2430", "middle", "700"))
        body.append(t(x + 130, 168, role, 16, "#1e3a5f", "middle", "700"))
        body.append(t(x + 130, 214, l1, 15, "#1e2430", "middle"))
        body.append(t(x + 130, 238, l2, 15, "#1e2430", "middle"))
    body.append(rrect(28, 352, 824, 64, "#fffdf8", "#e2dcd0", 1.5, 12))
    body.append(t(440, 390, "Las tres describen la interfaz a partir de datos. No son tres bases de datos ni tres servidores.", 16, "#1e2430", "middle"))
    return svg(880, 444, "Angular, React y Vue comparados: las tres describen la interfaz; React deja el marco para más adelante.", "\n".join(body))


def build():
    body = []
    boxes = [
        (24, "Fuente", "componentes,", "configuración"),
        (250, "Node y NPM", "taller que ensambla", "las piezas"),
        (476, "Resultado", "HTML, CSS y JS", "que el navegador lee"),
        (702, "Servidor web", "entrega esos", "archivos"),
    ]
    for i, (x, title, a, b) in enumerate(boxes):
        body.append(rrect(x, 118, 168, 130, "#fffdf8" if i != 1 else "#d5e4f7", "#2c5f94" if i == 1 else "#6f675c", 2, 14))
        body.append(t(x + 84, 162, title, 16, "#1e2430", "middle", "700"))
        body.append(t(x + 84, 190, a, 13, "#3d4654", "middle"))
        body.append(t(x + 84, 210, b, 13, "#3d4654", "middle"))
        if i < 3:
            body.append(arrow(x + 176, 183, x + 242, 183))
    body.append(t(440, 64, "Antes de publicarse hay un taller", 22, "#1e2430", "middle", "700"))
    body.append(t(440, 300, "Lo que se despliega es el resultado, no la estantería de carpetas del proyecto.", 16, "#3d4654", "middle"))
    body.append(t(440, 328, "NPM es el catálogo de piezas de ese taller. Node es quien lo ejecuta.", 16, "#3d4654", "middle"))
    return svg(880, 370, "Del código fuente al servidor web: Node y NPM construyen los archivos que el navegador sabe abrir.", "\n".join(body))


def funcion():
    body = []
    body.append(rrect(36, 120, 220, 120, "#f8e6b0", "#8d6a12", 2, 16))
    body.append(t(146, 168, "Dato", 14, "#8d6a12", "middle", "700"))
    body.append(t(146, 198, "L2", 22, "#1e2430", "middle", "700"))
    body.append(t(146, 222, "retraso leve", 16, "#1e2430", "middle"))
    body.append(arrow(266, 180, 330, 180))
    body.append(rrect(338, 100, 200, 160, "#d5e4f7", "#2c5f94", 2.5, 18))
    body.append(t(438, 158, "Pieza", 14, "#2c5f94", "middle", "700"))
    body.append(t(438, 190, "FilaLinea", 22, "#1e2430", "middle", "700"))
    body.append(t(438, 218, "describe la fila", 15, "#1e3a5f", "middle"))
    body.append(arrow(548, 180, 612, 180))
    body.append(rrect(620, 120, 224, 120, "#fffdf8", "#2c333d", 2, 16))
    body.append(t(732, 168, "En pantalla", 14, "#5c6570", "middle", "700"))
    body.append(t(732, 202, "L2 · Retraso leve", 18, "#1e2430", "middle", "700"))
    body.append(t(440, 56, "La interfaz es una función de los datos", 22, "#1e2430", "middle", "700"))
    body.append(t(440, 320, "Si el dato pasa a «en servicio», la misma pieza describe otra fila.", 16, "#3d4654", "middle"))
    body.append(t(440, 346, "Nadie edita el letrero a mano en paralelo.", 16, "#3d4654", "middle"))
    return svg(880, 390, "Un dato entra en una pieza y sale la fila que se ve. Si el dato cambia, la misma pieza describe otra fila.", "\n".join(body))


def browser_chrome(x, y, w, h):
    parts = [
        rrect(x, y, w, h, "#fffdf8", "#2c333d", 2, 16),
        f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="16" fill="#e7e2d8"/>',
        f'<rect x="{x}" y="{y+18}" width="{w}" height="20" fill="#e7e2d8"/>',
        f'<circle cx="{x+22}" cy="{y+18}" r="5" fill="#e07a5f"/>',
        f'<circle cx="{x+38}" cy="{y+18}" r="5" fill="#e6b325"/>',
        f'<circle cx="{x+54}" cy="{y+18}" r="5" fill="#81b29a"/>',
    ]
    return parts


def boceto():
    body = []
    body += browser_chrome(170, 24, 540, 560)
    body.append(t(440, 46, "boceto", 13, "#5c6570", "middle"))
    # inner sketch strokes only
    body.append(t(210, 100, "Panel de servicio", 22, "#1e2430", weight="700"))
    body.append(rrect(200, 118, 480, 40, "#fff", "#2c333d", 1.6, 8))
    body.append(t(216, 144, "Buscar línea…", 16, "#8a8175"))
    body.append(rrect(200, 172, 16, 16, "#fff", "#2c333d", 1.6, 3))
    body.append(t(224, 186, "Solo incidencias", 15, "#1e2430"))
    body.append(t(200, 230, "METRO", 13, "#5c6570", weight="700"))
    for i, (name, state) in enumerate([("L1", "En servicio"), ("L2", "Retraso leve")]):
        yy = 244 + i * 64
        body.append(rrect(200, yy, 480, 52, "#fff", "#2c333d", 1.6, 8))
        body.append(t(216, yy + 32, name, 16, weight="700"))
        body.append(t(520, yy + 32, state, 15, "#3d4654", "end"))
    body.append(t(200, 392, "BUS", 13, "#5c6570", weight="700"))
    body.append(rrect(200, 404, 480, 52, "#fff", "#2c333d", 1.6, 8))
    body.append(t(216, 436, "B12", 16, weight="700"))
    body.append(t(520, 436, "Interrumpida", 15, "#3d4654", "end"))
    body.append(t(440, 620, "Primero el dibujo. Las piezas salen de rodear lo que ya se entiende.", 16, "#3d4654", "middle"))
    return svg(880, 652, "Boceto de un panel de servicio: búsqueda, filtro, grupos Metro y Bus, y una fila por línea.", "\n".join(body))


def cajas():
    body = []
    body += browser_chrome(20, 20, 560, 600)
    body.append(t(300, 42, "panel", 13, "#5c6570", "middle"))
    # whole app
    body.append(rrect(36, 70, 528, 530, "#e7e2d8", "#6f675c", 2, 12))
    body.append(t(52, 96, "PanelServicio", 14, "#3d4654", weight="700"))
    body.append(t(52, 116, "el panel entero", 13, "#5c6570"))
    body.append(t(52, 148, "Panel de servicio", 20, "#1e2430", weight="700"))
    # search
    body.append(rrect(52, 164, 496, 108, "#d5e4f7", "#2c5f94", 2, 10))
    body.append(t(66, 186, "BarraBusqueda", 13, "#2c5f94", weight="700"))
    body.append(rrect(66, 196, 468, 32, "#fff", "#2c5f94", 1.5, 8))
    body.append(t(80, 217, "Buscar línea…", 14, "#8a8175"))
    body.append(rrect(66, 238, 14, 14, "#fff", "#2c5f94", 1.5, 3))
    body.append(t(86, 250, "Solo incidencias", 14, "#1e2430"))
    # list
    body.append(rrect(52, 286, 496, 296, "#e3dcf5", "#66558f", 2, 10))
    body.append(t(66, 308, "ListaLineas", 13, "#66558f", weight="700"))
    body.append(rrect(66, 318, 468, 26, "#d5ead6", "#2f6b3a", 1.5, 6))
    body.append(t(78, 336, "METRO", 13, "#2f6b3a", weight="700"))
    body.append(t(430, 336, "GrupoLinea", 12, "#2f6b3a", "end"))
    rows = [("L1", "En servicio", 352), ("L2", "Retraso leve", 414)]
    for name, state, yy in rows:
        body.append(rrect(66, yy, 468, 52, "#f8e6b0", "#8d6a12", 2, 8))
        body.append(t(80, yy + 22, "FilaLinea", 11, "#8d6a12", weight="700"))
        body.append(t(80, yy + 40, name, 15, "#1e2430", weight="700"))
        body.append(t(518, yy + 36, state, 14, "#1e2430", "end"))
    body.append(rrect(66, 476, 468, 26, "#d5ead6", "#2f6b3a", 1.5, 6))
    body.append(t(78, 494, "BUS", 13, "#2f6b3a", weight="700"))
    body.append(t(430, 494, "GrupoLinea", 12, "#2f6b3a", "end"))
    body.append(rrect(66, 510, 468, 52, "#f8e6b0", "#8d6a12", 2, 8))
    body.append(t(80, 532, "FilaLinea", 11, "#8d6a12", weight="700"))
    body.append(t(80, 550, "B12", 15, "#1e2430", weight="700"))
    body.append(t(518, 546, "Interrumpida", 14, "#1e2430", "end"))
    # legend
    body.append(t(760, 48, "Las cinco piezas", 16, "#1e2430", "middle", "700"))
    legend = [
        (78, "#e7e2d8", "#6f675c", "PanelServicio", "contiene el resto"),
        (168, "#d5e4f7", "#2c5f94", "BarraBusqueda", "texto y casilla"),
        (258, "#e3dcf5", "#66558f", "ListaLineas", "el conjunto"),
        (348, "#d5ead6", "#2f6b3a", "GrupoLinea", "un rótulo de modo"),
        (438, "#f8e6b0", "#8d6a12", "FilaLinea", "una línea y su estado"),
    ]
    for y, fill, stroke, name, sub in legend:
        body.append(rrect(620, y, 300, 72, fill, stroke, 2, 10))
        body.append(t(636, y + 30, name, 16, "#1e2430", weight="700"))
        body.append(t(636, y + 52, sub, 14, "#3d4654"))
    body.append(t(770, 560, "Cada caja hace una cosa.", 14, "#3d4654", "middle"))
    body.append(t(770, 582, "Si crece, se parte.", 14, "#3d4654", "middle"))
    return svg(960, 640, "El boceto del panel con cajas de color: PanelServicio, BarraBusqueda, ListaLineas, GrupoLinea y FilaLinea.", "\n".join(body))


def jerarquia():
    body = []
    body.append(t(440, 42, "El mismo dibujo, en árbol", 22, "#1e2430", "middle", "700"))
    body.append(rrect(330, 64, 220, 54, "#e7e2d8", "#6f675c", 2, 10))
    body.append(t(440, 97, "PanelServicio", 16, "#1e2430", "middle", "700"))
    body.append(f'<line x1="440" y1="118" x2="440" y2="146" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(f'<line x1="220" y1="146" x2="660" y2="146" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(f'<line x1="220" y1="146" x2="220" y2="170" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(f'<line x1="660" y1="146" x2="660" y2="170" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(rrect(110, 170, 220, 54, "#d5e4f7", "#2c5f94", 2, 10))
    body.append(t(220, 203, "BarraBusqueda", 16, "#1e2430", "middle", "700"))
    body.append(rrect(550, 170, 220, 54, "#e3dcf5", "#66558f", 2, 10))
    body.append(t(660, 203, "ListaLineas", 16, "#1e2430", "middle", "700"))
    body.append(f'<line x1="660" y1="224" x2="660" y2="250" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(f'<line x1="520" y1="250" x2="800" y2="250" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(f'<line x1="520" y1="250" x2="520" y2="274" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(f'<line x1="800" y1="250" x2="800" y2="274" stroke="#1e3a5f" stroke-width="2"/>')
    body.append(rrect(410, 274, 220, 48, "#d5ead6", "#2f6b3a", 2, 10))
    body.append(t(520, 304, "GrupoLinea", 16, "#1e2430", "middle", "700"))
    body.append(rrect(690, 274, 220, 48, "#f8e6b0", "#8d6a12", 2, 10))
    body.append(t(800, 304, "FilaLinea", 16, "#1e2430", "middle", "700"))
    body.append(t(440, 370, "GrupoLinea y FilaLinea se repiten: dos modos, tres líneas, las mismas piezas.", 16, "#3d4654", "middle"))
    body.append(t(440, 398, "El rótulo METRO y la fila L2 no son dos diseños. Son la misma función con otros datos.", 16, "#3d4654", "middle"))
    return svg(880, 440, "Árbol de piezas del panel: PanelServicio contiene la búsqueda y la lista; la lista contiene grupos y filas.", "\n".join(body))


def props():
    body = []
    body.append(t(440, 40, "Lo que baja y lo que se recuerda", 22, "#1e2430", "middle", "700"))
    body.append(rrect(250, 64, 380, 110, "#e7e2d8", "#6f675c", 2, 14))
    body.append(t(440, 96, "PanelServicio recuerda", 16, "#1e2430", "middle", "700"))
    body.append(rrect(276, 112, 150, 40, "#fff", "#8d6a12", 1.5, 8))
    body.append(t(351, 137, "texto: «L»", 14, "#1e2430", "middle"))
    body.append(rrect(444, 112, 160, 40, "#fff", "#8d6a12", 1.5, 8))
    body.append(t(524, 137, "casilla: no", 14, "#1e2430", "middle"))
    body.append(arrow(360, 174, 250, 230, soft=True))
    body.append(arrow(520, 174, 640, 230, soft=True))
    body.append(rrect(70, 236, 300, 100, "#d5e4f7", "#2c5f94", 2, 12))
    body.append(t(220, 272, "BarraBusqueda", 16, "#1e2430", "middle", "700"))
    body.append(t(220, 300, "recibe el texto", 14, "#1e3a5f", "middle"))
    body.append(t(220, 320, "y avisa al escribir", 14, "#1e3a5f", "middle"))
    body.append(rrect(510, 236, 300, 100, "#e3dcf5", "#66558f", 2, 12))
    body.append(t(660, 272, "ListaLineas", 16, "#1e2430", "middle", "700"))
    body.append(t(660, 300, "recibe las líneas ya filtradas", 14, "#3d4654", "middle"))
    body.append(t(660, 320, "no guarda el filtro", 14, "#3d4654", "middle"))
    body.append(rrect(70, 370, 740, 78, "#fffdf8", "#e2dcd0", 1.5, 12))
    body.append(t(440, 402, "Esas entradas se llaman props. El recuerdo del panel se llama estado.", 16, "#1e2430", "middle", "700"))
    body.append(t(440, 428, "La lista filtrada no se guarda: se calcula con el texto, la casilla y las líneas.", 15, "#3d4654", "middle"))
    return svg(880, 476, "El panel recuerda el texto y la casilla. La búsqueda y la lista reciben props. La lista filtrada se calcula.", "\n".join(body))


def actualizacion():
    body = []
    body.append(t(220, 40, "Antes", 16, "#5c6570", "middle", "700"))
    body.append(t(660, 40, "Después del dato", 16, "#5c6570", "middle", "700"))
    body.append(rrect(40, 60, 360, 250, "#fffdf8", "#2c333d", 2, 14))
    body.append(rrect(480, 60, 360, 250, "#fffdf8", "#2c333d", 2, 14))
    body.append(t(60, 96, "texto vacío · casilla no", 14, "#5c6570"))
    body.append(t(500, 96, "casilla: solo incidencias", 14, "#8d6a12", weight="700"))
    rows_l = [(116, "L1", "En servicio", False), (166, "L2", "Retraso leve", True), (216, "B12", "Interrumpida", True)]
    for y, name, state, hot in rows_l:
        body.append(rrect(60, y, 320, 40, "#f8e6b0" if hot else "#fff", "#8d6a12" if hot else "#e2dcd0", 1.5, 8))
        body.append(t(76, y + 26, f"{name}   {state}", 15, "#1e2430"))
    rows_r = [(116, "L2", "Retraso leve"), (166, "B12", "Interrumpida")]
    for y, name, state in rows_r:
        body.append(rrect(500, y, 320, 40, "#f6d5ce", "#9a4638", 1.5, 8))
        body.append(t(516, y + 26, f"{name}   {state}", 15, "#1e2430"))
    body.append(t(660, 250, "L1 ya no sale.", 15, "#3d4654", "middle"))
    body.append(t(660, 272, "No se borró a mano.", 15, "#3d4654", "middle"))
    body.append(arrow(410, 180, 468, 180))
    body.append(t(440, 350, "Cambia el recuerdo. Se vuelve a describir la lista. La fila es la misma pieza, con menos datos.", 16, "#3d4654", "middle"))
    return svg(880, 390, "Al marcar solo incidencias, la lista se vuelve a describir y la línea en servicio deja de mostrarse.", "\n".join(body))


def vdom():
    body = []
    body.append(t(440, 40, "Dos descripciones, un retoque", 22, "#1e2430", "middle", "700"))
    body.append(rrect(36, 70, 250, 250, "#fffdf8", "#6f675c", 2, 14))
    body.append(t(161, 102, "Descripción anterior", 15, "#1e2430", "middle", "700"))
    body.append(t(161, 148, "ListaLineas", 15, "#66558f", "middle", "700"))
    body.append(t(161, 180, "Fila L1 · en servicio", 14, "#3d4654", "middle"))
    body.append(t(161, 208, "Fila L2 · retraso", 14, "#3d4654", "middle"))
    body.append(t(161, 236, "Fila B12 · interrumpida", 14, "#3d4654", "middle"))
    body.append(rrect(310, 70, 250, 250, "#fffdf8", "#2c5f94", 2, 14))
    body.append(t(435, 102, "Descripción nueva", 15, "#1e2430", "middle", "700"))
    body.append(t(435, 148, "ListaLineas", 15, "#66558f", "middle", "700"))
    body.append(t(435, 180, "Fila L1 · en servicio", 14, "#3d4654", "middle"))
    body.append(rrect(332, 194, 206, 28, "#f6d5ce", "#9a4638", 1.5, 6))
    body.append(t(435, 213, "Fila L2 · en servicio", 14, "#1e2430", "middle", "700"))
    body.append(t(435, 248, "Fila B12 · interrumpida", 14, "#3d4654", "middle"))
    body.append(arrow(570, 180, 630, 180))
    body.append(rrect(640, 110, 204, 170, "#f8e6b0", "#8d6a12", 2, 14))
    body.append(t(742, 150, "Página real", 15, "#1e2430", "middle", "700"))
    body.append(t(742, 184, "Se toca la fila L2.", 14, "#1e2430", "middle"))
    body.append(t(742, 210, "El resto de la", 14, "#3d4654", "middle"))
    body.append(t(742, 232, "página sigue.", 14, "#3d4654", "middle"))
    body.append(t(440, 360, "A esa descripción intermedia se le llama DOM virtual. El nombre importa menos que el efecto:", 15, "#3d4654", "middle"))
    body.append(t(440, 384, "tú declaras cómo debe verse; React calcula el retoque.", 15, "#3d4654", "middle"))
    return svg(880, 420, "React compara la descripción anterior con la nueva y retoca en la página real solo la fila que cambió.", "\n".join(body))


def carpetas():
    body = []
    body.append(t(300, 42, "La estantería del proyecto", 22, "#1e2430", "middle", "700"))
    floors = [
        (70, "#d5e4f7", "#2c5f94", "Pantallas", "una por tarea: listado, detalle, alarma"),
        (150, "#f8e6b0", "#8d6a12", "Componentes", "las piezas que se repiten"),
        (230, "#e3dcf5", "#66558f", "Estado y datos", "recuerdos de pantalla y acceso a la API"),
        (310, "#d5ead6", "#2f6b3a", "Estilos", "cómo se ve, separado de qué significa"),
    ]
    for y, fill, stroke, name, sub in floors:
        body.append(rrect(40, y, 520, 68, fill, stroke, 2, 12))
        body.append(t(60, y + 30, name, 18, "#1e2430", weight="700"))
        body.append(t(60, y + 52, sub, 14, "#3d4654"))
    body.append(rrect(590, 70, 250, 308, "#fffdf8", "#6f675c", 2, 14))
    body.append(t(715, 108, "Lo que se publica", 16, "#1e2430", "middle", "700"))
    body.append(t(715, 150, "no es esta", 15, "#3d4654", "middle"))
    body.append(t(715, 174, "estantería.", 15, "#3d4654", "middle"))
    body.append(t(715, 214, "Es el resultado", 15, "#3d4654", "middle"))
    body.append(t(715, 238, "del taller", 15, "#3d4654", "middle"))
    body.append(t(715, 262, "Node.", 15, "#3d4654", "middle"))
    body.append(t(715, 310, "Un marco como", 15, "#3d4654", "middle"))
    body.append(t(715, 334, "Next cambia", 15, "#3d4654", "middle"))
    body.append(t(715, 358, "los nombres", 15, "#3d4654", "middle"))
    return svg(880, 430, "Cuatro plantas de un proyecto React: pantallas, componentes, estado y datos, y estilos. Se publica el resultado de la construcción.", "\n".join(body))


def dos_piezas():
    body = []
    body.append(t(440, 42, "Quién decide y quién pinta", 22, "#1e2430", "middle", "700"))
    body.append(rrect(40, 80, 360, 200, "#e3dcf5", "#66558f", 2, 16))
    body.append(t(220, 120, "Decide", 14, "#66558f", "middle", "700"))
    body.append(t(220, 156, "ListaLineas", 22, "#1e2430", "middle", "700"))
    body.append(t(220, 190, "sabe el filtro", 16, "#1e2430", "middle"))
    body.append(t(220, 214, "elige qué filas existen", 16, "#1e2430", "middle"))
    body.append(t(220, 248, "lógica", 14, "#66558f", "middle"))
    body.append(arrow(410, 180, 470, 180))
    body.append(t(440, 166, "props", 13, "#1e3a5f", "middle"))
    body.append(rrect(480, 80, 360, 200, "#f8e6b0", "#8d6a12", 2, 16))
    body.append(t(660, 120, "Pinta", 14, "#8d6a12", "middle", "700"))
    body.append(t(660, 156, "FilaLinea", 22, "#1e2430", "middle", "700"))
    body.append(t(660, 190, "recibe nombre y estado", 16, "#1e2430", "middle"))
    body.append(t(660, 214, "no sabe cuántas líneas hay", 16, "#1e2430", "middle"))
    body.append(t(660, 248, "presentación", 14, "#8d6a12", "middle"))
    body.append(arrow(640, 328, 240, 328, "#9a4638"))
    body.append(t(440, 316, "la fila avisa: han pulsado L2", 14, "#9a4638", "middle"))
    body.append(t(440, 390, "El aviso sube. El dato baja. La fila sigue siendo intercambiable.", 16, "#3d4654", "middle"))
    return svg(880, 430, "ListaLineas decide qué filas hay. FilaLinea solo pinta el nombre y el estado, y avisa si la pulsan.", "\n".join(body))


def alcances():
    body = []
    body.append(t(440, 40, "Tres sitios donde puede vivir un recuerdo", 22, "#1e2430", "middle", "700"))
    cards = [
        (28, "#f8e6b0", "#8d6a12", "En la pieza", "Un desplegable abierto.", "Al salir de la pieza, se olvida."),
        (310, "#d5e4f7", "#2c5f94", "En la pantalla", "El texto de búsqueda.", "Lo comparten búsqueda y lista."),
        (592, "#e3dcf5", "#66558f", "En la aplicación", "La sesión, un aviso global.", "Varias pantallas lo leen."),
    ]
    for x, fill, stroke, title, a, b in cards:
        body.append(rrect(x, 70, 260, 210, fill, stroke, 2, 16))
        body.append(t(x + 130, 116, title, 20, "#1e2430", "middle", "700"))
        body.append(t(x + 130, 166, a, 15, "#1e2430", "middle"))
        body.append(t(x + 130, 192, b, 15, "#1e2430", "middle"))
    body.append(t(440, 320, "Sube el recuerdo hasta la pieza más baja que todavía alcance a todas las que lo necesitan.", 16, "#3d4654", "middle"))
    body.append(t(440, 348, "Si solo lo usa una fila, dejarlo en la aplicación entera estorba.", 16, "#3d4654", "middle"))
    return svg(880, 390, "Tres alcances del estado: la pieza, la pantalla y la aplicación. El recuerdo sube solo hasta donde hace falta.", "\n".join(body))


def ciclo():
    body = []
    phases = [
        (40, "Aparece", "Entra en pantalla.", "Puede pedir datos.", "#d5ead6", "#2f6b3a"),
        (310, "Se actualiza", "Un dato cambia.", "Se vuelve a describir.", "#d5e4f7", "#2c5f94"),
        (580, "Se va", "La persona cambia de vista.", "Deja de escuchar.", "#f6d5ce", "#9a4638"),
    ]
    for x, title, a, b, fill, stroke in phases:
        body.append(rrect(x, 80, 250, 160, fill, stroke, 2, 16))
        body.append(t(x + 125, 130, title, 22, "#1e2430", "middle", "700"))
        body.append(t(x + 125, 170, a, 15, "#1e2430", "middle"))
        body.append(t(x + 125, 196, b, 15, "#1e2430", "middle"))
    body.append(arrow(290, 160, 305, 160))
    body.append(arrow(560, 160, 575, 160))
    body.append(t(440, 48, "La visita de una pieza", 22, "#1e2430", "middle", "700"))
    body.append(t(440, 290, "Un hook es el nombre de un enchufe de esa visita: uno recuerda, otro reacciona cuando algo cambia.", 16, "#3d4654", "middle"))
    body.append(t(440, 318, "En un fichero verás useState (recuerdo) y useEffect (reacción). La idea es esta línea de tres momentos.", 16, "#3d4654", "middle"))
    return svg(880, 360, "Ciclo de una pieza: aparece, se actualiza cuando cambian los datos y se va cuando deja de mostrarse.", "\n".join(body))


def fuentes():
    body = []
    body.append(rrect(330, 150, 220, 120, "#f8e6b0", "#8d6a12", 2, 16))
    body.append(t(440, 200, "Pantalla", 20, "#1e2430", "middle", "700"))
    body.append(t(440, 228, "React", 16, "#8d6a12", "middle"))
    sources = [
        (36, 36, "API REST", "pregunta y respuesta", 146, 150),
        (624, 36, "JSON de fichero", "datos que viajan con la app", 624, 150),
        (36, 340, "Broker", "buzón: el mensaje espera", 146, 270),
        (624, 340, "WebSocket", "línea abierta, llega solo", 624, 270),
    ]
    for x, y, title, sub, ax, ay in sources:
        body.append(rrect(x, y, 220, 90, "#fffdf8", "#2c5f94", 2, 12))
        body.append(t(x + 110, y + 38, title, 16, "#1e2430", "middle", "700"))
        body.append(t(x + 110, y + 64, sub, 13, "#3d4654", "middle"))
    body.append(arrow(256, 90, 360, 160))
    body.append(arrow(624, 90, 530, 160))
    body.append(arrow(256, 370, 360, 250))
    body.append(arrow(624, 370, 530, 250))
    body.append(t(440, 500, "La pantalla no es la fuente. Enseña lo que alguna de estas vías le trae.", 16, "#3d4654", "middle"))
    return svg(880, 530, "Cuatro vías hacia la pantalla: una API REST, un fichero JSON, un broker de mensajes y un WebSocket.", "\n".join(body))


def desenlaces():
    body = []
    cards = [
        (24, "#e7e2d8", "#6f675c", "Cargando", "Ya se pidió.", "Aún no hay respuesta.", "La pantalla lo dice."),
        (242, "#d5ead6", "#2f6b3a", "Con datos", "Hay líneas.", "Se describen las filas.", "Se puede actuar."),
        (460, "#d5e4f7", "#2c5f94", "Vacío", "La respuesta llegó.", "La lista tiene cero.", "No es un fallo."),
        (678, "#f6d5ce", "#9a4638", "Error", "No hay respuesta útil.", "Se dice qué pasa", "y si se puede reintentar."),
    ]
    for x, fill, stroke, title, a, b, c in cards:
        body.append(rrect(x, 70, 200, 250, fill, stroke, 2, 14))
        body.append(t(x + 100, 120, title, 18, "#1e2430", "middle", "700"))
        body.append(t(x + 100, 170, a, 14, "#1e2430", "middle"))
        body.append(t(x + 100, 194, b, 14, "#1e2430", "middle"))
        body.append(t(x + 100, 218, c, 14, "#1e2430", "middle"))
    body.append(t(440, 42, "Cuatro finales de una petición", 22, "#1e2430", "middle", "700"))
    body.append(t(440, 360, "Una entrega que solo enseña el caso feliz esconde tres de los cuatro finales.", 16, "#3d4654", "middle"))
    return svg(900, 400, "Cuatro estados de una petición: cargando, con datos, vacío y error.", "\n".join(body))


def capas():
    layers = [
        ("Persona", "mira, filtra, decide", "#f8e6b0", "#8d6a12"),
        ("Navegador", "React describe la pantalla", "#d5e4f7", "#2c5f94"),
        ("Middleware", "identidad, proxy, permisos de red", "#e7e2d8", "#6f675c"),
        ("Backend", "API: la pregunta admitida", "#e3dcf5", "#66558f"),
        ("Fuentes", "bases, colas, servicios de negocio", "#d5ead6", "#2f6b3a"),
    ]
    body = [t(440, 40, "De la persona al dato", 22, "#1e2430", "middle", "700")]
    for i, (name, sub, fill, stroke) in enumerate(layers):
        y = 64 + i * 62
        body.append(rrect(140, y, 600, 52, fill, stroke, 2, 10))
        body.append(t(160, y + 32, name, 16, "#1e2430", weight="700"))
        body.append(t(340, y + 32, sub, 15, "#3d4654"))
    return svg(880, 400, "Capas: persona, navegador con React, middleware, backend y fuentes de datos.", "\n".join(body))


def revision():
    notes = [
        (36, 80, "Piezas", "¿Se señala la caja\ny el dato por separado?"),
        (250, 80, "Espera", "¿Hay carga, vacío\ny error?"),
        (464, 80, "Acceso", "¿Se usa sin ratón\ny sin depender del color?"),
        (678, 80, "Dispositivos", "¿La decisión cabe\nen el teléfono?"),
        (36, 250, "Pruebas", "¿Alguien demuestra\nel comportamiento frágil?"),
        (250, 250, "Contrato", "¿El JSON tiene dueño\ny está escrito?"),
        (464, 250, "Secretos", "¿La clave vive\nen el servidor?"),
        (678, 250, "Taller", "¿Se publica el resultado\nde la construcción?"),
    ]
    body = [t(460, 46, "Qué mirar en un entregable", 22, "#1e2430", "middle", "700")]
    for x, y, title, sub in notes:
        body.append(rrect(x, y, 196, 140, "#fffdf8", "#2c5f94", 2, 12))
        body.append(t(x + 98, y + 36, title, 16, "#1e3a5f", "middle", "700"))
        lines = sub.split("\n")
        body.append(t(x + 98, y + 70, lines[0], 13, "#1e2430", "middle"))
        body.append(t(x + 98, y + 92, lines[1], 13, "#1e2430", "middle"))
    return svg(910, 430, "Ocho preguntas para revisar un entregable React sin leerlo como un programador.", "\n".join(body))


def alertas():
    items = [
        ("Un solo fichero", "La pantalla, la regla de negocio y la llamada al servidor viven juntos."),
        ("El letrero copiado", "«En servicio» está escrito en diez sitios. Cambiará en nueve."),
        ("Dos verdades", "La lista dice tres y un contador guardado dice cuatro."),
        ("Marco de más", "Gatsby para una pared de alarmas en vivo, o Electron para abrir una URL."),
    ]
    body = [t(440, 46, "Cuatro señales de alerta", 22, "#1e2430", "middle", "700")]
    for i, (title, sub) in enumerate(items):
        y = 76 + i * 78
        body.append(rrect(40, y, 800, 66, "#fffdf8", "#9a4638", 2, 12))
        body.append(f'<rect x="40" y="{y}" width="10" height="66" rx="4" fill="#9a4638"/>')
        body.append(t(70, y + 28, title, 16, "#1e2430", weight="700"))
        body.append(t(70, y + 50, sub, 14, "#3d4654"))
    return svg(880, 410, "Señales de alerta: un fichero enorme, textos copiados, datos duplicados y un marco que no responde al problema.", "\n".join(body))


def marcos():
    cols = [
        (24, "React solo", "El HTML útil nace\nen el navegador,\ndespués de cargar.", "#e7e2d8", "#6f675c"),
        (242, "Next.js", "Puede nacer en el\nservidor, al publicar\no en el navegador.", "#d5e4f7", "#2c5f94"),
        (460, "Gatsby", "Nace al publicar,\ndesde el contenido.\nCada visita lo recibe hecho.", "#d5ead6", "#2f6b3a"),
        (678, "Remix", "Nace en el servidor\nen cada navegación.\nEl formulario es el modelo.", "#f8e6b0", "#8d6a12"),
    ]
    body = [t(450, 42, "Cuándo nace el HTML", 22, "#1e2430", "middle", "700")]
    for x, title, sub, fill, stroke in cols:
        body.append(rrect(x, 70, 200, 250, fill, stroke, 2, 14))
        body.append(t(x + 100, 112, title, 18, "#1e2430", "middle", "700"))
        yy = 160
        for line in sub.split("\n"):
            body.append(t(x + 100, yy, line, 14, "#1e2430", "middle"))
            yy += 24
    body.append(t(450, 360, "Los cuatro usan la idea de React. El marco no sustituye a las piezas: decide dónde se fabrican.", 15, "#3d4654", "middle"))
    return svg(900, 400, "React solo, Next.js, Gatsby y Remix comparados según el momento en que se fabrica el HTML.", "\n".join(body))


def superficies():
    body = []
    body.append(rrect(330, 150, 220, 110, "#d5e4f7", "#2c5f94", 2.5, 16))
    body.append(t(440, 196, "Misma idea", 18, "#1e2430", "middle", "700"))
    body.append(t(440, 222, "piezas y estado", 15, "#1e3a5f", "middle"))
    spots = [
        (40, 40, "Navegador", "React en la web"),
        (600, 40, "Móvil empaquetado", "Ionic"),
        (40, 340, "Móvil nativo", "React Native"),
        (600, 340, "Puesto de escritorio", "Electron"),
    ]
    for x, y, title, sub in spots:
        body.append(rrect(x, y, 240, 80, "#fffdf8", "#6f675c", 2, 12))
        body.append(t(x + 120, y + 34, title, 16, "#1e2430", "middle", "700"))
        body.append(t(x + 120, y + 58, sub, 14, "#3d4654", "middle"))
    body.append(arrow(280, 80, 340, 160, soft=True))
    body.append(arrow(600, 80, 540, 160, soft=True))
    body.append(arrow(280, 360, 340, 250, soft=True))
    body.append(arrow(600, 360, 540, 250, soft=True))
    body.append(t(440, 500, "Cambia la superficie, no la pregunta: ¿de qué dato sale esta caja?", 16, "#3d4654", "middle"))
    return svg(880, 530, "La misma idea de piezas y estado en cuatro superficies: navegador, Ionic, React Native y Electron.", "\n".join(body))


def pasos():
    labels = [
        ("1", "Rodea", "el boceto"),
        ("2", "Nombra", "el árbol"),
        ("3", "Quieta", "solo datos"),
        ("4", "Mínimo", "que cambia"),
        ("5", "El clic", "sube"),
    ]
    body = []
    for i, (n, a, b) in enumerate(labels):
        x = 24 + i * 172
        body.append(rrect(x, 24, 156, 110, "#fffdf8", "#2c5f94", 2, 14))
        body.append(f'<circle cx="{x+28}" cy="52" r="14" fill="#1e3a5f"/>')
        body.append(t(x + 28, 57, n, 14, "#fff", "middle", "700"))
        body.append(t(x + 52, 50, a, 15, "#1e2430", weight="700"))
        body.append(t(x + 52, 74, b, 15, "#1e2430", weight="700"))
        if i < 4:
            body.append(arrow(x + 160, 78, x + 168, 78))
    return svg(880, 156, "Cinco pasos: rodear el boceto, nombrar el árbol, imaginar la pantalla quieta, quedarse con el mínimo que cambia y subir el clic.", "\n".join(body))


def pantallas():
    cards = [
        (24, "Listado", "Muchas filas,", "una pieza repetida."),
        (242, "Detalle", "Una identidad,", "el resto son props."),
        (460, "Panel", "Varios bloques,", "cada uno con su dato."),
        (678, "Alarma", "El dato llega solo,", "la fila aparece."),
    ]
    body = [t(450, 40, "Cuatro pantallas, la misma pregunta", 22, "#1e2430", "middle", "700")]
    for x, title, a, b in cards:
        body.append(rrect(x, 70, 200, 180, "#fffdf8", "#2c5f94", 2, 14))
        body.append(t(x + 100, 116, title, 20, "#1e2430", "middle", "700"))
        body.append(t(x + 100, 160, a, 15, "#3d4654", "middle"))
        body.append(t(x + 100, 184, b, 15, "#3d4654", "middle"))
    body.append(t(450, 290, "¿De qué dato sale esta caja, y quién lo modifica?", 16, "#1e2430", "middle", "700"))
    return svg(900, 330, "Listado, detalle, panel y alarma se leen con la misma pregunta: de qué dato sale cada caja.", "\n".join(body))


def calidad():
    rows = [
        ("Mantenible", "Un cambio de significado tiene un sitio."),
        ("Rendimiento", "Cambiar una fila no redibuja la ciudad."),
        ("Teléfono", "La decisión cabe en una mano."),
        ("Acceso", "Teclado, contraste, no solo el color."),
        ("Seguridad", "El navegador es la máquina de la persona."),
    ]
    body = [t(440, 42, "Lo que se nota sin leer el código", 22, "#1e2430", "middle", "700")]
    for i, (name, sub) in enumerate(rows):
        y = 70 + i * 58
        body.append(rrect(40, y, 800, 48, "#fffdf8", "#e2dcd0", 1.5, 10))
        body.append(t(60, y + 30, name, 16, "#1e3a5f", weight="700"))
        body.append(t(250, y + 30, sub, 16, "#1e2430"))
    return svg(880, 390, "Cinco cualidades observables: mantenimiento, rendimiento, teléfono, acceso y seguridad.", "\n".join(body))


def muro():
    body = []
    body += browser_chrome(150, 20, 580, 430)
    body.append(t(440, 42, "muro de alarmas", 13, "#5c6570", "middle"))
    body.append(rrect(174, 72, 150, 32, "#d5ead6", "#2f6b3a", 1.5, 16))
    body.append(t(249, 93, "En vivo", 14, "#2f6b3a", "middle", "700"))
    body.append(t(174, 132, "Abiertas", 13, "#5c6570", weight="700"))
    body.append(rrect(174, 142, 250, 250, "#f6d5ce", "#9a4638", 2, 12))
    body.append(t(188, 166, "FilaAlarma", 12, "#9a4638", weight="700"))
    alarms = [(188, "L2 · grave · ahora"), (240, "B12 · leve · hace 4 min"), (292, "L1 · aviso · hace 9 min")]
    for y, label in alarms:
        body.append(rrect(188, y, 222, 40, "#fffdf8", "#9a4638", 1.5, 8))
        body.append(t(200, y + 25, label, 13, "#1e2430"))
    body.append(t(450, 132, "Detalle", 13, "#5c6570", weight="700"))
    body.append(rrect(450, 142, 250, 250, "#f8e6b0", "#8d6a12", 2, 12))
    body.append(t(464, 174, "DetalleAlarma", 12, "#8d6a12", weight="700"))
    body.append(t(464, 214, "L2", 22, "#1e2430", weight="700"))
    body.append(t(464, 244, "Gravedad: grave", 15, "#1e2430"))
    body.append(t(464, 270, "Vía abierta.", 15, "#3d4654"))
    body.append(t(464, 294, "El dato llegó solo.", 15, "#3d4654"))
    body.append(t(440, 490, "EstadoConexion dice si oímos. FilaAlarma se repite. El detalle es una identidad.", 16, "#3d4654", "middle"))
    return svg(880, 530, "Muro de alarmas: un letrero de conexión en vivo, una lista de filas y el detalle de la alarma elegida.", "\n".join(body))


def pliego_hueco():
    body = []
    body.append(rrect(28, 28, 824, 420, "#fffdf8", "#c9c1b4", 2, 14))
    body.append(t(52, 66, "Prescripciones técnicas", 17, weight="700"))
    body.append(t(52, 98, "El equipo, las comunicaciones, la instalación", 14, "#5c6570"))
    anchos = [620, 540, 680, 480, 600, 560, 700, 520, 640, 580, 660, 500]
    for i, w in enumerate(anchos):
        y = 114 + i * 20
        body.append(t(52, y + 10, f"R.{i + 1}", 11, "#8a8175"))
        body.append(rrect(94, y, w, 10, "#e2dcd0", "#e2dcd0", 0, 5))
    body.append(t(52, 384, "La aplicación que se ve", 14, "#5c6570"))
    body.append(t(52, 412, "R.13", 11, "#8a8175"))
    body.append(rrect(94, 396, 700, 26, "#f8e6b0", "#8d6a12", 2, 6))
    body.append(t(108, 414, "Será una aplicación web progresiva (React) y responsive.", 13))
    body.append(t(440, 486, "Mismo documento. Doce requisitos para la caja. Uno para lo único que ve el viajero.", 16, "#3d4654", "middle"))
    return svg(880, 520, "Hoja de prescripciones con doce requisitos para el equipo y uno solo para la aplicación.", "\n".join(body))


def dos_pantallas():
    body = []
    # el que se ve
    body.append(rrect(48, 56, 360, 190, "#1e2430", "#1e2430", 0, 10))
    body.append(rrect(60, 68, 336, 166, "#16222e", "#0d1620", 1.5, 6))
    body.append(t(80, 100, "Avisos", 15, "#9fb4c7"))
    for i, linea in enumerate(["Aviso en la zona 2", "Obras en el acceso norte"]):
        y = 114 + i * 42
        body.append(rrect(80, y, 290, 32, "#1e3340", "#2a4152", 1.5, 5))
        body.append(t(94, y + 21, linea, 14, "#fffdf8"))
    body.append(t(48, 286, "El que se ve", 17, weight="700"))
    body.append(t(48, 316, "Nadie se identifica.", 15, "#3d4654"))
    body.append(t(48, 340, "No hay perfiles ni permisos.", 15, "#3d4654"))
    body.append(t(48, 364, "Se valida mirándolo.", 15, "#3d4654"))
    # el que se usa
    body.append(rrect(472, 56, 360, 190, "#fffdf8", "#2c333d", 2, 10))
    body.append(rrect(472, 56, 360, 30, "#2c333d", "#2c333d", 0, 10))
    body.append(rrect(472, 72, 360, 14, "#2c333d", "#2c333d", 0, 0))
    body.append(t(652, 77, "Herramienta de gestión", 12, "#fffdf8", "middle"))
    body.append(rrect(562, 104, 180, 122, "#f3efe6", "#c9c1b4", 1.5, 8))
    body.append(t(580, 132, "Entrar", 15, weight="700"))
    body.append(rrect(580, 144, 144, 20, "#fffdf8", "#c9c1b4", 1.5, 4))
    body.append(rrect(580, 172, 144, 20, "#fffdf8", "#c9c1b4", 1.5, 4))
    body.append(rrect(580, 198, 68, 20, "#1e3a5f", "#1e3a5f", 0, 4))
    body.append(t(614, 213, "Acceder", 11, "#fffdf8", "middle", "700"))
    body.append(t(472, 286, "El que se usa para gestionarlo", 17, weight="700"))
    body.append(t(472, 316, "Usuarios, perfiles y permisos.", 15, "#3d4654"))
    body.append(t(472, 340, "Registro de quién hizo qué.", 15, "#3d4654"))
    body.append(t(472, 364, "Se valida entrando.", 15, "#3d4654"))
    body.append(rrect(48, 396, 784, 68, "#fffdf8", "#1e3a5f", 2, 12))
    body.append(t(440, 428, "Dos programas. Casi siempre se describen como uno.", 17, "#1e2430", "middle", "700"))
    body.append(t(440, 452, "Y entonces la oferta presupuesta el que se ve.", 14, "#9a4638", "middle"))
    return svg(880, 492, "Dos programas en el mismo pliego: el que se ve, sin nadie delante, y el que se usa para gestionarlo, con usuario y contraseña.", "\n".join(body))


def la_entrega():
    body = []
    # la caja que llega
    body.append(rrect(40, 56, 380, 200, "#f8e6b0", "#8d6a12", 2, 10))
    body.append(t(64, 92, "Lo que te entregan", 17, weight="700"))
    for i, (titulo, sub) in enumerate([("La receta", "el código escrito aquí"), ("La lista de la compra", "los nombres de lo demás")]):
        x = 64 + i * 172
        body.append(rrect(x, 110, 156, 120, "#fffdf8", "#8d6a12", 1.5, 6))
        body.append(t(x + 14, 138, titulo, 14, weight="700"))
        body.append(t(x + 14, 158, sub, 12, "#5c6570"))
        for j in range(4):
            body.append(rrect(x + 14, 174 + j * 14, 110 - j * 12, 6, "#e2dcd0", "#e2dcd0", 0, 3))
    # la despensa de internet
    body.append(rrect(472, 56, 368, 200, "#fffdf8", "#5c6b7a", 1.5, 12))
    body.append(t(496, 92, "La despensa está en internet", 17, weight="700"))
    body.append(t(496, 116, "Cientos de piezas hechas por otros", 13, "#5c6570"))
    for i in range(10):
        x = 496 + (i % 5) * 68
        y = 136 + (i // 5) * 58
        body.append(rrect(x, y, 52, 44, "#e7e2d8", "#8a8175", 1.5, 5))
        body.append(rrect(x + 12, y - 6, 28, 8, "#c9c1b4", "#8a8175", 1.5, 3))
    body.append(arrow(424, 150, 468, 150))
    body.append(t(440, 302, "La despensa no viene en la caja. Se baja de internet cada vez que se construye.", 16, "#3d4654", "middle"))
    body.append(rrect(40, 332, 390, 112, "#f6d5ce", "#9a4638", 2, 10))
    body.append(t(64, 366, "Dentro de dos años", 15, "#9a4638", weight="700"))
    body.append(t(64, 394, "falta un tarro, o está en otra versión.", 14, "#3d4654"))
    body.append(t(64, 418, "Lo que sale ya no es lo que te dieron.", 14, "#3d4654"))
    body.append(rrect(450, 332, 390, 112, "#d5ead6", "#2f6b3a", 2, 10))
    body.append(t(474, 366, "Lo que hay que pedir", 15, "#2f6b3a", weight="700"))
    body.append(t(474, 394, "Una copia de la despensa, en casa.", 14, "#3d4654"))
    body.append(t(474, 418, "Y montarlo una vez sin el proveedor.", 14, "#3d4654"))
    return svg(880, 476, "La caja que entrega el proveedor lleva la receta y la lista, pero la despensa vive en internet.", "\n".join(body))


def dias_seguidos():
    body = []
    pantallas = [
        ("Día 1", "3 min", "#fffdf8", "todo bien"),
        ("Día 4", "6 min", "#fffdf8", "todo bien"),
        ("Día 8", "6 min", "#f8e6b0", "el contador no baja"),
        ("Día 11", "", "#1e2430", "negro"),
    ]
    for i, (dia, valor, color, pie) in enumerate(pantallas):
        x = 28 + i * 212
        body.append(rrect(x, 40, 188, 124, "#1e2430", "#1e2430", 0, 8))
        body.append(rrect(x + 10, 50, 168, 104, "#16222e" if valor else "#0a0f14", "#0d1620", 1.5, 5))
        if valor:
            body.append(t(x + 26, 84, "Próximo paso", 12, "#9fb4c7"))
            body.append(t(x + 26, 124, valor, 28, color, weight="700"))
        body.append(t(x + 94, 190, dia, 15, "#1e2430", "middle", "700"))
        body.append(t(x + 94, 212, pie, 13, "#5c6570", "middle"))
    body.append(t(28, 264, "Memoria ocupada", 14, "#5c6570"))
    for i, h in enumerate([16, 30, 50, 66]):
        x = 28 + i * 212
        body.append(rrect(x + 60, 348 - h, 68, h, "#f6d5ce", "#9a4638", 1.5, 4))
    body.append(f'<line x1="28" y1="350" x2="852" y2="350" stroke="#c9c1b4" stroke-width="1.5"/>')
    body.append(t(440, 396, "La red funciona. El equipo está arrancado.", 16, "#3d4654", "middle"))
    body.append(t(440, 422, "Lo que lleva once días sin volver a empezar es la aplicación.", 16, "#3d4654", "middle"))
    return svg(880, 450, "Cuatro días de la misma pantalla: el contador se queda quieto y acaba en negro mientras la memoria sube.", "\n".join(body))


def pruebas_casos():
    body = []
    casos = [
        ("#2f6b3a", "#d5ead6", "Con datos", "Se ven los tres avisos.", ["Aviso en L2", "Aviso en L4", "Obras en B12"]),
        ("#6f675c", "#e7e2d8", "Sin datos", "«No hay avisos.»", []),
        ("#9a4638", "#f6d5ce", "Con error", "«No se ha podido cargar.»", []),
        ("#8d6a12", "#f8e6b0", "Un dato mal formado", "Se ven los correctos.", ["Aviso en L2", "Obras en B12"]),
    ]
    for i, (stroke, fill, titulo, frase, filas) in enumerate(casos):
        x = 28 + i * 212
        body.append(rrect(x, 40, 188, 150, "#fffdf8", stroke, 2, 10))
        body.append(rrect(x, 40, 188, 26, fill, stroke, 0, 10))
        body.append(rrect(x, 54, 188, 12, fill, fill, 0, 0))
        body.append(t(x + 94, 58, titulo, 12, "#1e2430", "middle", "700"))
        if filas:
            for j, fila in enumerate(filas):
                body.append(rrect(x + 14, 82 + j * 30, 160, 24, "#f3efe6", "#e2dcd0", 1.5, 5))
                body.append(t(x + 24, 98 + j * 30, fila, 12, "#1e2430"))
            if len(filas) == 2:
                body.append(f'<rect x="{x + 14}" y="142" width="160" height="24" rx="5" fill="none" stroke="#9a4638" stroke-width="1.5" stroke-dasharray="5 4"/>')
                body.append(t(x + 94, 158, "este se ignora", 11, "#9a4638", "middle"))
        else:
            body.append(t(x + 94, 128, frase, 13, "#5c6570", "middle"))
        body.append(t(x + 94, 216, frase if filas else "", 13, "#3d4654", "middle"))
    body.append(t(440, 282, "Cuatro pruebas por cada pantalla del inventario.", 16, "#3d4654", "middle"))
    body.append(t(440, 308, "La frase de cada caso la escribe el pliego, no el proveedor.", 16, "#3d4654", "middle"))
    return svg(880, 336, "Cuatro casos de prueba de la misma pantalla: con datos, sin datos, con error y con un dato mal formado.", "\n".join(body))


def main():
    items = {
        "evolucion.svg": evolucion(),
        "spa-vs-tradicional.svg": spa(),
        "react-en-el-mapa.svg": mapa(),
        "cuando-encaja.svg": cuando(),
        "angular-vue-react.svg": bibliotecas(),
        "taller-node.svg": build(),
        "funcion-del-dato.svg": funcion(),
        "boceto-panel.svg": boceto(),
        "cajas-componentes.svg": cajas(),
        "arbol-piezas.svg": jerarquia(),
        "props-y-estado.svg": props(),
        "actualizacion.svg": actualizacion(),
        "virtual-dom.svg": vdom(),
        "estanteria.svg": carpetas(),
        "decide-y-pinta.svg": dos_piezas(),
        "tres-recuerdos.svg": alcances(),
        "visita-de-una-pieza.svg": ciclo(),
        "fuentes.svg": fuentes(),
        "cuatro-finales.svg": desenlaces(),
        "capas.svg": capas(),
        "revision.svg": revision(),
        "alertas.svg": alertas(),
        "cuando-nace-el-html.svg": marcos(),
        "superficies.svg": superficies(),
        "cinco-pasos.svg": pasos(),
        "cuatro-pantallas.svg": pantallas(),
        "cualidades.svg": calidad(),
        "muro-alarma.svg": muro(),
        "pliego-el-hueco.svg": pliego_hueco(),
        "dos-pantallas.svg": dos_pantallas(),
        "la-entrega.svg": la_entrega(),
        "dias-seguidos.svg": dias_seguidos(),
        "pruebas-cuatro-casos.svg": pruebas_casos(),
    }
    for name, content in items.items():
        save(name, content)
        print(name, len(content))


if __name__ == "__main__":
    main()
