def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'

        nonlocal b  # -> para cambiar el valor de b
        b = 'cambio de valor'
        print(a)
        print(b)

    funcion_anidada()
    

funcion_principal()