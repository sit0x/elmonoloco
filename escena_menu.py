#!/usr/bin/env python
# coding: utf-8
import pilasengine

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        texto = self.pilas.actores.Texto(u"ELIJA UNA OPCION")
        self._aplicar_animacion(texto)

        self.pilas.fondos.Fondo('data/monointro.png')

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
        #self.crear_texto_ayuda()
    #def crear_texto_ayuda(self):
        #titulo = self.pilas.actores.Texto(u"pulsa ESC para volver")
        #titulo.y = 250
        #self.pilas.avisar("pulsa ESC para volver a Ayuda")

        #self.pilas.eventos.click_de_mouse.conectar(self._volver)
        #self.pilas.eventos.pulsa_tecla_escape.conectar(self._volver)



    def _arrancar_Nivel_1(self):
        self.pilas.escenas.EscenaJuego()

    def _arrancar_Nivel_2(self):
        self.pilas.escenas.EscenaJuego2()

    def _volver(self):
        self.pilas.escenas.EscenaAyuda()

    def _aplicar_animacion(self, texto):
        texto.y = -450
        texto.escala = 6
        texto.color = 'amarillo'
        texto.escala = [1], 4
        texto.y = [-200], 1
