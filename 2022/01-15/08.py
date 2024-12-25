
def solve_a(data):
    m = len(data)
    n = len(data[0])
    left = [[0 for _ in range(n)] for _ in range(m)]
    right = [[0 for _ in range(n)] for _ in range(m)]
    top = [[0 for _ in range(n)] for _ in range(m)]
    bottom = [[0 for _ in range(n)] for _ in range(m)] 

    for i in range(m):
        p = 0
        for j in range(n):
            left[i][j] = p
            p = max(p,data[i][j])

    # print(f"Left: {len(left)} x {len(left[0])}")
    # print(left[2])

    for i in range(m):
        p = 0
        for k in range(n):
            j = n-k-1
            right[i][j] = p
            p = max(p,data[i][j])

    # print(f"Right: {len(right)} x {len(right[0])}")
    # print(right[2])


    for j in range(n):
        p = 0
        for i in range(m):
            top[i][j] = p
            p = max(p,data[i][j])

    # print(f"Top: {len(top)} x {len(top[0])}")
    # print(top[2])

    for j in range(n):
        p = 0
        for k in range(m):
            i = m-k-1
            bottom[i][j] = p
            p = max(p,data[i][j])
    # print(f"Top: {len(bottom)} x {len(bottom[0])}")
    # print(bottom[-3])
    

    res = 2*n + 2*(m-2)
    for i in range(1,m-1):
        for j in range(1,n-1):
            a = data[i][j]
            if (a > left[i][j]) or (a > right[i][j]) or (a > top[i][j]) or (a > bottom[i][j]):
                res += 1
    return res

def score(m,n,i,j,data):
    l,r,t,b = 0,0,0,0

    a = data[i][j]

    # top
    x = i-1
    while(x >= 0):
        t += 1
        if data[x][j] >= a:
            break
        x -= 1

    # bottom
    x = i+1
    while(x < m):
        b += 1
        if data[x][j] >= a:
            break
        x += 1

    # left
    x = j-1
    while(x >= 0):
        l += 1
        if data[i][x] >= a:
            break
        x -= 1
    
    # right
    x = j+1
    while(x < n):
        r += 1
        if data[i][x] >= a:
            break
        x += 1
    

    return l*r*t*b

def solve_b(data):
    res = 0
    m = len(data)
    n = len(data[0])

    for i in range(1,m-1):
        for j in range(1,n-1):
            s = score(m,n,i,j,data)
            res = max(res,s)

    return res

if __name__ == "__main__":
    data = []
    with open("08-input.txt") as fin:
        for line in fin:
            data.append(list(map(int,line.strip())))

    print(f"All data read. Grid size = {len(data)} x {len(data[0])}")

    print(f"{'='*15} A {'='*15}")
    res_a = solve_a(data)
    print(f"Solution for problem A : {res_a}")

    print(f"{'='*15} B {'='*15}")
    res_b = solve_b(data)
    print(f"Solution for problem B : {res_b}")
    