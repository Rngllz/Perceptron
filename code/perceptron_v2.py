import numpy as np

entradas = [1, 7 ,5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    return e.dot(p)

def stepFunction(soma):
    if(soma > 0):
        return 1
    return 0

s = soma(entradas, pesos)
r = stepFunction(s)

print(r)