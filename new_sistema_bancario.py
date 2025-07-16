contador = 0
lista = []
#toda vez que inicio uma função eu incremento contador. 
class Banco:
    def __init__(self):
        self.contas = []
        self.agencia = "0001"
    def add_contas(self, obj):
        self.contas.append(obj)
    def listar_contas(self):
        for conta in self.contas:
            print(f"{conta.nmr_conta} : {conta.cpf}")
    def procura_conta(self, cpf = []):
        for conta in self.contas:
            if conta.cpf == cpf: 
                return conta
            return None
      
class contaCorrente(Banco):
    contador = 0 

    def __init__(self):
        self.nmr_conta = contaCorrente.contador 
        contaCorrente.contador +=1
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

class User: 
    def __init__(self, nome = str, data_de_nascimento = str, cpf = int, endereco = str):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []
    def ad_conta(self, conta):
        self.contas.append(conta)

def isdigit(input):
         var = "0123456789"
         '''
         for i in var:
             if input == var[i]:
                 return True
         '''
         for i in range(len(var)):
             if input == var[i]:
                 return True
         return False  

def main():
    banco = Banco()
    user1 = User("Maria", "12.03.2000", "58989000099")
    banco.add_contas(user1)

    while True:
      print("Bem vindo ao seu sistema bancário!")
      entrada = str(input("O que você gostaria de fazer?\n a. Acessar uma conta\n c. Criar uma conta\n"))
      match entrada: 
            case "a":
              id = []
              cpf = str(input("Digite seu cpf: "))
              for i in range(len(cpf)):
                  if isdigit(cpf[i]) == True: 
                      id.append(str(cpf[i]))
              #se tiver alguma conta correspondente a esse número de cpf existindo aqui, acesse ela
              if (Banco.procura_conta(id)):
                  conta = Banco.procura_conta(id)
                  print("Digite a conta que você deseja acessar: ")
      
                  i = int(input(" Para depositar digite '1' \n Para sacar digite '2' \n Para ver extrato digite '3' \n Para sair digte '4' \n Digite aqui: "))
                  match i:
                   case 1:
                      conta.depositar(float(input("Digite a quantia que você gostaria de depositar: ")))
                   case 2:
                      conta.sacar(int(input("Digite a quantia que você gostaria de sacar: ")))
                   case 3: 
                      conta.extrato()
                   case 4: 
                        break
              else:
                  print("Nenhuma conta corresponde a esse cpf")

              ''' 
              entrada1 = str(input("O que você gostar de fazer?\n d. Depositar \n s.Sacar\n e. Acessar Extrato\n"))
              match entrada1:
                  case "d":
                      
                  case "s":
                  case "e":
              '''     

    

main()
