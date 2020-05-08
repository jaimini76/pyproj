import logging


def factorial_rec(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        res = n * factorial(n -1)
        return res

def factorial(n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res


logging.getLogger().setLevel(logging.INFO)

i = 4

res = factorial(i)

logging.info(f"factorial of {i} is : {res}")


