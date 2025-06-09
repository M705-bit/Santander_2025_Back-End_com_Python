class BankAccount:
    def __init__(self):
        self.saldo = 0 
        self.lista_de_depositos = []
        self.lista_de_saques = []
    def depositar(self, valor):
        if valor > 0: 
            self.saldo+=valor
            self.lista_de_depositos.append(valor)
        else:
            print("O sistema não permite depositos negativos")
    def sacar(self,valor):
        if (len(self.lista_de_saques) < 3) and (self.saldo >= valor) and (valor <= 500): 
            self.saldo -= valor
            self.lista_de_saques.append(valor)
        else: 
            print("Você passou do limite estipulado de saques!")
    def extrato(self):
        print("\nExtrato: \n")

        for i in range(len(self.lista_de_saques)):
            print(f'Saque de R${(self.lista_de_saques[i]):.2f} realizado')

        for i in range (len(self.lista_de_depositos)):
            print(f'Deposito de R${(self.lista_de_depositos[i]):.2f} realizado')

        print(f'O seu saldo atual é de R${self.saldo:.2f}\n')

minha_conta=BankAccount()      
while True:
    print("Bem vindo ao seu sistema bancário!")
    i = int(input(" Para depositar digite '1' \n Para sacar digite '2' \n Para ver extrato digite '3' \n Digite aqui: "))
    match i:
        case 1:
            minha_conta.depositar(float(input("Digite a quantia que você gostaria de depositar: ")))
        case 2:
            minha_conta.sacar(int(input("Digite a quantia que você gostaria de sacar: ")))
        case 3: 
            minha_conta.extrato()
            
             