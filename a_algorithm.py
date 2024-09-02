import os

listaAberta = []
listaFechada = []

dicHeuristica = {}

vertices = []

 
grafo = {}

def reset_info():
    global listaAberta 
    global listaFechada
    global dicHeuristica
    global vertices
    global grafo

    listaAberta = []
    listaFechada = []
    dicHeuristica = {}
    vertices = []
    grafo = {}

def exibir_fila(iteracao):
    print(f"Iteração {iteracao}:")
    fila_str = "Fila: "
    for vertice in listaAberta:
        custo = posicoesCalculadas[vertice][1]
        heuristica = posicoesCalculadas[vertice][2]
        fila_str += f"({vertice}: {custo} + {heuristica} = {custo + int(heuristica)}) "
    print(fila_str.strip())

def calcular_medida_desempenho(iteracao):
    # A medida de desempenho pode ser baseada no número de nós processados e o custo total atual
    medida = iteracao * 1.5  # Exemplo: baseando-se na iteração, pode ser ajustado
    print(f"Medida de desempenho: {medida:.1f}")

def ordena_por_custo():
    global listaAberta
    listaAberta_aux = []

    for chave in listaAberta:
        listaAberta_aux.append(posicoesCalculadas[chave])

    #sorted(listaAberta_aux, key=lambda t: (t[1]+t[2]))

    listaAberta = []

    for element in listaAberta_aux:
        listaAberta.append(element[0])

def recuperar_caminho(atual):
    global posicoesCalculadas
    
    caminho_completo = []
    if(atual != inicio):
        origem = posicoesCalculadas[atual][3]
    else:
        origem = inicio

    caminho_completo.append(atual)
    while(origem != inicio):
        caminho_completo.append(origem)
        origem = posicoesCalculadas[origem][3]
    if inicio not in caminho_completo:
        caminho_completo.append(inicio)

    caminho_completo.reverse()
    return caminho_completo

def calcula_custos(atual, vizinhos):
    global posicoesCalculadas

    for vizinho in vizinhos:
        heuristica = int(dicHeuristica[vizinho]["custo"])
        if vizinho not in posicoesCalculadas:
            custo = posicoesCalculadas[atual][1] + 1  # custo = custo do atual + 1
            posicoesCalculadas[vizinho] = (vizinho, custo, heuristica, atual)
    return posicoesCalculadas

def encontre_vizinhos(atual):
    global listaFechada

    vizinhos = []

    for vizinho in grafo[atual]:
        if(vizinho not in listaFechada):
            vizinhos.append(vizinho)
    return vizinhos

def buscar():
    iteracao = 1
    listaAberta.append(inicio)
    
    # Inicializar o ponto inicial na posicaoCalculadas
    posicoesCalculadas[inicio] = (inicio, 0, int(dicHeuristica[inicio]["custo"]), None)

    found = False
    caminhoCompleto = []  # Inicializa caminhoCompleto como uma lista vazia

    while listaAberta and not found:
        atual = listaAberta[0]

        exibir_fila(iteracao)  # Exibe a fila atual
        calcular_medida_desempenho(iteracao)  # Calcula e exibe a medida de desempenho

        vizinhos = encontre_vizinhos(atual)
        calcula_custos(atual, vizinhos)

        for vizinho in vizinhos:
            if vizinho not in listaAberta:
                listaAberta.append(vizinho)

        listaAberta.remove(atual)
        listaFechada.append(atual)

        if final in listaFechada:
            found = True
            caminhoCompleto = recuperar_caminho(atual)

        ordena_por_custo()
        iteracao += 1  # Incrementa a iteração

    return caminhoCompleto


def data_input():
    global inicio
    global final

    i = 0
    n = 0
    arq_str = input('Digite o nome do arquivo de entrada\n')

    while True:
        if os.path.isfile(arq_str) is True:
            break
        else:
            print('Arquivo não existe, digite novamente...')
            arq_str = input('Digite o nome do arquivo de entrada\n')

    with open(arq_str, 'r') as arq:
        linha = arq.readline()
        while linha and linha.startswith('p'):
            linha = arq.readline()

        info = linha.replace("h(", "").replace(")", "").split(',')
        u = info[0]; grafo[u] = {}
        dicHeuristica[info[0]] = {"destino": info[1], "custo": info[2]}
        for linha in arq:
            info = linha.replace("h(", "").replace(")", "").split(',')
            u = info[0]; grafo[u] = {}
            dicHeuristica[info[0]] = {"destino": info[1], "custo": info[2]}
        #for id, chave in enumerate(heuristica):
        #   heuristica[chave]["index"] = id
        #print(heuristica)
        #global grafo
        #grafo = gf.Grafo(len(heuristica))
        
    with open(arq_str, 'r') as arq:
        inicio = arq.readline().strip().replace("ponto_inicial(", "").replace(")", "") #le a primeira linha (ponto inicial)
        final = arq.readline().strip().replace("ponto_final(", "").replace(")", "") #le a segunda linha (ponto final)

        linha = arq.readline().strip()
        info = linha.replace("pode_ir(", "").replace(")", "").split(',')
        u = info[0]; v = info[1]; p = info[2]
        grafo[u][v] = p
        for linha in arq: #comeca a ler as linhas enquanto for pode_ir() e coloca as infos no grafo
            if(linha.startswith('p') == True):
                info = linha.replace("pode_ir(", "").replace(")", "").split(',')
                u = info[0]; v = info[1]; p = info[2]
                grafo[u][v] = p
            else:
                break
    #print(grafo)
    #print(heuristica) 
    #print(inicio + " " + final)

def run_star():
    data_input()

    if inicio == final:
        print('Fim!')
    else:
        resultado = buscar()
        print("\nFim da execução")
        distancia_total = posicoesCalculadas[final][1]
        print(f"Distância: {distancia_total}")
        caminho = ' - '.join(resultado)
        print(f"Caminho: {caminho}")
        calcular_medida_desempenho(len(listaFechada))  # Medida de desempenho final
        reset_info()
    return 0



posicoesCalculadas = {}