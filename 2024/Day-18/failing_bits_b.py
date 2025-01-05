from collections import deque


def find_path(grid: list[list[int]], grid_size: int):
    """
    Find the shortest path from the top left to the bottom right of the grid
    On the grid 1 is an obstacle. You can only move left, right, up or down
    """
    # Create a visited grid
    visited = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    visited[0][0] = True

    # Create a queue to store the coordinates
    queue = deque([(0, 0, 0)])

    # Create a list of directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y, dist = queue.popleft()

        if x == grid_size - 1 and y == grid_size - 1:
            return dist

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if new_x < 0 or new_x >= grid_size or new_y < 0 or new_y >= grid_size:
                continue

            if visited[new_y][new_x] or grid[new_y][new_x] == 1:
                continue

            visited[new_y][new_x] = True
            queue.append((new_x, new_y, dist + 1))

    return -1


def process_file(file_name: str, grid_size: int):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    with open(file_name, "r") as file:
        cnt = 0
        for line in file.readlines():
            cnt += 1
            line = line.strip()
            if line == "":
                continue
            y, x = map(int, line.split(","))
            grid[x][y] = 1
            if find_path(grid, grid_size) == -1:
                return (y,x)


    return (-1,-1)



if __name__ == "__main__":
    print(process_file("18_example_7x7.txt", 7))
    print(process_file("18_input_71x71.txt", 71))
