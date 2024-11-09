# crie uma classe "computador" com um atributo privado "memoria_ram" e um metodo que permita somente valores maiores que zero
class Computador:
    def __init__(self, memoria_ram):
        self.set_memoria_ram(memoria_ram)

    def set_memoria_ram(self, valor):
        if valor > 0:
            self.__memoria_ram = valor
        else:
            print("A memória RAM deve ser um valor positivo.")

    def get_memoria_ram(self):
        return self.__memoria_ram

meu_pc = Computador(8)
print("A memória RAM do meu computador é:", meu_pc.get_memoria_ram(), "GB")


