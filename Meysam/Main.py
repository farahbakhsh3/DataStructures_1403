import time
import random

array_size = 1000000
sorted_array = list(range(array_size))

def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

target = random.randint(0, array_size - 1)

start_time = time.time()
linear_search_result = linear_search(sorted_array, target)
linear_search_time = time.time() - start_time

start_time = time.time()
binary_search_result = binary_search(sorted_array, target)
binary_search_time = time.time() - start_time
