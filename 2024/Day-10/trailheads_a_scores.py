from pathlib import Path


def sum_of_heads(grid: list[list[int]]) -> int:
    r, c = len(grid), len(grid[0])
    mem = [[set() for _ in range(c)] for _ in range(r)]
    # check 9
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 9:
                mem[i][j].add((i, j))

    for k in range(8,-1,-1):
        for i in range(r):
            for j in range(c):
                if grid[i][j] == k:
                    for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0 <= a < r and 0 <= b < c and grid[a][b] == k+1:
                            mem[i][j] |= mem[a][b]

    return sum(len(mem[i][j]) for i in range(r) for j in range(c) if grid[i][j] == 0)


def solve(file_path: str) -> int:
    grid = []
    for line in Path(file_path).read_text().splitlines():
        grid.append(list(map(int, line)))
    print(f"Grid: {len(grid)}x{len(grid[0])}")
    return sum_of_heads(grid)


if __name__ == "__main__":
    print(solve("example_10.txt"))
    print(solve("input_10.txt"))
