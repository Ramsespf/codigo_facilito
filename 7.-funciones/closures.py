def saludar(username):
    mensaje = f'Hola {username}'  #Variable local

    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)

respuesta()