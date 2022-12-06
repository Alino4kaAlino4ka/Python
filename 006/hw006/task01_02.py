# 1 Подсчитать сумму цифр в вещественном числе.


my_list = list(map(int, input('Введите вещественное число (c точкой): ').split('.')))
print(sum(my_list))



# def sum_num(input_str):
#     res = 0
#     for i in input_str:
#         if i.isdigit():
#             res += int(i)
#     return res

# print(sum_num(input('Введите число: ')))


# print(sum(map(int, list(input('Введите число: ')))))


# def s(a):
#     res = 0
#     while a > 0:
#         res += a % 10
#         a //= 10
#     return res
 
# print(s(int(input('Введите число: '))))



