"""
Find the umber of XMAS string in input grid.
"""

directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1))


def visit(
    grid: list[str],
    i: int,
    j: int,
    d: int,
    step: int,
) -> int:
    """
    Visit the grid starting from the given position (i, j) and count the number of XMAS strings.
    """

    if step >= 4:
        return 1

    # Check if the current position is out of bounds
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0

    req = ("XMAS")[step]
    res = 0

    if grid[i][j] == req:
        di, dj = directions[d]
        res = visit(grid, i + di, j + dj, d, step + 1)

    return res


def count_xmas(grid: list[str]) -> int:
    """
    Count the number of XMAS strings in the grid.

    Args:
        grid (list[str]): A list of strings representing the grid.

    Returns:
        int: The number of XMAS strings found in the grid.
    """
    # Initialize the count of XMAS strings
    count = 0

    # Iterate over each line in the grid
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            # If the current character is 'X', increment the count
            if char == "X":
                for k in range(8):
                    count += visit(grid, i, j, k, 0)

    # Return the total count of XMAS strings
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
