import math as m

PI = m.pi

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
    tiempo = 1
    Rpm = 0
    if kwargs:
        try:
            tiempo = kwargs['tiempo']
            Rpm = kwargs['rpm']
        except Exception as e:
            print(f'Hubo un error {str(e)}')
    try:
        resultado = Rpm / (2 * tiempo)
    except ZeroDivisionError as zde:
        print(f'Hubo un error {str(zde)}')
    return resultado

def aceleracion_tangencial(**kwargs):
    Rpm = 0
    Radio = 0
    if kwargs:
        try:
            Rpm = kwargs['rpm']
            Radio = kwargs['radio']
        except Exception as e:
            print(f'Hubo un error {str(e)}')
    periodo = m.pow(Rpm, -1)
    try:
        resultado = (2 * PI * Radio) / periodo
    except ZeroDivisionError as zde:
        print(f'Hubo un error {str(zde)}')
    return resultado
