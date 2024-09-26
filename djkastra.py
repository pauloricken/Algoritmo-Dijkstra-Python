import heapq


def dijkstra(grafo, inicio, destino):
    # Inicializa as distâncias e a fila de prioridade
    distancias = {cidade: float('inf') for cidade in grafo}
    distancias[inicio] = 0
    lista_prioridade = [(0, inicio)]  # (distância, cidade)
    caminho = {cidade: None for cidade in grafo}  # Para rastrear o caminho

    while lista_prioridade:
        distancia_atual, cidade_atual = heapq.heappop(
            lista_prioridade)  #Essa função tem como objetivo retornar o menor elemento

        # Se chegamos ao destino, podemos parar
        if cidade_atual == destino:
            break

        # Verifica se a distância atual é maior que a registrada
        if distancia_atual > distancias[cidade_atual]:
            continue

        # Atualiza as distâncias dos vizinhos
        for cidade_adjacente, valor_nova_distancia in grafo[cidade_atual].items():
            nova_distancia = distancia_atual + valor_nova_distancia

            if nova_distancia < distancias[cidade_adjacente]:
                distancias[cidade_adjacente] = nova_distancia
                caminho[cidade_adjacente] = cidade_atual
                heapq.heappush(lista_prioridade, (nova_distancia, cidade_adjacente))

    # Reconstruir o caminho
    percurso = []
    cidade_atual = destino
    while cidade_atual is not None:
        percurso.append(cidade_atual)  #inserir na lista
        cidade_atual = caminho[cidade_atual]
    percurso.reverse()  # Para ter o caminho do início ao destino

    return distancias[destino], percurso

