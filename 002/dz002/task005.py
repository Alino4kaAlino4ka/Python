# 5 Реализовать алгоритм перемешивания списка.
import random


def fill_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(-n, n))
    return list


list = fill_list(int(input('Введите число: ')))
print(list)

for i in range(len(list)-1, -1, -1):
    j = random.randint(0, i)
    list[i], list[j] = list[j], list[i]
    # print(list[j], list[i], i, j)

print(list)
