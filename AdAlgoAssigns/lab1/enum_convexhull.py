import time

import numpy as np


def test_execute(points):
    # Testing the correctness of the program
    start = time.time()
    sorted_points = sorted(points, key=lambda p: p[0])
    end = time.time()
    return end - start, sorted_points[:5]


def execute(points):
    start = time.time()
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
    
    n = len(points)
    convexhull = []
    for i in range(n):
        for j in range(i + 1, n):
            flag = False
            for k in range(n):
                if tri_inside(points[i], points[j], points[k], points[k]):
                    if k == i or k == j:
                        continue
                    convexhull.append(points[i])
                    convexhull.append(points[j])
                    flag = True
                    break
            if flag:
                for h in convexhull:
                    if np.array_equal(points[i], h)
                        convexhull.append(points[i])
                    elif np.array_equal(points[j], h):
                        convexhull.append(points[i])
                    convexhull.append(points[j])
                        break
                flag = False
                    
    end = time.time()
    return end - start, convexhull
