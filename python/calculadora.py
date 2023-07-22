# Calculadora
"""
Menu con las 4 operaciones
"""
num1 = 1
num2 = 2
opcion = 0

def suma(x,y):
    print("Estoy sumando "+str(x+y))

#def resta():
def resta(d,e):
    #print("Estoy restando")
    print("Estoy restando"+str(d-e))

def multiplicacion():
    print("Estoy multiplicando")

def division():
    print("Estoy diviendo")
    #return None

def Menu():
    # Menu de aplicacion
    print("Calculadora")
    print("1 Suma")
    print("2 Resta")
    #print("3 Multiplicacion")
    #print("4 Division")
    print("Seleccion una opcion")
    opcionDentroDelMenu = int(input())
    return opcionDentroDelMenu

opcion = Menu()
#print(type(opcion))

while opcion != 0:
    print(">> Estoy en bucle <<")
    print("Ingrese valor de a")
    a = int(input())
    print("Ingrese valor de b")
    b = int(input())
    if(opcion == 1):
        suma(a,b)
    if(opcion == 2):
        #resta()
        resta(a,b)
    if(opcion >= 3):
        print("aun no tengo eso")
    opcion = Menu()

if(opcion == 0 ):
    print("--Fin del programa--")
