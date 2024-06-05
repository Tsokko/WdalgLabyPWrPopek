def zad1(slowo1 = "kruk", slowo2 = "wrak"):
    def dystans_hamminga(slowo1, slowo2):
        if len(slowo1) != len(slowo2):
            raise ValueError("Ciągi są różnej długości")
        return sum(charA != charB for charA, charB in zip(slowo1, slowo2))
    print("Odległość Hamminga:", dystans_hamminga(slowo1, slowo2))
def zad1b(slowo1 = "pies", slowo2 = "koty"):
    # Mapa dla klawiatury
    mapa_klawiatury = {
        'q': set('wa'), 'w': set('qeas'),
        'e': set('wrsd'), 'r': set('etdf'), 
        't': set('ryfg'),'y': set('tugh'),
        'u': set('yihj'), 'i': set('uojk'),
        'o': set('ipkl'), 'p': set('ol'),
        'a': set('qwsz'), 's': set('awedxz'), 
        'd': set('serfcx'), 'f': set('drtgvc'), 
        'g': set('ftyhbv'), 'h': set('gyujbn'),
        'j': set('huiknm'), 'k': set('jiolm'), 
        'l': set('kop'),'z': set('asx'),
        'x': set('zsdc'), 'c': set('xdfv'),
        'v': set('cfgb'), 'b': set('vghn'),
        'n': set('bhjm'), 'm': set('njk')
    }


    def zmodyfikowany_dystans_hamminga(slowo1, slowo2):
        if len(slowo1) != len(slowo2):
            raise ValueError("Ciągi muszą być tej samej długości")

        distance = 0
        for charA, charB in zip(slowo1, slowo2):
            if charA != charB:
                if charB in mapa_klawiatury.get(charA, set()):
                    distance += 1
                else:
                    distance += 2
        return distance


    print("Zmodyfikowana odległość Hamminga:", zmodyfikowany_dystans_hamminga(slowo1, slowo2))

def zad1c(slowo_do_sprawdzenia = "kitty"):
    slownik = [
        "house", "mother", "cat", "dog", "flower", "tree", "car", "bike", "street", "city",
        "computer", "programming", "keyboard", "mouse", "monitor", "school", "student", "teacher",
        "doctor", "baker", "architect", "engineer", "construction", "project", "bill", "nature",
        "mathematics", "physics", "chemistry", "biology", "history", "geography", "sport", "tourism",
        "religion", "philosophy", "literature", "art", "music", "theatre", "cinema", "movie", "actor",
        "painter", "sculptor", "poet", "writer", "journalist", "photography", "phone", "mobile",
        "smartphone", "tablet", "laptop", "internet", "network", "website", "portal", "service", "application",
        "system", "database", "data", "server", "client", "user", "passslowo", "security",
        "protection", "safety", "alarm", "camera", "police", "fire brigade", "fire", "water", "air",
        "earth", "fire", "method", "solution", "problem", "riddle", "game", "play", "sport",
        "entertainment", "leisure", "rest", "work", "job", "company", "enterprise", "corporation",
        "product", "production", "factory", "warehouse"
    ]
    def dystans_hamminga(slowo1, slowo2):
        if len(slowo1) != len(slowo2):
            raise ValueError("Ciągi są różnej długości")
        return sum(charA != charB for charA, charB in zip(slowo1, slowo2))
    
    def znajdz_podobne_slowa(slowo_do_sprawdzenia, slownik):
        if slowo_do_sprawdzenia in slownik:
            return "Twoje słowo znajduje się w słowniu"
        else:
            podobne_slowo = [(slowo, dystans_hamminga(slowo_do_sprawdzenia, slowo)) for slowo in slownik if len(slowo) == len(slowo_do_sprawdzenia)]
            podobne_slowo.sort(key=lambda x: x[1])
            return [slowo for slowo, dist in podobne_slowo[:3]]

    # Przykład
    print("Najbardziej podobne słowa dla:", slowo_do_sprawdzenia, znajdz_podobne_slowa(slowo_do_sprawdzenia, slownik))

#2C
# Częstości liter dla języka angielskiego i niemieckiego bezpośrednio z artykułu

