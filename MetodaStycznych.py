#!/usr/bin/python

# import parametrow
import param as p

# glowna petla programu
i = 1
while(True):
    x = p.odcinek[i]
    temp = x - p.f(x) / p.g(x)
    print '{:.20f}'.format(p.f(temp))
    if abs(p.f(temp)) < p.epsilon:
        break
    else:
        p.odcinek.append(temp)
        i += 1
