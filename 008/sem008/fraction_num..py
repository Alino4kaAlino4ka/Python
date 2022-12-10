from fractions import Fraction

x_str = '3/7'
x = Fraction(x_str)
y_str = '2/3'
y = Fraction(y_str)
# print(x, y)
# print(type(x))
z = x + y
print(z)
z = x - y
print(z)
z = x * y
print(z)
z = x / y
print(z)