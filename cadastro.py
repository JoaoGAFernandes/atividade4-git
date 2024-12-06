from abc import ABC, abstractmethod

class Cadastro(ABC):
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    @abstractmethod
    def set_nome(self, nome):
        pass

    def set_idade(self, idade):
        self.__idade = idade

    def set_email(self, email):
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_email(self):
        return self.__email

class Pessoa(Cadastro):
    def set_nome(self, nome):
        self.__nome = nome
        
'''    
TESTANDO

p = Pessoa("João", "17 anos", "Joao@gmail.com")


print(f"Nome: {p.get_nome()}")
print(f"Idade: {p.get_idade()}")
print(f"Email: {p.get_email()}")
'''




