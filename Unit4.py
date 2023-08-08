list_1 = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
list_2 = [3, 9, 12, 15, 18]

set_1 = set(list_1)
set_2 = set(list_2)

array_1 = []

for i in set_1:
    if i in set_1 and i in set_2:
        array_1.append(i)

if array_1 == []:
    print('Повторяющихся чисел нет')
else:
    print(*array_1)
