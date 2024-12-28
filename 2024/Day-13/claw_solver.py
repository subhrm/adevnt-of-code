from pathlib import Path
from decimal import Decimal


def is_int(d: Decimal):
    return d.as_integer_ratio()[1] == 1


def solve(X, Y, params):
    """
    x1*a+x2*b = X
    y1*a+y2*b = Y

    b = (Y- y1*a)/y2

    x1*a + x2*(Y- y1*a)/y2 = X
    x1*y2*a - x2*y1*a = X*y2 - Y*x2
    """
    x1, y1, x2, y2 = params
    # print(f"Button A: ({x1},{y1}) Button B: ({x2},{y2}) Prize: ({X},{Y})")

    a = Decimal((X * y2) - (Y * x2)) / Decimal((x1 * y2) - (x2 * y1))
    b = Decimal(Y - (y1 * a)) / Decimal(y2)

    if a >= 0 and b >= 0 and is_int(a) and is_int(b):
        # print(f"Solution: a={a} b={b}")
        return 3 * int(a) + int(b)

    return 0


def get_parms(line, sep="+"):
    _, parm = line.split(":")
    x, y = parm.split(",")

    return [int(p.split(sep)[1]) for p in [x, y]]


def process_input_file(file_path, extra=0):
    res = 0
    params = []
    for line in Path(file_path).read_text().splitlines():
        line = line.strip()
        if len(line) == 0:
            continue

        if line.startswith("Button"):
            params.extend(get_parms(line))
        elif line.startswith("Prize"):
            X, Y = get_parms(line, "=")
            X = X + extra
            Y = Y + extra
            r = solve(X, Y, params)
            params.clear()
            res += r

    return res


def test_a():
    r = process_input_file("exmaple_13.txt")
    print(r)
    assert r == 480


if __name__ == "__main__":
    test_a()
    # Part - A
    print(process_input_file("input_13.txt"))
    # Part - B
    print(process_input_file("input_13.txt", extra=10000000000000))
