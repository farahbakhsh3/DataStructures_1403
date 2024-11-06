import time

def normal_search(arr:list[int], num:int) -> int:
    for i,x in enumerate(arr):
        if x == num:
            return i
    return -1

def binary_search(arr:list[int], num:int) -> int:
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            high = mid - 1
        elif arr[mid] < num:
            low = mid + 1
    return -1

def calc_time(func, epoch:int = 10) -> int:
    total_time = 0
    for _ in range(epoch):
        arr = [i for i in range(1000000)]
        start = time.time_ns()
        func(arr, arr[-1])
        stop = time.time_ns()
        total_time += stop - start
    return total_time / 10


if __name__ == "__main__":
    print(f"normal search: {calc_time(normal_search)}ns")
    print(f"binary search: {calc_time(binary_search)}ns")