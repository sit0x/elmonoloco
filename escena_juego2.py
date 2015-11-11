#!/usr/bin/env python
# coding: utf-8
import pilasengine
import random

class EscenaJuego2(pilasengine.escenas.Escena):

    def iniciar(self):
        self.pilas.fondos.Fondo('data/selva2.png')
        self.texto = self.pilas.actores.Texto('NIVEL 2')
        #Aplico animación al texto
        self._aplicar_animacion(self.texto)
        self.pilas.avisar("Arrastrar al mono con el mouse y ayudalo a ganar")
        self.bananas = []
        self.bombas = []
        self.cantidad_de_bombas = 4
        self.cantidad_de_bananas = 20
        self.bananas_comidas = []

        self.mono = self.pilas.actores.Mono()
        self.mono.escala = 0.5
        self.mono.x = 280
        self.mono.y = 0
        self.mono.radio_de_colision = 30
        self.mono.aprender(self.pilas.habilidades.Arrastrable)
        self.mono.aprender(self.pilas.habilidades.LimitadoABordesDePantalla)
        self.puntos = self.pilas.actores.Puntaje(x=230, y=200,
                                                    color=self.pilas.colores.rojo)

        self.puntos.magnitud = 40
        #self.puntos.definir(cantidad_puntos)
        self.pilas.actores.Sonido()
        self.pilas.tareas.agregar(1, self._crear_banana)
        #Agrego 1 bomba cada 1 segundo y hasta llegar a ser 4
        self.pilas.tareas.agregar(0.3, self._crear_bomba)
        #Agrego colisiones
        self.pilas.colisiones.agregar(self.mono, self.bananas, self.comer_banana)
        self.pilas.colisiones.agregar(self.mono, self.bombas, self.hacer_explotar_una_bomba)

        self.fin_de_juego = False
    '''Crea bananas enemigas de manera random, limitando la cantidad para que el mono
    no pueda comer bananas sin moverse.'''
    def _crear_banana(self):
        for i in range(self.cantidad_de_bananas):
            banana = self.pilas.actores.Banana()
            banana.escala = 1
            banana.radio_de_colision = 20
            banana.x = random.randrange(-250, +220)
            banana.y = random.randrange(-220, +200)
            self.bananas.append(banana)
    '''Crea las bombas enemigas de manera random'''
    def _crear_bomba(self):
        for i in range(self.cantidad_de_bombas):
            bomba = self.pilas.actores.Bomba()
            bomba.escala = 0.8
            bomba.radio_de_colision = 18
            bomba.aprender("PuedeExplotar")
            x = random.randrange(-250, 240)
            y = random.randrange(-240, 240)

            if x >= 0 and x <= 100:
                x = 50
            elif x <= 0 and x >= -100:
                x = -50

            if y >= 0 and y <= 100:
                y = 70
            elif y <= 0 and y >= -100:
                y = -70


            bomba.x = [x, y]*100,2
            bomba.y = [y, x]*100,2.5
            self.bombas.append(bomba)


    '''Éste método es utilizado cada vez que el mono come una banana. Aumenta
    la escala y el radio de colisión, aparte de otros eventos que posee el mono.'''
    def comer_banana(self, mono, banana):
        '''Controlo la cantidad de bananas comidas para saltar BUG del juego
        y poder aumentar radio de colision y escala sin alterar mal el puntaje'''
        if banana not in self.bananas_comidas:
            self.bananas_comidas.append(banana)
            mono.escala = self.mono.escala + 0.02
            radio = self.mono.escala * 50
            self.mono.radio_de_colision = radio
            self.puntos.escala = 0
            self.pilas.utils.interpolar(self.puntos, 'escala', 1, duracion=0.5)
            self.puntos.aumentar(1)
        #Elimino banana
        banana.eliminar()
        #Eventos del Mono Loco
        self.mono.rotacion = [30, -30,0]
        self.mono.sonreir()
        self.mono.decir("Quiero Mas")
        #Si llega a los 20 puntos, gana el juego
        if self.puntos.obtener() == 20:
            self.pilas.escenas.EscenaGanarJuego(self.puntos.obtener())
    '''Si el mono toca una bomba, entra en acción este método llevándote
    a la escena Perder'''
    def hacer_explotar_una_bomba(self,mono, bomba):
        bomba.explotar()
        self.mono.gritar()
        self.mono.eliminar()
        self.pilas.tareas.eliminar_todas()
        self.pilas.escenas.EscenaPerder(self.puntos.obtener(), '2')
    '''Método para aplicar animación al texto'''
    def _aplicar_animacion(self, texto):
        texto.y = -500
        texto.escala = 4
        texto.escala = [1], 2
        texto.y = [-180], 1
