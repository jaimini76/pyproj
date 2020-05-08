import logging

def max_two(l):
    if l[0] > l[1]:
        first_max = l[0]
        second_max = l[1]
    else:
        first_max = l[1]
        second_max = l[0]

    for i in range(2,len(l)):

        if l[i] < second_max:
            continue
        if l[i] > first_max:
            second_max = first_max
            first_max = l[i]

    return (first_max, second_max)

logging.getLogger().setLevel(logging.INFO)

my_list = [100, 2, 3, 15, 10, 8, 5, 300, 22]

max_1, max_2 = max_two(my_list)

logging.info(f"max_1 = {max_1}, max_2 = {max_2}")


