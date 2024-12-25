with open("01-input.txt") as fin:
    data = fin.read().splitlines()

calories=[]
c = 0
for line in data:
    if len(line.strip())  == 0:
        calories.append(c)
        c = 0
    else:
        n = int(line)
        c += n

calories.append(c)
calories.sort(reverse=True)

print(f"max_val = {calories[0]}")
print(f"Sum of top 3 vals {sum(calories[:3])}")
        