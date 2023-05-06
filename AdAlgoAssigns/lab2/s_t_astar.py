import numpy as np
import heapq


def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def execute(map, start, end):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    close_set_start = set()
    came_from_start = {}
    gscore_start = {start: 0}
    fscore_start = {start: heuristic(start, end)}
    oheap_start = []

    heapq.heappush(oheap_start, (fscore_start[start], start))

    close_set_end = set()
    came_from_end = {}
    gscore_end = {end: 0}
    fscore_end = {end: heuristic(end, start)}
    oheap_end = []

    heapq.heappush(oheap_end, (fscore_end[end], end))

    intersect_node = None

    while oheap_start and oheap_end:

        if oheap_start[0][0] < oheap_end[0][0]:
            current = heapq.heappop(oheap_start)[1]

            if current in close_set_start:
                continue

            close_set_start.add(current)

            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore_start[current] + np.sqrt(i ** 2 + j ** 2)

                if 0 <= neighbor[0] < map.shape[0]:
                    if 0 <= neighbor[1] < map.shape[1]:
                        if map[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set_start and tentative_g_score >= gscore_start.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore_start.get(neighbor, 0) or neighbor not in [i[1] for i in oheap_start]:
                    came_from_start[neighbor] = current
                    gscore_start[neighbor] = tentative_g_score
                    fscore_start[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(oheap_start, (fscore_start[neighbor], neighbor))

                    if neighbor in came_from_end:
                        intersect_node = neighbor
                        break

            if intersect_node:
                data = []
                node = intersect_node
                while node in came_from_start:
                    data.append(node)
                    node = came_from_start[node]
                node = came_from_end[intersect_node]
                while node in came_from_end:
                    data.append(node)
                    node = came_from_end[node]
                data.append(start)
                return [tuple(reversed(x)) for x in data[::-1]]

        else:
            current = heapq.heappop(oheap_end)[1]

            if current in close_set_end:
                continue

            close_set_end.add(current)

            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore_end[current] + np.sqrt(i ** 2 + j ** 2)

                if 0 <= neighbor[0] < map.shape[0]:
                    if 0 <= neighbor[1] < map.shape[1]:
                        if map[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set_end and tentative_g_score >= gscore_end.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore_end.get(neighbor, 0) or neighbor not in [i[1] for i in oheap_end]:
                    came_from_end[neighbor] = current
                    gscore_end[neighbor] = tentative_g_score
                    fscore_end[neighbor] = tentative_g_score + heuristic(neighbor, start)
                    heapq.heappush(oheap_end, (fscore_end[neighbor], neighbor))

                    if neighbor in came_from_start:
                        intersect_node = neighbor
                        break

            if intersect_node:
                data = []
                node = intersect_node
                while node in came_from_end:
                    data.append(node)
                    node = came_from_end[node]
                node = came_from_start[intersect_node]
                while node in came_from_start:
                    data.append(node)
                    node = came_from_start[node]
                data.append(end)
                return [tuple(reversed(x)) for x in data]

    return None
