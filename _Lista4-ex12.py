class Estudante:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

estudante1 = Estudante("Rogério", "76589")
print('#################################')
print(estudante1.get_nome())     
print(estudante1.get_matricula()) 


estudante1.set_nome("João")
estudante1.set_matricula("985632")
print('#################################')
print(estudante1.get_nome())
print(estudante1.get_matricula()) 
