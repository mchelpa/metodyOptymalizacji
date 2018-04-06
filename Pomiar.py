#!/usr/bin/python
import operator
from subprocess import check_output
import inspect
import param
import time

# nazwy metod
metody = [
          'Bisekcji', 
          'Stycznych', 
          'Siecznych'
         ]

#metody = [('./Metoda' + m + '.py') for m in metody]

# slownik z wynikami
wyniki = {}

# klasa opisujaca metode numeryczna
class Metoda:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.skrypt = './Metoda' + nazwa + '.py'

    def ustawIleIteracji(self, ile):
        self.iteracji = ile

    def ustawWynik(self, wynik, dokladnosc):
        self.wynik = wynik
        self.dokladnosc = dokladnosc

    def ustawCzas(self, czas):
        self.czas = czas

    def obliczWspolczynnik(self):
        return (abs(self.dokladnosc) * self.iteracji * self.czas * 10**5)

    def podsumowanie(self):
        desc = 'Metoda ' + self.nazwa + ':\n'
        # desc = desc + 'Wspolczynnik skutecznosci: ' + str(self.obliczWspolczynnik()) + '\n'
        desc = desc + 'Czas: ' + str(self.czas) + '\n'
        desc = desc + 'Iteracji: ' + str(self.iteracji) + '\n'
        desc = desc + 'Dokladnosc: ' + str(self.dokladnosc) + '\n'
        desc = desc + 'Wynik: ' + str(self.wynik) + '\n'
        desc = desc + '\n'
        return desc



# petla glowna po roznych metodach
for m in metody:

    # utworz obiekt badanej metody
    badanaMetoda = Metoda(m)

    # rozpocznij mierzenie czasu
    start = time.time()

    # uruchom skrypt i zapisz jego output do zmiennej out
    out = check_output(['python', badanaMetoda.skrypt])

    # zakoncz mierzenie czasu
    end = time.time()

    # deserializacja outputu skryptu do listy
    wypisane = out.split(b'\n')
    wypisane = [float(w.decode('utf-8')[:-1]) for w in wypisane[:-1]]

    # rozdziel odebrana liste na wynik i przyblizenia
    wynik = wypisane[-1]           # ostatni element listy jest znalezionym x
    przyblizenia = wypisane[:-1]   # wszystkie procz ostatniego to przyblizenia
    dokladnosc = przyblizenia[-1] # ostatnie przyblizenie jest dokladnoscia otrzymanego wyniku

    # policz ilosc iteracji na podstawie wypisanych linii
    cnt = len(przyblizenia)

    # zapisz dane o metodzie
    badanaMetoda.ustawIleIteracji(cnt)
    badanaMetoda.ustawWynik(wynik, dokladnosc)
    badanaMetoda.ustawCzas(end - start)

    # zapisz klase w slowniku
    wyniki[m] = badanaMetoda

    # debug
    #print('*' * 10)
    #print(m + ':')
    #print(przyblizenia)
    #print('Znaleziono wynik: ', wynik, 'w ' + str(cnt) + ' iteracjach')
    #print('*' * 10)

## znajdz nazwy metod ktore mialy najmniejsza ilosc iteracji
#best = min(wyniki.keys(), key = wyniki.get)
#print best

print('# ' * 20)
print('# ', 'Autor:  Mikołaj Chełpa')
print('# ', 'Indeks: 350362')
print('# ' * 20, '\n')
print('Badana funkcja: ', inspect.getsource(param.f))
print('RANKING METOD')
print('=' * 20, '\n')

for w in sorted(wyniki, key = lambda met: wyniki[met].obliczWspolczynnik()):
    print(wyniki[w].podsumowanie())
