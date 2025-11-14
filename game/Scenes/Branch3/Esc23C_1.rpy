label esc_23C_1:

    scene bg hospedaje_noche with fade

    n "El interior del armario trasero estaba envuelto en oscuridad y polvo."
    n "Las perchas se balanceaban apenas, y el olor a lavanda vieja se mezclaba con el aire húmedo."
    n "Scott y Tessie permanecían inmóviles, respirando lo menos posible."

    n "El silencio era tan espeso que cada exhalación parecía delatarlos."

    n "Afuera, las ruedas metálicas del carro crujían sobre los adoquines, cada movimiento más cercano que el anterior."
    n "El chirrido de un engranaje recorrió el pasillo como una amenaza contenida."

    te "(susurrando, apenas audible) Scott… Van a entrar. Si ven lo que hemos estado leyendo…"

    sc "(voz baja, seca) Lo sé."

    n "El haz de una linterna se filtró por la rendija del armario, dibujando una línea pálida en la madera."

    n "A través de esa franja, Tessie alcanzó a ver la mesa, el libro amarillo aún abierto y el pequeño broche con el signo brillando débilmente."
    n "El reflejo los observaba. Cada símbolo parecía esperar."

    te "(en un hilo de voz) No pueden verlo. Tengo que sacarlo."

    n "Scott apretó las manos contra sus rodillas. No respondió. No se movió."
    n "Solo cerró los ojos, como si eso bastara para hacerla desaparecer."

    n "Tessie lo miró por última vez. No había reproche, solo una certeza muda."

    n "Se deslizó fuera del armario, con movimientos lentos, medidos."
    n "El abrigo rozó el suelo."

    n "Scott permaneció quieto en la oscuridad, el miedo apretándole el pecho, incapaz de intervenir."

    n "Desde su rincón solo veía el resplandor del libro, y la sombra de Tessie avanzando hacia él."

    n "Afuera, los pasos del régimen se detuvieron junto a la puerta."

    n "Un golpe seco. El metal resonó en el piso de arriba."

    n "Scott contuvo la respiración."
    n "El silencio era absoluto. Solo el roce de las telas del armario, y el pulso en sus sienes."

    n "Tessie estiró la mano."
    n "El dorado del libro reflejó su movimiento, como si el objeto la reconociera."

    n "Scott, en la sombra, no hizo nada."
    n "Ni una palabra."
    n "Ni un gesto."
    n "Solo esperó, sabiendo que, al no actuar, acababa de decidir."

    # -----------------------------
    # DECISIÓN POR TIEMPO — 30s
    # -----------------------------
    menu:
        "Detenerla — intervenir antes de que toque el libro":
            $ choice23 = 2
            jump esc_24C_1B

        "No hacer nada":
           
            $ choice23 = 1
            jump esc_24C_1A

    return

label esc_24C_1_auto:
    jump esc_24C_1A
