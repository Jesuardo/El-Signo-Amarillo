# =====================================================
# ESCENA 2C — BRANCH 3
# RECUERDO DEL FRENTE ORIENTAL
# =====================================================

label esc_2C:

    # Entrar al recuerdo
    scene black 
    play sound audio.sfx_transicion

    n "Scott cierra los ojos."
    n "El murmullo de la ciudad se disuelve, y el sonido de la bruma da paso a un eco distante: la nieve helada del frente oriental."

    scene bg flashback  



    play sound audio.amb_guerra_distant
    n "El paisaje es blanco, interminable."
    n "La tierra está teñida de rojo; el barro pegajoso se mezcla con la sangre."
    n "Los tanques avanzan lentamente, chirriando como animales de hierro."
    n "Los fusiles resuenan como un coro de muerte."

    n "Los gritos —de oración, de furia, de desesperación— se confunden con el rugido del viento."
    n "Scott está allí, entre los cuerpos que caen uno tras otro, sin rostro, sin nombre."

    n "La nieve se vuelve fango, el fango se vuelve tumba."
    n "En su pecho crece algo oscuro: furia."

    n "Odio hacia el régimen que ha mandado a esos hombres al sacrificio,"
    n "odio hacia los oficiales que gritan órdenes ciegas,"
    n "odio hacia la guerra que devora todo lo vivo."

    n "Recuerda la noche en que desertó."
    n "El frío. Los cuerpos."
    n "La decisión."

    n "Dos ojos vacíos de los caídos, ni las voces rotas que todavía lo llaman en sueños."

    # Regreso al presente
    play sound audio.sfx_transicion
    scene bg estudio1 with fade

    play sound audio.sfx_motor
    n "El sonido de los motores blindados lo trae de vuelta. El recuerdo se disuelve lentamente."
    n "Scott abre los ojos."

    n "Está otra vez en su estudio."
    n "El humo gris cubre la ciudad."
    n "Los estandartes ondean."
    n "La sensación de horror persiste, flotando sobre las calles vigiladas."

    n "Frente a él, el caballete vacío."
    n "El lienzo parece esperarlo, pero los colores están contaminados por la memoria y la furia."
    n "Nada de lo que pinte podrá escapar de esa sombra."

    # El agente
    scene bg atrio_iglesia_agente 

    n "Fuera, algo se mueve."
    n "Scott se inclina."
    n "En el atrio de la iglesia, un hombre inmóvil, vestido con uniforme gris, lo observa."
    n "Su rostro es hinchado, blando, casi inhumano."

    n "Por un instante, los dos mundos se superponen:"
    n "la guerra y la vigilancia,"
    n "el pasado y el presente."

    n "El hombre parece un eco del frente,"
    n "un recordatorio vivo de la opresión,"
    n "de la muerte,"
    n "de la obediencia impuesta."

    # Vuelta al estudio
    scene bg estudio1 

    n "Scott apaga su cigarrillo."
    n "No aparta la vista."

    n "El silencio vuelve a llenar el estudio."

    scene black with fade
    stop ambient fadeout 1.0

    return
