class novoPaciente():
     def __init__(self, nome, idade, estado, prioridade = 0):
        self.nome = nome
        self.idade = idade
        self.estado = estado
        self.prioridade = 0 

def seta_prioridade(lista):

    for i in range(len(lista)):

        if lista[i].estado == 'urgente' and paciente.idade >= 60: 
            lista[i].prioridade = 1
        elif lista[i].estado == 'urgente' and paciente.idade < 60: 
            lista[i].prioridade = 2
        elif lista[i].estado == 'normal' and paciente.idade > 60: 
            lista[i].prioridade = 3
        else:
            lista[i].prioridade = 4
def ordena(lista):
    lista1 = []
    for i in range(len(lista)):
        if lista[i].prioridade == 1:
            lista1.insert(0, paciente)
        elif lista[i].prioridade == 2:
             for i in range(len(lista)):
            if lista[i].prioridade != "urgente":
                lista.insert(i, paciente)
                inserido = True
                break
        if not inserido:
            lista.append(paciente)
            lista1.insert(i, paciente)
        elif lista[i].prioridade == 3:

'''
def add_paciente(lista, nome, idade, estado):

    paciente = novoPaciente(nome, idade, estado)

    if paciente.estado == 'urgente' and paciente.idade >= 60:
        lista.insert(0, paciente)
    elif paciente.estado == 'urgente' and paciente.idade < 60:
        for i in range(len(lista)):
             if lista[i].estado == 
                lista.insert(i, paciente)
                inserido = True
                break
             
    elif paciente.idade > 60:
        inserido = False
        for i in range(len(lista)):
            if lista[i].estado != "urgente":
                lista.insert(i, paciente)
                inserido = True
                break
        if not inserido:
            lista.append(paciente)

    else:
        lista.append(paciente)
'''

n = int(input().strip())
lista = []
for _ in range(n):
    nome, idade, estado = input().strip().split(", ")
    paciente = novoPaciente(nome, int (idade), estado)
    lista.append(paciente)

seta_prioridade(lista)
    

print("Ordem de atendimento: ", end="")

for i in range(n):
    if i > 0:
        print(f", {lista[i].nome}", end="")
    else:
         print(lista[i].nome, end="")

