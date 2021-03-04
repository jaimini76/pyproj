import pytest

def generator_1():
    i = 0
    while True:
        i = i + 1
        yield i * i


generator_obj = generator_1()

print("type of generator_obj = ", type(generator_obj))

while True:
    res = next(generator_obj)
    if res > 100:
        break
    print(f"type of res = {type(res)}")
    print(f"res = {res}")

generator_obj = generator_1()

for res in generator_1():
    print(f"type of res = {type(res)}")
    if res > 100:
        break
    print(f"res = {res}")


def generator_2():
    g = 555
    yield g


g2 = generator_2()
print("g2 = ", g2)
print("next(g2) = ", next(g2))
print("type(g2) = ", type(g2))


def generator_3():
    def gen_3():
        print("This is gen3")

    yield gen_3


g3 = generator_3()
print("g3 = ", g3)
print("type(g3) = ", type(g3))
g3_func = next(g3)
g3_func()

# Note in all above case when yield will always return generator object

# But when Fixture that returns generator object with yield statement and when that fixture is used by other fixture.
# In parameter as dependent fixture, then that generator is automatically evaluated.

# Note: Fixture generator_a uses fixture generator_b which yields something
# here yield will return generator object, but when that is used  in parameter
# to other fixture it automatically evaluates to the value which is "generator_b"

# Note: To execute following test_generator_a() pytest test case run on command line as:
# pytest --capture=no  generator_1.py


@pytest.fixture
def generator_b():
    print("")
    print("In generator_b")
    signature = "generator_b"
    yield signature


@pytest.fixture
def generator_a(generator_b):
    print("In generator_a")
    print("In generator_a, printing generator_b = ", generator_b)


def test_generator_a(generator_a):
    print("Testing generator_a fixture call, in turn will invoke generator_b fixture, which yields generator object "
          "that is automatically evaluated.")
