# crie uma classe "veiculo" com atributo privado "velocidade_maxima" e um metodo getter que retorne esse valor
class Veiculo:
    def __init__(self, velocidade_maxima):
        self.__velocidade_maxima = velocidade_maxima
    def get_velocidade_maxima(self):
        return self.__velocidade_maxima

carro1 = Veiculo(200)
velocidade_maxima_carro = carro1.get_velocidade_maxima()
print("#########################################")
print("A velocidade máxima do carro é:", velocidade_maxima_carro, "km/h")


    
 