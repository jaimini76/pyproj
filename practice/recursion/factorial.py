import logging


def factorial_rec(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


logging.getLogger().setLevel(logging.INFO)

num = 4
res = factorial(num)
logging.info(f"factorial of {num} is : {res}")