# Przybliżone wartości dla języka polskiego, sumując częstości podobnych liter
polska_czest = {
    'a': 8.965 + 1.021, 'b': 1.482, 'c': 3.988 + 0.448, 'd': 3.293, 'e': 7.921 + 1.131,
    'f': 0.312, 'g': 1.377, 'h': 1.072, 'i': 8.286, 'j': 2.343,
    'k': 3.411, 'l': 2.136 + 1.746, 'm': 2.911, 'n': 5.600 + 0.185, 'o': 7.590,
    'p': 3.101, 'q': 0.003, 'r': 4.571, 's': 4.263 + 0.683, 't': 3.966,
    'u': 2.347, 'v': 0.034, 'w': 4.549, 'x': 0.019, 'y': 3.857,
    'z': 5.620 + 0.061 + 0.885
}
angielska_czest = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15, 'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0, 'z': 0.074}
niemiecka_czest = {'a': 6.516, 'b': 1.886, 'c': 2.732, 'd': 5.076, 'e': 16.396, 'f': 1.656, 'g': 3.009, 'h': 4.577, 'i': 6.550, 'j': 0.268, 'k': 1.417, 'l': 3.437, 'm': 2.534, 'n': 9.776, 'o': 2.594, 'p': 0.670, 'q': 0.018, 'r': 7.003, 's': 7.270, 't': 6.154, 'u': 4.166, 'v': 0.846, 'w': 1.921, 'x': 0.034, 'y': 0.039, 'z': 1.134}



def wyswietl_tablice_czest(language, tablica_czest):
    print(f"Częstości liter dla języka {language}:")
    for letter, freq in sorted(tablica_czest.items()):
        print(f"{letter}: {freq}%")
wyswietl_tablice_czest("Polski", polska_czest)


import string
from collections import Counter
# Zamienianie tekstu na czestość
def tekst_do_tablicy_czestosci(tekst):
    # Usuwanie nie potrzebnych znaków
    tekst = ''.join([znak.lower() for znak in tekst if znak in string.ascii_lowercase])
    liczba_liter = Counter(tekst)
    liczba_wszystkich_liter = sum(liczba_liter.values())
    tabela_czestosci = {litera: liczba / liczba_wszystkich_liter for litera, liczba in liczba_liter.items()}
    return tabela_czestosci

# Przykład użycia:
przykladowy_tekst = " Funkcja zamieniająca tekst na tablicę częstości liter"
print(tekst_do_tablicy_czestosci(przykladowy_tekst))

#C Funkcja obliczająca częstość samogłosek i spółgłosek
def czestosc_spolglosek_i_samoglosek(tekst):
    samogloski = set('aeiouyąę')
    tekst = ''.join([znak.lower() for znak in tekst if znak in string.ascii_lowercase])
    liczba_samoglosek = sum(1 for znak in tekst if znak in samogloski)
    liczba_spolglosek = len(tekst) - liczba_samoglosek
    liczba_wszystkich_liter = len(tekst)
    if liczba_wszystkich_liter == 0:
        return {'samogloski': 0, 'spolgloski': 0}
    return {'samogloski': liczba_samoglosek / liczba_wszystkich_liter, 'spolgloski': liczba_spolglosek / liczba_wszystkich_liter}


# Przykład użycia:
print(czestosc_spolglosek_i_samoglosek(przykladowy_tekst))

# Porównywanie języków
def identyfikuj_jezyk(tekst, tablice_czestotliwosci):
    czestosci = tekst_do_tablicy_czestosci(tekst)
    
    def oblicz_roznice(tablica1, tablica2):
        return sum(abs(tablica1.get(litera, 0) - tablica2.get(litera, 0)) for litera in string.ascii_lowercase)
    
    roznice = {jezyk: oblicz_roznice(czestosci, tablica_czest) for jezyk, tablica_czest in tablice_czestotliwosci.items()}
    
    return min(roznice, key=roznice.get)


# Tabele częstości dla przykładowych języków (przykładowe dane)
tablice_czestotliwosci = {
    'Angielska': angielska_czest,
    'Niemiecka': niemiecka_czest,
    'Polska': polska_czest
}


tekst_przykladowy = "Die Sonne scheint hell am blauen Himmel."


print(identyfikuj_jezyk(tekst_przykladowy, tablice_czestotliwosci))


def najdluzszy_wspolny_podciag(slowo1, slowo2):
    max_dlugosc = 0
    dp = [[0] * (len(slowo2) + 1) for _ in range(len(slowo1) + 1)]

    for i in range(1, len(slowo1) + 1):
        for j in range(1, len(slowo2) + 1):
            if slowo1[i - 1] == slowo2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_dlugosc = max(max_dlugosc, dp[i][j])
            else:
                dp[i][j] = 0

    return max_dlugosc


print(najdluzszy_wspolny_podciag("konwalia", "zawalina"))


def najdluzszy_wspolny_podciag(slowo1, slowo2):
    dp = [[0] * (len(slowo2) + 1) for _ in range(len(slowo1) + 1)]

    for i in range(1, len(slowo1) + 1):
        for j in range(1, len(slowo2) + 1):
            if slowo1[i - 1] == slowo2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)

    return dp[len(slowo1)][len(slowo2)]

print(najdluzszy_wspolny_podciag("ApqBCrDsEF", "tABuCvDEwxFyz")) 
