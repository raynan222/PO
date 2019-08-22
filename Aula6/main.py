import timeit
from random import *
import matplotlib.pyplot as plt

"""FUNÇÕES DE GERAÇÃO DE LISTA"""
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista

def gerlistaaI(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def gerlistaaO(tam):
    lista = list(range(1, tam + 1))
    return lista
"""FUNÇÕES DE GERAÇÃO DE LISTA"""

""""FUNÇÃO PARA DESENHAR GRAFICO"""
def desenhaGrafico(x,SHSort , xLabel = "Entradas", yLabel = "Saídas", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,SHSort, label = "Shell Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)
""""FUNÇÃO PARA DESENHAR GRAFICO"""

""""FUNÇÕES PARA ORDENAÇÃO"""
def SHSort(lista): 
  gap=int(len(lista)/2) 
  while gap > 0: 
    for i in range(gap,len(lista)): 
      aux=lista[i] 
      j=i 
      while j>=gap and lista[j-gap]>aux: 
        lista[j]=lista[j-gap] 
        j-=gap 
      lista[j]=aux
    gap=int(gap/2)
""""FUNÇÃO PARA DESENHAR GRAFICO"""


lista = [100000, 200000, 400000, 500000, 1000000, 2000000]
saidaSH = []

for i in range(len(lista)):
  print("Começou: " + str(lista[i]))
  saidaSH.append(timeit.timeit("SHSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,SHSort",number=1))
  print("Terminou: "+str(lista[i]))

desenhaGrafico(lista, saidaSH, nam="Tempo")
