# 4 Показать первую цифру дробной части числа.

# n = float(input('Введите дробное число: '))
# print(int((n*10) % 10))

n = input('Введите дробное число: ')
n = n.split(".")
print(int(n[1][0]))

