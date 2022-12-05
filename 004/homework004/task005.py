#  Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import Task004

# n = Task004
# k = int(input('Введите натуральную степень k:'))
# k2 = int(input('Введите натуральную степень k2:'))

# k_lst = Task004.write_file(task004.koef(k))
# k_lst2 = Task004.create_list(k2)





with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
    
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')


with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()

with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()


with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')


print(*list_of_poly_1, ' + ', *list_of_poly_2)
sum_poly = *list_of_poly_1,  *list_of_poly_2




