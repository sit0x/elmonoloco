#!/usr/bin/env python
# coding: utf-8
import pilasengine
import escena_ayuda
import escena_menu
import escena_juego
import escena_juego2
import escena_ganar
import escena_perder
import escena_ganar_juego
pilas = pilasengine.iniciar()


# Vinculamos las escenas
pilas.escenas.vincular(escena_ayuda.EscenaAyuda)
pilas.escenas.vincular(escena_menu.EscenaMenu)
pilas.escenas.vincular(escena_juego.EscenaJuego)
pilas.escenas.vincular(escena_juego2.EscenaJuego2)
pilas.escenas.vincular(escena_ganar.EscenaGanar)
pilas.escenas.vincular(escena_ganar_juego.EscenaGanarJuego)
pilas.escenas.vincular(escena_perder.EscenaPerder)

# Definimos como escena inicial al menú
pilas.escenas.EscenaMenu()

pilas.ejecutar()
