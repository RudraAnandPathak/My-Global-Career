from heapq import heappush, heappop

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, end):
    open_list = []
    closed = set()

    start_node = Node(start)
    goal_node = Node(end)

    heappush(open_list, start_node)

    while open_list:
        current = heappop(open_list)

        if current.position == goal_node.position:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed.add(current.position)

        x, y = current.position

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                continue

            if grid[nx][ny] == 1:
                continue

            if (nx, ny) in closed:
                continue

            neighbor = Node((nx, ny), current)
            neighbor.g = current.g + 1
            neighbor.h = heuristic(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h

            skip = False
            for node in open_list:
                if node.position == neighbor.position and node.g <= neighbor.g:
                    skip = True
                    break

            if not skip:
                heappush(open_list, neighbor)

    return None


grid = [
    [0,0,0,0,0],
    [1,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0]
]

path = astar(grid, (0,0), (4,4))

print("Shortest Path:")
print(path)
