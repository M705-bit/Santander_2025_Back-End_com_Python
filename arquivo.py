# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:


def ordena(fila_de_atendimento):
    
    tam = len(fila_de_atendimento)
    fila_urgente = []
    fila_n_urgente = []
    for i in range(tam):
            if fila_de_atendimento[i][2] == "urgente":
                     fila_urgente.append(fila_de_atendimento[i])   
            else:
                 fila_n_urgente.append(fila_de_atendimento[i]) 

    def bubble_sort(array):
        tam=len(array)
        for i in range(tam):
            for j in range(0, tam-1):
            		if array[j][1] < array[j+1][1]:
                         temp = array[j]
                         array[j] = array[j+1]
                         array[j+1] = temp 
        return array
    
    fila_urgente = bubble_sort(fila_urgente)
    fila_n_urgente = bubble_sort(fila_n_urgente)

    array = []

    for i in range(len(fila_urgente)):
         array.append(fila_urgente[i])
    for i in range(len(fila_n_urgente)):
         array.append(fila_n_urgente[i])

    return array 
    
array = ordena(pacientes)

# TODO: Exiba a ordem de atendimento com título e vírgulas:
print("Ordem de atendimento: ", end="")

for i in range(n):
        if i > 0:
            print(f", {array[i][0]}", end="")
        else:
            print(f"{array[i][0]}", end="")
