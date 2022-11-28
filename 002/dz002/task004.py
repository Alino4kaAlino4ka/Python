# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:

from random import randint


def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число >= 6: '))
numbers = list(n)
print(numbers)
positions = [1, 3, 6]
result = numbers[positions[0] - 1] * numbers[positions[1] - 1] * numbers[positions[2] - 1]
print(result)


