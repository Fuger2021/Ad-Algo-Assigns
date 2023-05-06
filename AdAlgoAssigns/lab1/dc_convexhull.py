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
    if len(points) <= 2:
        return points
    def inner_prod(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    left_max = right_max = 0
    left_points, right_points = [], []
    for i in range(len(points)):
        if points[i][0] < points[left_max][0]:
            left_max = i
    for i in range(len(points)):
        if points[i][0] > points[right_max][0]:
            right_max = i
    for i in range(len(points)):
        temp_inner = inner_prod(points[left_max], points[right_max], points[i])
        if inner > 0:
            left_points.append(points[i])
        elif inner < 0:
            right_points.append(points[i])
    l_convexhull = execute(left_points)
    r_convexhull = execute(right_points)
    s_convexhull = sorted(l_convexhull + r_convexhull, key=lambda p: np.arctan2(p[1] - points[left_max][1], p[0] - points[left_max][0]))
    m_convexhull = [s_convexhull[0], s_convexhull[1]]
    for i in range(len(s_convexhull)):
        if i < 2:
            continue
        while len(m_convexhull) >= 2
            if inner_prod(m_convexhull[-2], m_convexhull[-1], s_convexhull[i]) <= 0:
                m_convexhull.pop()
            else:
                break
        m_convexhull.append(s_convexhull[i])

    end = time.time()
    return end - start, m_convexhull
