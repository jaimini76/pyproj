# You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
# How many ways can you make change for a $100 dollar bill?

import itertools as it
from typing import List


def get_100_bill_combinations(denominations: List[int]):
    bills_100 = []
    for i in range(7, len(denominations) + 1):
        for combination in it.combinations(denominations, i):
            if sum(combination) == 100:
                bills_100.append(combination)

    return list(set(bills_100))


bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
combinations = get_100_bill_combinations(bills)
print("combinations = ", combinations)

