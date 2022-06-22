class Usuario:
    #Attrs de clase
    username = ''
    email = ''

Usuario.username = 'User1'
Usuario.email = 'info@codigofacilito.com'

print(Usuario.username)
print(Usuario.email)

user1 = Usuario()
user2 = Usuario()
# 1.- Verifica si el attr existe dentro del objeto
# 2.- Verifica si el attr existe dentro de la clase -> Lectura solamente
# 3.- Lanzar un error

print(user1.username)



user1.username = 'Cody' # Añadimos el attrs al objeto de Insyacnia
user1.password = 'password'
print(user1.__dict__) # Muestra todos los atributos dentro del objeto

print(user2.username)   # user2 no tiene ningun atributo d instancia, solamente puede leer los atributos de clase


