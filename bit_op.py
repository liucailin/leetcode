"""
一些常见的算数运算用位运算替代
n % 2  =   n & 1
n // 2 =   n >> 1
n * 2  =   n << 1
"""


def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

result = add(5, 3)  # 等价于 5 + 3
print(result)  # 输出: 8


def subtract(a, b):
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a

result = subtract(5, 3)  # 等价于 5 - 3
print(result)  # 输出: 2


def multiply(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result

result = multiply(5, 3)  # 等价于 5 * 3
print(result)  # 输出: 15


def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    negative = (dividend < 0) ^ (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    return -quotient if negative else quotient

result = divide(15, 3)  # 等价于 15 / 3
print(result)  # 输出: 5



def power(x, y):
    if y == 0:
        return 1
    temp = power(x, y // 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp

result = power(2, 3)  # 等价于 2^3
print(result)  # 输出: 8


def sqrt(x):
    if x < 0:
        raise ValueError("Square root of negative number is not allowed.")
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

result = sqrt(16)  # 等价于 sqrt(16)
print(result)  # 输出: 4
