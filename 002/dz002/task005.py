# 5 Реализовать алгоритм перемешивания списка.
import random


def fill_list(n):
    f_list = []
    for i in range(n):
        f_list.append(random.randint(-n, n))
    return f_list


f_list = fill_list(int(input('Введите число: ')))
print(f_list)

for i in range(len(f_list)-1, -1, -1):
    j = random.randint(0, i)
    f_list[i], f_list[j] = f_list[j], f_list[i]
    # print(f_list[j], f_list[i], i, j)

print(f_list)
