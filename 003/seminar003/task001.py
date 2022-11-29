# # Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# # псевдослучайных чисел.

import time
print(time.time())
print(time.time_ns())
num = time.time_ns() % 1000 // 100
print(num)
numb = time.time_ns() % 1000 // 100
print(numb)



