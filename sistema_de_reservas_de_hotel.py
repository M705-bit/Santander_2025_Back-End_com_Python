def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    #confirmadas = set(reservas_solicitadas) & quartos_disponiveis
    confirmadas = set(reservas_solicitadas).intersection(quartos_disponiveis)
    #recusadas = set(reservas_solicitadas) - quartos_disponiveis
    recusadas = set(reservas_solicitadas).difference(quartos_disponiveis)
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()
