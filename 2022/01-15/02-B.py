def score(a,b):
    return points[a][idx[b]]

idx = {"X": 0, "Y":1, "Z": 2}
points = {
    "A" : (3,4,8),
    "B" : (1,5,9),
    "C" : (2,6,7)
}

if __name__ == "__main__":
    res = 0
    with open("02-input.txt") as fin:
        for line in fin:
            a,b = line.strip().split()
            res += score(a,b)

    print(res)