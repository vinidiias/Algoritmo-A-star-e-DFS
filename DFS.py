grafo = {}
mark = 0
performance_measure = 0.0
caminho = []
inicio = ""
final = ""
bench = False

def reset_info():
    global grafo
    global mark
    global performance_measure
    global caminho
    global inicio
    global final
    global bench

    performance_measure = 0.0
    caminho = []
    inicio = ""
    final = ""
    bench = False
    mark = 0
    grafo = {}

def DFS_visit(u, iteration):
    global mark
    global performance_measure
    
    grafo[u]["cor"] = "cinza"
    mark += 1
    grafo[u]["d"] = mark
    
    # Preparando a fila para exibição e cálculo da medida de desempenho
    fila = []
    for v, peso in grafo[u]["vizinhos"]:
        if grafo[v]["cor"] == "branco":
            fila.append(f"{v}({grafo[u]['d']} + {peso} = {int(grafo[u]['d']) + int(peso)})")
    
    # Se a fila não estiver vazia, mostra o estado atual
    if fila:
        fila_str = " ".join(fila)
        performance_measure += len(fila) * 1.5  # Exemplo de cálculo de desempenho

        print(f"Iteração {iteration}:")
        print(f"Fila: {fila_str}")
        print(f"Medida de desempenho: {performance_measure:.1f}\n")

    for (v, peso) in grafo[u]["vizinhos"]:
        if grafo[v]["cor"] == "branco":
            DFS_visit(v, iteration + 1)
    
    grafo[u]["cor"] = "preto"
    mark += 1
    grafo[u]["f"] = mark

def DFS():
    global mark
    iteration = 1
    for u in grafo:
        grafo[u]["cor"] = "branco"
    mark = 0

    if inicio in grafo and grafo:
        if not grafo[inicio]["vizinhos"]:
            print('Ponto inicial sem vizinhos para percorrer')
        else:
            global bench; bench = True
            DFS_visit(inicio, iteration)
    else:
        print('Ponto inicial não contido no grafo')

    #for u in grafo:
    #    if grafo[u]["cor"] == "branco":
    #        DFS_visit(u, iteration)
    #        iteration += 1

def data_input():
    global inicio
    global final

    with open('input.txt', 'r') as arq:
        # Lendo ponto inicial e final
        inicio = arq.readline().strip().replace("ponto_inicial(", "").replace(")", "")
        final = arq.readline().strip().replace("ponto_final(", "").replace(")", "")
        
        # Inicializando o grafo com nós e seus vizinhos
        for linha in arq:
            if linha.startswith("pode_ir("):
                info = linha.replace("pode_ir(", "").replace(")", "").split(',')
                u = info[0]
                v = info[1]
                p = int(info[2])
                
                # Inicializando os nós caso ainda não existam no grafo
                if u not in grafo:
                    grafo[u] = {"cor": "indefinido", "d": 0, "f": 0, "vizinhos": []}
                if v not in grafo:
                    grafo[v] = {"cor": "indefinido", "d": 0, "f": 0, "vizinhos": []}
                
                grafo[u]["vizinhos"].append((v, p))

def run_dfs():
    data_input()
    DFS()
    #print(grafo)
    if bench:
        print("Fim da execução")
        print(f"Distância total: {mark}")
        print(f"Caminho final: {inicio} -> {final}")
        print(f"Medida de desempenho final: {performance_measure:.1f}")
        reset_info()
