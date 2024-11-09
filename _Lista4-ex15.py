# 15- Crie uma classe "Curso" com atributos privados "nome" e "duracao". Crie métodos para modificar e acessar esses atributos.
class Curso:
    def __init__(self, nome, duracao):
        self.__nome = nome
        self.__duracao = duracao

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        self.__duracao = duracao

curso = Curso("Java para Iniciantes", 40)

print(f"Curso: {curso.get_nome()}")
print(f"Duração: {curso.get_duracao()} horas")

curso.set_nome("Java Avançado")
curso.set_duracao(60)

print(f"Novo Curso: {curso.get_nome()}")
print(f"Nova Duração: {curso.get_duracao()} horas")