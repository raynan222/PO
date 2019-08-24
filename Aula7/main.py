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
def desenhaGrafico(x,CSort, xLabel = "Entradas", yLabel = "Saídas", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,CSort, label = "Counting Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)
""""FUNÇÃO PARA DESENHAR GRAFICO"""

""""FUNÇÕES PARA ORDENAÇÃO"""
def Csort(lista, maior):
    indice = maior + 1
    count = [0] * indice
    for i in lista:
        count[i] += 1
    j = 0
    for i in range(indice):
        for k in range(count[i]):
            lista[j] = i
            j += 1

def preCount(lista):
    maior=max(lista)
    Csort(lista, maior)
""""FUNÇÃO PARA DESENHAR GRAFICO"""

lista = [100000, 200000, 400000, 500000, 1000000, 2000000]
saidaC = []

for i in range(len(lista)):
  print("Começou: "+str(lista[i]))
  saidaC.append(timeit.timeit("preCount({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,preCount",number=1))
  print("Terminou: "+str(lista[i]))

desenhaGrafico(lista,saidaC,nam="Tempo")
