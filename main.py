from grafo import Graph


if __name__ == "__main__":
    # g = Graph(5)
    # g.insere(1,2)
    # g.insere(1,3)
    # g.insere(2,3)
    # g.mostra()
    # print(g.grau_saida(1))
    # print(g.grau_entrada(3))


    # g = Graph(5, [(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)])
    # g.mostra()

    # g = Graph(4, [(1, 2), (1, 3), (3, 2), (2, 4), (4, 3), (2, 2)], True)
    # g.mostra()

    # g = Graph(5,None,True,True)
    # g.insere(1,2)
    # g.insere(1,3)
    # g.insere(2,3)
    # g.mostra()
    # print(g.grau_saida(1))
    # print(g.grau_entrada(3))

    # g = Graph(5)
    # g.insere(1,2)
    # g.insere(1,3)
    # g.insere(2,3)
    # g.mostra()

    # g = Graph.lista_para_matriz(g)
    # g.mostra()

    # g = Graph(5,None,True,True)
    # g.insere(1,2)
    # g.insere(1,3)
    # g.insere(2,3)
    # g.mostra()

    # g.matriz_para_lista()
    # g.mostra()
################
    # g = Graph(5,None,True,True)
    # g.insere(1,2)
    # g.insere(1,3)
    # g.insere(2,3)

    # h = Graph(5,None,True,False)
    # h.insere(1,2)
    # h.insere(1,3)
    # h.insere(2,3)

    # print(Graph.compara_grafos(g, h))
    
###################
    g = Graph(v=6, e = None, direcionado = True,usaMatriz = False)
    g.insere(1,2)
    g.insere(1,5)
    g.insere(3,1)
    g.insere(3,4)
    g.insere(3,5)
    g.insere(4,5)
    g.insere(4,6)
    g.insere(5,2)
    g.insere(5,6)
    g.insere(6,1)
    g.mostra()
    #Graph.dfs_visita(g, 1)
    print(g.inverte_lista_adjacencia(2))