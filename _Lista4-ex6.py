class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco(self):
        return self._preco

    def preco_valor(self, valor):
        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self._preco = valor

produto1 = Produto("Arroz", 40)
print(produto1.nome())
print(produto1.preco())