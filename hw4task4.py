a = int(input('Введите количество элементов в списке: '))
b = int(input('Введите наибольшее число списка: '))
from random import randint
lst = [randint(0, b) for i in range(a)]
print(lst)
my_list = [el for el in lst if lst.count(el) < 2]
print(my_list)
