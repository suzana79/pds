class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self,valor):
        self.saldo += valor  

    def exibir_detalhes(self):
        print("Número da Conta", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)
    
    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente, você está miserável")

    

#aqui estou criando um instância do objeto ContaBancaria
#com o nome conta_da_maki
numero_conta = input("Digite o número da conta")
titular_conta = input("Digite o titular da conta")
saldo_inicial = float (input("Digite o saldo inicial da conta").replace(",","."))

conta_da_maki = ContaBancaria(numero_conta, titular_conta, saldo_inicial)
valor_deposito = float(input("Digite o valor a ser depositado").replace(",","."))
valor_saque = float (input("Digite o valor a ser sacado").replace(",","."))

conta_da_maki.depositar(7000)
conta_da_maki.sacar(7200)
conta_da_maki.exibir_detalhes()

 