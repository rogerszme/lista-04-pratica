# 20 - Crie uma classe "professor" com atributos privados "nome" e "disciplina". Crie metodos para modificar e acessar esses atributos.
class Professor:
    def __init__(self, nome, disciplina):
        self.__nome = nome
        self.__disciplina = disciplina

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_disciplina(self):
        return self.__disciplina
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

professor = Professor("John Souza lima", "Inglês")

print(professor.get_nome())       
print(professor.get_disciplina())

professor.set_nome("Adriana Acorsi")
professor.set_disciplina("Sociologia")

print(professor.get_nome())
print(professor.get_disciplina())