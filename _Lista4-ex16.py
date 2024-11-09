# Crie uma classe "jogo" com um atributo privado "pontuiacao" e um metodo getter para acessar a pontuação.
class Jogo:
    def __init__(self):
        self.__pontuacao = 0

    def get_pontuacao(self):
        return self.__pontuacao

    def set_pontuacao(self, pontuacao):
        if pontuacao >= 0:
            self.__pontuacao = pontuacao
        else:
            print("Pontuação não pode ser negativa!")

jogo = Jogo()
print(jogo.get_pontuacao()) 

jogo.set_pontuacao(10)
print(jogo.get_pontuacao())
