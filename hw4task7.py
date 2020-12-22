from itertools import count
from math import factorial

def func():
    for el in count(1):
        yield factorial(el)

n = int(input('Введите количество чисел: '))
x = 0
for i in func():
    if x < n:
        print(i)
        x += 1
    else:
        break