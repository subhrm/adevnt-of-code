"""
Find the umber of XMAS string in input grid.
"""

directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1))


def visit(grid: list[str], i: int, j: int) -> int:
    """
    Visit the grid starting from the given position (i, j) and count the number of XMAS strings.
    """
    d1,d2 = False, False

    # check diagonal 1
    if (grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S") or (grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M"):
        d1 = True
    
    # check diagonal 2
    if (grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S") or (grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M"):
        d2 = True

    return d1 & d2


def count_xmas(grid: list[str]) -> int:
    """
    Count the number of XMAS pairs in the grid.
    """
    count = 0
    m = len(grid)
    n = len(grid[0])

    # Iterate over each line in the grid
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == "A":
                count += visit(grid, i, j)

    # Return the total count of XMAS pairs
    return count


def process_input(input_file: str):
    print(f"Processing {input_file}")
    ip_grid = []
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                ip_grid.append(line.strip())

    print(count_xmas(ip_grid))


if __name__ == "__main__":
    process_input("example_04_0.txt")
    process_input("example_04.txt")
    process_input("input_04.txt")
