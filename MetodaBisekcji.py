#!/usr/bin/python

# import parametrow
import param as p

a = p.odcinek[0]
b = p.odcinek[1]

# glowna petla programu
while(True):
    c = (a + b) / 2
    print('{:.20f}'.format(p.f(c)))
    if(abs(p.f(c)) < p.epsilon):
        print(c)
        break
    elif(p.f(c) * p.f(a) < 0):
        b = c
    else:
        a = c
