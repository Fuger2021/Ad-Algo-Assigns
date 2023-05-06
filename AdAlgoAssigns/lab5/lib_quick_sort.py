import time


def execute(arr: list):
    start = time.time()
    arr.sort()
    return time.time() - start
