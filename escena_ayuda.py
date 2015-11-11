#!/usr/bin/env python
# coding: utf-8
import pilasengine

'''Esta Clase muestra las intrucciones del jueg'''
class EscenaAyuda(pilasengine.escenas.Escena):
    "Es la escena que da instrucciones de como jugar."

    def iniciar(self):

        self.mensaje_ayuda = """
        En Mono Loco:
        Tenes que poder lograr comer 20 bananas
        sin tocar las bombas o que ellas te toquen.
        Para poder ayudar al mono a comer BANANAS,
        tenes que deslizar al MONO por la pantalla.
        Como? Haces click y  mantenes presionado
        mientras lo arrastras!"""
        self.pilas.fondos.Fondo('data/monopensativo.png')
        self.x = 10
        self.y = 50
        self.crear_texto_ayuda(self.x, self.y, self.mensaje_ayuda)

        self.help_message = '''Tene en cuenta que el mono crece
        al comer las bananas'''
        self.x = 10
        self.y = -130

        self.crear_texto_ayuda(self.x, self.y, self.help_message)

    def crear_texto_ayuda(self, x, y, mensaje_ayuda):
        titulo = self.pilas.actores.Texto(mensaje_ayuda)
        titulo.x = x
        titulo.y = y
        titulo.color = 'amarillo'
        self.pilas.avisar("Haga click para volver al Menu Principal")
        self.pilas.eventos.click_de_mouse.conectar(self._avanzar)

    def _avanzar(self, evento):
        self.pilas.escenas.EscenaMenu()
