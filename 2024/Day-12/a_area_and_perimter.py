from collections import deque
from pathlib import Path


def score_region(i, j, visited, grid) -> int:
    area = 0
    perimeter = 0
    region = grid[i][j]

    r, c = len(grid), len(grid[0])
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()
        area += 1
        if (i == 0) or (grid[i - 1][j] != region):
            perimeter += 1
        if (i == r - 1) or (grid[i + 1][j] != region):
            perimeter += 1
        if (j == 0) or (grid[i][j - 1] != region):
            perimeter += 1
        if (j == c - 1) or (grid[i][j + 1] != region):
            perimeter += 1

        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (
                (0 <= x < r)
                and (0 <= y < c)
                and (not visited[x][y])
                and (grid[x][y] == region)
            ):
                visited[x][y] = True
                q.append((x, y))

    return area * perimeter


def process_grid(grid: list[list]) -> int:
    r, c = len(grid), len(grid[0])

    visited = [[False for _ in range(c)] for _ in range(r)]
    res = 0
    for i in range(r):
        for j in range(c):
            if not visited[i][j]:
                visited[i][j] = True
                r = score_region(i, j, visited, grid)
                res += r
    return res


def solve(file_path: str) -> int:
    print(f"Solving: {file_path}")
    grid = []
    for line in Path(file_path).read_text().splitlines():
        grid.append(list(line))
    print(f"Grid: {len(grid)}x{len(grid[0])}")
    return process_grid(grid)


def test_solve_a():
    assert solve("example_12_1.txt") == 140
    assert solve("example_12_2.txt") == 772
    assert solve("example_12_3.txt") == 1930


if __name__ == "__main__":
    test_solve_a()

    # Main input
    print(solve("input_12.txt"))
