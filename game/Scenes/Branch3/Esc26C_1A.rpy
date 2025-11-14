label esc_26C_1A:

    scene bg hospedaje_noche with fade

    n "Tessie cayó de rodillas."
    n "El libro amarillo seguía entre sus manos, los dedos resbalando con la sangre."
    n "Su respiración era corta, rota, cada exhalación un hilo que se extinguía en el aire cargado de humo y polvo."

    n "Scott avanzó lentamente desde las sombras."
    n "No podía hablar. El miedo y la culpa le apretaban la garganta."
    n "Solo observaba, impotente."

    # El agente aparece
    # show ag at center (cuando tengas sprite)
    n "Un agente se acercó."
    n "Su silueta recortada contra la luz del pasillo parecía más una sombra que un hombre."

    n "Sin decir una palabra, le arrancó de las manos el libro,"
    n "lo sostuvo unos segundos bajo la luz trémula"
    n "y luego se lo guardó bajo el abrigo."

    show te_confusa at right with dissolve
    n "Tessie intentó moverse, pero el dolor la doblegó."
    n "Su otra mano buscó su pecho, donde llevaba prendido el broche con el signo."

    n "El agente la tomó del cuello de la blusa,"
    n "arrancó el broche con un tirón seco,"
    n "y el sonido metálico del cierre se perdió entre los pasos y la respiración entrecortada de ella."

    hide te_confusa with dissolve

    n "Scott dio un paso hacia adelante, pero se detuvo."
    n "Las botas del agente resonaron contra el suelo, y el eco del metal pareció llenarlo todo."

    show te at right with dissolve
    n "Tessie lo miró una última vez."
    n "Su rostro estaba pálido, sus ojos abiertos, llenos de comprensión y resignación."
    hide te with dissolve

    n "El agente se apartó sin mirarla."
    n "Salió al pasillo."
    n "El sonido de las ruedas metálicas del carro volvió a oírse, alejándose entre la bruma."

    # Scott se acerca a Tessie
    n "Scott se quedó quieto unos segundos, mirando el hueco que la ausencia dejaba."
    n "Después, avanzó."
    n "Sus pasos fueron lentos, vacilantes."

    show sc_tenso at left with dissolve
    n "Se inclinó junto a ella."
    n "El suelo estaba frío."
    n "El aire olía a hierro, tinta y miedo."

    n "La tocó apenas, sus dedos manchados de rojo."
    n "El silencio era total."

    sc "(en un murmullo) Tessie…"

    n "Sus labios temblaron, pero no dijo más."

    hide sc_tenso with dissolve

    n "Se levantó despacio."
    n "Miró hacia la puerta abierta, hacia el pasillo vacío donde la niebla se mezclaba con el humo del régimen."

    n "Dio un paso fuera del cuarto."
    n "Su sombra se perdió entre la bruma."

    n "El Signo Amarillo en la pared —pintado con la sangre y la luz que quedaba— pareció observarlo partir."

    scene black with fade

    return
