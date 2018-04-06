from math import exp
epsilon = 0.00001
odcinek = [-1.0, 0.0]
f = lambda x: exp(-2.0 * x) - 5.0
g = lambda x: -2.0 * exp(-2.0 * x) # pochodna f
#f = lambda x: pow(x, 3) + 4 * pow(x, 2) - 10
#g = lambda x: 3 * pow(x, 2) + 8 * x
