import timeit
from random import randint
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
def geraListaI(tam):
    lista =[]
    while tam:
      lista.append(tam)
      tam-=1
    return lista

def desenhaGrafico(x,SSort,SISort,xl = "Entradas", yl = "Saídas",nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,SSort, label = "Selection Sort")
    ax.plot(x,SISort, label = "Selection Sort INVERTIDO")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def SSort(lista):
  count=0
  for i in range(len(lista)):
    indexadorMinimo=i
    for j in range(i+1, len(lista)):
        if lista[indexadorMinimo]>lista[j]:
            indexadorMinimo=j
            count = count+1
    aux=lista[i]
    lista[i]=lista[indexadorMinimo]
    lista[indexadorMinimo]=aux
  return count

lista = [10000, 20000, 50000, 100000]
saidaS = []
saidaSI = []
saidaSW = []
saidaSWI = []



for i in range(len(lista)):
  saidaS.append(timeit.timeit("SSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,SSort",number=1))
  saidaSI.append(timeit.timeit("SSort({})".format(geraListaI(lista[i])),setup="from __main__ import geraListaI,SSort",number=1))
  print(lista[i])
desenhaGrafico(lista,saidaS,saidaSI,nam="Tempo",yl="Tempo")

for i in range(len(lista)):
  saidaSW.append(SSort(geraLista(lista[i])))
  saidaSWI.append(SSort(geraListaI(lista[i])))
  print(lista[i])
desenhaGrafico(lista,saidaSW,saidaSWI,nam="Swaps",yl="Swaps")
