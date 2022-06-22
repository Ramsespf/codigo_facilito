def saludar():

    def mostrar_mensaje():
        print('Hola, nos encontramos en el curso de Python')

    return mostrar_mensaje  # -> esta es la forma de retornar funciones anidadas

respuesta = saludar()
respuesta()

