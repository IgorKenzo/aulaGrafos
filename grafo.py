from functools import reduce
# 1
class Graph():
    """Construa uma classe Digrafo para representar o grafo orientado utilizando a matriz de adjacência."""
    def __init__(self, v : int = 0, e = None, direcionado = False, usaMatriz = False):
        self.v = v
        self.le = e
        self.direcionado = direcionado
        self.usaMatriz = usaMatriz
        self.cria_lista_adjacencia()

    def cria_lista_adjacencia(self):
        if not self.usaMatriz:
            self.e = [[] for _ in range(self.v)]
        else:
            self.e = [[0 for _ in range(self.v)] for _ in range(self.v)]

        
        if self.le != None:
                for u,w in self.le:
                    self.insere(u,w)


    def insere(self, u, w):

        if not self.usaMatriz:
            self.e[u].append(w)
            if not self.direcionado:
                self.e[w].append(u)
        else:
            self.e[u][w] = 1
            if not self.direcionado:
                self.e[w][u] = 1

    def remov(self, u, w):
        if not self.usaMatriz:
            self.e[u][w] = 0
            if not self.direcionado:
                self.e[w][u] = 0
        else:
            self.e[u].remove(w)
            if not self.direcionado:
                self.e[w].remove(u)

    def mostra(self):
        print(f"V =  {self.v}")
        if self.usaMatriz:
            print(f"E = \n")
            for i in self.e:
                print(i)
        else:
            for i,v in enumerate(self.e):
                print(f"{i} -> {v}")

    ### 3 
#     Escreva um método grau entrada() que calcula o grau de
# entrada de um vértice v de um digrafo. Escreva também a função
# grau saida() que calcula o grau de saída de v no digrafo. As
# funções devem ser implementadas na classe Digrafo que utiliza
# uma matriz de adjacência.
    def grau_entrada(self, v):
        """Escreva um método grau entrada() que calcula o grau de
# entrada de um vértice v de um digrafo."""
        gr = 0
        if self.usaMatriz:
            for i in range(self.v):
                gr += self.e[i][v]
        else:
            for i in range(self.v):
                gr += 1 if (v in self.e[i]) else 0

        return gr
            
    
    def grau_saida(self, v):
        """Escreva também a função
# grau saida() que calcula o grau de saída de v no digrafo."""
        if self.usaMatriz:
            return reduce(lambda a, b: a + b, self.e[v])
        else:
            return len(self.e[v])
    ### fim 3

    ### 4
    def compara_grafos(g, h):
        """Escreva uma função que decida se dois grafos são iguais.
A função deve ser implementada para classe Grafo que utiliza
matriz e listas de adjacência."""
        if g.v != h.v: return False

        if g.usaMatriz == True and h.usaMatriz == True:
            return _compara_matriz(g, h)
        elif g.usaMatriz == False and h.usaMatriz == False:
            return _compara_lista(g, h)
        else: 
            if g.usaMatriz == True and h.usaMatriz == False:
                j = Graph(h.v)
                j.e = h.e.copy()
                j.direcionado = h.direcionado
                j.usaMatriz = h.usaMatriz

                j = lista_para_matriz(j)
                return _compara_matriz(g, j)
            else:
                j = Graph(g.v)
                j.e = g.e.copy()
                j.direcionado = g.direcionado
                j.usaMatriz = g.usaMatriz


                j = lista_para_matriz(j)
                return _compara_matriz(j, h)
    ### fim 4

    ### 6
    def inverte_lista_adjacencia(self, u):
        """ Escreva uma função que recebe um digrafo armazenado em
        listas de adjacência e inverta as listas de todos os vértices do
        grafo."""
        if self.usaMatriz: print("Não usa lista de adjacencia"); return

        return list(reversed(self.e[u]))
    ### fim 6

