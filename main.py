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

def gerlistaaI(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def gerlistaaO(tam):
    lista = list(range(1, tam + 1))
    return lista
"""FUNÇÕES DE GERAÇÃO DE LISTA"""

saidaSwaps = []

""""FUNÇÃO PARA DESENHAR GRAFICO"""
def desenhaGrafico(x,BSort,ISort,SSort,SHSort,MSort,QSort,RSort,HSort, xLabel = "Entradas", yLabel = "Saídas", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,BSort, label = "Bubble Sort")
    ax.plot(x,ISort, label = "Insertion Sort")
    ax.plot(x,SSort, label = "Selection Sort")
    ax.plot(x,SHSort, label = "Shell Sort")
    ax.plot(x,MSort, label = "Merge Sort")
    ax.plot(x,QSort, label = "Quick Sort")
    ax.plot(x,RSort, label = "Radix Sort")
    ax.plot(x,HSort, label = "Heap Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)
""""FUNÇÃO PARA DESENHAR GRAFICO"""

""""FUNÇÕES PARA ORDENAÇÃO"""
def BSort(lista):
  for i in range(len(lista)):
    for j in range(0, len(lista)-i-1):
      if lista[j] > lista[j+1]:
        aux=lista[j]
        lista[j]=lista[j+1]
        lista[j+1]=aux

def ISort(lista): 
  for i in range(1, len(lista)): 
    pivo=lista[i] 
    j=i-1
    while j>=0 and pivo<lista[j]: 
      lista[j+1]=lista[j] 
      j-=1
    lista[j+1]=pivo

def SSort(lista):
  for i in range(len(lista)): 
    indexadorMinimo=i 
    for j in range(i+1, len(lista)): 
        if lista[indexadorMinimo]>lista[j]: 
            indexadorMinimo=j 
    aux=lista[i]
    lista[i]=lista[indexadorMinimo]
    lista[indexadorMinimo]=aux

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

def particao(lista,com,fim): 
  i = ( com-1 )
  pivo = lista[fim]
  for j in range(com , fim): 
    if   lista[j] <= pivo: 
      i = i+1 
      lista[i],lista[j] = lista[j],lista[i] 
  lista[i+1],lista[fim] = lista[fim],lista[i+1] 
  return ( i+1 ) 
def QSort(lista,com,fim): 
  if com<fim: 
    aux = particao(lista,com,fim) 
    QSort(lista, com, aux-1) 
    QSort(lista, aux+1, fim)
def preQuick(lista):
  QSort(lista,0,len(lista)-1)

def CSort(lista, exp1): 
  n = len(lista) 
  saida = [0] * (n) 
  count = [0] * (10) 
  for i in range(0, n): 
    aux = int((lista[i]/exp1) )
    count[ (aux)%10 ] += 1
  for i in range(1,10): 
    count[i] += count[i-1] 
  i = n-1
  while i>=0: 
    aux = (lista[i]/exp1) 
    saida[ count[ int((aux)%10) ] - 1] = lista[i] 
    count[ int((aux)%10) ] -= 1
    i -= 1
  i = 0
  for i in range(0,len(lista)): 
    lista[i] = saida[i] 
def RSort(lista): 
  maximo = max(lista) 
  exp = 1
  while maximo/exp > 0: 
    CSort(lista,exp) 
    exp *= 10

def heap(lista, n, i): 
  maior = i
  es = 2 * i + 1
  di = 2 * i + 2
  if es < n and lista[i] < lista[es]:
    maior = es 
  if di < n and lista[maior] < lista[di]: 
    maior = di
  if maior != i: 
    lista[i], lista[maior] = lista[maior],lista[i]
    heap(lista, n, maior)

def HSort(lista): 
  n = len(lista)
  for i in range(n, -1, -1): 
    heap(lista, n, i) 
  for i in range(n-1, 0, -1): 
    lista[i], lista[0] = lista[0], lista[i]
    heap(lista, i, 0) 
""""FUNÇÃO PARA DESENHAR GRAFICO"""


lista = [1,10,100,1000]
saidaB = []
saidaI = []
saidaS = []
saidaSH = []
saidaM = []
saidaQ = []
saidaR = []
saidaH = []


for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaB.append(timeit.timeit("BSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,BSort",number=1))
  print("Terminou: "+str(lista[i])
for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaI.append(timeit.timeit("ISort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,ISort",number=1))
  print("Terminou: "+str(lista[i])
for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaS.append(timeit.timeit("SSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,SSort",number=1))
  print("Terminou: "+str(lista[i])
for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaSH.append(timeit.timeit("SHSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,SHSort",number=1))
  print("Terminou: "+str(lista[i])
for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaM.append(timeit.timeit("preMerge({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,preMerge",number=1))
  print("Terminou: "+str(lista[i])
for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaQ.append(timeit.timeit("preQuick({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,preQuick",number=1))
  print("Terminou: "+str(lista[i])
for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaR.append(timeit.timeit("RSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,RSort",number=1))
  print("Terminou: "+str(lista[i])
for i in range(len(lista)):
  print("Começou: "+str(lista[i])
  saidaH.append(timeit.timeit("HSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,HSort",number=1))
  print("Terminou: "+str(lista[i])

desenhaGrafico(lista,saidaB,saidaI,saidaS,saidaSH,saidaM,saidaQ,saidaR,saidaH,nam="Tempo")
