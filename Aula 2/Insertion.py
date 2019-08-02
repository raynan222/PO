import timeit
from random import randint
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,ISort,xl = "Entradas", yl = "Saídas",nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,ISort, label = "Insertion Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

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

saidaI = []

saidaSI = []

for i in range(len(lista)):
  saidaI.append(timeit.timeit("ISort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,ISort",number=1))
  print(lista[i])
desenhaGrafico(lista,saidaI,nam="Tempo",yl="Tempo")

for i in range(len(lista)):
  saidaSI.append(timeit.timeit("ISort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,ISort",number=1))
  print(lista[i])
desenhaGrafico(lista,saidaSI,nam="Swaps",yl="Swaps")
