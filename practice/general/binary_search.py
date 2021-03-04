from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def binary_search(numbers: List[int], search: int) -> bool:
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if numbers[mid] == search:
            print("Number", search, " found in the list.")
            return True
        elif numbers[mid] > search:
            high = mid - 1
        else:
            low = mid + 1

    print("Number", search, " not found in the list.")
    return False


nums = [6, 20, 4, 3, 34, 8, 15]
result = bubble_sort(nums)
print("result = ", result)
binary_search(result, 10)
