import logging

def bubble(arr):
    for j in range (0, len(arr)-1):
        for i in range(0, (len(arr)-1-j)):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def binary(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        logging.info(f"low = {low}")
        logging.info(f"high = {high}")
        mid = int((low+high)/2)
        logging.info(f"mid = {mid}")
        if arr[mid] == x:
            logging.info(f"Search element '{x}' found at index '{mid}'")
            return mid
        if arr[mid] > x:
            high = mid -1
        else:
            low = mid + 1

    logging.info(f"Search element '{x}' Not found in Array")
    return -1

arr=[10,7,3,14,29,13,19,15]
logging.getLogger().setLevel(logging.INFO)
bubble(arr)
logging.info(f"sorted array is: {arr}")
x=21
binary(arr, x)
x=19
binary(arr, x)
x=7
binary(arr, x)