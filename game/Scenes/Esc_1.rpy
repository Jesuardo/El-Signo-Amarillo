# =====================================================
# ESCENA 1 – EL ESTUDIO DE SCOTT – TARDE BRUMOSA
# =====================================================

label esc_1:

    scene bg escena1

    n "La bruma cubre la ciudad."
    n "El humo de las fábricas se eleva entre los tejados, donde los estandartes del régimen ondean rígidos, sin color."

    n "Cada bocina, cada patrulla, cada sombra de soldado que cruza la plaza parece recordarle a todos que la ciudad respira bajo control."
    n "El aire huele a carbón, acero caliente y aceite quemado."

    n "Scott permanece inmóvil, apoyado sobre el alféizar de la ventana de su estudio."
    
    show sc1 at left
    n "Sus manos descansan sobre la piedra fría."

    n "Desde allí observa la plaza, las calles desiertas, los edificios envueltos en humo."
    n "La luz gris se refleja en el vidrio, deformando su rostro."
    n "Todo parece detenido."

    play sound audio.sfx_motor
    n "A lo lejos, se escuchan los motores de los vehículos blindados patrullando el perímetro."

    play sound audio.sfx_botas
    n "El eco metálico de las botas resuena entre los adoquines."

    play sound audio.theme_ventisca
    n "El viento golpea el vidrio, arrastrando polvo y hollín."

    n "Frente a él, el caballete vacío."
    n "La tela blanca lo espera."
    n "Scott no pinta. Solo observa."

    n "Piensa en Tessie y en cómo la ciudad podría filtrarse incluso en los colores:"
    n "los trazos manchados de obediencia, la pintura infectada por la tensión del aire."

    n "Sus ojos recorren la plaza una vez más."
    n "Las patrullas avanzan lentamente, exactas, como un mecanismo sin alma."

    n "Por un instante, la sombra de un hombre de rostro blando y abultado se proyecta sobre el lienzo."
    n "Scott parpadea; la figura desaparece."

    play sound audio.sfx_cigarrillo
    n "Saca un cigarrillo. Lo enciende."
    n "La llama tiembla y el humo asciende, mezclándose con la neblina exterior."

    #poner imagen de scott
    sc "Nada escapa de esto."

    n "Permanece allí, apoyado en el alféizar."
    n "El humo lo rodea, se funde con la bruma."
    n "Por un momento, él mismo parece disolverse dentro de ese aire gris, vigilado e inevitable."

    n "El silencio pesa."
    n "La ciudad respira."

    # CORTE A NEGRO
    scene black with fade
    stop ambient fadeout 1.0

    # ===========================================
    # DECISIÓN DE LOS 3 RECUERDOS
    # ===========================================

    n "Scott cierra los ojos. Algo intenta abrirse paso desde la memoria."

    menu:
        n "¿Qué logra recordar?"

        "Nada. Reprimir el recuerdo. (Branch 1)":
            $ branch = 1

        "La infancia en los bosques bretón. (Branch 2)":
            $ branch = 2

        "El frente oriental: la nieve y la deserción. (Branch 3)":
            $ branch = 3

    return
