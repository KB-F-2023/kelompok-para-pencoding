import heapq

# fungsi heuristik banyaknya puzzle yang salah penempatan
def misplaced_tiles(state):
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    misplaced = sum([1 for i in range(9) if state[i] != goal[i]])
    return misplaced

# fungsi untuk mengembalikan langkah-langkah yang ditempuh untuk mencapai solusi
def get_path(node):
    path = []
    while node:
        path.append(node[3])
        node = node[2]
    return path[::-1]


# fungsi untuk mencari solusi
def solve(initial_state):
    heap = [(misplaced_tiles(initial_state), 0, None, initial_state)]
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
                heapq.heappush(heap, (g + 1 + misplaced_tiles(new_state), g + 1, (h, g, parent, state), new_state))
        if i not in [6, 7, 8]:  # move down
            new_state = state[:]
            new_state[i], new_state[i + 3] = new_state[i + 3], new_state[i]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (g + 1 + misplaced_tiles(new_state), g + 1, (h, g, parent, state), new_state))
        if i not in [0, 3, 6]:  # move left
            new_state = state[:]
            new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (g + 1 + misplaced_tiles(new_state), g + 1, (h, g, parent, state), new_state))
        if i not in [2, 5, 8]:  # move right
            new_state = state[:]
            new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (g + 1 + misplaced_tiles(new_state), g + 1, (h, g, parent, state), new_state))
    return None  # tidak ditemukan solusi

# contoh penggunaan
initial_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
path = solve(initial_state)
if path:
    print("Langkah-langkah yang ditempuh untuk mencapai solusi:")
    for i, state in enumerate(path):
        print(f"Langkah {i}:")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("Tidak ditemukan solusi.")S