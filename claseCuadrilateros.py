import pygame
import time
import random

#Dimensiones display (1200, 750)

class Cuadrilateros:
    def __init__(self, largo, ancho, movimiento_x, movimiento_y, posicion_x, posicion_y):
        self.largo = largo
        self.ancho = ancho
        self.movimiento_x = movimiento_x
        self.movimiento_y = movimiento_y
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y



Bola = Cuadrilateros(20,20,0,0,200,200)
Borde_Superior = Cuadrilateros(20,1000,0,0,10,10)
Borde_Inferior = Cuadrilateros(20,1000,0,0,10,650)
Paleta_Player1 = Cuadrilateros(150,25,0,0,50,300)
Paleta_Player2 = Cuadrilateros(150,25,0,0,1000,300)
Paleta1Dual_player1 = Cuadrilateros(150,25,0,0,50,250)
Paleta2Dual_player1 = Cuadrilateros(150,25,0,0,50,350)
Paleta1Dual_player2 = Cuadrilateros(150,25,0,0,1000,250)
Paleta2Dual_player2 = Cuadrilateros(150,25,0,0,1000,350)
