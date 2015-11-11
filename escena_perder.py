#!/usr/bin/env python
# coding: utf-8
import pilasengine
import random

class EscenaPerder(pilasengine.escenas.Escena):
    def iniciar(self, puntaje, nivel):
        self.pilas.fondos.Fondo('data/monolosepng.png')

        mensaje = "PERDISTE! Hiciste {} puntos.".format(puntaje)
        self.texto = self.pilas.actores.Texto(mensaje)
        self.nivel = nivel
        boton = self.pilas.interfaz.Boton("Volver a intentarlo")
        boton.y = 200
        boton.x = 250
        #Conecto al nivel que corresponda
        boton.conectar(self._action_)

    def _action_(self):
        if self.nivel == '1':
            self.pilas.escenas.EscenaJuego()
        else:
            self.pilas.escenas.EscenaJuego2()
