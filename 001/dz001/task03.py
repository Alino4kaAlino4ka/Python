# 3 Вывести на экран числа от -N до N.

n = int(input('Введите число N: '))
# m = -n
# while m != n+1:
#     print(m)
#     m += 1

# list = []
# while m != n+1:
#     list.append(m)
#     m += 1
# print(list)

for i in range(-n, n+1):
    print(i)