### 5
def lista_para_matriz(g):
    """Escreva uma função que converta uma representação de grafo
em outra, por exemplo, converta um grafo armazenado em uma
matriz de adjacência em uma lista de adjacência."""
    matriz = [[ 0 for _ in range(g.v)] for _ in range(g.v)]

    for i in range(g.v):
        for j in g.e[i]:
            matriz[i][j-1] = 1

    g.e = matriz.copy()
    g.usaMatriz = True
    return g

def matriz_para_lista(g):
    """Escreva uma função que converta uma representação de grafo
em outra, por exemplo, converta um grafo armazenado em uma
matriz de adjacência em uma lista de adjacência."""
    lista = [[] for _ in range(g.v)]

    for i in range(g.v):
        for j in range(g.v):
            if g.e[i][j]:
                lista[i].append(j+1)
            
    g.e = lista.copy()
    g.usaMatriz = False
    return g
### fim 5

### 7
def le_arquivo_grafo_direcionado(filename):
    """
    Um grafo pode ser armazenado em um arquivo com o seguinte
    formato:

    Onde na primeira linha contém um inteiro V (vértice), na segunda contém um inteiro A (arestas) e nas demais linha contém
    dois inteiros pertencentes ao intervalo 0 . . V − 1. Se interpretarmos cada linha do arquivo como uma aresta, podemos dizer que
    o arquivo define um grafo com vértices 0 . . V − 1. Escreva uma
    função que receba um nome de arquivo com o formato acima e
    construa uma representação (matriz e listas de adjacência) do
    grafo.

    """
    f = open(filename, "r")
    v = int(f.readline())
    n_e = int(f.readline())
    e = []
    for _ in range(n_e):
        u_v = f.readline()
        u_v = u_v.split()
        e.append((int(u_v[0]), int(u_v[1])))

    f.close()

    return Graph(v=v, e = e, direcionado = True, usaMatriz = False)
### fim 7

### 8
def eh_fonte(g: Graph, v):
    """
    Escreva uma função que receba um dígrafo e um vértice
    como parâmetro e retorne 1 se vértice for uma fonte (grau de
    saída maior que zero e grau de entrada igual a 0), ou 0 caso
    contrário. A função deve ser implementada para a classe Grafo
    que utilizam matriz e listas de adjacência.
    """
    if not g.direcionado: return 0

    saida, entrada = 0, 0

    if g.usaMatriz:
        saida = reduce(lambda a,b: a + b, g.e[v])
        entrada = reduce(lambda a,b: a + b, [g.e[i][v] for i in range(g.v)])
    else:
        saida = len(g.e[v])
        entrada = reduce(lambda a,b: a + b, [1 if v in g.e[i] else 0 for i in range(g.v)])

    if saida > 0 and entrada == 0:
        return 1
    else:
        return 0
### fim 8

### 9
def eh_sorvedouro(g: Graph, v):
    """ Escreva uma função que receba um dígrafo e um vértice
    como parâmetro, retorne 1 se vértice for uma sorvedouro (grau
    de entrada maior que zero e grau de saída igual a 0), ou 0 caso
    contrário. A função deve ser implementada para a classe Grafo
    que utiliza matriz e listas de adjacência
    """
    if not g.direcionado: return 0

    saida, entrada = 0, 0

    if g.usaMatriz:
        saida = reduce(lambda a,b: a + b, g.e[v])
        entrada = reduce(lambda a,b: a + b, [g.e[i][v] for i in range(g.v)])
    else:
        saida = len(g.e[v])
        entrada = reduce(lambda a,b: a + b, [1 if v in g.e[i] else 0 for i in range(g.v)])

    if saida == 0 and entrada > 0:
        return 1
    else:
        return 0
### fim 9

### 10

def eh_simetrico(g: Graph):
    """
    Escreva uma função que retorna 1 se o dígrafo for simétrico
    e 0 caso contrário. Um dígrafo é simétrico se cada uma das
    arestas é anti-paralela a outra. A função deve ser implementada
    para classe Grafo que utilizam matriz e listas de adjacência.

    Exemplo: o grafo G = (V, E), com V = {1, 2, 3} e arestas E =
    {(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), } é um dígrafo simétrico.
    """
    if not g.direcionado: return 1

    if g.usaMatriz:
        for i in range(g.v):
            for j in range(g.v - i):
                if g.e[i][i+j] != g.e[i+j][i]: return 0
        return 1
    else:
        for i in range(g.v):
            for j in g.e[i]:
                if not (i in g.e[j] and j in g.e[i]): return 0
        return 1
