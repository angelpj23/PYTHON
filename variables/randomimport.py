#el archivo no puede llamarse random, porque python confunde lo que busca
from random import random

for t in range(10):
    x = random()
    print(x)