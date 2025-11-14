label esc_6:

    scene bg estudiooche with fade

    n "El humo flota pesado sobre la mesa."
    n "El aire huele a aguarrás y miedo."
    n "La pintura, todavía húmeda, refleja un brillo enfermo bajo la luz del farol."

    n "Tessie aparta la cabeza y apoya las manos sobre la mesa."
    n "Tiembla. Sus ojos húmedos relucen a la luz tenue."
    n "La respiración se acelera, entrecortada."

    te "¡No puedo…! Siento que algo terrible va a pasar…"

    show sc1:
        xalign 0.2
        yalign 1.0
        alpha 0.0
        linear 1.0 alpha 1.0
    sc "(voz baja) Tranquila, Tessie…"

    n "Scott comprende que debe actuar antes de que la ansiedad la consuma."

    scene black with fade

    n "¿Cómo debería Scott calmarla?"


    # ============================
    # MENU DE CALMA — DESBLOQUEADO POR BRANCH
    # ============================

    menu:

        # ---- SOLO BRANCH 1 ----
        "Recomendar a Tessie salir de la ciudad unos días. (BRANCH 1)" if branch == 1:
            $ subbranch = 1
            jump post_esc6

        # ---- SOLO BRANCH 2.1 ----
        "Invitarla a tomarse un tiempo junto a la ventana, con algo de tabaco. (BRANCH 2.1)" if branch == 2:
            $ subbranch = 21
            jump post_esc6

        # ---- SOLO BRANCH 2 ----
        "Recomendarle pasar unos días en el campo; transmitirle serenidad y apoyo. (BRANCH 2)" if branch == 2:
            $ subbranch = 2
            jump post_esc6

        # ---- SOLO BRANCH 3 ----
        "Contarle la historia de un país sin represión. (BRANCH 3)" if branch == 3:
            $ subbranch = 3
            jump post_esc6

    return


label post_esc6:

    if subbranch == 1:
        n "Scott, con voz contenida, le sugiere a Tessie que abandone la ciudad unos días..."

    elif subbranch == 21:
        n "Scott la guía hacia la ventana, dejándole un cigarrillo para estabilizar el temblor..."

    elif subbranch == 2:
        n "Scott le propone pasar unos días en el campo, lejos del gris y las patrullas..."

    elif subbranch == 3:
        n "Scott empieza a contarle la historia de un país sin represión…"

    return
