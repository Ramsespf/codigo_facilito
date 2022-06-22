rango = range(11)   # -> 0 - 10

for valor in range(5, 20, 3):   # -> 5 - 19 pero con saltos d 3
    print(valor)


numeros = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros):   # -> retorna un objeto iterable q posee tuplas con 2 valores el 1ro es la referencia del indice y el segundo el valor
    print(indice, numero)



