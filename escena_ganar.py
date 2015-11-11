#!/usr/bin/env python
# coding: utf-8
import pilasengine
import random
'''Escena que se muestra al ganar el nivel 1'''
class EscenaGanar(pilasengine.escenas.Escena):
    def iniciar(self,puntaje):

        if puntaje == 20:
            #Fondo
            self.pilas.fondos.Fondo('data/monogana.png')
            #Texto
            mensaje = "PASASTE DE NIVEL! Hiciste {} puntos.".format(puntaje)
            self.texto = self.pilas.actores.Texto(mensaje)

            self.contador = 10
            #Temporizador
            self.reloj = self.pilas.actores.Texto('Comenzara el nivel 2 en 10')
            self.reloj.color = self.pilas.colores.amarillo
            self.reloj.y = -100
            self.reloj.x = -10
            self.paso_un_segundo = self.pilas.evento.Evento(['x', 'y'])
            self.paso_un_segundo.conectar(self.avanzar_segundero)
            self.pilas.tareas.siempre(1, self.funcion_pasa_un_segundo)

    '''Evento cada un segundo'''
    def funcion_pasa_un_segundo(self):
        self.paso_un_segundo.emitir(argumento1=1, argumento2=0)

    '''Temporizador para comenzar el nivel 2'''
    def avanzar_segundero(self, evento):
        self.contador -= 1
        self.reloj.texto = 'Comenzara el nivel 2 en ' + str(self.contador)

        if self.contador == 0:
            self.pilas.escenas.EscenaJuego2()
