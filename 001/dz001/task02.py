# 2 Найти максимальное из пяти чисел.

print('Вам нужно ввести 5 чисел через пробел')
numbers = [int(i) for i in input().split(' ')]
print(max(numbers))

mx = 0
for i in numbers:
    if mx < i: 
        mx = i
print(mx)
