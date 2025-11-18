# =====================================================
# CHARACTERS.RPY — PERSONAJES PRINCIPALES (ESC. 1–6)
# Project: El Signo Amarillo (Visual Novel)
# =====================================================

# -----------------------------------------------------
# NARRADOR
# -----------------------------------------------------

define n = Character(
    None,                      # No se muestra nombre
    what_color = "#e6e6e6",    # Color del texto del narrador
    window_yalign = 0.85       # Ubicación del cuadro de texto
)


# -----------------------------------------------------
# PERSONAJES PRINCIPALES
# -----------------------------------------------------

define sc = Character(
    "Scott",
    color = "#89b4fa",
    what_prefix = "«",
    what_suffix = "»"
)

define te = Character(

    "Tessie",
    color = "#f5c2e7",
    )

define th = Character(
    "Thomas",
    color = "#a6d189",
)


# -----------------------------------------------------
# OPCIONAL — PARA FUTUROS TEXTOS (Libro, documentos)
# -----------------------------------------------------

define doc = Character(
    None,
    what_color = "#f9ffb5",
    what_prefix = "«",
    what_suffix = "»"
)
