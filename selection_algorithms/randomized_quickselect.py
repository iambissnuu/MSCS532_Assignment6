import random

def quickselect(arr, k):
    if not 1 <= k <= len(arr):
        return None

    def partition(low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def select(low, high, k):
        if low == high:
            return arr[low]
        pi = partition(low, high)
        if k == pi:
            return arr[pi]
        elif k < pi:
            return select(low, pi - 1, k)
        else:
            return select(pi + 1, high, k)

    return select(0, len(arr) - 1, k - 1)

nums = [7, 2, 1, 6, 8, 5, 3, 4]
k = 4
print(f"{k}th smallest element is", quickselect(nums, k))
