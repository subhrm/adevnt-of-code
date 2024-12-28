
def solve_a(data):
    res = 0

    return res

def solve_b(data):
    res = 0

    return res

if __name__ == "__main__":
    data = []
    with open("08-input.txt") as fin:
        for line in fin:
            data.append(list(map(int,line.strip())))

    print(f"All data read. Num lines = {len(data)} width of lines : {len(data[0])}")

    print(f"{'='*15} A {'='*15}")
    res_a = solve_a(data)
    print(f"Answer for problem A : {res_a}")

    print(f"{'='*15} B {'='*15}")
    res_b = solve_b(data)
    print(f"Answer for problem B : {res_b}")
    