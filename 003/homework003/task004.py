# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число '))

print(bin(n))

def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)     
    print(n % 2, end='')
decimal_to_binary(n)

print()

b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
if n == 0:
    b = 0
print(b)






