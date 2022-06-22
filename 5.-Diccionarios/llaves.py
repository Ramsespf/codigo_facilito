diccionario = {'a': 1, 'b':2, 'c': 3, 'd': 4}

llaves = diccionario.keys() # -> retorna un objeto dond tiene todas las llaves del diccionario

valores = diccionario.values()  # -> retorna un objeto dond tiene todas las valores del diccionario

elementos = diccionario.items() # -> etorna un objeto en forma de tupla con (llave, valor)

# Se recomienda q los objetos se conviertan a tuplas para no modificarlos

llaves = tuple(diccionario.keys())
