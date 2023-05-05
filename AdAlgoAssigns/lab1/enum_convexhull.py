import time

import numpy as np


def test_execute(points):
    # Testing the correctness of the program
    start = time.time()
    sorted_points = sorted(points, key=lambda p: p[0])
    end = time.time()
    return end - start, sorted_points[:5]


def inner_prod(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])


def tri_inside(a, b, c, d):
    vec_a_b = inner_prod(a, b, d)
    vec_c_b = inner_prod(b, c, d)
    vec_a_c = inner_prod(c, a, d)

    if vec_a_b >= 0:
        if vec_a_c >= 0:
            if vec_c_b >= 0:
                return True
    else:
        if vec_a_c <= 0:
            if vec_c_b <= 0:
                return True
    return False


def execute(points):
    start = time.time()
    n = len(points)
    hull = []
    for i in range(n):
        for j in range(i + 1, n):
            is_valid = True
            for k in range(n):
                if k != i and k != j and inside_triangle(points[i], points[j], points[k], points[k]):
                    is_valid = False
                    break
            if is_valid:
                for h in hull:
                    if np.array_equal(points[i], h) or np.array_equal(points[j], h):
                        is_valid = False
                        break
                if is_valid:
                    hull.append(points[i])
                    hull.append(points[j])
    end = time.time()
    return end - start, np.array(hull)
