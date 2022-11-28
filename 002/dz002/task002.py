# 2 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]


def fill_factorial_list(n):
    list = []
    f = 1
    for i in range(1, n + 1):
        f *= i
        list.append(f)
    return list


print(fill_factorial_list(int(input('Введите число: '))))
