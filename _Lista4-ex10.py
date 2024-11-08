class Celular:
    def __init__(self, marca=""):
        self.__marca = marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca
    
celular_novo = Celular()
celular_novo.set_marca("Motorola")
print('######################')
print(celular_novo.get_marca())

celular_novo2 = Celular()
celular_novo2.set_marca("Xiaomi")
print('######################')
print(celular_novo2.get_marca())

