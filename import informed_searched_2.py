import heapq
import math

# fungsi heuristik jarak manhattan
def manhattan_distance(state):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x = abs(i % 3 - goal.index(state[i]) % 3)
            y = abs(i // 3 - goal.index(state[i]) // 3)
            distance += x + y
    return distance

# fungsi untuk mengembalikan langkah-langkah yang ditempuh untuk mencapai solusi
def get_path(node):
    path = []
    while node:
        path.append(node[3])
        node = node[2]
    return path[::-1]


# fungsi untuk mencari solusi
def solve(initial_state):
    heap = [(manhattan_distance(initial_state), 0, None, initial_state)]
    visited = set()
    while heap:
        (h, g, parent, state) = heapq.heappop(heap)
        if state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return get_path((h, g, parent, state))
        visited.add(tuple(state))
        i = state.index(0)
        if i not in [0, 1, 2]:  # move up
            new_state = state[:]
            new_state[i], new_state[i - 3] = new_state[i - 3], new_state[i]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (g + 1 + manhattan_distance(new_state), g + 1, (h, g, parent, state), new_state))
        if i not in [6, 7, 8]:  # move down
            new_state = state[:]
            new_state[i], new_state[i + 3] = new_state[i + 3], new_state[i]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (g + 1 + manhattan_distance(new_state), g + 1, (h, g, parent, state), new_state))
        if i not in [0, 3, 6]:  # move left
            new_state = state[:]
            new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (g + 1 + manhattan_distance(new_state), g + 1, (h, g, parent, state), new_state))
        if i not in [2, 5, 8]:  # move right
            new_state = state[:]
            new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (g + 1 + manhattan_distance(new_state), g + 1, (h, g, parent, state), new_state))
    return None  # tidak ditemukan solusi

# contoh penggunaan
initial_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
path = solve(initial_state)
if path:
    print("Steps taken to reach solution")
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("Solution not found.")