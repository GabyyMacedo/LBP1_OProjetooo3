class Users:
    def __init__(self, username, senha):
        self.username=username
        self.senha=senha

Users=[
    ("user", 123)
]

def addUSer(username, senha):
    newUser=Users(username, senha)
    Users.append(newUser)
