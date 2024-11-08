class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome  
        self.__nota = nota  

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")

aluno = Aluno("João Cleber", 8.5)

print(f"Nome do aluno: {aluno.get_nome()}")
print(f"Nota do aluno: {aluno.get_nota()}")

aluno.set_nome("Maria Clara")
aluno.set_nota(9.2)

print(f"Novo nome do aluno: {aluno.get_nome()}")
print(f"Nova nota do aluno: {aluno.get_nota()}")

aluno.set_nota(11)
