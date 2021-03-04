def factorial_rec(num: int):
    factorial = 1
    if num == 0 or num == 1:
        return factorial
    else:
        return num * factorial_rec(num - 1)


def factorial_non_rec(num: int):
    factorial = 1
    if num == 0 or num == 1:
        return factorial
    else:
        while num > 0:
            factorial = factorial * num
            num -= 1
    return factorial


x = factorial_rec(4)
print("factorial = ", x)
x = factorial_non_rec(4)
print("factorial = ", x)
x = factorial_rec(0)
print("factorial = ", x)
x = factorial_non_rec(0)
print("factorial = ", x)
x = factorial_rec(1)
print("factorial = ", x)
x = factorial_non_rec(1)
print("factorial = ", x)

