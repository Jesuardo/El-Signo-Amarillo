label esc_25C_1A:

    scene bg hospedaje_noche with fade

    n "El aire vibró."
    n "Un crujido recorrió el piso de madera, seguido por el sonido seco de las ruedas metálicas deteniéndose frente a la puerta."

    n "Un instante después, el golpe."

    # SFX sugerido: golpe de puerta
    # play sfx audio.sfx_puerta_golpe

    n "La madera cedió."
    n "Las botas entraron al cuarto, marcando el ritmo exacto de la amenaza."

    n "La lámpara tembló."
    n "Su luz proyectó sombras que se alargaban por las paredes, retorciéndose sobre los símbolos dorados del libro."

    # Scott sigue oculto
    show sc at left
    n "Scott, oculto tras el armario, vio cómo la puerta se abría del todo."
    hide sc 

    n "Su respiración se detuvo."
    n "No podía moverse. No podía emitir un sonido."

    show te at right 

    n "Tessie retrocedió, el libro todavía entre sus manos."
    n "Su rostro, iluminado por la luz trémula, mezclaba miedo y una obstinación casi febril."

    # Agentes entrando
    # show ag at center (si más adelante tenés el sprite)
    n "Los agentes cruzaron la habitación."
    n "El ruido del metal y el cuero se mezcló con el zumbido eléctrico de la lámpara."

    n "Uno de ellos la alcanzó."
    n "El empujón la lanzó contra la mesa."

    # SFX sugerido: golpe
    # play sfx audio.sfx_golpe_cuerpo

    n "El golpe fue seco, brutal."
    n "Un trozo de madera se quebró bajo su cuerpo."

    n "Tessie cayó de lado."
    n "Un corte profundo se abrió en su muñeca y su costado."
    n "La sangre comenzó a correr, lenta, densa, goteando sobre el suelo y sobre las páginas abiertas del libro amarillo."

    hide te 

    n "Scott la vio caer."
    n "Su cuerpo se inclinó un poco hacia adelante, como si fuera a moverse."
    n "Pero no lo hizo."

    n "El miedo lo había paralizado por completo."
    n "Sus labios se abrieron, pero ningún sonido salió."

    n "El Signo en la tapa del libro reflejó un brillo vivo, una pulsación que recorrió el aire."

    n "La bruma del exterior se coló por la ventana rota, mezclándose con el humo de la lámpara."

    n "Los agentes se detuvieron un segundo, sus linternas temblando sobre las paredes cubiertas de símbolos."
    n "La luz dorada parecía multiplicarse, moviéndose sola, respirando."

    n "Scott comprendió, sin palabras, que lo que veía no era solo el régimen irrumpiendo en su escondite."
    n "Era el Signo Amarillo manifestándose, desplegándose a través de ellos, de Tessie, del aire, de su culpa."

    n "El resplandor aumentó."

    n "El silencio fue absoluto."

    # Tessie final
    show te at right
    n "Tessie, aún en el suelo, sostuvo el libro una última vez."
    n "Su cuerpo tembló."
    hide te 

    n "Después, cayó quieta."

    # Lámpara apagándose
    n "La lámpara parpadeó tres veces"

    # Podés animarlo así si querés:
    # $ renpy.pause(0.4)
    # $ renpy.pause(0.4)
    # $ renpy.pause(0.4)

    n "y se apagó."

    scene black with fade

    return
