def do_moves(grid: list[list[int]], moves: str):
    move_map = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    m = len(grid)
    n = len(grid[0])

    # find start pos
    x, y = None, None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                x, y = i, j
                break

    for move in moves:
        dx, dy = move_map[move]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == 0:
            grid[x][y] = 0
            x, y = nx, ny
        elif grid[nx][ny] == 1:
            found_blank = False
            i, j = nx, ny
            while grid[i][j] != 2:
                if grid[i][j] == 0:
                    found_blank = True
                    break
                i, j = i + dx, j + dy

            if found_blank:
                while i != x or j != y:
                    grid[i][j] = grid[i - dx][j - dy]
                    i, j = i - dx, j - dy
                grid[x][y] = 0
                x, y = nx, ny


def score(grid: list[list[int]]) -> int:
    total = 0

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == 1:
                total += (100 * i) + j
    return total


def read_file(file_path: str) -> tuple[list, str]:
    char_map = {"#": 2, "O": 1, "@": -1, ".": 0}
    grid = []
    moves = []

    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                if line[0] == "#":
                    grid.append([char_map[c] for c in line])
                else:
                    moves.append(line)

    return (grid, "".join(moves))


def process_file(file_path: str) -> int:
    print(f"Processing file : {file_path}")
    grid, moves = read_file(file_path)
    do_moves(grid, moves)
    # for row in grid:
    #     print(row)
    return score(grid)


if __name__ == "__main__":
    print(process_file("example-s.txt"))
    print(process_file("example-l.txt"))
    print(process_file("input_15.txt"))
