import random
import time


def execute(data: list, p: int = 0, r: int = None):
    start = time.time()
    if r is None:
        r = len(data) - 1
    if p < r:
        i = random.randint(p, r)
        data[i], data[r] = data[r], data[i]
        pivot = data[r]
        i = p - 1
        for j in range(p, r):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[r] = data[r], data[i + 1]
        execute(data, p, i)
        execute(data, i + 2, r)
    return time.time() - start
