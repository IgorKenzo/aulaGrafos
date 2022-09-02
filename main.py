from grafo import Graph, dfs, le_arquivo_grafo_direcionado, tem_ciclo


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
    
#########################

    # g = le_arquivo_grafo_direcionado("in.txt")
    # g.mostra()


###################
    # g = Graph(v=6, e = None, direcionado = True,usaMatriz = False)
    # g.insere(0,1)
    # g.insere(0,4)
    # g.insere(2,0)
    # g.insere(2,3)
    # g.insere(2,4)
    # g.insere(3,4)
    # g.insere(3,5)
    # g.insere(4,1)
    # g.insere(4,5)
    # g.insere(5,0)
    # g.mostra()
    # dfs(g)
    # print(g.inverte_lista_adjacencia(2))

###########
    """ Não tem ciclo"""
    # g = Graph(v=6, e = None, direcionado = True,usaMatriz = True)
    # g.insere(0,1)
    # g.insere(0,4)
    # g.insere(2,0)
    # g.insere(2,3)
    # g.insere(2,4)
    # g.insere(3,4)
    # g.insere(3,5)
    # g.insere(4,1)
    # g.insere(4,5)
    # g.insere(5,1)
    # g.mostra()

    # print(tem_ciclo(g))

###########
    """ TEm ciclo """
    g = Graph(v=3, e = None, direcionado = True,usaMatriz = False)
    g.insere(0,1)
    g.insere(1,2)
    g.insere(2,0)

    g.mostra()

    print(tem_ciclo(g))