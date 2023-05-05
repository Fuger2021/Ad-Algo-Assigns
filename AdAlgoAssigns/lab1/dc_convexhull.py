import time
import numpy as np
import time


def test_execute(points):
    start = time.time()
    sorted_points = sorted(points, key=lambda p: p[0])
    end = time.time()
    return end - start, sorted_points[:5]


def execute(points):
    start = time.time()

    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    # 找到最左边和最右边的点
    leftmost_idx = 0
    rightmost_idx = 0
    for i in range(len(points)):
        if points[i][0] < points[leftmost_idx][0]:
            leftmost_idx = i
        if points[i][0] > points[rightmost_idx][0]:
            rightmost_idx = i

    # 递归结束条件：只有两个或更少的点
    if len(points) <= 2:
        return points

    # 分别对左半部分和右半部分进行递归处理
    left_points = []
    right_points = []
    for i in range(len(points)):
        if ccw(points[leftmost_idx], points[rightmost_idx], points[i]) > 0:
            left_points.append(points[i])
        elif ccw(points[leftmost_idx], points[rightmost_idx], points[i]) < 0:
            right_points.append(points[i])

    left_hull = execute(left_points)
    right_hull = execute(right_points)

    # 合并左半部分和右半部分的凸包
    hull = left_hull + right_hull

    anchor = points[leftmost_idx]
    sorted_hull = sorted(hull, key=lambda p: np.arctan2(p[1] - anchor[1], p[0] - anchor[0]))

    merged_hull = [sorted_hull[0], sorted_hull[1]]
    for i in range(2, len(sorted_hull)):
        while len(merged_hull) >= 2 and ccw(merged_hull[-2], merged_hull[-1], sorted_hull[i]) <= 0:
            merged_hull.pop()
        merged_hull.append(sorted_hull[i])

    end = time.time()
    return end - start, merged_hull
