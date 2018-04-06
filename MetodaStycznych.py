#!/usr/bin/python

# import parametrow
import param as p

# glowna petla programu
x = p.odcinek[0]
while(True):
    temp = x - p.f(x) / p.g(x)
    print('{:.20f}'.format(p.f(temp)))
    if(abs(p.f(temp)) < p.epsilon):
        print(temp)
        break
    else:
        x = temp