### fim 10

def _compara_matriz(g, h):
    for i in range(g.v):
        for j in range(g.v):
            if g.e[i][j] != h.e[i][j]:
                return False
    return True

def _compara_lista(g ,h):
    for i in range(g.v):
        if len(g.e[i]) != len(h.e[i]):
            return False
        for j in range(len(g.e[i])):
            if g.e[i][j] != h.e[i][j]:
                return False
    return True

########### Aula 02 ###########
### 1
def tem_caminho(g: Graph, cam: list[int]):
    """Escreva uma função que verifique se uma dada sequência
    seq[0..k] de vértices de um grafo é um caminho. A função
    devolve 1 caso a sequencia seja um caminho e 0 caso contrário.
    Faça duas versões do método:supõe que o grafo dado por sua
    matriz de adjacência e outra supõe que o grafo é dado por listas
    de adjacência."""
    if g.usaMatriz:
        for i in range(0, len(cam)-1):
            if not g.e[cam[i]][cam[i+1]]: return 0
        return 1
    else:
        for i in range(0, len(cam)-1):
            if not cam[i+1] in g.e[cam[i]]: return 0
        return 1
### fim 1

### 2
def tem_caminho_simples(g:Graph, cam: list[int]):
    """Escreva uma função que verifique se uma dada sequência
    seq[0..k] de vértices de um grafo é um caminho simples. A
    função devolve 1 caso a sequencia seja um caminho e 0 caso
    contrário. Faça duas versões do método:supõe que o grafo dado
    por sua matriz de adjacência e outra supõe que o grafo é dado
    por listas de adjacência.
    """
    res = tem_caminho(g, cam) and (len(set(cam)) == len(cam))
    return 1 if res else 0
### fim 2


### 3
def caminho(g: Graph, s: int, t: int):
    """Dados vértices s e t de um grafo G, escreva uma função que
    retorna 1 se existe um caminho ou 0 se não existe um caminho
    de s a t em G. Faça duas versões: uma supõe que o grafo é
    dado por sua matriz de adjacência e outra supõe que o grafo
    é dado por listas de adjacência.
    """
    if s == t: return 1

    if g.usaMatriz:
        for j in range(g.v):
            if g.e[s][j] == 1:
                if s == j: continue
                else: 
                    if caminho(g, j, t): return 1
    else:
        for j in g.e[s]:
            if caminho(g, j, t): return 1
    # return False
### fim 3


### 4
def mostra_caminho(g: Graph, s: int, t: int) -> int:
    """Dados vértices s e t de um grafo G, escreva uma função que
    encontra e exibe (caso exista) um caminho de s a t. Faça duas
    versões da função: uma supõe que o grafo é dado por sua matriz
    de adjacência e outra supõe que o grafo é dado por listas de
    adjacência.
    """
    if s == t: print(s); return 1

    if g.usaMatriz:
        print(s)
        for j in range(g.v):
            if g.e[s][j] == 1:
                if s == j: continue
                else: 
                    if mostra_caminho(g, j, t): return 1
    else:
        print(s)
        for j in g.e[s]:
            if mostra_caminho(g, j, t): return 1
    # return False
### fim 4

### 5
def dfs_iterativo(g: Graph):
    visitado = [0 for _ in range(g.v)]
    stack = []

    if g.usaMatriz:
        for u in range(g.v):
            if not visitado[u]:
                print(u)
                stack.append(u)
                visitado[u] = 1
                while len(stack) > 0:
                    v = stack.pop()
                    for z, w in enumerate(g.e[v]):
                        if w == 1:
                            if not visitado[z]:
                                print(z)
                                visitado[z] = 1
                                stack.append(z)
    else:
        for u in range(g.v):
            if not visitado[u]:
                print(u)
                stack.append(u)
                visitado[u] = 1
                while len(stack) > 0:
                    v = stack.pop()
                    for w in g.e[v]:
                        if not visitado[w]:
                            print(w)
                            visitado[w] = 1
                            stack.append(w)

