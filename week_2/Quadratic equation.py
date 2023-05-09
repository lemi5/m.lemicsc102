from math import sqrt

print("Hello i am your PYTHON quadratic equation calculato")

a = int(input("input your value of a: "))
b = int(input("input your value of b: "))
c = int(input("input your value of c: "))
d = -1.00 * b
e = b * b - (4.00 * a * c)
f = sqrt(e)
g = 2.00 * a
x = (d + f) / g
h = -1.00 * b
i = b * b - (4.00 * a * c)
j = sqrt(i)
k = 2.00 * a
y = (h - j) / k

if (b * b) - (4.00 * a * c) < 0.00:
    print("There are no real root of this equation")
elif (b * b) - (4.00 * a * c) == 0.00:
    print("The of this equation habe the same value of + x")
else:
    print("THe distint roots of this quadratic equation are (x), and (y) as requested for, Thanks")





