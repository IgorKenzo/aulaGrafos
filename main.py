from grafo import *


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
    # g = Graph(v=3, e = None, direcionado = True,usaMatriz = False)
    # g.insere(0,1)
    # g.insere(1,2)
    # g.insere(2,0)

    # g.mostra()

    # print(tem_ciclo(g))
######
    """Eh fonte"""
    # g = Graph(v=3, e = None, direcionado = True, usaMatriz = False)
    # g.insere(0,1)
    # g.insere(0,2)

    # # g.mostra()

    # print(eh_sorvedouro(g,1))
#######
    """ Simetrico"""
    # g = Graph(v=4, e = [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)], direcionado = True,usaMatriz = False)
    
    # g.mostra()

    # print(eh_simetrico(g))
########
    """ caminho """
    # g = Graph(v=3, e = None, direcionado = True, usaMatriz = False)
    # g.insere(0,1)
    # g.insere(1,0)
    # g.insere(1,2)
    # print(tem_caminho_simples(g, [0,1,0,1,2]))

#######
    """outro caminho"""
    # g = Graph(v=3, e = None, direcionado = True, usaMatriz = True)
    # g.insere(0,1)
    # # g.insere(0,2)
    # g.insere(1,2)
    # # print(caminho(g, 0, 2))
    # # mostra_caminho(g, 0, 2)
    # dfs_iterativo(g)


#######
    """Topologica"""
    # g = Graph(v=6, e = None, direcionado = True,usaMatriz = True)
    # g.insere(0,2)
    # g.insere(0,4)
    # g.insere(0,3)

    # g.insere(2,1)

    # g.insere(3,4)
    # g.insere(3,5)

    # g.insere(4,1)
    # g.insere(4,2)
    # g.insere(4,5)
    
    # g.insere(5,1)
    # g.mostra()

    # print(tem_ciclo(g))
    # print(ordenacao_topologica(g))



#######
########
    """tempo só lista adj""" 
    # g = Graph(v=6, e = None, direcionado = True,usaMatriz = False)
    # g.insere(0,2)
    # g.insere(0,4)
    # g.insere(0,3)

    # g.insere(2,1)

    # g.insere(3,4)
    # g.insere(3,5)

    # g.insere(4,1)
    # g.insere(4,2)
    # g.insere(4,5)
    
    # g.insere(5,1)
    # # g.mostra()

    # dfs_tempo(g)

#####

    # """ Grafo induzido"""
    # g = Graph(v = 7, e= None, direcionado= False, usaMatriz= False)
    # g.insere(0, 1)
    # g.insere(1, 2)
    # g.insere(2, 3)
    # g.insere(3, 4)
    # g.insere(4, 5)
    # g.insere(5, 0)

    # g.insere(6, 0)
    # g.insere(6, 1)
    # g.insere(6, 2)
    # g.insere(6, 3)
    # g.insere(6, 4)
    # g.insere(6, 5)

    # # g.mostra()

    # # h = grafo_induzido(g, [0,1,2,3,4,5])
    # # h.mostra()

    # # GRAFO ARESTA INDUZIDO

    # i = grafo_aresta_induzido(g, [(6, 0),(6, 1),(6, 2),(6, 3),(6, 4),(6, 5)])
    # i.mostra()
######
 
    """ Grafo subgrafo"""
    # g = Graph(v = 6, e= None, direcionado= False, usaMatriz= False)
    # h = Graph(v = 6, e= None, direcionado= False, usaMatriz= False)

    
    # g.insere(1, 2)
    # g.insere(1, 4)
    # g.insere(2, 4)
    # g.insere(4, 3)
    # g.insere(3, 5)

    # g.mostra()

    # h.insere(1, 4)
    # h.insere(2, 4)
    # h.insere(4, 3)

    # h.mostra()


    # print(eh_subgrafo(g, h))

######
    """Numero de componenetes"""
    # g = Graph(v = 6, e= None, direcionado= False, usaMatriz= False)

    # g.insere(1, 2)
    # g.insere(1, 4)
    # g.insere(2, 4)
    # g.insere(4, 3)
    # g.insere(3, 5)

    # print(componentes(g))

######
    """Bipartido"""

    # g = Graph(v = 8, e= None, direcionado= False, usaMatriz= False)
    # g.insere(0, 1)
    # g.insere(1, 2)
    # g.insere(2, 3)
    # g.insere(3, 0)

    # g.insere(4, 5)
    # g.insere(5, 6)
    # g.insere(6, 7)
    # g.insere(7, 4)

    # g.insere(0, 4)
    # g.insere(1, 5)
    # g.insere(2, 6)
    # g.insere(3, 7)

    # print(eh_bipartido(g))

#######
    """Detectar pontes"""
    # g = Graph(v = 6, e= None, direcionado= False, usaMatriz= False)

    # g.insere(0, 1)
    # g.insere(1, 2)
    # g.insere(2, 0)

    # g.insere(1, 3)

    # g.insere(3, 4)
    # g.insere(4, 5)
    # g.insere(5, 3)

    # detectar_pontes(g)

######
    """Detectar articulações"""
    g = Graph(v = 6, e= None, direcionado= False, usaMatriz= False)

    g.insere(0, 1)
    g.insere(1, 2)
    g.insere(2, 0)

    g.insere(1, 3)

    g.insere(3, 4)
    g.insere(4, 5)
    g.insere(5, 3)

    detectar_articulacoes(g)