from pathlib import Path


def get_stone_count(line: list[int], steps: int = 0):
    cnt = {}
    for a in line:
        cnt[a] = cnt.get(a, 0) + 1
    
    for _ in range(steps):
        new_cnt = {}
        for a, c in cnt.items():
            spawn = []
            s = str(a)
            if a == 0:
                spawn.append(1)
            elif len(s)%2 == 0:
                left = s[:len(s)//2]
                right = s[len(s)//2:]
                spawn.append(int(left))
                spawn.append(int(right))
            else:
                spawn.append(a*2024)

            for b in spawn:
                new_cnt[b] = new_cnt.get(b, 0) + c

        cnt = new_cnt

    return sum(cnt.values())


def solve(file_path: str, steps:int) -> int:
    line = list(map(int, Path(file_path).read_text().split()))

    return get_stone_count(line, steps)


if __name__ == "__main__":
    # part A
    print("Part A")
    assert solve("example_11.txt", 25) == 55312
    print(solve("input_11.txt", 25))

    # part B
    print("Part B")
    print(solve("input_11.txt", 75))
