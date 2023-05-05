import time
import numpy as np


def test_execute(points):
    start = time.time()
    sorted_points = sorted(points, key=lambda p: p[0])
    end = time.time()
    return end - start, sorted_points[:5]


def execute(points):
    # 找到最下面的点并将其与points[0]交换
    start = time.time()
    min_idx = 0
    for i in range(len(points)):
        if points[i][1] < points[min_idx][1]:
            min_idx = i
    points[0], points[min_idx] = points[min_idx], points[0]

    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    # 根据极角排序points[1:]
    anchor = points[0]
    sorted_points = sorted(points[1:], key=lambda p: np.arctan2(p[1] - anchor[1], p[0] - anchor[0]))

    # 执行Graham Scan
    hull = [points[0], sorted_points[0]]
    for s in sorted_points[1:]:
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)

    end = time.time()
    return end - start, hull
