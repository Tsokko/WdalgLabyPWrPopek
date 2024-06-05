import random


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def _length(self):
        itr = self.head
        counter = 0
        while itr:
            itr = itr.next
            counter += 1
        return counter

    def _pop(self, searched):
        if self._length() == 0:
            return None

        itr = self.head

        if searched == "E":
            self.head = itr.next
            return itr.data

        prev = None

        while itr:
            if itr.data[0] == searched:
                if prev:
                    prev.next = itr.next
                else:
                    self.head = itr.next
                return itr.data
            prev = itr
            itr = itr.next

        return None

    def delete_at(self, n):
        itr = self.head
        while itr:
            if n - 1 == 0:
                itr.next = itr.next.next
                print("ded")
                return
            else:
                n -= 1
                print("aa", itr.data, itr.next)
                itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


okienka = [
    ["A", 3],
    ["A", 3],
    ["A", 3],
    ["B", 7],
    ["B", 7],
    ["B", 7],
    ["C", 13],
    ["C", 13],
    ["C", 13],
    ["E", 9],
]

okienka2 = [
    ["A", 3],
    ["A", 3],
    ["A", 3],
    ["B", 7],
    ["B", 7],
    ["B", 7],
    ["C", 13],
    ["C", 13],
    ["C", 13],
]
okienka3 = [
    ["A", 3],
    ["A", 3],
    ["B", 7],
    ["B", 7],
    ["C", 13],
    ["E", 9],
    ["E", 9],
    ["E", 9],
]

okienka4 = [
    ["A", 3],
    ["B", 7],
    ["B", 7],
    ["C", 13],
    ["C", 13],
    ["C", 13],
    ["E", 9],
]


def ktores_pelne(okienka):
    for x in okienka:
        if x[1] is not None:
            return True
    return False


def odejmij_z_kazdego(okienka):
    for x in range(len(okienka)):
        # print(okienka)
        # print(okienka[x], okienka[x][1])
        if okienka[x][1] == None:
            continue
        elif okienka[x][1] == 1:
            okienka[x][1] = None
        else:
            okienka[x][1] -= 1
    # print(okienka)
    return okienka


def dodaj_klientów(lista, n):
    mozliwi_klienci = (
        [["A", x] for x in range(1, 5)]
        + [["B", x] for x in range(5, 9)]
        + [["C", x] for x in range(9, 13)]
    )
    for _ in range(n):
        lista.insert(random.choice(mozliwi_klienci))


def glowna_petla(okienka, lista):
    iteracja = 0
    # lista.print()
    liczba_obsluzonych_w_okienku = dict()
    # print(okienka)
    # print(ktores_pelne(okienka))
    while ktores_pelne(okienka):
        okienka = odejmij_z_kazdego(okienka)
        iteracja += 1
        # print(okienka, end="\n")
        # print(okienka)

        for x in range(len(okienka)):
            if okienka[x][1] == None:
                popped = lista._pop(okienka[x][0])
                if popped == None:
                    continue
                else:
                    okienka[x][1] = popped[1]
                    if x not in liczba_obsluzonych_w_okienku:
                        liczba_obsluzonych_w_okienku[x] = 0
                    else:
                        liczba_obsluzonych_w_okienku[x] += 1
    print(f"{iteracja=}")
    liczba_obsluzonych_w_okienku = dict(sorted(liczba_obsluzonych_w_okienku.items()))
    print(liczba_obsluzonych_w_okienku)
    return iteracja


import copy
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

lista_okienek = [okienka, okienka2, okienka3, okienka4]
lista_wyników = []
for x in range(len(lista_okienek)):
    temp = []
    for _ in range(100):
        lista = LinkedList()
        dodaj_klientów(lista, 30)
        temp.append(glowna_petla(copy.deepcopy(lista_okienek[x]), lista))
    lista_wyników.append(temp)

print([np.mean(x) for x in lista_wyników])


sns.histplot(lista_wyników, multiple="fill")
plt.show()
