# 1 Подсчитать сумму цифр в вещественном числе.

print(sum(map(int, list(input('Введите число: ')))))


def s(a):
    res = 0
    while a > 0:
        res += a % 10
        a //= 10
    return res
 
print(s(int(input('Введите число: '))))
