def parse_input(file_path):
    grid = []
    x, y = 0, 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                row = []
                for c in line:
                    match c:
                        case ".":
                            row.append(0)
                        case "#":
                            row.append(-1)
                        case "^":
                            row.append(1)
                            x = len(grid)
                            y = len(row)

                grid.append(row)

    print(f"Grid: {len(grid)}x{len(grid[0])}")
    return x, y, grid


if __name__ == "__main__":
    x, y, grid = parse_input("example_06.txt")
    print(f"Start at: {x},{y}")
    for row in grid:
        print(row)
