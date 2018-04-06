#!/usr/bin/python

# import parametrow
import param as p

# glowna petla programu
i = 1
x = p.odcinek

while(True):
    temp = x[i] - (p.f(x[i])) * ((x[i] - x[i - 1]) / (p.f(x[i]) - p.f(x[i - 1])))
    print('{:.20f}'.format(p.f(temp)))
    if abs(p.f(temp)) < p.epsilon:
        print(temp)
        break
    else:
        x.append(temp)
        i += 1
