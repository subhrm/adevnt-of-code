from string import ascii_lowercase, ascii_uppercase

char_map = {
    c:i+1 for i,c in enumerate(ascii_lowercase + ascii_uppercase)
}

if __name__ == "__main__":
    res = 0
    with open("03-input.txt") as fin:
        data = fin.readlines()
        l = len(data)
        assert l%3 == 0, "The file must has 3x lines"
        m = l//3
        for i in range(m):
            n = i*3
            a,b,c = data[n:n+3]
            a,b,c = a.strip(), b.strip(), c.strip()
            r = list(set(a).intersection(b).intersection(c))[0]
            res += char_map[r]
    print(res)

    