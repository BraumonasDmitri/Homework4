from itertools import islice, count

for i in islice(count(int(input('Введите стартовое значение: '))),
                int(input('Введите количество итераций: '))):
    print(i)

from itertools import cycle

a = int(input('Введите количество итераций: '))
count = 0
for item in cycle(['no', True, 'yes', 123, False]):
    if count > a:
        break
    print(item)
    count += 1