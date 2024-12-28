def solve(s, m):
    n = len(s)
    for i in range(m-1,n):
        b = set(s[i-m+1:i+1])
        if len(b) == m:
            return i+1

    return -1

if __name__ == "__main__":
    with open("06-input.txt") as fin:
        data = fin.read().strip()
    
    a_res = solve(data,4)
    print(f"Result for problem A : {a_res}")
    
    b_res = solve(data,14)
    print(f"Result for problem B : {b_res}")