### fim 5

def dfs(g):
    visitados = [False for _ in range(g.v)]
    for u in range(len(g.e)):
        if not visitados[u]:
            dfs_visita(g, u, visitados)

def dfs_visita(g, u, visitados):
    visitados[u] = True
    print(u)
    for w in g.e[u]:
        if not visitados[w]:
            dfs_visita(g, w, visitados)


###########################################################
def tem_ciclo(g):
    for i in range(g.v):
        if ciclo(g, i, i): return True
    
    return False

def ciclo(g, s, e):
    if g.usaMatriz:
        for j in range(g.v):
            if g.e[s][j] == 1:
                if j == e: return True
                if ciclo(g, j, e): return True
    else:
        for j in g.e[s]:
            if j == e: return True
            if ciclo(g, j, e): return True
    return False

############ Aula 4 $$#########

def remove_no(g, v):
    if g.usaMatriz:
        for i in range(g.v):
            g.e[i][v] = 0
            g.e[v][i] = 0
    else:
        g.e[v] = []
        for i in range(g.v):
            if i in g.e[i]:
                g.e[i].remove(v)


def dfs_visita_tempo(g, u, visitados, tempo, d, f, pai):
    visitados[u] = True

    tempo += 1
    d[u] = tempo

    for w in g.e[u]:
        if not visitados[w]:
            pai[w] = u
            tempo = dfs_visita_tempo(g, w, visitados, tempo, d, f, pai)    

    tempo += 1
    f[u] = tempo
    return tempo

def dfs_tempo(g: Graph):
    # for u in range(g.v):
    #     visitado[u] = 0
    #     d[u] = -1
    #     f[u] = -1
    #     pai[u] = -1

    visitado = [False for _ in range(g.v)]
    d = [-1 for _ in range(g.v)]
    f = [-1 for _ in range(g.v)]
    pai = [-1 for _ in range(g.v)]

    tempo = 0

    for u in range(g.v):
        if not visitado[u]:
            pai[u] = u
            dfs_visita_tempo(g, u, visitado, tempo, d, f, pai)

    return d, f, pai
    


def ordenacao_topologica(g: Graph):
    h = Graph(g.v,None, g.direcionado, g.usaMatriz)
    h.e = g.e.copy()

    ordem = []
    usado = [0 for _ in range(h.v)]

    while reduce(lambda a, b: a+b, usado, 0) != h.v:
        for i in range(h.v):
            if h.grau_entrada(i) == 0 and not usado[i]:
                ordem.append(i)
                usado[i] = 1
                remove_no(h ,i)
    return ordem

def grafo_induzido(g: Graph, v = []):
    if g.direcionado: exit("PRECISA SER NAO DIRECIONADO")

    for i in v:
        if i not in range(g.v): exit("Vértice não pertence ao grafo")

    qtd_v = g.v - len(v)

    vertices_restantes = list(set([i for i in range(g.v)])- set(v))
    vertices_restantes.sort()

    h = Graph(qtd_v, e= None, direcionado= False, usaMatriz=False)

    for i, vr in enumerate(vertices_restantes):
        h.e[i] = g.e[vr].copy()

        for vretirado in v:
            if vretirado in h.e[i]:
                h.e[i].remove(vretirado)


    return h

def grafo_aresta_induzido(g: Graph, e = []):
    if g.direcionado: exit("PRECISA SER NAO DIRECIONADO")

    h = Graph(g.v, e= None, direcionado= False, usaMatriz=g.usaMatriz)
    h.e = g.e.copy()

    if g.usaMatriz:
        for u,v in e:
            h.e[u][v] = 0
            h.e[v][u] = 0
    else:
        for u,v in e:
            if v in h.e[u]: h.e[u].remove(v)
            if u in h.e[v]: h.e[v].remove(u)

    return h

