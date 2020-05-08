# This function returns sorted list using bubble sort algorithm
# Input parameter:  It takes list object to be sorted as parameter.
# Returns True.

def bubble_sort(arr):

    #For n elemens we need to run the loop for n-1 passes
    n = len(arr)
    for i in range(0, n-1):
        # Everytime we find an largest element we need to run loop
        # one time less and hence n-1-i
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return True

# This method removes duplicates from list
def remove_dups(arr: list):
    n = len(arr)
    i = 0
    while i < n-1:
        if arr[i] != arr[i+1]:
            i=i+1
        else:
            arr.pop(i+1)
            # Removing one element from the list
            # need to adjust the end counter
            n=n-1
            # Note: we are not incrementing i because
            # after shifing left due to pop the current
            # i+1 can be again a duplicate and if we
            # increment the counter it will be skipped.
    print(f"new length of array is: {len(arr)}")
    return(len(arr))

def merge_sorted_lists(nums1: list, nums2: list):

    i=0
    for num in nums2:
        num_inserted = False
        while not num_inserted:
            print(f"processing num2 element : {num}")
            if (num <= nums1[i]):
                print(f"inserting {num} in at index {i}")
                nums1.insert(i, num)
                num_inserted = True
                i=i+1
            else:
                if (i == len(nums1)-1):
                    print(f"appending {num} in at index {i}")
                    nums1.append(num)
                    num_inserted = True
                    i=i+1
                else:
                    # safe to increment counter
                    i=i+1
                    print(f"num is >, i incremmented to {i}")

    return True

if __name__ == '__main__':
    import random
    arr = []
    for i in range(0,10):
       arr.append(random.randint(0,10))
    print(f"before sorting: {arr}")
    bubble_sort(arr)
    print(f"after sorting: {arr}")
    remove_dups(arr)
    print(f"after removing duplicates : {arr}")

    nums1=[]
    for i in range(0,10):
       nums1.append(random.randint(0,10))

    nums2=[]
    for i in range(0,10):
       nums2.append(random.randint(0,10))

    bubble_sort(nums1)
    bubble_sort(nums2)
    nums1 = [0, 1, 1, 2, 3, 5, 6, 6, 7, 8]
    nums2 = [0, 0, 2, 3, 5, 6, 6, 7, 9, 10]
    print(f"nums1 before = {nums1}")
    print(f"nums2 before = {nums2}")
    merge_sorted_lists(nums1,nums2)
    print(f"nums1 after = {nums1}")