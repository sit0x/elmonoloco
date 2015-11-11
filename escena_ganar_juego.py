#!/usr/bin/env python
# coding: utf-8
import pilasengine
import random
class EscenaGanarJuego(pilasengine.escenas.Escena):
    def iniciar(self,puntaje):

        if puntaje == 20:


            self.pilas.fondos.Fondo('data/monoganajuego8.png')
            mensaje = "GANASTE TODOS LOS NIVELES! Hiciste {} puntos.".format(puntaje)
            self.texto = self.pilas.actores.Texto(mensaje)
            self.texto.color = self.pilas.colores.amarillo
            self.texto.y = -220
            menu = self.pilas.interfaz.Boton("volver al Menu")
            menu.y = 200
            menu.x = 250
            menu.conectar(self._volver_)

            salir = self.pilas.interfaz.Boton("Salir")
            salir.y = 160
            salir.x = 250
            salir.conectar(self._salir_)

    def _volver_(self):
        self.pilas.escenas.EscenaMenu()

    def _salir_(self):
        self.pilas.terminar()
