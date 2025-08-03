def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    def chunks(lst):
        for i in range(0, len(lst), 5):
            yield lst[i:i+5]

    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks(arr)]
    pivot = median_of_medians(medians, len(medians)//2)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))

nums = [12, 3, 5, 7, 4, 19, 26]
k = 3
print(f"{k}rd smallest element is", median_of_medians(nums, k - 1))
