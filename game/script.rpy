# =====================================================
#  Control general del prólogo — SOLO FLUJO
# =====================================================

default branch = 0          # Recuerdo elegido en Escena 1
default subbranch = 0       # Decisión en Escena 6
default path11 = 0          # Elección en Escena 11
default choice23 = 0        # Elección/timeout en Escena 23


label start:

    call esc_1          # → jugador elige branch (1,2,3)

    if branch == 1:
        call esc_2A
    elif branch == 2:
        call esc_2B
    elif branch == 3:
        call esc_2C

    call esc_3
    call esc_4
    call esc_5

    # En Escena 6 el jugador elige subbranch (1 / 2.1 / 2 / 3)
    call esc_6

    # =============== Ramas desde ESC.6 ==================

    if subbranch == 1:
        jump esc_7A
    elif subbranch == 21:
        jump esc_7B
    elif subbranch == 2:
        jump esc_7
    elif subbranch == 3:
        jump esc_7C

    return



# =====================================================
#   FLUJO RAMA 1 (subbranch = 1)
# =====================================================

label esc_7A:
    call esc_8A
    call esc_9A
    call esc_10A
    call esc_11A

    # Final rama 1 (lineal)
    call esc_12A
    call esc_13A
    return



# =====================================================
#   FLUJO RAMA 2.1 (subbranch = 21)
# =====================================================

label esc_7B:
    call esc_8B
    call esc_9B
    call esc_10B
    call esc_11B

    # Final rama 2.1 (lineal)
    call esc_12B
    call esc_13B
    return



# =====================================================
#   FLUJO RAMA 2 (subbranch = 2)
# =====================================================

label esc_7:
    call esc_8
    call esc_9
    call esc_10
    call esc_11

    # Final rama 2 (lineal)
    call esc_12
    call esc_13
    return



# =====================================================
#   FLUJO RAMA 3 (subbranch = 3)
# =====================================================

label esc_7C:
    call esc_8C
    call esc_9C
    call esc_10C

    # Escena 11 tiene bifurcación
    call esc_11C

    if path11 == 1:
        # → Buscar a Tessie
        jump esc_12C_1
    else:
        # → Ir a la iglesia
        jump esc_12C_2



# -----------------------------------------------------
#  SUBRAMA 3A — Scott va al hospedaje de Tessie
# -----------------------------------------------------

label esc_12C_1:
    call esc_13C_1
    call esc_14C_1
    call esc_15C_1
    call esc_16C_1
    call esc_17C_1
    call esc_18C_1
    call esc_19C_1
    call esc_20C_1
    call esc_21C_1
    call esc_22C_1

    # Escena 23C_1 tiene decisión por tiempo
    call esc_23C_1

    if choice23 == 1:
        # Jugador NO hizo nada (timeout o elección)
        jump esc_24C_1A
    elif choice23 == 2:
        # Jugador la detuvo
        jump esc_24C_1B

    return


# ----- Continuación — NO HACER NADA -----
label esc_24C_1A:
    call esc_25C_1A
    call esc_26C_1A
    call esc_27C_1A
    call esc_28C_1A
    call esc_29C_1A
    call esc_30C_1A
    return

# ----- Continuación — DETENERLA -----
label esc_24C_1B:
    call esc_25C_1B
    call esc_26C_1B
    call esc_27C_1B
    call esc_28C_1B
    call esc_29C_1B
    call esc_30C_1B
    return



# -----------------------------------------------------
#  SUBRAMA 3B — Scott va a la iglesia
# -----------------------------------------------------

label esc_12C_2:
    call esc_13C_2
    call esc_14C_2
    call esc_15C_2
    call esc_16C_2
    call esc_17C_2
    call esc_18C_2
    call esc_19C_2
    call esc_20C_2
    call esc_21C_2
    call esc_22C_2
    call esc_23C_2
    call esc_24C_2
    call esc_25C_2
    call esc_26C_2
    call esc_27C_2
    call esc_28C_2
    call esc_29C_2
    call esc_30C_2
    return



# =====================================================
#  cada label más abajo contendrá solo el contenido
# =====================================================
