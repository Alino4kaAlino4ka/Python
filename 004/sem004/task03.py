# 3 Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.


a, b = map(int, input().split())
i = min(a, b)
while True:
    if i % a == 0 and i % b == 0:
        break
    i += 1
print(i)


# exit()


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(a*b//gcd(a, b))

import math



print((a*b) // math.gcd(a, b))  # gcd - greatest common devisor


print(math.lcm(a, b))





import numpy as np


print(np.lcm(14, 21))

