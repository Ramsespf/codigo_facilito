def suma(n1, n2):   # -> la n1, n2 son parametros
    return n1 + n2, 'La funcion retorna dos valores'    # return puede devolver n elementos

numero_uno = int(input('INgresa el primer numero: '))
numero_dos = int(input('Ingrese el segundo numero: '))

resultado, mensaje = suma(numero_uno, numero_dos)    # -> numero_uno, numero_dos son argumentos
print(resultado)
print(mensaje)