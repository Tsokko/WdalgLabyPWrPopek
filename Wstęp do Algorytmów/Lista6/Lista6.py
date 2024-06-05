import random
import heapq
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    def __init__(self, liczba_wierzch):
        self.liczba_wierzch = liczba_wierzch
        self.lista_sasiedztwa = [[] for _ in range(liczba_wierzch)]
        self.krawedzie = []

    def dodaj_wierzch(self, u, v, waga):
        self.lista_sasiedztwa[u].append((v, waga))
        self.lista_sasiedztwa[v].append((u, waga))
        self.krawedzie.append((waga, u, v))

    def generuj_graf(self, prawd_wierzch, max_waga=10):
        for i in range(self.liczba_wierzch):
            for j in range(i + 1, self.liczba_wierzch):
                if random.random() < prawd_wierzch:
                    waga = random.randint(1, max_waga)
                    self.dodaj_wierzch(i, j, waga)

    def bfs(self, start, odwiedzono):
        queue = deque([start])
        komponent = []
        
        while queue:
            node = queue.popleft()
            if node not in odwiedzono:
                odwiedzono.add(node)
                komponent.append(node)
                for sasiad, _ in self.lista_sasiedztwa[node]:
                    if sasiad not in odwiedzono:
                        queue.append(sasiad)
        
        return komponent
    
    def find_connected_komponenty(self):
        odwiedzono = set()
        komponenty = []
        
        for node in range(self.liczba_wierzch):
            if node not in odwiedzono:
                komponent = self.bfs(node, odwiedzono)
                komponenty.append(komponent)
        
        return komponenty

    def dijkstra(self, start, end):
        dystanse = {node: float('inf') for node in range(self.liczba_wierzch)}
        dystanse[start] = 0
        kolejka_prio = [(0, start)]
        rodzice = {start: None}

        while kolejka_prio:
            obecny_dystans, obecny_wierzch = heapq.heappop(kolejka_prio)

            if obecny_wierzch == end:
                sciezka = []
                while obecny_wierzch is not None:
                    sciezka.append(obecny_wierzch)
                    obecny_wierzch = rodzice[obecny_wierzch]
                sciezka.reverse()
                return sciezka, dystanse[end]

            if obecny_dystans > dystanse[obecny_wierzch]:
                continue

            for sasiad, waga in self.lista_sasiedztwa[obecny_wierzch]:
                distance = obecny_dystans + waga
                if distance < dystanse[sasiad]:
                    dystanse[sasiad] = distance
                    rodzice[sasiad] = obecny_wierzch
                    heapq.heappush(kolejka_prio, (distance, sasiad))
        
        return None, float('inf')

    def kruskal(self):
        rodzic = list(range(self.liczba_wierzch))
        ranking = [0] * self.liczba_wierzch

        def find(u):
            if rodzic[u] != u:
                rodzic[u] = find(rodzic[u])
            return rodzic[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                if ranking[root_u] > ranking[root_v]:
                    rodzic[root_v] = root_u
                elif ranking[root_u] < ranking[root_v]:
                    rodzic[root_u] = root_v
                else:
                    rodzic[root_v] = root_u
                    ranking[root_u] += 1

        mst = []
        self.krawedzie.sort()

        for waga, u, v in self.krawedzie:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, waga))
        return mst

    def prim(self):
        wierzch_startowy = 0
        odwiedzono = [False] * self.liczba_wierzch # lista nieodwiedzonych
        min_heap = [(0, wierzch_startowy, -1)]  # start
        mst = [] # drzewo

        while min_heap: # dopóki mni_heap nie pusty
            waga, u, prev = heapq.heappop(min_heap) # weź pierwszy z min heapa
            if not odwiedzono[u]:
                odwiedzono[u] = True # zamień u na odwiedzone
                if prev != -1:
                    mst.append((prev, u, waga)) 

                for v, next_waga in self.lista_sasiedztwa[u]: # odwiedzamy każdego sąsiada 
                    if not odwiedzono[v]:
                        heapq.heappush(min_heap, (next_waga, v, u))

        return mst

    def visualize_graph(self, mst=None, sciezka=None):
        plt.figure(figsize=(10, 10))
        pos = {i: (random.random(), random.random()) for i in range(self.liczba_wierzch)}

        for u in range(self.liczba_wierzch):
            for v, waga in self.lista_sasiedztwa[u]:
                if u < v:
                    plt.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color='gray', alpha=0.5)

        if mst:
            for u, v, waga in mst:
                plt.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color='red', alpha=0.8, linewidth=2)

        if sciezka:
            for i in range(len(sciezka) - 1):
                u, v = sciezka[i], sciezka[i + 1]
                plt.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color='blue', alpha=0.8, linewidth=2)

        plt.scatter([pos[i][0] for i in range(self.liczba_wierzch)], [pos[i][1] for i in range(self.liczba_wierzch)], color='blue')
        plt.show()

# Parametry grafu
liczba_wierzch = 10
prawd_wierzch = 0.3

# Generowanie grafu
graph = Graph(liczba_wierzch)
graph.generuj_graf(prawd_wierzch)

# Znalezienie składowych spójnych
komponenty = graph.find_connected_komponenty()
print("Składowe spójne grafu:", komponenty)

def dijkstra_func():
    wierzch_startowy = random.randint(0, liczba_wierzch - 1)
    end_node = random.randint(0, liczba_wierzch - 1)
    while end_node == wierzch_startowy:
        end_node = random.randint(0, liczba_wierzch - 1)

    # Algorytm Dijkstry
    sciezka, distance = graph.dijkstra(wierzch_startowy, end_node)
    if sciezka:
        print(f'Najkrótsza ścieżka z {wierzch_startowy} do {end_node} to: {sciezka} o długości {distance}')
    else:
        print(f'Nie ma ścieżki z {wierzch_startowy} do {end_node}')
    graph.visualize_graph(sciezka=sciezka)

def kruskal_func():
    mst_kruskal = graph.kruskal()
    print("Minimalne Drzewo Rozpinające (Kruskal):", mst_kruskal)
    graph.visualize_graph(mst=mst_kruskal)

def prim_func():
    mst_prim = graph.prim()
    print("Minimalne Drzewo Rozpinające (Prim):", mst_prim)
    graph.visualize_graph(mst=mst_prim)

prim_func()
