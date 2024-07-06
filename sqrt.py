
n = 10
#  sqrt(10) = 3.1622776601683795


def f(x):
    return x * x - n

def d(x):
    return 2 * x


def newton(x):
    print(f'{x} - {f(x) / d(x)} = {x - f(x) / d(x)}')
    x = x - f(x) / d(x)
    return x


# 迭代6次就能得出比较精确的结果
iter = 6

x = n
for i in range(iter):
    x = newton(x)
    print(x)