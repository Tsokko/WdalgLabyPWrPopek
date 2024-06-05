L = [3, 4, 5, 1, 2, 4, 3, 2, 1]


def bubble_sort_z_przew(L):
    for i in range(len(L)):
        zmiany = 0
        for j in range(0, len(L) - 1):
            if L[j] > L[j + 1]:
                zmiany += 1
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
        if zmiany == 0:
            return L
    return L


def bubble_sort(L):
    for i in range(len(L)):
        for j in range(0, len(L) - 1 - i):
            if L[j] > L[j + 1]:
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
    return L


def bubble_sort_naiwny(L):
    for i in range(len(L)):
        for j in range(0, len(L) - 1):
            if L[j] > L[j + 1]:
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
    return L


# print(bubble_sort(L))


def insertion_sort(L):
    for i in range(len(L)):
        for j in range(0, i):
            if L[i] < L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L


# print(insertion_sort(L))


def selection_sort(L):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L


# print(selection_sort(L))
import random


class Generator_tablic:
    def __init__(self, tablica) -> None:
        self.tablica = tablica

    def generuj_n_elementowa_tablice(self, n):
        return list(random.randint(0, 1000) for _ in range(n))

    def generuj_y_tablic(self, y, n):
        lista_list = []
        for _ in range(y):
            lista_list.append(self.generuj_n_elementowa_tablice(n))
        return lista_list


import time
from numpy import log10, mean
import seaborn as sns
import matplotlib.pyplot as plt


class Timer:
    def __init__(self, tablica, sorter) -> None:
        self.tablica = tablica
        self.sorter = sorter
        self.times = []
        self.max_times = []
        self.mean_times = []

    def run_algo(self):
        for x in self.tablica:
            start = time.time()
            self.sorter(x)
            stop = time.time()
            interval = stop - start
            self.times.append(interval)
        self.analyze()

    def analyze(self):
        self.max_times.append(max(self.times))
        self.mean_times.append(mean(self.times))

    def plot(self):
        sns.lineplot(
            {"Średni czas": self.mean_times, "Maksymalny czas": self.max_times}
        )
        plt.title(f"Maksymalne i średnie czasu dla: {self.sorter.__name__}")
        plt.xlabel("Index")
        plt.ylabel("Czas w ms")
        plt.show()


def run(algorytmy, n):
    a = Generator_tablic(tablica=[])
    for algorytm in algorytmy:
        list_of_lists = []
        for num in n:
            list_of_lists.append(a.generuj_y_tablic(10, num))

        obj = Timer(tablica=[], sorter=algorytm)
        for x in list_of_lists:
            obj.tablica = x
            obj.run_algo()
        print(
            tuple(
                zip(
                    n,
                    obj.mean_times,
                    [
                        (n[ind] * log10(n[ind])) / obj.mean_times[ind]
                        for ind in range(len(n))
                    ],
                )
            ),
            obj.sorter.__name__,
        )
        obj.plot()


algorytmy = [bubble_sort, insertion_sort, selection_sort]
# run(algorytmy, n=[10, 20, 50, 100, 200, 500, 1000])
bubble_sorty = [bubble_sort, bubble_sort_naiwny, bubble_sort_z_przew]
run(bubble_sorty, n=[10, 100, 1000])
