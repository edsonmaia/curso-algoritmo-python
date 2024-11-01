# Arquivo main.py

import utils

print(utils.somar(10,2))

#from utils import *
#print(somar(10,2))

# antes faça a instalação
# pip install numpy
import numpy as np

lista = np.array([10, 20, 30])
aleatorios = np.random.rand(5)

print(lista)
print(lista[0])
print(np.min(lista))
print(np.max(lista))
print(np.mean(lista))
print(aleatorios)
