import random
import re
#
# input_str = '54x^4-22x^3+34x^2+5x+18=0'
# pattern = r'([+-]?\d+)x\^?(\d*)|(\d*)=0$'
# # pattern = r'([-+]?\d*)(x\^*\d*)*'
# # pattern2 = r'([-+]?\d*)(x\^*\d*)*|(\=0)'
#
# # res = re.findall(pattern, input_str)
# # print(res)
# # re.compile()
# output = re.compile(pattern)
# result = output.findall(input_str)
# print(result)
# print(int(result[1][0]))
# res_dict = dict()
# for i in result:
#     if i[1]:
#         res_dict[int(i[1])] = int(i[0])
#     elif i[1] == '' and i[0]:
#         res_dict[1] = int(i[0])
#     elif i[2]:
#         res_dict[0] = int(i[2])
# print(res_dict)
# # '54x^4-22x^3+34x^2+5x+18=0'
# # k = 3
# # res_dict = dict()
# # res_dict[2] = random.randint(0, 100)
# # # res_dict = {
# # #     3: 22,
# # #     2: 34,
# # #     1: 5,
# # #     0: 18
# # # }
# # out = ''
# # for k in res_dict:
# #     out += f'{res_dict[k]}x^{k}'
#
# # [18, 5, 34, -22, 54]
# # [5, 0, 73, 14, 0]
# # [23, 5, 107, -8, 54].reverse()
#
# # res_list = []
# # key_list = []
# # max_x = 0
# # for i in result:
# #     try:
# #         koef = float(i[0])
# #     except ValueError:
# #         continue
# #     if i[1]:
# #         x1 = i[1]
# #         x1 = x1.replace('x^', '')
# #         if x1.isdigit() and int(x1) > max_x:
# #             max_x = int(x1)
# #         key_list.append(x1)
# #     res_list.append(koef)
# #
# #
# # print(res_list)
# # print(key_list)
# # print(max_x)
# #
# # # [54.0, -22.0, 34.0, 5.0, 18.0]
# # # {:+f}
d1 = {4: 54, 3: -22, 0: 18}
d2 = {3: 14, 2: 15, 0: 35}
d3 = dict()
# print(d2.get(4))
# d3[4] = d1.get(4) + d2.get(4)
all_keys = set(d1.keys())
all_keys = all_keys.union(d2.keys())
print(all_keys)
# for i in range(0, max_key + 1):
for i in all_keys:
    if d1.get(i):
        if d2.get(i):
            d3[i] = d1.get(i) + d2.get(i)
        else:
            d3[i] = d1.get(i)
    elif d2.get(i):
        d3[i] = d2.get(i)
    # print(i)
print(d3)
