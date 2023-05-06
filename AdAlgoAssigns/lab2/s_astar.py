import numpy as np
import heapq
import math


def execute(map, start, end):
    gscore = {start: 0}
    fscore = {start: cost(start, end)}
    pathheap = []

    def cost(a, b):
        return math.sqrt(math.pow((b[0] - a[0]), 2) + math.pow((b[1] - a[1]), 2))

    visited = set()
    v_path = {}

    heapq.heappush(pathheap, (fscore[start], start))
    while pathheap:
        node = heapq.heappop(pathheap)[1]
        visited.add(node)
        vision_matrix = [(0, 1), (0, -1), (1, 0),
                         (-1, 0), (1, 1), (1, -1),
                         (-1, 1), (-1, -1)]

        for v in vision_matrix:
            visionable = node[0] + v[0], node[1] + v[1]
            t_g_score = gscore[node] + cost(v[0], v[1])

            if visionable in visited:
                if t_g_score >= gscore.get(visionable, 0):
                    continue
            v_y = [i[1] for i in pathheap]
            if t_g_score >= gscore.get(visionable, 0):
                if visionable in v_y:
                    continue
                v_path[visionable] = node
                gscore[visionable] = t_g_score
                fscore[visionable] = t_g_score + cost(visionable, end)
                heapq.heappush(pathheap, (fscore[visionable], visionable))
        if node == end:
            path = [node for node in v_path]
            path.append(start)
            ret_path = [reversed(x) for x in path]
            return ret_path.reverse()

    return None
