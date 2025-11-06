# script_prologo.rpy
# Primeras 5 escenas de la novela (Branch 3) — Ren'Py

# ---------- CONFIG & CHARAS ----------
define sc = Character("Scott", color="#89b4fa")
define te = Character("Tessie", color="#f5c2e7")
define n  = Character(None)        # narrador

# (Reemplazá estos nombres de archivos por tus assets reales)
image bg studio_day    = "bg/studio_day.jpg"
image bg plaza_haze    = "bg/plaza_haze.jpg"
image bg iglesia_atrio = "bg/iglesia_atrio.jpg"
image bg estudio_noche = "bg/studio_night.jpg"

# Opcional: un retrato/pose si ya tenés sprites
# image te neutral = "char/tessie_neutral.png"
# image sc neutral = "char/scott_neutral.png"

# Música / ambientes (poné tus propios .ogg/.mp3 en game/audio/)
# Si no tenés aún los archivos, dejalos comentados.
# define audio.amb_city   = "audio/amb_city.ogg"
# define audio.amb_studio = "audio/amb_studio.ogg"
# define audio.amb_war    = "audio/amb_war_distant.ogg"
# define audio.theme       = "audio/theme_intro.ogg"

# ---------- PREFERENCIAS RÁPIDAS ----------
default preferences.text_cps = 50
define config.rollback_enabled = True

# ---------- INICIO ----------
label start:
    # (Opcional) Música de tema general
    # play music audio.theme fadein 1.0

    call escena_1
    call escena_2
    call escena_3
    call escena_4
    call escena_5

    n "Fin del bloque de introducción (escenas 1–5)."
    return

# ---------- ESCENA 1: El estudio ----------
label escena_1:
    scene bg studio_day with fade
    # play ambient audio.amb_studio fadein 1.5
    n "La bruma se mezcla con el humo de las fábricas y los estandartes del régimen sobre los tejados."
    n "Desde la ventana, Scott escucha motores blindados y el paso mecánico de botas sobre adoquines."
    n "Recuerdos del frente oriental le laten adentro como una furia concentrada."
    sc "…Tessie, tomá la pose un momento."
    n "El caballete permanece vacío, pero la ciudad parece colarse en los colores antes de nacer."
    n "Por un instante, una sombra con rostro blando y abultado se proyecta sobre el lienzo, allá en el atrio de la iglesia."
    # show sc neutral at center
    sc "Que no nos alcance el gris de afuera…"
    return

# ---------- ESCENA 2: Recuerdo de la batalla y retorno al estudio ----------
label escena_2:
    scene bg plaza_haze with dissolve
    # play ambient audio.amb_war fadein 1.0
    n "{i}Nieve manchada de sangre. Tanques. Gritos. Órdenes ciegas. Una guerra que devora todo lo vivo.{/i}"
    n "Scott recuerda la noche en que desertó. Cuerpos, barro… y la culpa pegada a la piel."
    # stop ambient fadeout 1.0
    scene bg studio_day with fade
    # play ambient audio.amb_studio fadein 1.0
    n "Abre los ojos. El estudio. El humo gris persiste."
    n "En el atrio de la iglesia, un hombre inmóvil con uniforme gris y rostro hinchado."
    sc "(No es solo un funcionario. Es la opresión hecha carne.)"
    return

# ---------- ESCENA 3: Primera aparición del agente y efecto sobre la pintura ----------
label escena_3:
    scene bg iglesia_atrio with fade
    n "El hombre permanece quieto, impregnando el aire con tensión."
    scene bg studio_day with dissolve
    n "Scott vuelve al caballete. Tessie retoma la pose."
    te "¿He hecho algo malo?"
    sc "No… arruiné este brazo. No sé cómo se contaminó así."
    n "La piel en el lienzo se vuelve amarillenta, corrupta, como si absorbiera la sombra del agente."
    te "¡Qué color tan horrible! ¿Mi carne parece queso putrefacto?"
    sc "Claro que no. ¿Alguna vez me viste pintar así?"
    te "Nunca. Debe de ser el aguarrás… o algo."
    n "Scott frota con aguarrás; la mancha se extiende como gangrena."
    te "(Ríe nerviosa) ¡Vas a romper los pinceles como un niño!"
    n "La ciudad y el estudio se funden en una sola tensión silenciosa."
    return

# ---------- ESCENA 4: La pintura bajo la sombra del agente ----------
label escena_4:
    scene bg studio_day with fade
    n "Tessie posa; el lienzo exhala tonos enfermos que absorben la luz."
    te "No entiendo… Tu pintura se ve {i}horrible{/i}."
    sc "No es tu culpa. Es la luz, el calor… y la sombra de ese hombre allá afuera."
    te "¿El del atrio?"
    sc "Es como si absorbiera la vida de todo alrededor."
    n "Scott frota la tela, pero la corrupción crece. La figura se vuelve translúcida bajo la luz gris."
    te "¿Le parece que mi piel está… podrida?"
    sc "No. Nunca pinté así."
    n "Tessie apoya la cabeza en su hombro; el estudio respira miedo contenido."
    n "Scott presiente que la siguiente revelación vendrá de ella: el sueño, la premonición."
    return

# ---------- ESCENA 5: El sueño y la premonición de Tessie ----------
label escena_5:
    scene bg estudio_noche with fade
    # stop ambient fadeout 0.5
    # play ambient audio.amb_city fadein 1.0
    n "El humo del cigarrillo de Tessie gira perezoso en el aire."
    te "Scott… debo contarte un sueño. O algo más: una premonición."
    te "Era invierno. Escuché campanas. La calle, vacía y más oscura de lo habitual."
    te "Un golpeteo sobre los adoquines… un carro blindado del régimen."
    te "Dentro, un hombre trajeado con el rostro en sombras. Sentí un miedo helado."
    te "Capturaron a alguien. Y al conductor… lo reconocí. Como el hombre del atrio."
    te "Y usted estaba allí, atrapado, sin poder moverse."
    n "La pintura enferma, la ciudad vigilada y el recuerdo de la guerra se superponen al relato."
    te "No es solo un sueño. Es una premonición. Algo se acerca… Siento que el Signo Amarillo no está lejos."
    sc "…Debemos tener cuidado."
    n "El miedo y la alerta se instalan en silencio, uniendo la herida del frente con la visión de Tessie."
    return
