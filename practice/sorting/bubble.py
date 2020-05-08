import logging

def bubble(arr):
    for j in range (0, len(arr)-1):
        for i in range(0, (len(arr)-1-j)):
            logging.info(f"len(arr)-1-j = {len(arr)-1-j}")
            logging.info(f"i = {i}, j = {j}")
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


arr=[10,7,3,14,29,13,19,15]
logging.getLogger().setLevel(logging.INFO)
bubble(arr)
logging.info(f"sorted array is: {arr}")