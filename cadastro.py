

class Cadastro:
    def __init__(self, nome, idade, email):
        self._nome = nome
        self._idade = idade
        self._email = email

    def set_nome(self, nome):
        self._nome=nome

    def set_idade(self, idade):
        self._idade = idade

    def set_email(self, email):
        self._email = email

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_email(self):
        return self._email
    def mostrar(self):
        print(f"Nome: {self.get_nome()}, Idade: {self.get_idade()}, Email: {self.get_email()}")

'''
c = Cadastro("Joao", 17, "Joao@gmail.com",)
c.mostrar()
'''