class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip() == "":
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome

pessoa = Pessoa("João Cleber")
print(pessoa.get_nome()) 
# Tratamento para Tentar alterar o nome para um valor vazio
try:
    pessoa.set_nome("") 
except ValueError as e:
    print(e)
##############################################################
pessoa.set_nome("Maria Clara")
print(pessoa.get_nome())
