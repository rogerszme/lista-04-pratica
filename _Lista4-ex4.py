class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    def get_saldo(self):
        return self.__saldo
    ##############################################
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("#######################################")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("#######################################")
            print("O valor do depósito deve ser positivo.")
    ##############################################
    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > self.__saldo:
            print("#######################################")
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.__saldo -= valor
            print("#######################################")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
    ##############################################
conta = ContaBancaria(3000)
print("#######################################") 
print(f"Saldo atual: R${conta.get_saldo():.2f}") 

conta.depositar(400) 
conta.depositar(-200)
conta.sacar(300) 
conta.sacar(1600)

print("#######################################")  
print(f"Saldo final: R${conta.get_saldo():.2f}") 
