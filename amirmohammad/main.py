import numpy as np
import time


array_size = 1000000
sorted_array = np.arange(array_size)


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


target_value = 999999


start_time = time.time()
linear_result = linear_search(sorted_array, target_value)
linear_time = time.time() - start_time


start_time = time.time()
binary_result = binary_search(sorted_array, target_value)
binary_time = time.time() - start_time


print(f"Linear Search Result: {linear_result}, Time: {linear_time:.6f} seconds")
print(f"Binary Search Result: {binary_result}, Time: {binary_time:.6f} seconds")
