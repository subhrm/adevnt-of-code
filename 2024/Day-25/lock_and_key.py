from pathlib import Path


def parse_file(file_path: Path):
    """
    The locks are schematics that have the top row filled (#) and the bottom row empty (.);
    the keys have the top row empty and the bottom row filled.
    If you look closely, you'll see that each schematic is actually a set of columns of various heights,
    either extending downward from the top (for locks) or upward from the bottom (for keys).
    """

    locks = []
    keys = []

    cnt = 0
    input_type = None
    values = []
    for line in file_path.read_text().splitlines():
        cnt += 1

        if cnt % 8 == 7:
            if input_type == 1:
                locks.append(values)
            else:
                keys.append(values)

        elif cnt % 8 == 0:
            input_type = None

        elif cnt % 8 == 1:
            values = [0, 0, 0, 0, 0]
            if line[0] == "#":
                input_type = 1  # Lock
            else:
                input_type = -1  # Key
        else:
            for i in range(5):
                if line[i] == "#":
                    values[i] += 1

    return locks, keys


def get_matches(locks, keys):
    match_cnt = 0
    for i, lock in enumerate(locks):
        for j, key in enumerate(keys):
            is_match = True
            for k in range(5):
                if lock[k] + key[k] > 5:
                    is_match = False
                    break
            if is_match:
                match_cnt += 1

    return match_cnt


def process_file(file_path: str):
    print(f"Processing file: {file_path}")
    locks, keys = parse_file(Path(file_path))
    print(f"{len(locks)=}, {len(keys)=}")
    print(f"{get_matches(locks, keys)=}")


if __name__ == "__main__":
    process_file("example_25.txt")
    process_file("input_25.txt")
