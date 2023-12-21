
# 5. Graph and Pathfinding Utilities
import heapq
from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


def dijkstra(use_graph=False, grid=None, graph=None, grid_wall_val="#"):
    """Dijkstra's algorithm either with a grid (with numbers as distances and grid_wall_val as wall)
    or graph as list of tuples as (start, dist, end), returns total distance and path points"""

    if use_graph:
        return dijkstra_graph(graph)
    else:
        return dijkstra_grid(grid, grid_wall_val)


def dijkstra_grid(grid, wall_val):
    if not grid:
        return 0, []

    rows, cols = len(grid), len(grid[0])
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    distances[(0, 0)] = grid[0][0]

    min_heap = [(distances[(0, 0)], (0, 0))]
    path = {}

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if node == (rows - 1, cols - 1):
            break

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] != wall_val:
                alt = dist + grid[x][y]
                if alt < distances[(x, y)]:
                    distances[(x, y)] = alt
                    heapq.heappush(min_heap, (alt, (x, y)))
                    path[(x, y)] = node

    if (rows - 1, cols - 1) not in path:
        return -1, []

    total_dist = distances[(rows - 1, cols - 1)]
    path_points = []
    current = (rows - 1, cols - 1)

    while current:
        path_points.append(current)
        current = path.get(current)

    path_points.reverse()
    return total_dist, path_points


def dijkstra_graph(graph):
    if not graph:
        return 0, []

    graph_dict = {}
    for start, dist, end in graph:
        if start not in graph_dict:
            graph_dict[start] = []
        graph_dict[start].append((dist, end))

    distances = {node: float('inf') for _, node in graph}
    distances[graph[0][0]] = 0

    min_heap = [(0, graph[0][0])]
    path = {}

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if node not in graph_dict:
            continue

        for next_dist, neighbor in graph_dict[node]:
            alt = dist + next_dist
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                heapq.heappush(min_heap, (alt, neighbor))
                path[neighbor] = node

    if graph[-1][2] not in path:
        return -1, []

    total_dist = distances[graph[-1][2]]
    path_points = []
    current = graph[-1][2]

    while current:
        path_points.append(current)
        current = path.get(current)

    path_points.reverse()
    return total_dist, path_points
