# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print(bin(int(input('Введите число: '))))


n = int(input('Введите число '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)


def decimalToBinary(n):
    if(n > 1):
        decimalToBinary(n//2)     
    print(n%2, end='')
decimalToBinary(int(input('Введите число: ')))



