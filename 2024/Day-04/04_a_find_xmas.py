"""
Find the umber of XMAS string in input grid.
"""


def visit(grid: list[str], mem: list[list[int]], i: int, j: int, step: int = 0) -> int:
    """
    Visit the grid starting from the given position (i, j) and count the number of XMAS strings.

    Args:
        grid (list[str]): A list of strings representing the grid.
        mem (list[list[int]]): A 2D list to store the memoized results.
        i (int): The row index of the starting position.
        j (int): The column index of the starting position.
        step (int, optional): The current step in the recursion. Defaults to 0.

    Returns:
        int: 1 if the current position is the start of an XMAS string, 0 otherwise.
    """
    if step >= 4:
        return 1

    # Check if the current position is out of bounds
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0

    # Check if the current position is already visited
    if mem[i][j] != -1:
        return mem[i][j]

    req = ("XMAS")[step]
    res = 0

    if grid[i][j] == req:
        # Check neighboring positions
        for di, dj in (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ):
            res += visit(grid, mem, i + di, j + dj, step + 1)

    # If the current position is not 'X', mark it as visited
    mem[i][j] = res
    return res


def count_xmas(grid: list[str]) -> int:
    """
    Count the number of XMAS strings in the grid.

    Args:
        grid (list[str]): A list of strings representing the grid.

    Returns:
        int: The number of XMAS strings found in the grid.
    """

    m = len(grid)
    n = len(grid[0])

    mem = [[-1 for _ in range(n)] for _ in range(m)]

    # Initialize the count of XMAS strings
    count = 0

    # Iterate over each line in the grid
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            # If the current character is 'X', increment the count
            if char == "X":
                count += visit(grid, mem, i, j)

    # Return the total count of XMAS strings

    for line in grid:
        print(line)
    print("="*30)
    for line in mem:
        print(line)

    return count


if __name__ == "__main__":
    ip_grid  = []

    while True:
        try:
            line = input()
            ip_grid.append(line.strip())
        except EOFError:
            break
    
    print(count_xmas(ip_grid))
