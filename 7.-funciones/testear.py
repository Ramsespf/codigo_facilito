# Docstring
# __doc__ (Modulos, Clases, Metodos y Funciones)
# para testear en el cmd -> python -m doctest testear.py

def suma(numero_1, numero_2):
    """
    La funcion suma 2 numeros enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros

    >>> suma(10, 20)    #para testear
    30                  # debe ser o sea el resultado

    >>> suma(200, 300)
    300
    """

    return numero_1 + numero_2

