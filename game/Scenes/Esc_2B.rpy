# =====================================================
# ESCENA 1 — EL ESTUDIO DE SCOTT (TARDE BRUMOSA)
# =====================================================

label esc_1:

    # --- Ambiente inicial ---
    play ambient audio.amb_bruma fadein 1.0

    # --- Fondo del estudio ---
    scene bg estudio_day with fade

    # --- Inicio de la narración ---
    n "La bruma cubre la ciudad."

    n "El humo de las fábricas se eleva entre los tejados, donde los estandartes del régimen ondean rígidos, sin color."

    n "Cada bocina, cada patrulla, cada sombra de soldado que cruza la plaza parece recordarle a todos que la ciudad respira bajo control."

    n "El aire huele a carbón, acero caliente y aceite quemado."

    # Scott en la ventana
    n "Scott permanece inmóvil, apoyado sobre el alféizar de la ventana de su estudio."
    n "Sus manos descansan sobre la piedra fría."
    n "Desde allí observa la plaza, las calles desiertas, los edificios envueltos en humo."

    n "La luz gris se refleja en el vidrio, deformando su rostro."
    n "Todo parece detenido."

    # Sonido de blindados
    play sound audio.sfx_blindado
    n "A lo lejos, se escuchan los motores de los vehículos blindados patrullando el perímetro."
    play sound audio.sfx_botas
    n "El eco metálico de las botas resuena entre los adoquines."

    n "El viento golpea el vidrio, arrastrando polvo y hollín."

    # Caballete
    n "Frente a él, el caballete vacío."
    n "La tela blanca lo espera."
    n "Scott no pinta. Solo observa."

    n "Piensa en Tessie y en cómo la ciudad podría filtrarse incluso en los colores: los trazos manchados de obediencia, la pintura infectada por la tensión del aire."

    n "Sus ojos recorren la plaza una vez más."
    n "Las patrullas avanzan lentamente, exactas, como un mecanismo sin alma."

    # Aparición espectral
    n "Por un instante, la sombra de un hombre de rostro blando y abultado se proyecta sobre el lienzo."
    n "Scott parpadea; la figura desaparece."

    # Cigarrillo
    play sound audio.sfx_fosforo
    n "Saca un cigarrillo. Lo enciende."
    n "La llama tiembla y el humo asciende, mezclándose con la neblina exterior."

    sc "Nada escapa de esto."

    n "Permanece allí, apoyado en el alféizar."
    n "El humo lo rodea, se funde con la bruma."
    n "Por un momento, él mismo parece disolverse dentro de ese aire gris, vigilado e inevitable."

    n "El silencio pesa."
    n "La ciudad respira."

    # Corte final
    scene black with fade
    stop ambient fadeout 1.0

    return
