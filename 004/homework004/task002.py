# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def prime_fact(n):
    i = 2
    prim_fact = []
    while i * i <= n:
        while n % i == 0:
            prim_fact.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prim_fact.append(n)
    return prim_fact

pf = int(input(f'Задайте натуральное число N    '))
print(*prime_fact(pf))


