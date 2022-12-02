# 1 В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

data = open("test.txt", 'w', encoding='utf-8')
lst = "5 6 8 9 10 11"
data.write(lst)
data.close()

with open("test.txt", 'r', encoding='utf-8') as fd:
    x = fd.read()
print(x)
print(type(x))
y =list(map(int, x.split()))
print(y)
for i in range(1, len(y)):
    if y[i]-1 != y[i - 1]:
        print(y[i] - 1)
    # print(x)
    # print(type(x))
    y =list(map(int, x.split()))
    # print(y)
    # return y


def find_num(y):
    for i in range(1, len(y)):
        if y[i] - 1 != y[i - 1]:
            return y[i] - 1 


if __name__ == '__main__':
    create_file("5 6 8 9 10 11")
    lst2 = read_file()
    print(lst2)
    print(find_num(lst2))










# 5 Создайте программу для игры в "Крестики-нолики".
# a = [
#     [" 1 ", " 2 ", " 3 "],
#     [" 4 ", " 5 ", " 6 "],
#     [" 7 ", " 8 ", " 9 "]
# ]
# for i in a:
#     print(i)
# print(a[1][1])
# a[1][1] = " x " 
# for i in a:
#     print(i)

# if i != " x " or i != " o ":

