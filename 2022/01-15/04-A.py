def check_complete_ovelap(a,b):
    x1,y1 = map(int, a.split("-"))
    x2,y2 = map(int, b.split("-"))
    
    if (x1>= x2 and x1<=y2 and y1<=y2) or (x2>= x1 and x2<=y1 and y2<=y1):
        return 1

    return 0

if __name__ == "__main__":
    res = 0
    with open("04-input.txt") as fin:
        for line in fin:
            a,b = line.strip().split(",")
            res +=  check_complete_ovelap(a,b)
        
    print(res)

    