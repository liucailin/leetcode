


def fact(n):
    f = 1
    while n:
        f = f * n
        n -= 1
    return f




def print_fact(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(str(i))
    process = ' x '.join(numbers)
    print(f'{n}! = {process} = {fact(n)}')



for i in range(51):
    print_fact(i)