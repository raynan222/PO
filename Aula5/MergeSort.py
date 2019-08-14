import timeit
from random import *
import matplotlib.pyplot as plt


"""

Utilizar count para contagem que o professor desejar
Utilizar saidaSwap.append(count)para armazenar a contagem do plot.
Utilizar return count no fim das funções de ordenação

desenhaGrafico(lista,saidaS,saidaSI,nam="Tempo",yl="Tempo")
desenhaGrafico(lista,saidaSwaps[0:4],saidaSwaps[4:],nam="Swaps",yl="Swaps")

"""

"""FUNÇÕES DE GERAÇÃO DE LISTA"""
def geraLista(tam):
  lista = list(range(1, tam + 1))
  shuffle(lista)
  return lista
def geraListaI(tam):
    lista =[]
    while tam:
      lista.append(tam)
      tam-=1
    return lista

def geraListaO(tam):
    lista =[]
    aux=1
    while aux<tam+1:
      lista.append(aux)
      aux+=1
    return lista
"""FUNÇÕES DE GERAÇÃO DE LISTA"""

saidaSwaps = []

""""FUNÇÃO PARA DESENHAR GRAFICO"""
def desenhaGrafico(x,MSort, xLabel = "Entradas", yLabel = "Saídas", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,MSort, label = "Merge Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)
""""FUNÇÃO PARA DESENHAR GRAFICO"""

""""FUNÇÕES PARA ORDENAÇÃO"""
def merge(lista, es, me, di): 
  aux1=me-es+1
  aux2=di-me 
  L=[0]*(aux1) 
  R=[0]*(aux2) 
  for i in range(0 , aux1): 
    L[i] = lista[es + i] 
  for j in range(0 , aux2): 
    R[j] = lista[me + 1 + j] 
  i = 0
  j = 0
  k = es
  while i < aux1 and j < aux2:
    if L[i] <= R[j]: 
      lista[k] = L[i] 
      i += 1
    else: 
      lista[k] = R[j] 
      j += 1
    k += 1
  while i < aux1:
    lista[k] = L[i] 
    i += 1
    k += 1
  while j < aux2:
    lista[k] = R[j] 
    j += 1
    k += 1
def MSort(lista,es,di): 
  if es < di:
    me = int((es+(di-1))/2)
    MSort(lista, es, me) 
    MSort(lista, me+1, di) 
    merge(lista, es, me, di) 
def preMerge(lista):
  MSort(lista,0,len(lista)-1)

   #print("Merging ",alist)
""""FUNÇÃO PARA DESENHAR GRAFICO"""


lista = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
saidaM = []


for i in range(len(lista)):
  print("Começando: "+str(lista[i]))
  saidaM.append(timeit.timeit("preMerge({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,preMerge",number=1))
  print("Terminou: "+str(lista[i]))
desenhaGrafico(lista,saidaM,nam="Tempo")
