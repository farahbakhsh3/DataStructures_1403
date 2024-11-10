import time
import random

def linear_search(nums, s):
    for a in nums:
        if a == s:
            return True
    return -1

def binary_search(nums, s):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == s:
            return True

        if nums[mid] > s:
            high = mid - 1
        elif nums[mid] < s:
            low = mid + 1
    return -1

nums = list(range(1000000))

start = time.time()
print(linear_search(nums=nums, s=random.choice(nums)))
print(time.time() - start)

start = time.time()
print(binary_search(nums=nums, s=random.choice(nums)))
print(time.time() - start)
