
# inp_lst = ['1', '22', '3.0']
# inp_str = ''
# def my_filter(x):
#     if x.isdigit():
#         return True
# out_lst = list(filter(my_filter, inp_lst))
# print(out_lst)


# out_lst = list(map(int, inp_lst))
# print(out_lst)
# out_lst = []
# for i in inp_lst:
#     out_lst.append(int(i))
# '2.3' ['2', '3'] [2, 3]
# out_lst = list(map(int, input('введите число: ').split('.')))
# print(out_lst)
# def mult(x):
#     return int(x) * 2


# inp_lst = ['1', '22', '3.0']
# # out_lst = list(map(mult, inp_lst))
# for i in inp_lst:
#     mult(i)
# print(out_lst)
# out_lst = list(map(lambda x: int(x) * 2, inp_lst))
# print(out_lst)

# lst = [[1, 2], [5, 6, 7]]
# out = list(map(tuple, lst))
# print(out)

# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c']
# z = dict(zip(a, b))
# print(z)
import random

rand_lst = []
for i in range(5):
    rand_lst.append(random.randint(0, 10))

print(rand_lst)

n = 3
rnd_lst = [random.randint(0, 10) for i in range(n)]
# list comprehension
print(rnd_lst)

# rnd_lst2 = (random.randint(0, 10) for i in range(n))
# for i in rnd_lst2:
#     print(i)
#
# print(next(rnd_lst2))

