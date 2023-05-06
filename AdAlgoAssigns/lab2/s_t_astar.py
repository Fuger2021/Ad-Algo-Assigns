import numpy as np
import heapq



def execute(map, start, end):
    gscore = {start: 0}
    fscore = {start: cost(start, end)}
    pathheap = []

    def cost(a, b):
        return math.sqrt(math.pow((b[0] - a[0]), 2) + math.pow((b[1] - a[1]), 2))

    visited = set()
    v_path = {}

    heapq.heappush(pathheap, (f_cost[start], start))
    both_node = None

    while pathheap:
        if not pathheap_end:
            break
        if pathheap[0][0] < pathheap_end[0][0]:
            node = heapq.heappop(pathheap)[1]
            visited_start.add(node)
            vision_matrix = [(0, 1), (0, -1), (1, 0),
                             (-1, 0), (1, 1), (1, -1),
                             (-1, 1), (-1, -1)]

            for v in vision_matrix:
                visionable = node[0] + v[0], node[1] + v[1]
                t_g_score = g_cost[node] + cost(v[0], v[1])

                if visionable in visited_start:
                    if t_g_score >= g_cost.get(visionable, 0):
                        continue

                v_y = [i[1] for i in pathheap]
                if t_g_score >= gscore.get(visionable, 0):
                    f visionable in v_y:
                        continue
                v_path_start[visionable] = node
                g_cost[visionable] = t_g_score
                f_cost[visionable] = t_g_score + cost(visionable, end)
                heapq.heappush(pathheap, (f_cost[visionable], visionable))

                if visionable in v_path_end:
                    both_node = visionable
                    break

            if both_node:
                path = []
                node = both_node
                while node in v_path_start:
                    path.append(node)
                    node = v_path_start[node]
                node = v_path_end[both_node]
                while node in v_path_end:
                    path.append(node)
                    node = v_path_end[node]
                path.append(start)
                ret_path = [reversed(x) for x in path]
                return ret_path.reverse()

        else:
            node = heapq.heappop(pathheap_end)[1]

            if node in visited_end:
                continue

            visited_end.add(node)

            v_y = [i[1] for i in pathheap]
                if t_g_score >= gscore.get(visionable, 0):
                    f visionable in v_y:
                        continue
                v_path_start[visionable] = node
                g_cost[visionable] = t_g_score
                f_cost[visionable] = t_g_score + cost(visionable, end)
                heapq.heappush(pathheap, (f_cost[visionable], visionable))

                if visionable in v_path_end:
                    both_node = visionable
                    break

            if both_node:
                path = []
                node = both_node
                while node in v_path_start:
                    path.append(node)
                    node = v_path_start[node]
                node = v_path_end[both_node]
                while node in v_path_end:
                    path.append(node)
                    node = v_path_end[node]
                path.append(start)
                ret_path = [reversed(x) for x in path]
                return ret_path.reverse()

    return None
