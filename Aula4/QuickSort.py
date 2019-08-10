import timeit
import matplotlib.pyplot as plt
import sys


"""FUNÇÕES DE GERAÇÃO DE LISTA"""
def geraListaI(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]
"""FUNÇÕES DE GERAÇÃO DE LISTA"""


""""FUNÇÃO PARA DESENHAR GRAFICO"""
def desenhaGrafico(x, QSort, xLabel = "Entradas", yLabel = "Saídas", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,QSort, label = "Quick Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)
""""FUNÇÃO PARA DESENHAR GRAFICO"""


""""FUNÇÃO PARA ORDENAÇÃO"""
def particao(lista,com,fim):
  i = (com-1)
  pivo = lista[fim]

  for j in range(com, fim):
    if lista[j] <= pivo:
      i = i+1
      lista[i], lista[j] = lista[j], lista[i]
  lista[i+1], lista[fim] = lista[fim], lista[i+1]
  return (i+1)

def QSort(lista, com, fim):
    tam = fim - com + 1
    pilha = [0] * (tam)
    topo = -1
    topo = topo + 1
    pilha[topo] = com
    topo = topo + 1
    pilha[topo] = fim

    while topo >= 0:
        fim = pilha[topo]
        topo = topo - 1
        com = pilha[topo]
        topo = topo - 1
        pivo = particao(lista, com, fim)

        if pivo - 1 > com:
            topo = topo + 1
            pilha[topo] = com
            topo = topo + 1
            pilha[topo] = pivo - 1

        if pivo + 1 < fim:
            topo = topo + 1
            pilha[topo] = pivo + 1
            topo = topo + 1
            pilha[topo] = fim

def preQuick(lista):
  QSort(lista,0,len(lista)-1)
""""FUNÇÃO PARA ORDENAÇÃO"""


saidaQ=[]
lista = [100000,200000,400000,500000,1000000,2000000]

for i in range(len(lista)):
  print("Começou: "+str(lista[i]))
  saidaQ.append(timeit.timeit("preQuick({})".format(geraListaI(lista[i])),setup="from __main__ import geraListaI,preQuick",number=1))
  print("Terminou: "+str(lista[i]))
  print(saidaQ)

desenhaGrafico(lista,saidaQ,nam="Tempo",yLabel='Tempo')
