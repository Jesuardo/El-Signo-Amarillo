# =====================================================
# AUDIO.RPY — DEFINICIÓN DE MÚSICAS, AMBIENTES Y SFX
# Proyecto: EL SIGNO AMARILLO (Novel Visual)
# =====================================================

# -----------------------------------------------------
# NOTA IMPORTANTE:
# Todos los archivos deben estar en:
# game/audio/
# Ejemplo:
# game/audio/amb_studio.ogg
# game/audio/theme_main.ogg
# -----------------------------------------------------

# -----------------------------------------------------
# MÚSICA (BGM)
# -----------------------------------------------------
define audio.theme_main        = "audio/bgm/ambientacionTensa.ogg"
define audio.theme_signo       = "audio/bgm/introMisteriosoOscuro.ogg"
define audio.theme_tension     = "audio/bgm/tensionCorta.ogg"
define audio.theme_suspenso    = "audio/bgm/hojasVolando.ogg"
define audio.theme_misterio    = "audio/bgm/pasajeHojasPapel.ogg"
define audio.theme_recuerdo    = "audio/bgm/sirenasLejanas.ogg"
define audio.theme_guerra      = "audio/bgm/tensionCorta.ogg"
define audio.theme_si          = "audio/bgm/vientoCiudad.ogg"
define audio.theme_no          = "audio/bgm/vientoFrio.ogg"


# -----------------------------------------------------
# AMBIENTES (AMB)
# -----------------------------------------------------
define audio.amb_studio_day    = "audio/amb_studio_day.ogg"
define audio.amb_studio_night  = "audio/amb_studio_night.ogg"
define audio.amb_city          = "audio/amb_city.ogg"
define audio.amb_city_heavy    = "audio/amb_city_heavy.ogg"
define audio.amb_plaza_haze    = "audio/amb_plaza_haze.ogg"
define audio.amb_rain_soft     = "audio/amb_rain_soft.ogg"
define audio.amb_rain_hard     = "audio/amb_rain_hard.ogg"
define audio.amb_church_inside = "audio/amb_church_inside.ogg"
define audio.amb_church_empty  = "audio/amb_church_empty.ogg"
define audio.amb_guerra_distant = "audio/amb_guerra_distant.ogg"

# -----------------------------------------------------
# EFECTOS DE SONIDO (SFX)
# -----------------------------------------------------
define audio.sfx_door_creak     = "audio/sfx/abrazo.ogg"
define audio.sfx_door_knock     = "audio/sfx/campanaMinecraft.ogg"
define audio.sfx_step_stone     = "audio/sfx/chillidoPuerta.ogg"
define audio.sfx_step_wood      = "audio/sfx/encenderCigarrillo.ogg"
define audio.sfx_paper_rustle   = "audio/sfx_paper_rustle.ogg"
define audio.sfx_cig_light      = "audio/sfx_cig_light.ogg"
define audio.sfx_match_strike   = "audio/sfx_match_strike.ogg"
define audio.sfx_metal_gate     = "audio/sfx_metal_gate.ogg"
define audio.sfx_chain_clank    = "audio/sfx_chain_clank.ogg"
define audio.sfx_symbol_resonar = "audio/sfx_symbol_resonar.ogg"   # Efecto asociado al Signo Amarillo
define audio.sfx_boom_distant   = "audio/sfx_boom_distant.ogg"
define audio.sfx_heartbeat      = "audio/sfx_heartbeat.ogg"
define audio.sfx_tension_hit    = "audio/sfx_tension_hit.ogg"

# -----------------------------------------------------
# EFECTOS ESPECIALES (USO RARO)
# -----------------------------------------------------
define audio.fx_distorsion      = "audio/fx_distorsion.ogg"
define audio.fx_hum_signo       = "audio/fx_hum_signo.ogg"          # Murmullo subgrave del Signo
define audio.fx_rumble_low      = "audio/fx_rumble_low.ogg"
define audio.fx_memory_echo     = "audio/fx_memory_echo.ogg"        # Para recuerdos / flashbacks

# -----------------------------------------------------
# FUNCIONES RECOMENDADAS (OPCIONAL)
# -----------------------------------------------------
# Podés llamar a estas funciones desde cualquier escena
# para un manejo más elegante del audio.

python early:
    def play_music(track, fadein=1.0):
        renpy.music.play(track, channel="music", loop=True, fadein=fadein)

    def stop_music(fadeout=1.0):
        renpy.music.stop(channel="music", fadeout=fadeout)

    def play_amb(track, fadein=1.0):
        renpy.music.play(track, channel="ambient", loop=True, fadein=fadein)

    def stop_amb(fadeout=1.0):
        renpy.music.stop(channel="ambient", fadeout=fadeout)

    def sfx(track):
        renpy.music.play(track, channel="sfx", loop=False)

# -----------------------------------------------------
# EJEMPLOS DE USO (ELIMINAR SI QUERÉS EL ARCHIVO MÁS LIMPIO)
# -----------------------------------------------------
# play_music(audio.theme_signo, fadein=2.0)
# play_amb(audio.amb_studio_day)
# sfx(audio.sfx_door_creak)
# stop_music(1.5)
# stop_amb(1.0)

