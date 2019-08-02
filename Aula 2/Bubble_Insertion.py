import timeit
from random import randint
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,BSort,ISort,xl = "Entradas", yl = "Saídas",nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,BSort, label = "Bubble Sort")
    ax.plot(x,ISort, label = "Insertion Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def BSort(lista):
  count=0
  for i in range(len(lista)):
    for j in range(0, len(lista)-i-1):
      if lista[j] > lista[j+1]:
        count+=1
        aux=lista[j]
        lista[j]=lista[j+1]
        lista[j+1]=aux

def ISort(lista):
  count=0
  for i in range(1, len(lista)):
    pivo=lista[i]
    j=i-1
    while j>=0 and pivo<lista[j]:
      count += 1
      lista[j+1]=lista[j]
      j-=1
    lista[j+1]=pivo

lista = [10000, 20000, 50000, 100000]

saidaB = []
saidaI = []

saidaSB = []
saidaSI = []

for i in range(len(lista)):
  saidaB.append(timeit.timeit("BSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,BSort",number=1))
  saidaI.append(timeit.timeit("ISort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,ISort",number=1))
  print(lista[i])
desenhaGrafico(lista,saidaB,saidaI,nam="Tempo",yl="Tempo")

for i in range(len(lista)):
  saidaSB.append(timeit.timeit("BSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,BSort",number=1))
  saidaSI.append(timeit.timeit("ISort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,ISort",number=1))
  print(lista[i])
desenhaGrafico(lista,saidaSB,saidaSI,nam="Swaps",yl="Swaps")
