# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


my_list = input("Введите числа через пробел: ").split()
multi_list = []
size = len(my_list)
end = size / 2 

if size % 2 == 0:
    for i in range(size // 2):
        j = -i -1
        multi_list.append(int((my_list[i])) * int(my_list[j]))
        print((my_list[i]), my_list[j])
else:
    j = -1
    for i in range(size // 2 + 1):
        if i == j:
            multi_list.append(int((my_list[i])) * int(my_list[j]))
            print((my_list[i]), my_list[j], i , j)
        else:
            multi_list.append(int((my_list[i])) * int(my_list[j]))
            print((my_list[i]), my_list[j], i, j)
        j -= 1
print(multi_list)

 


exit()

def multiplier(size, my_list, multi_list):
    if size % 2 == 0:
        for i in range(size // 2):
            j = -i -1
            multi_list.append(int((my_list[i])) * int(my_list[j]))
            print((my_list[i]), my_list[j])
    else:
        j = -1
        for i in range(size // 2 + 1):
            if i == j:
                multi_list.append(int((my_list[i])) * int(my_list[j]))
                print((my_list[i]), my_list[j], i , j)
            else:
                multi_list.append(int((my_list[i])) * int(my_list[j]))
                print((my_list[i]), my_list[j], i, j)
            j -= 1
    return multi_list

first_list = input("Введите числа через пробел: ").split()
finish_list = []
print(multiplier(len(first_list), first_list, finish_list))
