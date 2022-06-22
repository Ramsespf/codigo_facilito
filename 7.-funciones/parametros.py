from unittest import result


def area_circulo(radio, pi=3.14):   # -> pi=valor es para poner un parametro por default, los parametros x default simpre van a la derecha
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)