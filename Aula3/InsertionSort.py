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

def geraListaO(tam):
    lista =[]
    aux=1
    while aux<tam+1:
      lista.append(aux)
      aux+=1
    return lista

def desenhaGrafico(x,ISort,IISort,xl = "Entradas", yl = "Saídas",nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,ISort, label = "Insertion Sort")
    ax.plot(x,IISort, label = "Insertion Sort INVERTIDO")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)
    
saidaSwap = []
def ISort(lista):
  count=0
  for i in range(1, len(lista)): 
    pivo=lista[i] 
    j=i-1
    while j>=0 and pivo<lista[j]:
      count+=1
      lista[j+1]=lista[j] 
      j-=1
    lista[j+1]=pivo
  saidaSwap.append(count)

lista = [10000, 20000, 50000, 100000]
saidaS = []
saidaSI = []

for i in range(len(lista)):
  saidaS.append(timeit.timeit("ISort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,ISort",number=1))
  print(lista[i])
for i in range(len(lista)):
  saidaSI.append(timeit.timeit("ISort({})".format(geraListaI(lista[i])),setup="from __main__ import geraListaI,ISort",number=1))
  print(lista[i])

print(saidaSwap)
desenhaGrafico(lista,saidaS,saidaSI,nam="Tempo",yl="Tempo")
desenhaGrafico(lista,saidaSwap[0:4],saidaSwap[4:],nam="Swaps",yl="Swaps")
