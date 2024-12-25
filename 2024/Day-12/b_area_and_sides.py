from collections import defaultdict, deque
from pathlib import Path


def count_segments(arr: list[int]) -> int:
    arr.sort()
    cnt = 1
    prev = arr[0]
    for a in arr[1:]:
        if a != prev + 1:
            cnt += 1
        prev = a

    return cnt


def score_region(i, j, visited, grid) -> int:
    area = 0
    side_up = defaultdict(list)
    side_down = defaultdict(list)
    side_left = defaultdict(list)
    side_right = defaultdict(list)

    region = grid[i][j]

    r, c = len(grid), len(grid[0])
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()
        area += 1
        if (i == 0) or (grid[i - 1][j] != region):
            side_up[i].append(j)
        if (i == r - 1) or (grid[i + 1][j] != region):
            side_down[i].append(j)
        if (j == 0) or (grid[i][j - 1] != region):
            side_left[j].append(i)
        if (j == c - 1) or (grid[i][j + 1] != region):
            side_right[j].append(i)

        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (
                (0 <= x < r)
                and (0 <= y < c)
                and (not visited[x][y])
                and (grid[x][y] == region)
            ):
                visited[x][y] = True
                q.append((x, y))

    sides = 0
    for i, arr in side_up.items():
        sides += count_segments(arr)
    for i, arr in side_down.items():
        sides += count_segments(arr)

    for j, arr in side_left.items():
        sides += count_segments(arr)
    for j, arr in side_right.items():
        sides += count_segments(arr)

    # print(f"Region: {region}, Area: {area}, Sides: {sides}")

    return area * sides


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

    return process_grid(grid)


def test_solve_b():
    assert solve("example_12_1.txt") == 80
    assert solve("example_12_2.txt") == 436
    assert solve("example_12_4.txt") == 236
    assert solve("example_12_5.txt") == 368


if __name__ == "__main__":
    test_solve_b()

    # Main input
    res = solve("input_12.txt")
    print(f"Final Result: {res}")
