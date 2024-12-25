from collections import defaultdict
def parse_dir(data):
    
    pwd = []
    children = defaultdict(list)
    sizes = defaultdict(int)

    for line in data:
        line = line.strip()
        if line[0] == "$":
            cmd = line[2:]
            if cmd[:2] == "ls":
                pwd_str = "/".join(pwd)
                sizes[pwd_str] = 0
            elif cmd[:2] == "cd":
                path = cmd[3:]
                if path == "..":
                    pwd.pop()
                else:
                    pwd.append(path)
        else:
            a,name = line.split()
            pwd_str = "/".join(pwd)
            if a == "dir":
                sub_dir = "/".join(pwd+[name])
                children[pwd_str].append(sub_dir)
            else:
                s = int(a)
                sizes[pwd_str] += s

    def get_size(d):
        r = sizes[d]
        for c in children[d]:
            r += get_size(c)
        return r

    res = {}
    for k in sizes.keys():
        res[k] = get_size(k)
    return res

def solve_a(all_dir):
    res  = 0
    for s in all_dir.values():
        if s <= 100000:
            res += s

    return res 

def solve_b(all_dir):
    MAX_SIZE = 70_000_000
    REQ = 30_000_000

    root_size = all_dir["/"]
    free_space = MAX_SIZE - root_size
    needed = REQ - free_space
    print(f"Size of root {root_size:,} free_space = {free_space:,}  Need {needed}")

    sizes = sorted(all_dir.values())
    for s in sizes:
        if s > needed:
            return s
    return -1


if __name__ == "__main__":
    with open("07-input.txt") as fin:
        data = fin.readlines()

    all_dir = parse_dir(data)

    print(f"All data read. Num lines = {len(data)}")

    print(f"{'='*15} A {'='*15}")
    res_a = solve_a(all_dir)
    print(f"Solution for problem A : {res_a}")

    print(f"{'='*15} B {'='*15}")
    res_b = solve_b(all_dir)
    print(f"Solution for problem B : {res_b}")
    