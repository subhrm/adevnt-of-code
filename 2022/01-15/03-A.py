from string import ascii_lowercase, ascii_uppercase

char_map = {
    c:i+1 for i,c in enumerate(ascii_lowercase + ascii_uppercase)
}

if __name__ == "__main__":
    res = 0
    with open("03-input.txt") as fin:
        for line in fin:
            line = line.strip()
            l = len(line)
            m = l//2
            a,b = line[:m], line[m:]
            s = set(a).intersection(set(b))
            for x in s:
                res += char_map[x]

    print(res)

    