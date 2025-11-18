label esc_7C:

    scene bg estudioNoche with fade

    n "La tensión persiste, pero el ambiente se ha vuelto más íntimo."
    n "La lámpara del escritorio lanza un círculo cálido sobre la mesa."
    n "Scott se sienta frente a Tessie, que aún tiembla."

    n "Él se inclina lentamente y toma sus manos. Su voz es baja, serena, cargada de cansancio."

    show sc1 at left
    sc "Respira, Tessie."
    sc "Cierra los ojos un momento."
    sc "Déjame contarte algo."

    n "Tessie obedece, respirando hondo."

    n "Scott busca palabras que puedan apartarla, aunque sea por un instante, de la sombra que los rodea."

    sc "Imagina un lugar donde la ciudad no está vigilada."
    sc "Donde las calles son libres y la gente camina sin miedo."
    sc "Antes de la invasión, hubo días así."
    sc "El aire era claro."
    sc "El arte respiraba."
    sc "La vida no necesitaba permiso."

    n "Tessie exhala lentamente. Su cuerpo, tenso hasta hace un momento, comienza a relajarse."
    n "Los temblores ceden."

    sc "Los parques eran tranquilos."
    sc "Había risas en los mercados."
    sc "Y la pintura… la pintura tenía luz propia."
    sc "La libertad era posible."

    n "Tessie lo escucha, con los ojos cerrados."
    n "Por un momento, su rostro parece en paz. El miedo se repliega."

    sc "(voz firme, afectuosa) Lo ves, Tessie. Por ahora estás a salvo. Estoy aquí."

    n "El silencio vuelve. Pero ya no es hostil, sino humano."
    n "Fuera, el viento mueve los estandartes del régimen."
    n "Dentro, la calma recupera su lugar por un instante."

    call esc_8C from _call_esc_8C
    call esc_9C from _call_esc_9C
    call esc_10C from _call_esc_10C

    # Escena 11 tiene bifurcación
    call esc_11C from _call_esc_11C

    if path11 == 1:
        # → Buscar a Tessie
        jump esc_12C_1
    else:
        # → Ir a la iglesia
        jump esc_12C_2

    return
