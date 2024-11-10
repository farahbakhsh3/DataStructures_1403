import timeit
import random

def linear_search(arr):
    target = random.choice(arr)

    for item in arr:
        if item == target:
            return True
    return False

def binary_search(arr):
    target = random.choice(arr)

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



# Create a sorted list of numbers for testing
sorted_list = list(range(1_000_000))

# Define the setup code for timeit
setup_code = '''
from __main__ import linear_search, binary_search, sorted_list
'''

# Define the test code for linear search
linear_test_code = '''
linear_search(sorted_list)
'''

# Define the test code for binary search
binary_test_code = '''
binary_search(sorted_list)
'''

# Measure execution time for linear search
linear_time = timeit.timeit(stmt=linear_test_code, setup=setup_code, number=10000)
print(f"Linear Search Time: {linear_time} seconds")

# Measure execution time for binary search
binary_time = timeit.timeit(stmt=binary_test_code, setup=setup_code, number=10000)
print(f"Binary Search Time: {binary_time} seconds")




