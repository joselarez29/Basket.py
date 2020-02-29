global lista
lista=list()


class jugador():		
	Nombre=""
	Dorsal=""
	canastas=0
	faltas=0
	rebotes=0
	asistencias=0

def registro():
	H=jugador()

	H.Nombre=raw_input('Ingrese el nombre del jugador')
	H.Dorsal=raw_input ('Ingrese el Dorsal del jugador')
	H.canastas= raw_input('Ingrese las canastas del Jugador')
	H.faltas= raw_input('Ingrese la cantidad de Faltas hechas')
	H.rebotes= raw_input('Ingrese la cantidad de Rebotes')
	H.asistencias= raw_input('Ingrese las Asistencias')

	lista.append(H)

def datos():
	print('Datos del juego')

		for H in lista:
			print H.Nombre,'-'H.Dorsal,'-'H.canastas,'-'H.faltas,'-'H.rebotes,'-'H.asistencias 


def buscarjugador():
	print('Buscar Jugador')
		añadir= raw_input('ingrese el Dorsal del jugador')

			for H in lista:
				if H.Dorsal==añadir or H.Nombre==añadir:
					print H.Nombre,'-'H.Dorsal,'-'H.canastas,'-'H.faltas,'-'H.rebotes,'-'H.asistencias 

def salir()
	print('Gracias por utilizar el programa')


def Menu()
	op=0
		while op!= 4
		print 'Programa para registro de un Juego de Basket'
		print 'Menu\n 1)- registro de juego\n 2)- datos de juego\n 3)- buscar jugador\n 4)- salir '
		op=input('ingrese una opcion')
				if op==1:
					registro()
				elif op==2:
					buscarjugador()
				elif op==3:
					salir()
				elif op==4:	
					salir()

Menu()					






