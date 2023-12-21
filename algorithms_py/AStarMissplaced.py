import heapq
import time

def a_star_search_missplaced(start, goal):
    def heuristic(state, goal):
        n = len(state)
        return sum(1 for i in range(n) for j in range(n) if state[i][j] != goal[i][j])

    def reconstruct_path(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]

    def get_neighbors(matrix):
        n = len(matrix)
        neighbors = []
        for i in range(n):
            for j in range(n):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = i + dx, j + dy
                    if 0 <= new_x < n and 0 <= new_y < n:
                        new_matrix = [row[:] for row in matrix]
                        new_matrix[i][j], new_matrix[new_x][new_y] = new_matrix[new_x][new_y], new_matrix[i][j]
                        neighbors.append(new_matrix)
        return neighbors

    start_time = time.time()
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {tuple(map(tuple, start)): 0}
    nodes_expanded = 0

    while frontier:
        _, current = heapq.heappop(frontier)
        nodes_expanded += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(came_from, tuple(map(tuple, current)))
            return path, nodes_expanded, len(path) - 1, (end_time - start_time) * 1000

        for next_state in get_neighbors(current):
            new_cost = cost_so_far[tuple(map(tuple, current))] + 1
            next_state_tuple = tuple(map(tuple, next_state))
            if next_state_tuple not in cost_so_far or new_cost < cost_so_far[next_state_tuple]:
                cost_so_far[next_state_tuple] = new_cost
                priority = new_cost + heuristic(next_state, goal)
                heapq.heappush(frontier, (priority, next_state))
                came_from[next_state_tuple] = tuple(map(tuple, current))

    end_time = time.time()
    return None, nodes_expanded, 0, (end_time - start_time) * 1000

# # Example usage 3x3
# initial_state = [[8, 6, 7],
#                  [2, 5, 4],
#                  [3, 0, 1]]
#
# goal_state = [[0, 1, 2],
#               [3, 4, 5],
#               [6, 7, 8]]
# # Example usage 4x4
# initial_state = [[15, 14, 8, 12],
#                  [10, 11, 9, 13],
#                  [2, 6, 5, 1],
#                  [3, 7, 4, 0]]
#
# goal_state = [[0, 1, 2, 3],
#               [4, 5, 6, 7],
#               [8, 9, 10, 11],
#               [12, 13, 14, 15]]
# # Example usage 5x5
# initial_state = [[24, 21, 19, 10, 17],
#               [22, 16, 11, 15, 14],
#               [13, 9, 5, 6, 7],
#               [3, 4, 8, 23, 18],
#               [2, 12, 20, 1, 0]]
# goal_state= [[0, 1, 2, 3, 4],
#                  [5, 6, 7, 8, 9],
#                  [10, 11, 12, 13, 14],
#                  [15, 16, 17, 18, 19],
#                  [20, 21, 22, 23, 24]]
#
#
# path, nodes_expanded, depth, runtime = a_star_search_missplaced(initial_state, goal_state)
#
# if path:
#     print("Path to solution:")
#     for step in path:
#         for row in step:
#             print(row)
#         print()
#     print(f"Total nodes expanded: {nodes_expanded}")
#     print(f"Depth of the solution: {depth}")
#     print(f"Runtime to find goal: {runtime:.2f} ms")
# else:
#     print("No solution found.")
#     print(f"Total nodes expanded: {nodes_expanded}")
#     print(f"Runtime: {runtime:.2f} ms")
