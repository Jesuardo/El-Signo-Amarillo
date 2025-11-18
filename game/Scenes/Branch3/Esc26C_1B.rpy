label esc_26C_1B:

    scene bg ciudad_lluvia_bruma_noche with fade
    play ambient "amb_lluvia_bruma.ogg" fadein 1.5

    n "La lluvia caía en hilos finos sobre los adoquines de la ciudad ocupada, transformando cada farol en un haz difuso de luz amarillenta que apenas atravesaba la bruma extendida sobre las calles."

    n "Scott y Tessie avanzaban pegados a las paredes, sus pasos casi inaudibles bajo el ruido constante del agua."
    n "Cada sombra parecía un vigilante, cada eco de ruedas o botas sonaba como una advertencia."

    show te1 at right
    te "“Nunca había sentido algo así… Es como si toda la ciudad nos observara.”"

    sc "«La ciudad no perdona. Todo lo que vimos hoy… cualquier paso en falso podría costarnos caro. Tenemos que mantenernos invisibles.»"

    play sound "pasos_mojados.ogg"
    n "Doblaron una esquina. El apartamento del artista surgió entre la bruma, sus ventanas dejando escapar una luz amarilla tenue."

    scene bg apartamento_artista_exterior_noche
    play sound "puerta_madera.ogg"
    n "Scott empujó la puerta. El crujido de la madera se confundió con el murmullo de la lluvia."

    scene bg apartamento_artista_interior_noche with fade
    stop ambient fadeout 1.0
    play ambient "amb_interiores_lluvia.ogg" fadein 1.0

    n "Entraron sin hablar. El interior olía a madera húmeda y aceite viejo. El goteo que caía del techo marcaba un ritmo irregular, mezclándose con el sonido del viento filtrándose por las rendijas."

    play sound "objeto_caer_suave.ogg"
    n "Tessie dejó caer su mochila junto a la mesa. Sus manos temblaban, la mirada perdida en el reflejo del cristal empañado."

    show sc1 at left
    sc "«Estamos a salvo… por ahora.»"

    n "Su voz sonó hueca, como si dudara incluso al pronunciarla."

    n "La luz de la lámpara tembló sobre las paredes. Las sombras parecían moverse con independencia, siguiendo el pulso de la lluvia."

    sc "«Pero esta noche… no termina aquí.»"

    te "“Scott…”"

    n "Tessie lo miró, el rostro pálido, los ojos abiertos, entendiendo que el peligro no se había ido, solo había cambiado de forma."

    n "La lluvia seguía golpeando los cristales, amplificando el silencio entre ellos."

    n "Fuera, la ciudad respiraba. Dentro, el miedo los mantenía despiertos."

    n "Scott dejó escapar un suspiro, una mezcla de impotencia y determinación."

    n "Sabía que la noche sería larga, y que el pasado prohibido que habían tocado no los dejaría descansar."

    scene black with fade
    return
