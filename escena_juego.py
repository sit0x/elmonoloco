#!/usr/bin/env python
# coding: utf-8
import pilasengine
import random

cantidad_puntos = 0

class EscenaJuego(pilasengine.escenas.Escena):

    def iniciar(self):
        #Fondo
        self.pilas.fondos.Fondo('data/jungla.png')
        #Texto y animaciones
        self.texto = self.pilas.actores.Texto('NIVEL 1')
        self._aplicar_animacion(self.texto)
        self.pilas.avisar("Arrastrar al mono con el mouse y ayudalo a ganar")
        #Listas
        self.bananas = []
        self.bananas_comidas = []
        self.bombas = []

        #Cantidad de bananas y bombas a crear
        self.cantidad_de_bananas = 20
        self.cantidad_de_bombas = 4
        #Creo actor Mono Loco
        self.mono = self.pilas.actores.Mono()
        self.mono.escala = 0.5
        self.mono.x = 280
        self.mono.y = 0
        self.mono.radio_de_colision = 30
        #Habilidades del mono
        self.mono.aprender(self.pilas.habilidades.Arrastrable)
        self.mono.aprender(self.pilas.habilidades.LimitadoABordesDePantalla)

        #Creo el actor puntaje
        self.puntos = self.pilas.actores.Puntaje(x=230, y=200,
                                                    color=self.pilas.colores.rojo)
        self.puntos.magnitud = 40

        self.pilas.actores.Sonido()
        #Agrego bananas a comer
        self.pilas.tareas.agregar(1, self._crear_banana)

        #Agrego 1 bomba cada 1 segundo y hasta llegar a ser 4
        self.pilas.tareas.agregar(0.3, self._crear_bomba)
        #Agrego colisiones
        self.pilas.colisiones.agregar(self.mono, self.bananas, self.comer_banana)
        self.pilas.colisiones.agregar(self.mono, self.bombas, self.hacer_explotar_una_bomba)
    '''Crea las bananas enemigas de manera random'''
    def _crear_banana(self):
        for i in range(self.cantidad_de_bananas):
            #Creo actor banana
            banana = self.pilas.actores.Banana()
            #Aumento escala y radio de colisión
            banana.escala = 1
            banana.radio_de_colision = 20
            #Creo banana enemiga de manera random
            banana.x = random.randrange(-250, +220)
            banana.y = random.randrange(-220, +200)
            #Agrego banana enemiga
            self.bananas.append(banana)

    '''Crea las bombas enemigas de manera random y con movimiento'''
    def _crear_bomba(self):
        self.counter_bomber = 0
        for i in range(self.cantidad_de_bombas):
            self.counter_bomber += 1

            bomba = self.pilas.actores.Bomba()
            bomba.escala = 0.8
            bomba.radio_de_colision = 18
            bomba.aprender("PuedeExplotar")

            if self.counter_bomber == 1:
                self.y = -130
                self.x = 40
                bomba.x = [40,-40]*100,2.5
            elif self.counter_bomber == 2:
                self.y = 130
                self.x = 40
                bomba.x = [-40,40]*100,2.5
            elif self.counter_bomber == 3:
                self.y = -150
                self.x = -200
                bomba.y = [150,-150]*100,2.5
            elif self.counter_bomber == 4:
                self.y = 0
                self.x = 200
                bomba.y = [-150,150]*100,2.5

            #Seteo la ubicación
            bomba.y = self.y
            bomba.x = self.x
            #Agrego a la lista bomba enemiga
            self.bombas.append(bomba)

    '''Metodo que se ejecuta cada vez que se come una banana'''
    def comer_banana(self, mono, banana):
        '''Controlo la cantidad de bananas comidas para saltar BUG del juego
        y poder aumentar radio de colision y escala sin alterar mal el puntaje'''
        if banana not in self.bananas_comidas:
            self.bananas_comidas.append(banana)
            mono.escala = self.mono.escala + 0.01
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
            self.pilas.escenas.EscenaGanar(self.puntos.obtener())


    def hacer_explotar_una_bomba(self,mono, bomba):
        bomba.explotar()
        self.mono.gritar()
        self.mono.eliminar()
        self.pilas.tareas.eliminar_todas()
        self.pilas.escenas.EscenaPerder(self.puntos.obtener(), '1')

    def _aplicar_animacion(self, texto):
        texto.y = -500
        texto.escala = 4
        texto.escala = [1], 2
        texto.y = [-180], 1
