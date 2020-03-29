# Basket.py
app
import os

Lista_personas = list()


class Registro_Pandemia:
    def __init__(self):
        self.estatus = 'Sospechoso'

@staticmethod
def registrar_datos():
        Estatus = Registro_Pandemia()
        for x in range(50):
            HOMEPATH = os.getenv('HOMEPATH')
            carpetaDePrograma = HOMEPATH + os.path.sep + "Documents" + os.path.sep + "Datos de los casos 1.0"
            if not os.path.exists(carpetaDePrograma):
                os.mkdir(carpetaDePrograma)
            archivo1 = carpetaDePrograma + os.path.sep + 'Nombre.txt'
            archivo2 = carpetaDePrograma + os.path.sep + 'Apellido.txt'
            archivo3 = carpetaDePrograma + os.path.sep + 'Edad.txt'
            archivo4 = carpetaDePrograma + os.path.sep + 'ID.txt'
            archivo5 = carpetaDePrograma + os.path.sep + 'Fecha de nacimiento.txt'
            archivo6 = carpetaDePrograma + os.path.sep + 'Pais de residencia.txt'
            archivo7 = carpetaDePrograma + os.path.sep + 'Genero.txt'
            with open(archivo1, 'a') as f:
                f.write(input("Ingrese el nombre de la persona: ") + '\n')
            with open(archivo2, 'a') as f:
                f.write(input("Ingrese el apellido de la persona: ") + '\n')
            with open(archivo3, 'a') as f:
                f.write(input("Ingrese la edad de la persona: ") + '\n')
            with open(archivo4, 'a') as f:
                f.write(input("Ingrese el numero de se tarjeta de identificación (cedula, pasaporte, I.D...): ") + '\n')
            with open(archivo5, 'a') as f:
                f.write(input("Ingrese la fecha de nacimiento de la persona: "))
            with open(archivo6, 'a') as f:
                f.write(input("Ingrese el pais de residencia de la personas: "))
            with open(archivo7, 'a') as f:
                f.write(input("Masculino/Femenino: ") + '\n')
            print("")
            Lista = ('Nombre.txt', 'Apellido.txt', 'Edad.txt', 'Cedula.txt', 'F_nacimiento.txt',
                     'P_residencia.txt', 'Genero.txt')
            print("")
            print("Pulse ENTER para continuar")
            print("")
            input()
            Estatus.sintomas()
            Lista_personas.append(Lista)
            Menu1()

@staticmethod
def sintomas(self=None):
        print("")
        print("Selecione los sintomas que posee la persona:")
        print("")
        print("1- Fiebre, tos seca, dificultad para respirar, dolor de cabeza y muscular.")
        print("")
        print("2- Tos con flema, moqueo frecuente, estornudos y malestar de garganta.")
        print("")
        print("3- Estornudos, tos, picazón (nariz, ojos y boca), moqueo y congestión nasal.")
        print("")
        opcion2 = input()
        if opcion2 == '1':
            print("Sintomas relacionados con el virus COVID-19")
            print("")
            print(" Pulse ENTER para volver al menu principal")
            input()
            Menu1()
        elif opcion2 == '2':
            print("La persona solo presenta un resfriado comun")
            print("")
            print("Pulse ENTER para volver al menu principal ")
            input()
            self.estatus = 'Descartado'
            Menu1()
        elif opcion2 == '3':
            print("La persona solo presenta una alergia")
            print("")
            print("Pulse ENTER para volver al menu principal ")
            input()
            self.estatus = 'Descartado'
            Menu1()
        else:
            print("Opcion invalida.")



def Menu1():
    Menu = Registro_Pandemia
    opcion = None
    while opcion != '0':
        print("  REGISTRO DE CASOS DE CORONAVIRUS ")
        print("")
        print("1- Registrar datos nuevos")
        print("2- Mostrar todos los casos registrados")
        print("3- Actualizar datos de los casos registrados")
        print("0- Salir")
        opcion = input()
        if opcion == '1':
            Menu.registrar_datos()
        elif opcion == '2':
        
            archivo = open('Nombre.txt', 'r')
            cadena = archivo.read()
            archivo.close()
            print(cadena)
            print("")
            print(" utilize ENTER para volver al menu principal ")
            input()
            Menu1()
        elif opcion == '3':
            registrar_datos = Registro_Pandemia()
            if not registrar_datos:
                print('No se encuentran pacientes en el registro')
                print("pulse ENTER para continuar ")
                input()
                Menu1()
            else:
                while True:
                    Nombre = str(input("Ingrese el nombre de la persona que desea actualizar: "))
                    ID = input("Ingrese la tarjeta de identificacion de la persona que desea actualizar: ")
                    if Nombre + '\n' == open("Nombre.txt").read() and ID + '\n' == open("ID.txt").read():
                        print("Se ha encontrado a: ", Nombre, "-")
                        print("")
                        print("¿cual es el nuevo estatus?")
                        print("")
                        print("1- Sospechoso")
                        print("2- Activo")
                        print("3- Descartado")
                        print("0- Volver al menu principal")
                        opc2 = input()
                        if opc2 == '1':
                            registrar_datos.estatus = "Sospechoso"
                            print("-Se ha actualizado la información de la persona")
                            print("")
                            print("pulse ENTER para volver al menu principal")
                            input()
                            Menu1()
                        elif opc2 == '2':
                            registrar_datos.estatus = "Activo"
                            print("Se ha actualizado la información de la persona")
                            print("")
                            print(" pulse ENTER para volver al menu principal ")
                            input()
                            Menu1()
                        elif opc2 == '3':
                            registrar_datos.estatus = "Descartado"
                            print("Se ha actualizado la información de la persona")
                            print("")
                            print(" Pulse ENTER para volver al menu principal ")
                            input()
                            Menu1()
                        elif opc2 == '0':
                            print("")
                            print(" pulse ENTER para volver al menu principal ")
                            input()
                            Menu1()
                        else:
                            print("Opcion invalida.")
                            print('')
                            pass
        elif opcion == '0':
            print("Gracias por la informacion ingresada")
            break
        else:
            print("Opcion invalida.")

Menu1()

