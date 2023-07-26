import formulas_auxiliares as metodos
## -------------------------------
# 1.- deber ingresar # de radios para calcular
# 2.- Guardar en un array (list)
# 3.- importamos el metodo perimetro_de_un_circulo, calculamos y guardamos
cuantosRadios = int(input("Ingrese # de radios: "))
cont = 0
lista = []
while cont < cuantosRadios:
    radio = float(input("Ingrese el valor del radio: "))
    perimetro = metodos.perimetro_de_un_circulo(radio)
    lista.append([radio, perimetro])
    cont += 1
print(lista)