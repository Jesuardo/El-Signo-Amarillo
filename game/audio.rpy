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
define audio.theme_main        = "audio/bgm/ambientacion_tensa.ogg"
define audio.theme_introduccion= "audio/bgm/intro_misterioso_oscuro.ogg"
define audio.theme_tension     = "audio/bgm/tension_corta.ogg"
define audio.theme_hojas_volando="audio/bgm/hojas_volando.ogg"
define audio.theme_hojas_pasando="audio/bgm/pasaje_hojas_papel.ogg"
define audio.theme_policia     = "audio/bgm/sirenas_lejanas.ogg"
define audio.theme_tension     = "audio/bgm/tension_corta.ogg"
define audio.theme_vendabal    = "audio/bgm/viento-ciudad.ogg"
define audio.theme_ventisca    = "audio/bgm/viento_frio.ogg"


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
define audio.amb_guerra_distant ="audio/sfx/amb_guerra_distant.mp3"

# -----------------------------------------------------
# EFECTOS DE SONIDO (SFX)
# -----------------------------------------------------
define audio.sfx_abrazo         = "audio/sfx/abrazo.mp3"
define audio.sfx_minecraft      = "audio/sfx/campana_minecraft.mp3"
define audio.sfx_chillido       = "audio/sfx/chillido_puerta.mp3"
define audio.sfx_cigarrillo     = "audio/sfx/encender_cigarrillo.mp3"
define audio.sfx_auto_fallando  = "audio/sfx/fallo_arranque_auto.mp3"
define audio.sfx_impactante     = "audio/sfx/impactante.mp3"
define audio.sfx_perro          = "audio/sfx/jesus.mp3"
define audio.sfx_libro_cerrado  = "audio/sfx/libro_cerrar.mp3"
define audio.sfx_fallo_motor    = "audio/sfx/malfuncionamiento_motor.mp3"
define audio.sfx_llanto_mujer   = "audio/sfx/mujer_llorando.mp3"   # Efecto asociado al Signo Amarillo
define audio.sfx_agente_escalera= "audio/sfx/pasos_escalera_agente.mp3"
define audio.sfx_disparos       = "audio/sfx/peloton_fusilamiento.mp3"
define audio.sfx_pinta          = "audio/sfx/pintando.mp3"
define audio.sfx_pintura        = "audio/sfx/pintando2.mp3"
define audio.sfx_caminata       = "audio/sfx/pisadas_genericos_tierra.mp3"
define audio.sfx_abrir          = "audio/sfx/puerta_abriendose.mp3"
define audio.sfx_cerrar         = "audio/sfx/puerta_cerrandose.mp3"
define audio.sfx_respiracion    = "audio/sfx/respiracion_pesada.mp3"
define audio.sfx_recuerdo_guerra= "audio/sfx/tiroteo_guerra.mp3"
define audio.sfx_transicion     = "audio/sfx/transicion.mp3"
define audio.sfx_campana        = "audio/sfx/un_golpe_campana.mp3"
define audio.sfx_auto           = "audio/sfx/viaje_Auto.mp3"
define audio.sfx_motor          = "audio/sfx/motor.mp3"
define audio.sfx_suspiro        = "audio/sfx/suspiro.mp3"
define audio.sfx_tessieRisa     = "audio/sfx/tessie_risa.mp3"
define audio.sfx_telaRomper     = "audio/sfx/tela_romper.mp3" 
define audio.sfx_botas          = "audio/sfx/botas.mp3"
# -----------------------------------------------------
# EFECTOS ESPECIALES (USO RARO)
# -----------------------------------------------------
define audio.fx_distorsion      = "audio/fx_distorsion.mp3"
define audio.fx_hum_signo       = "audio/fx_hum_signo.mp3"          # Murmullo subgrave del Signo
define audio.fx_rumble_low      = "audio/fx_rumble_low.mp3"
define audio.fx_memory_echo     = "audio/fx_memory_echo.mp3"        # Para recuerdos / flashbacks

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

#ME LA RE COMO