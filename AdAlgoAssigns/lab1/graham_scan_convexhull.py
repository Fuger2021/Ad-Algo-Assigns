import time
import numpy as np


def test_execute(points):
    start = time.time()
    s_points = sorted(points, key=lambda p: p[0])
    end = time.time()
    return end - start, s_points[:5]


def execute(points):
    start = time.time()
    def inner_prod(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    left_max = 0
    for i in range(len(points)):
        if points[i][1] < points[left_max][1]:
            left_max = i

    s_points = sorted(points, key=lambda p: np.arctan2(p[1] - points[left_max][1], p[0] - points[left_max][0]))
    convexhull = [points[0], s_points[0]]
    for i, s in enumerate(s_points):
        if i < 1:
            continue
        while True:
            if inner_prod(convexhull[-2], convexhull[-1], s) <= 0:
                convexhull.pop()
            if len(convexhull) >= 2:
                break
        convexhull.append(s)

    end = time.time()
    return end - start, convexhull
