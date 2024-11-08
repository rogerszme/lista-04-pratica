class Casa:
    def __init__(self, endereco, valor):
        self.__endereco = endereco
        self.__valor = valor

    def get_endereco(self):
        return self.__endereco

    def get_valor(self):
        return self.__valor

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_valor(self, valor):
        self.__valor = valor

casa = Casa("Avenida Liberdade, 458", 35000)
print(casa.get_endereco())  
print(casa.get_valor())     
casa.set_endereco("Avenida Perimetral, 820")
casa.set_valor(74911)
print(casa.get_endereco()) 
print(casa.get_valor())    
