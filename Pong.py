print("Hola")
#Comentario
print (2*2)
 
def hola(a):
	print ("hola")

class Juego:
	marcador_1 = 0
	marcador_2 = 0
	tablero = []
	dificultad = 1
	modo_juego = True

	def __init__(self, marcador_1, marcador_2, tablero, dificultad, modo_juego):
		self.marcador_1 = marcador_1
		self.marcador_2 = marcador_2
		self.tablero = tablero
		self.dificultad = dificultad
		self.modo_juego = modo_juego

	def gana_punto(self, posicion_x, posicion_y):
		if posicion_x > 1119:
			marcador_2 += 1
		if posicion_y < 10:
			marcador_1 += 1

	def ganador(self, marcador_1, marcador_2):
		if marcador_1 == 7 or marcador_2 == 7:
			posicion_y = 375
			posicion_x = 600
			marcador_1 = 0
			marcador_2 = 0
			dificultad = 2
			print ("Felicidades")
	
	def escoger_dificultad(self, dificultad):
		dificultad = dificultad



