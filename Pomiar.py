#!/usr/bin/python
from subprocess import check_output
import inspect
import param

# nazwy metod
metody = [
          'Bisekcji', 
          'Stycznych', 
          'Siecznych'
         ]

#metody = [('./Metoda' + m + '.py') for m in metody]

# slownik z wynikami
wyniki = {}

# petla glowna po roznych metodach
for m in metody:

    # zapisz output skryptu do zmiennej out
    out = check_output(['python', './Metoda' + m + '.py'])

    # policz ilosc iteracji na podstawie wypisanych linii
    cnt = len(out.split('\n')) - 1

    # przypisz wynik do nazwy metody w slowniku
    wyniki[m] = cnt

    print m + ':'
    print '*' * 10
    print out
    print 'Znaleziono wynik w ' + str(cnt) + ' iteracjach'
    print 
    print 

## znajdz nazwy metod ktore mialy najmniejsza ilosc iteracji
#best = min(wyniki.keys(), key = wyniki.get)
#print best

print '# ' * 20
print
print 'Badana funkcja: ', inspect.getsource(param.f)
print
print 'Ranking metod:'

i = 0
prev = 0
ranking = sorted(wyniki, key=wyniki.get)
for w in ranking:
    if(prev != wyniki[w]):
        i += 1
    print str(i) + '.', w, 'wykonala', wyniki[w], 'iteracji.'
    prev = wyniki[w]
