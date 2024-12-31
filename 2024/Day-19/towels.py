def possible(s, patterns, mem):
    # print(f"Checking {s} with {patterns}")
    if len(s) == 0:
        return 1
    if s in mem:
        return mem[s]

    res = 0

    for p in patterns:
        if s.startswith(p):
            res += possible(s[len(p) :], patterns, mem)

    mem[s] = res
    return res


def read_file(file_path):
    patterns = []
    required = []
    with open(file_path, "r") as file:
        cnt = 0
        for line in file:
            line = line.strip()
            if cnt == 0:
                patterns = [p.strip() for p in line.split(",")]
            elif line:
                required.append(line)

            cnt += 1

    return patterns, required


def process_file(file_path):
    patterns, required = read_file(file_path)
    cnt, total = 0, 0
    for req in required:
        mem = {}
        r = possible(req, patterns, mem)
        total += r
        if r > 0:
            cnt += 1

    return cnt, total


if __name__ == "__main__":
    print(process_file("19_example.txt"))
    print(process_file("19_input.txt"))
