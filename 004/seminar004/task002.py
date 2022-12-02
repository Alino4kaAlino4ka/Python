# 2.Для натурального n создать список, состоящий из элементов последовательности 3n + 1
# Пример:
# - Для n = 6: [4, 7, 10, 13, 16, 19]

print('Введите число N: ')
N = int(input())
result = []

for i in range(1, N+1):
    res = 3*i+1
    # print(res)
    result.append(res)

print(f"Для  {N}: {result}")



