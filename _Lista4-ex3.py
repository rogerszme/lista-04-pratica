class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo 

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

carro1 = Carro("Golf")
print(carro1.get_modelo())

carro1.set_modelo("Opala")
print(carro1.get_modelo())
