import random
koefs = {}
# k = 15
k = int(input('введите целое число больше 0: '))
for i in range(k + 1):
    koefs[i] = random.randint(1, 100)
print(koefs)
# {0: 71, 1: 62, 2: 44, 3: 89}
# 89x^3+44x^2
# print(max(koefs.keys()))
max_k = max(koefs.keys())
out_str = ''
# c = 0
first = True
for i in range(max_k, -1, -1):
    koef = koefs[i]
    pow_x = i
    if i > 1:
        # if c == 0:
        if first:
            out_str += f'{koef}x^{pow_x}'
            # 89x^3
        else:
            out_str += f'+{koef}x^{pow_x}'
            # +89x^3
    elif i == 1:
        if first:
            out_str += f'{koef}x'
            # 62x
        else:
            out_str += f'+{koef}x'
    else:
        out_str += f'+{koef}=0'
    # c += 1
    if first:
        first = False
print(out_str)
with open('result.txt', 'w', encoding='utf-8') as fd:
    fd.write(out_str)

