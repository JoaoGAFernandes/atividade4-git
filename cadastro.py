

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

'''
TESTE
c = Cadastro("João", "17 anos", "Joao@gmail.com")


print(f"Nome: {c.get_nome()}")
print(f"Idade: {c.get_idade()}")
print(f"Email: {c.get_email()}")
'''
