from collections import Counter

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

cntr = Counter(list2)

res = sum( a*cntr[a] for a in list1  )
print(f"Final result {res}")
