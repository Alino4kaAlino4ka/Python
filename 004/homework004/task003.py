# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.


seq = list(map(int, input('Введите числа через пробел ').split()))
unic = []

for i in seq:
    if i not in unic:
        unic.append(i)
    else:
        unic.remove(i)
print(*unic)

