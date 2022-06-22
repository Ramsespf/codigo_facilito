diccionario = {'a': 1, 'b':2, 'c': 3, 'd': 4}

valor = diccionario['a']

valor_get = diccionario.get('z', 'La llave no existe en el diccionario')    # -> devuelve un valor pero si no existe la llave no da error y puede dar un mensaje en caso de q no exista

valor_setdefault = diccionario.setdefault('e', 5)   # -> en caso de q no exista la llave la crea y le pone el valor

