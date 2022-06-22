
class Usuario:
    
    def inicializar(self, username, password):
        # Añadiendo atrrs al objeto
        self.username = username
        self.password = password


user1 = Usuario()
user2 = Usuario()

user1.inicializar('user1', 'password2')
user2.inicializar('user2', 'password2')

print(user1.__dict__)
print(user2.__dict__)