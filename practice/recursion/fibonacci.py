import logging


def fibonacci_rec(n):
    if n < 0:
        logging.info("Input error")
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibo_rec(n - 2)



logging.getLogger().setLevel(logging.INFO)


limit = 10
i = 0
res = 0
while res <= limit:
    res = fibo(i)
    if res <= limit:
        logging.info(f"{res}")
    i+=1