import random
import time

arr = sorted([random.randint(1, 1000000) for _ in range(1000000)])

def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

target = random.choice(arr)

start_time = time.time()
linear_search(arr, target)
linear_search_time = time.time() - start_time

start_time = time.time()
binary_search(arr, target)
binary_search_time = time.time() - start_time

print(f"زمان اجرای جستجوی خطی: {linear_search_time} ثانیه")
print(f"زمان اجرای جستجوی باینری: {binary_search_time} ثانیه")
