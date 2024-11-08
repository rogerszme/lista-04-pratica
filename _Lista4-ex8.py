class Funcionario:
    def __init__(self, salario):
        self._salario = 0
        self.set_salario(salario)

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        if salario > 0:
            self._salario = salario
        else:
            print("O salário deve ser um valor positivo.")

funcionario = Funcionario(3000)
print(funcionario.get_salario()) 

funcionario.set_salario(2000) 
print(funcionario.get_salario())

funcionario.set_salario(-500)