def eh_subgrafo(g: Graph, h: Graph):
    """Checa se h é sub grafo de g"""
    if g.direcionado or h.direcionado: exit("PRECISA SER NAO DIRECIONADO")

    for i in range(h.v):
        for j in h.e[i]: 
            if not j in g.e[i] :
                return False

    return True

def eh_subgrafo_gerador(g: Graph, h: Graph):
    if eh_subgrafo(g, h):
        for i in range(h.v):
            if not i in range(g.v): return False
        return True

    return False

####
def componentes(g: Graph):
    cc = [-1 for _ in range(g.v)]

    comp = 0

    for v in range(g.v):
        if cc[v] == -1:
            dfs_componentes(g, v, comp, cc)
            comp += 1
    
    return comp

def dfs_componentes(g: Graph, v: int, comp: int, cc: list[int]):
    cc[v] = comp

    for w in g.e[v]:
        if cc[w] == -1:
            dfs_componentes(g, w, comp, cc)

def eh_conexo(g: Graph):
    return componentes(g) == 1


def eh_bipartido(g: Graph):
    visitado = [False for _ in range(g.v)]
    cores = [-1 for _ in range(g.v)]
    cor = 0

    qual_cor = {0:[], 1:[]}

    for u in range(g.v):
        if not visitado[u]:
            dfs_bipartido(g, u, visitado, cor, cores)
    
    bipart = True
    for u in range(g.v):
        qual_cor[cores[u]].append(u)

        for v in g.e[u]:
            if cores[v] == cores[u]: bipart = False
        
    print(f"Azul: {qual_cor[0]}")
    print(f"Vermelho: {qual_cor[1]}")
    return bipart


def dfs_bipartido(g, u, visitados, cor, cores):
    visitados[u] = True
    cores[u] = cor

    for w in g.e[u]:
        if not visitados[w]:
            dfs_bipartido(g, w, visitados, 0 if cor else 1, cores)    


def detectar_pontes(g: Graph):
    tempo = 0
    pre = [-1 for _ in range(g.v)]
    pai = [-1 for _ in range(g.v)]
    low = [-1 for _ in range(g.v)]

    for v in range(g.v):
        if pre[v] == -1:
            pai[v] = v
            dfs_visita_ponte(g, v, tempo, pre, pai, low)

def dfs_visita_ponte(g: Graph, v, tempo, pre, pai, low):
    tempo += 1
    pre[v] = tempo
    low[v] = pre[v]

    for w in g.e[v]:
        if pre[w] == -1:
            pai[w] = v
            dfs_visita_ponte(g, w, tempo, pre, pai, low)
            low[v] = min(low[v], low[w])
            if low[w] == pre[w]:
                print(v, w)
        elif w != pai[v]:
            low[v] = min(low[v], pre[w])


def detectar_articulacoes(g: Graph):
    tempo = 0
    pre = [-1 for _ in range(g.v)]
    pai = [-1 for _ in range(g.v)]
    low = [-1 for _ in range(g.v)]

    for v in range(g.v):
        if pre[v] == -1:
            pai[v] = v
            dfs_visita_ponte(g, v, tempo, pre, pai, low)

def dfs_visita_articulacoes(g: Graph, v, tempo, pre, pai, low):
    tempo += 1
    pre[v] = tempo
    low[v] = pre[v]
    filhos = 0
    eh_articulacao = False

    for w in g.e[v]:
        if pre[w] == -1:
            pai[w] = v
            filhos += 1
            dfs_visita_ponte(g, w, tempo, pre, pai, low)
            low[v] = min(low[v], low[w])
            if low[w] >= pre[w]:
                eh_articulacao = True
        elif w != pai[v]:
            low[v] = min(low[v], pre[w])
    
    if(pai[v] != -1 and eh_articulacao) or (pai[v] == -1 and filhos > 0):
        print(v)