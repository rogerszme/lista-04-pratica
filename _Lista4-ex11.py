class Animal:
    def __init__(self, idade):
        self.__idade = idade 
        self.set_idade(idade) 

    def set_idade(self, idade):
        if isinstance(idade, int) and idade > 0:
            self.__idade = idade
        else:
            print("A idade deve ser um número inteiro positivo.")

    def get_idade(self):
        return self.__idade

animal = Animal(5)
print('######################')  
print(animal.get_idade())  

animal.set_idade(10)
print('######################')  
print(animal.get_idade()) 
