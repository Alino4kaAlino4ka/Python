# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = list(map(int, input('Введите числа через пробел: ').split()))
sum_el = [my_list[i] for i in range(1, len(my_list), 2)]
print(sum(sum_el))

# my_list = list(map(int, input('Введите числа через пробел: ').split()))
# sum_el = 0
# for i in range(1, len(my_list), 2):
#     sum_el += my_list[i]
# print(sum_el)
