# def summ(x): return x + 10
# def mult(x): return x ** 2


# summ(mult(2))


# def f(x):
#     return x ** 3
f = lambda x: x **3

print([(i, f(i)) for i in range(1, 12) if i % 2 == 0])


# def h(f, g, x): return f(g(x))

# h = lambda f, g, x: f(g(x))
# h(summ, mult, 5)
# h(lambda x: x+10, lambda x: x**2, 5)


data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)



