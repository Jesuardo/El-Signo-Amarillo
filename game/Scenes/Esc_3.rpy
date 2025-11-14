# =====================================================
# ESCENA 3 — ESTUDIO DE SCOTT / ATRIO DE LA IGLESIA
# =====================================================

label esc_3:

    scene bg estudio_tessie_pintada with fade

    
    n "Desde la ventana, Scott observa la plaza."
    
    n "Apoyado contra el atrio, un hombre permanece inmóvil."
    n "Su rostro, abultado y grisáceo, parece hecho de cera muerta."
    n "El uniforme del régimen lo oprime, como si la vida misma se hubiera rendido bajo la tela."

    n "El aire se vuelve pesado."
    n "La bruma se mezcla con el humo de las fábricas."
    n "Nada se mueve, pero todo parece observado."

    n "Scott aparta la vista."
    n "Vuelve al caballete."

    # Tessie posando
    n "Hace una seña a Tessie, que posa en silencio bajo la luz gris que entra por la ventana."

    play sound audio.sfx_pinta
    n "Trabaja unos minutos."
    n "La brocha avanza con ritmo contenido, pero algo empieza a fallar:"

    n "Los tonos que antes eran cálidos se apagan."
    n "La piel de Tessie se torna amarillenta, enfermiza."
    n "Cada trazo absorbe la tensión del aire, la presión del hombre que vigila desde el atrio."

    n "Scott se detiene, irritado."
    n "Mira el lienzo, incrédulo."

    # Diálogo
    
    te "¿He hecho algo malo?"

    play sound audio.sfx_cigarrillo
    n "Enciende un cigarrillo y lo observa con recelo."

    show sc1:
            xalign 0.2
            yalign 1.0
            alpha 0.0
            linear 1.0 alpha 1.0
    sc "No… he estropeado este brazo. No sé cómo pude contaminar la pintura así."

    te "¿No es culpa mía, verdad?"

    sc "No, es mía."

    n "Tessie baja la cabeza."

    n "Scott aplica trapo y aguarrás sobre la tela."
    play sound audio.sfx_pintura
    n "Cuanto más frota, más la pintura parece enfermar."
    n "La figura se pudre, los colores se mezclan, la luz desaparece."
    n "El lienzo parece absorber la corrupción misma de la ciudad."

    n "Scott se detiene, tenso."

    sc "(murmura) Debe de ser el aguarrás… o la sombra de ese hombre."

    n "Tessie se inclina sobre su silla, el humo del cigarrillo flotando entre ellos."

    te "¡Qué color tan horrible! ¿Le parece que mi carne parece queso putrefacto?"

    sc "No, claro que no. ¿Me has visto alguna vez pintar así?"

    te "¡Por supuesto que no!"

    sc "Entonces…"

    te "Debe de ser el aguarrás, o algo."

    play sound audio.sfx_suspiro  
    n "Scott suspira."
    n "Hundido en frustración, aprieta los pinceles contra la tela hasta deformarla."
    n "De su boca escapa una maldición que apenas se oye."

    sc "(exacerbado): ¡Muy bonito! ¡Arruina tus pinceles como un niño! Lleva semanas trabajando, y ahora mira… ¿¡de qué sirve!?" 
    
    play sound audio.sfx_telaRomper
    n "Scott desgarra el lienzo"

    n "Tessie no responde."
    n "El aire vibra, como si la ciudad respirara dentro del estudio."

    play sound audio.theme_policia
    n "El ruido lejano de las patrullas se mezcla con el roce del trapo."

    n "En el ventanal, la silueta del hombre del atrio sigue allí, fija, vigilante."

    n "La guerra, la vigilancia y la furia se funden en una sola imagen:"
    n "el lienzo enfermo,"
    n "la ciudad controlada,"
    n "la mente de Scott contaminada."

    scene black with fade
    stop ambient fadeout 1.0

    return
