from random import *
import matplotlib.pyplot as plt
import timeit

"""FUNÇÕES DE GERAÇÃO DE LISTA"""
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista

def geraListaI(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def geraListaO(tam):
    lista = list(range(1, tam + 1))
    return lista
"""FUNÇÕES DE GERAÇÃO DE LISTA"""

"""PerimetroSort"""
def PerimetroSort(lista,inicio,fim):
  while fim>inicio:
    for i in range(fim):
      if lista[fim]<lista[i]:
        lista[i],lista[fim]=lista[fim],lista[i]
      if lista[inicio]<lista[i]:
        lista[inicio],lista[i]=lista[i],lista[inicio]
    inicio+=1
    fim-=1
  return lista

def PP(lista):
  PerimetroSort(lista,0,len(lista)-1)
"""PerimetroSort"""

"""FUNÇÃO PARA DESENHAR GRAFICO"""
def desenhaGrafico(x, saidaOrdenada,saidaRandomica,saidaDecrescente, xLabel = "Numeros no vetor", yLabel = "Tempo", nam="img"): 
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,saidaOrdenada, label = "Perimetro Sort LISTA ORDENADA")
    ax.plot(x,saidaRandomica, label = "Perimetro Sort LISTA RANDOMICA")
    ax.plot(x,saidaDecrescente, label = "Perimetro Sort LISTA DECRESCENTE")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)
"""FUNÇÃO PARA DESENHAR GRAFICO"""

lista = [100,1000,10000,100000]
print (lista)
saidaOrdenada = []
saidaRandomica = []
saidaDecrescente = []

for i in range(len(lista)):
  print("Começou: "+str(lista[i]))
  saidaOrdenada.append(timeit.timeit("PP({})".format(geraListaO(lista[i])),setup="from __main__ import geraListaO,PP",number=1))
  saidaRandomica.append(timeit.timeit("PP({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,PP",number=1))
  saidaDecrescente.append(timeit.timeit("PP({})".format(geraListaI(lista[i])),setup="from __main__ import geraListaI,PP",number=1))
  print("Terminou: "+str(lista[i]))

desenhaGrafico(lista,saidaOrdenada,saidaRandomica,saidaDecrescente)
