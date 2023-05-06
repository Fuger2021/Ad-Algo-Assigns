import time


def Median3_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return [min(arr), max(arr)]
    first = arr[0]
    last = arr[-1]
    mid = arr[len(arr) // 2]
    pivot = sorted([first, mid, last])[1]
    # pivot = get_pivot(arr)
    left = []
    right = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
    return Median3_quick_sort(left) + [pivot] * (arr.count(pivot)) + Median3_quick_sort(right)


def execute(arr):
    start = time.time()
    arr[:] = Median3_quick_sort(arr)
    end = time.time()
    return end - start
