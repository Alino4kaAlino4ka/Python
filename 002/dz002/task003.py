# 3 Задать список из n чисел последовательности (1 + 1 / n) ** n и вывести на экран их сумму.


print('Введите число N: ')
n = int(input())
result = []

for i in range(1, n+1):
    res = (1 + 1 / i) ** i
    # print(res)
    result.append(res)

print(sum(result))
