import numpy as np
import random as rand


def losuj_macierz(m=5, n=5):
    tablica = np.zeros((m, n))
    oceny = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
    for a in range(m):
        for b in range(n):
            tablica[a][b] = rand.choice(oceny)
    return tablica


tablica = losuj_macierz(50, 5)
# print(tablica)


def ile_niezdalo(tablica):
    licznik = 0
    for x in range(tablica.shape[0]):
        czy_dodano = False
        for y in range(tablica.shape[1]):
            if tablica[x][y] < 3 and not czy_dodano:
                licznik += 1
                czy_dodano = True
    return licznik


def srednie(tablica):
    lista = []
    for x in range(tablica.shape[0]):
        lista.append((np.average(tablica[x]), tablica[x]))
    lista.sort()
    return lista


# lista = srednie(tablica)
# print(f"Najgorsza średnia: {lista[0]}")
# print(f"Najlepsza średnia: {lista[-1]}")
from collections import Counter


def najlepsze_oceny(tablica):
    oceny = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
    slownik = dict()
    for x in oceny:
        slownik[x] = list()
    for x in range(tablica.shape[0]):
        for y in range(tablica.shape[1]):
            slownik[tablica[x][y]].append(x)
    print(slownik)
    # print(slownik.values())
    val_count = Counter(list(slownik.values())[-1])
    x = val_count.most_common()[0][0]
    print(tablica[x])


najlepsze_oceny(tablica)
import seaborn as sns
import matplotlib.pyplot as plt


def histogramy(tablica):
    for x in range(tablica.shape[1]):
        sns.histplot(tablica[:, x])
        plt.show()


histogramy(tablica)


def nie_nizsza_srednia(tablica, prog=4.0):
    lista = srednie(tablica)

    for x in lista:
        if x[0] > prog:
            print(x)


# nie_nizsza_srednia(tablica)

a = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
b = np.array([[5, 4, 3], [4, 5, 6], [6, 7, 8]])


def odleglosc(a, b):
    print(sum(sum(abs(a - b))))


do_zredukowania = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [15, 12, 7, 3]])


def gauss(a):
    for x in range(a.shape[0] - 1):
        for y in range(x + 1, a.shape[0]):
            print(a[x], x, a[y], y)
            a[y] = a[y] - (a[y][x] / a[x][x]) * a[x]
            print(a)


# gauss(do_zredukowania)

######### Zad 4
# macierz 1 [NR_klienta;NumerProduktu;Ilość]
macierz1 = np.array(
    [[1, 2, 3, 4, 5, 1, 2], [5, 1, 2, 3, 5, 3, 4], [2, 5, 12, 32, 13, 12, 2]]
)
macierz1 = macierz1.transpose()
print(macierz1)
# macierz 2 [NR_towaru;Cena]
macierz2 = np.array([[1, 5], [2, 4], [3, 12], [4, 5], [5, 10]])
print(macierz2)


def czy_prod_istnieją(macierz1, macierz2):
    set_kupionych = set(macierz1[:, 1])
    set_bazy_danych = set(macierz2[:, 0])
    if len(set_kupionych - set_bazy_danych) > 0:
        print(
            "Na paragonie są produkty, których nie ma w bazie danych, id:",
            (set_kupionych - set_bazy_danych),
        )
    else:
        print("Produkty są poprawne")


def cena_paragonu(macierz1, macierz2):
    klienci = set(macierz1[:, 1])
    paragon = dict()
    for x in klienci:
        paragon[x] = 0
    for a in macierz1:
        nr_klienta = a[0]
        nr_prod = a[1]
        ilosc = a[2]
        for b in macierz2:
            nr_prod2 = b[0]
            cena = b[1]
            if nr_prod == nr_prod2:
                paragon[nr_klienta] += ilosc * cena
    print(paragon)


czy_prod_istnieją(macierz1, macierz2)
cena_paragonu(macierz1, macierz2)
