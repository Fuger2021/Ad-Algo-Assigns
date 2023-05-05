import random
import numpy as np


def generating(size=1000):
    points = []
    for i in range(size):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        points.append(np.array([x, y]))
    return points
