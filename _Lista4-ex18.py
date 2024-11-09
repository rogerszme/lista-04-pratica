# 18 - Crie uma classe "filme" com atributos privados "titulo" e "ano_lacamento". Use gettes e setters para esses atributos.
class Filme:
    def __init__(self, titulo, ano_lancamento):
        self.__titulo = titulo
        self.__ano_lancamento = ano_lancamento

    def titulo(self):
        return self.__titulo

    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    def ano_lancamento(self):
        return self.__ano_lancamento

    def ano_lancamento(self, novo_ano):
        if novo_ano > 1800: 
            self.__ano_lancamento = novo_ano
        else:
            print("Ano de lançamento inválido!")

filme1 = Filme("Alien vs Predador ", 1999)
print(f"Filme: {filme1.titulo}, Ano: {filme1.ano_lancamento}")

filme1.titulo = "Alien do passado : Parte II"
filme1.ano_lancamento = 1984
print(f"Filme: {filme1.titulo}, Ano: {filme1.ano_lancamento}")
