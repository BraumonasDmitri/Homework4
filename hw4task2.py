a = int(input('Введите количество элементов в списке: '))
from random import randint
lst = [randint(0, 1000) for i in range(a)]
my_list = [el for num, el in enumerate(lst) if lst[num - 1] < lst[num]]
print(f'Исходный список {lst}')
print(f'Новый список {my_list}')