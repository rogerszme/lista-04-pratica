class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo


    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

livro = Livro("1999", "Tomas Well")
print(livro.get_titulo())
print(livro.get_autor())

# Modificando os atributos
livro.set_titulo("Animais do Congo")
livro.set_autor("George Washington")
print(livro.get_titulo())
print(livro.get_autor())
