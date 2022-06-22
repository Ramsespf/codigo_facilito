lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort() #-> Ordena de menor a mayor

lista.sort(reverse=True) #-> Ordena de mayor a menor

print(min(lista)) #-> nos muestra el menor valor
print(max(lista)) #-> nos muestra el mayor valor

10 in lista #-> esto devuelve un booleano y lo q hace es preguntar si 10 esta in lista
11 not in lista #-> nos pregunta si 11 no esta en lista

index = lista.index(5) #-> retorna el 1er indice de el elemento encontrado
