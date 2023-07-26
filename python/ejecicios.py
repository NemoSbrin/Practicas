import math as m
"""
PENDIENTE

Un motor electrico gira de forma constante a 2857.0 rev/min. Si el radio de la armadura es de 2.685 cm
¿Cuál es la aceleracion del borde de la armadura?
"""
# 2403m/s^2
# Datos del ejercicio
PI = m.pi
Radio = float(input("Ingrese el radio: "))
Rpm = float(input("Ingrese las revoluciones: "))
#print(m.pi, Radio, Rpm)

def perimetro_de_un_circulo(radio):
    """
    El perimetro de un circulo es 2 * radio * pi.
    """
    return 2 * radio * m.pi

def distancia_recorrida(perimetro_de_un_circulo, rpm):
    """
    Distancia recorrida por el circulo al completar las revoluciones
    """
    return perimetro_de_un_circulo * rpm

def velocidad_angular(**kwargs):
    """
    Donde rotacion_angular son las revoluciones.
    
    El valor de regreso es radianes/segundos.
    """
    tiempo = 0
    if kwargs:
        tiempo = kwargs['tiempo']
    else:
        tiempo = 60
    print(tiempo)
    return Rpm / (2 * tiempo)

def aceleracion_tangencial():
    periodo = m.pow(Rpm, -1)
    #periodo = Rpm ** (-1)
    return (2 * PI * Radio) / periodo

