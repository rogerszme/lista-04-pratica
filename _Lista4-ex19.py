# 19 - Crie uma classe "cidade" com atributos privados "nome" e "populacao". adicione metodos para acessar e modificar esses atributos.

class Cidade:
    def __init__(self, nome, populacao):
        self.__nome = nome  
        self.__populacao = populacao  

    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def set_nome(self, nome):
        self.__nome = nome
    def set_populacao(self, populacao):
        self.__populacao = populacao

cidade = Cidade("São Paulo", 12000000)
print(f'Nome da cidade: {cidade.get_nome()}')
print(f'População da cidade: {cidade.get_populacao()}')

cidade.set_nome("Rio de Janeiro")
cidade.set_populacao(7000000)
print(f'Novo nome da cidade: {cidade.get_nome()}')
print(f'Nova população da cidade: {cidade.get_populacao()}')
