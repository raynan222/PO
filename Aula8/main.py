import timeit
from random import *
import matplotlib.pyplot as plt
import math

"""FUNÇÕES DE GERAÇÃO DE LISTA"""


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


"""FUNÇÕES DE GERAÇÃO DE LISTA"""

"""FUNÇÃO PARA DESENHAR GRAFICO"""


def desenhaGrafico(x, BUSort, xLabel="Entradas", yLabel="Saídas", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x, BUSort, label="Bucket Sort")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)


"""FUNÇÃO PARA DESENHAR GRAFICO"""

"""FUNÇÕES PARA ORDENAÇÃO"""


def bucketsort(lista):
    hasheada = hashing(lista)
    buckets = [list() for _ in range(hasheada[1])]

    for i in lista:
        x = reHashing(i, hasheada)
        buck = buckets[x]
        buck.append(i)

    for bucket in buckets:
        insertionsort(bucket)

    novoIndex = 0
    for b in range(len(buckets)):
        for v in buckets[b]:
            lista[novoIndex] = v
            novoIndex += 1


def hashing(lista):
    cur = lista[0]
    for i in range(1, len(lista)):
        if (cur < lista[i]):
            cur = lista[i]
    resultado = [cur, int(math.sqrt(len(lista)))]
    return resultado


def insertionsort(lista):
    for i in range(1, len(lista)):
        sup = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > sup:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = sup
    return lista


def reHashing(i, hasheada):
    return int(i / hasheada[0] * (hasheada[1] - 1))


"""FUNÇÕES PARA ORDENAÇÃO"""

lista = [100000, 200000, 400000, 500000, 1000000, 2000000]
saidaBU = []

for i in range(len(lista)):
    print("Começou: " + str(lista[i]))
    saidaBU.append(timeit.timeit("bucketsort({})".format(geraLista(lista[i])), setup="from __main__ import geraLista,bucketsort", number=1))
    print("Terminou: " + str(lista[i]))

desenhaGrafico(lista, saidaBU, nam="Tempo")
