from ast import arg


def promedio(*args):       # -> Python va a crear una tupla en el parametro args con todos los argumentos q ponga a la funcion
    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado )

def combinacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

combinacion(10, 21, 14, 2, 14, 33, 78)

def usuarios(**kwargs):     # -> uso de un diccionario
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernadno=[10, 9, 9])


def combinacion2(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion2(1, 2, 3, 4, 5, Cody=True, curso='Python')