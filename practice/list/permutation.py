# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
import logging

def permutation(start, end):

    if start == end:
        logging.info(f"list = {l}")
        return

    for i in range(start, end+1):
        logging.info(f"swapping l[{start}] <=> l[{i}]   {l[start]} <----> {l[i]}")
        l[start], l[i] = l[i], l[start]
        permutation(start+1, end)
        logging.info(f"swapping resore l[{start}] <=> l[{i}]   {l[start]} <----> {l[i]}")
        # Backtrack to restore original config to proceed with new combinations.
        l[start], l[i] = l[i], l[start]


logging.getLogger().setLevel(logging.INFO)

l=['a', 'b', 'c']
start = 0
end = len(l) - 1
permutation(start, end)

