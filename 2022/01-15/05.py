def read_data(fname="05-input.txt"):
    n = 0
    commands = []
    stack = []
    with open(fname) as fin:
        for line in fin:
            if line[1] == "1":
                n = int(line.strip().split()[-1])
                break
            else:
                stack.append(line)
        for line in fin:
            line = line.strip()
            if line.startswith("move"):
                commands.append(line)
    return n, stack, commands


def process_stack(n, stack):
    s = [ [] for _ in range(n) ]
    for line in stack:
        for i in range(n):
            k = i*4
            c = line[k+1]
            if c != " ":
                s[i].append(c)
    return [ si[::-1] for si in s]        

def parse_command(cmd):
    ws = cmd.split()
    return map(int, (ws[1], ws[3], ws[5]))    

def process_command_A(n,processed_stack, commands):
    for cmd in commands:
        m,s,t = parse_command(cmd)
        for _ in range(m):
            x = processed_stack[s-1].pop()
            processed_stack[t-1].append(x)

    return "".join( si[-1] for si in processed_stack)

def process_command_B(n,processed_stack, commands):
    for cmd in commands:
        m,s,t = parse_command(cmd)
        b = [ processed_stack[s-1].pop() for _ in range(m)]
        while(b):
            x = b.pop()
            processed_stack[t-1].append(x)

    return "".join( si[-1] for si in processed_stack)


if __name__ == "__main__":
    n, stack, commands = read_data()
    processed_stack = process_stack(n, stack)
    # print(processed_stack)
    res = process_command_A(n,processed_stack, commands)
    print(f"Ressult for part A : {res}")

    processed_stack = process_stack(n, stack)
    # print(processed_stack)
    res = process_command_B(n,processed_stack, commands)
    print(f"Ressult for part B : {res}")
