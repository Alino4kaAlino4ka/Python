# 1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N
# членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81


print('Введите число N: ')
N = int(input())
result = []

for i in range(0, N):
    res = (-3) ** i
    # print(res)
    result.append(res)

print(f"Для  {N}: {result}")


