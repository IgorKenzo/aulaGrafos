from functools import reduce
# 1
class Graph():
    """Construa uma classe Digrafo para representar o grafo orientado utilizando a matriz de adjacência."""
    def __init__(self, v = None, e = None, direcionado = False, usaMatriz = False):
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
                if not ( i in g.e[j] and j in g.e[i]): return 0
        return 1
            

### fim 10

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

    