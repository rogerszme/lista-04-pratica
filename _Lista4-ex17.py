# 17- Crie uma classe "empresa" com atributos privados "nome" e "numero_funcionarios". Crie métodos para acessar e modificar esses atributos.
class Empresa:
    def __init__(self, nome, numero_funcionarios):
        self.__nome = nome
        self.__numero_funcionarios = numero_funcionarios

    def get_nome(self):
        return self.__nome

    def get_numero_funcionarios(self):
        return self.__numero_funcionarios

    def set_nome(self, nome):
        self.__nome = nome

    def set_numero_funcionarios(self, numero_funcionarios):
        if numero_funcionarios >= 0:  
            self.__numero_funcionarios = numero_funcionarios
        else:
            print("O número de funcionários não pode ser negativo.")

empresa = Empresa("Google Solutions", 1500)

print(empresa.get_nome()) 
print(empresa.get_numero_funcionarios()) 

empresa.set_nome("Google Innovations")
empresa.set_numero_funcionarios(2000)

print(empresa.get_nome())
print(empresa.get_numero_funcionarios())
