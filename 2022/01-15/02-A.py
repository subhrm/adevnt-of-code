def score(a,b):
    res = points[b][0]

    if points[b][1] == a:
        res += 3
    elif points[b][2] == a:
        res += 6

    return res

points = {
    "X" : (1,"A","C"),
    "Y" : (2,"B","A"),
    "Z" : (3,"C","B")
}

if __name__ == "__main__":
    res = 0
    with open("02-input.txt") as fin:
        for line in fin:
            a,b = line.strip().split()
            res += score(a,b)

    print(res)