label esc_25C_1B:

    scene bg hospedaje_noche_bruma with fade
    play ambient "amb_bruma_noche.ogg" fadein 1.0

    n "La penumbra se volvió más densa cuando una sombra se deslizó desde la puerta entreabierta."

    play sound "pasos_madera_suaves.ogg"
    n "Un agente del régimen apareció sin ruido, sus botas resonando apenas sobre el piso de madera húmeda, pero cada paso parecía amplificarse en el silencio del cuarto."

    n "Scott y Tessie permanecían agazapados, ocultos detrás del caballete, conteniendo la respiración."
    n "Cada músculo de Scott estaba rígido; sabía que un solo sonido los condenaría."

    show agent_shadow at center 
    n "El agente avanzó con calma. Su silueta, recortada contra la luz del pasillo, se movía con la precisión de quien ya conoce el terreno."

    n "Se detuvo ante la mesa. Sus ojos se posaron en el libro amarillo, el volumen que contenía un fragmento del pasado que el régimen había decidido borrar."

    play sound "objeto_recogido.ogg"
    n "Con un gesto preciso, lo levantó. La lámpara reflejó el dorado de la cubierta sobre su rostro, y por un instante, pareció comprender el peso de lo que sostenía."

    n "Fue entonces cuando vio el broche con el Signo, abandonado junto al libro."
    play sound "metal_suave.ogg"
    n "Lo tomó con cuidado, sus dedos rozando el metal grabado, como si también lo reconociera."

    n "Scott sintió un escalofrío subirle por la espalda."
    n "Cada símbolo, cada línea del Signo, era una palabra prohibida, una memoria viva del pasado que no debía existir."

    n "El agente se enderezó, sus movimientos lentos, controlados. No habló."
    n "Solo observó el cuarto en silencio, como un depredador asegurándose de que la presa no respirara."

    hide agent_shadow 
    play sound "pasos_pasillo.ogg"
    n "Después, giró sobre sus talones y desapareció en la bruma del pasillo."
    n "El eco de sus pasos se perdió entre los muros."

    # Tessie respira
    play sound "exhalacion.ogg"
    te "..."

    n "Solo entonces Tessie soltó el aire que contenía, un suspiro leve, tembloroso."

    # Scott ayuda a Tessie
    n "Scott la tomó del brazo y la guió hasta el centro del cuarto."
    n "La lámpara parpadeaba, proyectando la sombra del caballete sobre la pared."

    n "El libro y el broche ya no estaban."
    n "Pero el peligro seguía allí, intacto, invisible, respirando con ellos."

    sc "«Lo han visto… y saben lo que significa.»"
    sc "«Ahora, más que nunca, debemos ser cautelosos.»"

    n "Tessie asintió, los ojos fijos en la puerta, aún brillando con miedo y fascinación."

    n "Afuera, la ciudad vigilada continuaba su marcha, y la noche apenas comenzaba."

    scene black with fade
    return
