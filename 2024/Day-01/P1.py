res = 0 

list1 = []
list2 = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            a,b = map(int, line.split())
            list1.append(a)
            list2.append(b) 

print(f"Read {len(list1)} lines")

list1.sort()
list2.sort()

res = sum( abs(a-b) for a,b in zip(list1,list2)  )
print(f"Final result {res}")
