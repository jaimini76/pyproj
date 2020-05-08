import logging


def permutation(start, end):

    if end == start:
        logging.info("end == start <------")
        logging.info(a)
        logging.info("I am returning <------")
        return
    logging.info("starting for loop..")
    for i in range(start, end+1):
        #swapping
        logging.info(f"swapping : i = {i}, start = {start}")
        a[i],a[start] = a[start],a[i]
        logging.info(f"calling with start+1={start+1}, end={end}")
        logging.info("-----------------------------")
        permutation(start+1, end)
        logging.info("-----------------------------")
        #restoring the array
        logging.info(f"swapping restore: i = {i},  start = {start}")
        a[i],a[start] = a[start],a[i]


a = ['a', 'b', 'c']

def main():
    logging.getLogger().setLevel(logging.INFO)
    logging.info(f"calling with start=0, end={len(a)}")
    logging.info("-----------------------------")
    permutation(0, len(a)-1)
    logging.info("-----------------------------")


if __name__ == "__main__":
    main()
