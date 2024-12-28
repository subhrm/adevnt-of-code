
def solve_a(data):
    tx,ty= 0,0
    hx,hy = 0, 0 
    visited = set( [ (tx,ty) ])

    for cmd, steps in data:
        if cmd == "R":
            hx += steps
        elif cmd == "L":
            hx -= steps
        elif cmd == "U":
            hy -= steps
        elif cmd == "D":
            hy += steps

        while not adjacent(hx,hy,tx,ty):
            if tx == hx:
                if hy > ty:
                    ty += 1
                else:
                    ty -= 1
            elif ty == hy:
                if hx > tx:
                    tx += 1
                else:
                    tx -= 1
            else:
                if hx > tx:
                    if hy > ty:
                        tx += 1
                        ty += 1
                    else:
                        tx += 1
                        ty -= 1
                else:
                    if hy > ty:
                        tx -= 1
                        ty += 1
                    else:
                        tx -= 1
                        ty -= 1

            visited.add((tx,ty))


    return len(visited)

def adjacent(hx,hy,tx,ty):

    if (abs(hy-ty) <= 1) and (abs(hx-tx) <= 1):
        return True

    return False

def solve_b(data):
    txs,tys= [0]*9, [0]*9
    hx,hy = 0, 0 
    visited = set( [ (0,0) ])

    for cmd, steps in data:
        for _ in range(steps):
            if cmd == "R":
                hx += 1
            elif cmd == "L":
                hx -= 1
            elif cmd == "U":
                hy -= 1
            elif cmd == "D":
                hy += 1

            for i in range(9):
                if i == 0:
                    _hx,_hy = hx,hy
                else:
                    _hx,_hy = txs[i-1], tys[i-1]

                tx,ty = txs[i], tys[i]
                while not adjacent(_hx,_hy,tx,ty):
                    if tx == _hx:
                        if _hy > ty:
                            ty += 1
                        else:
                            ty -= 1
                    elif ty == _hy:
                        if _hx > tx:
                            tx += 1
                        else:
                            tx -= 1
                    else:
                        if _hx > tx:
                            if _hy > ty:
                                tx += 1
                                ty += 1
                            else:
                                tx += 1
                                ty -= 1
                        else:
                            if _hy > ty:
                                tx -= 1
                                ty += 1
                            else:
                                tx -= 1
                                ty -= 1


                txs[i], tys[i] = tx, ty

            visited.add((txs[-1],tys[-1]))

    # print(visited)
    return len(visited)

if __name__ == "__main__":
    data = []
    with open("09-input.txt") as fin:
        for line in fin:
            cmd,steps = line.strip().split()
            data.append((cmd, int(steps)))

    print(f"All data read. Num lines = {len(data)}")

    print(f"{'='*15} A {'='*15}")
    res_a = solve_a(data)
    print(f"Answer for problem A : {res_a}")

    print(f"{'='*15} B {'='*15}")
    res_b = solve_b(data)
    print(f"Answer for problem B : {res_b}")
    