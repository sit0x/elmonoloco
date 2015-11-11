#!/usr/bin/env python
# coding: utf-8
import pilasengine

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        texto = self.pilas.actores.Texto(u"ELIJA UNA OPCION")
        self._aplicar_animacion(texto)

        self.pilas.fondos.Fondo('data/monointro.png')
        #Creo botones del Menu
        boton = self.pilas.interfaz.Boton("Comenzar Juego")
        boton.x = -70
        boton.y = -150
        boton.conectar(self._arrancar_Nivel_1)
        boton1 = self.pilas.interfaz.Boton("Nivel 1")
        boton1.x = -150
        boton1.y = -200
        boton1.conectar(self._arrancar_Nivel_1)
        boton2 = self.pilas.interfaz.Boton("Nivel 2")
        boton2.conectar(self._arrancar_Nivel_2)
        boton2.x = 150
        boton2.y = -200
        boton2.conectar(self._arrancar_Nivel_2)
        boton3 = self.pilas.interfaz.Boton("Ayuda")
        boton3.x = 70
        boton3.y = -150
        boton3.conectar(self._volver)
        self.pilas.actores.Sonido()
    #Comienza el Nivel 1
    def _arrancar_Nivel_1(self):
        self.pilas.escenas.EscenaJuego()
    #Comienza el Nivel 2
    def _arrancar_Nivel_2(self):
        self.pilas.escenas.EscenaJuego2()
    #Vuelve hacia atras
    def _volver(self):
        self.pilas.escenas.EscenaAyuda()
    #Animacion del texto
    def _aplicar_animacion(self, texto):
        texto.y = -450
        texto.escala = 6
        texto.color = 'amarillo'
        texto.escala = [1], 4
        texto.y = [-200], 1
