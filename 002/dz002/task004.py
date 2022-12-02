# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:

from random import randint


def fill_list(n):
    fill_list = []
    for i in range(n):
        fill_list.append(randint(-n, n))
    return fill_list

n = int(input('Введите число >= 6: '))
numbers = fill_list(n)
print(numbers)
positions = [1, 3, 6]
res = 1
for i in positions:
    if i <= len(numbers):
        res *=  numbers[i - 1]
# result = numbers[positions[0] - 1] * numbers[positions[1] - 1] * numbers[positions[2] - 1]
print(res)


