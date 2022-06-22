class Usuario:
    
    # Object
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

user1 = Usuario('User1', 'password1')
user2 = Usuario('User2', 'password2')



print(user1.__dict__)
print(user2.__dict__)