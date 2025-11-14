label esc_11:

    scene bg studio_day with fade

    n "La bruma cubre la ciudad como una tela húmeda."
    n "El sol apenas se adivina entre los estandartes del régimen."
    n "El aire tiene el mismo tono gris que las calles."

    n "Scott y Thomas observan la plaza desde la ventana."
    n "Los transeúntes cruzan con lentitud, envueltos en el silencio rutinario del control."
    n "El rumor de pasos y campanas lejanas flota entre los edificios."

    n "Tessie no ha aparecido. Su ausencia pesa en la mirada de Scott."

    sc "(para sí) No ha llegado todavía… Supongo que se entretuvo en su apartamento."

    th "(asintiendo) Quizá, señor. La mañana avanza rápido… y con tanto que investiga, podría haberse distraído."

    n "Scott asiente, sin convicción. El silencio los rodea."
    n "Solo se oye el sonido apagado de un carro lejano, y el roce del viento sobre las banderas."

    n "Scott cierra los ojos. Respira hondo."
    n "La bruma parece entrar en el estudio, mezclándose con el olor a pintura y papel."

    n "La inquietud crece. Debe decidir."

    n "La ausencia de Tessie lo llama a actuar. Hay dos caminos posibles."

    # --- DECISIÓN PRINCIPAL DE LA RAMA ---
    menu:
        "Ir a buscar a Tessie a su hospedaje":
            jump esc_12C1

        "Ir a la iglesia para investigar la ausencia y la sombra del atrio":
            jump esc_12C2

    return
