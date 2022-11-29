# 2 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]


def fill_factorial_list(n):
    f_list = []
    f = 1
    for i in range(1, n + 1):
        f *= i
        f_list.append(f)
    return f_list


print(fill_factorial_list(int(input('Введите число: '))))
