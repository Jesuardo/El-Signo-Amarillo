default branch = 0
default subbranch = 0
default path11 = 0
default choice23 = 0   


label start:

    call esc_1
    if branch == 1:
        call esc_2A
    elif branch == 2:
        call esc_2B
    else:
        call esc_2C

    call esc_3
    call esc_4
    call esc_5
    call esc_6

    # Subrama desde Escena 6
    if subbranch == 1:
        call esc_7A
        call esc_8A
        
    elif subbranch == 21:
        call esc_7B
        call esc_8B
        
    elif subbranch == 2:
        call esc_7
        call esc_8
        
    elif subbranch == 3:
        call esc_7C
        call esc_8C
        call esc_9C
        call esc_10C

        call esc_11C

        if path11 == 1:
            call esc_12C_1
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

            call esc_23C_1

            if choice23 == 1:
                call esc_24C_1A
                call esc_25C_1A
                
            else:
                call esc_24C_1B
                call esc_25C_1B
                
        else:
            call esc_12C_2
            