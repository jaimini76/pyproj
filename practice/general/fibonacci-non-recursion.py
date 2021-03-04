def fibonacci_rec(num: int):
    if num <= 1:
        return num
    else:
        return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


cache = {0: 0, 1: 1}


def fibonacci(num: int):
    if num <= 1:
        return cache[num]
    else:
        if num in cache.keys():
            return cache[num]
        else:
            cache[num] = cache[num - 1] + cache[num - 2]
            return cache[num]


def fibonacci_1(num: int):
    if num <= 1:
        return num
    else:
        a, b = 0, 1
        i = 0
        while i < num - 1:
            b, a = a + b, b
            i += 1
        return b


for i in range(7):
    number = fibonacci_rec(i)
    print("num = ", number)

for i in range(7):
    number = fibonacci(i)
    print("num = ", number)

for i in range(7):
    number = fibonacci_1(i)
    print("num = ", number)

