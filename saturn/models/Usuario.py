class Usuario:
    def __init__(self,id,nome,senha):
        self.id=id
        self.nome=nome
        self.senha=senha

listaUsuarios=[]
listaUsuarios.append(Usuario(1, "Gaby", "1234"))
listaUsuarios.append(Usuario(2, "Gigi", "5678"))