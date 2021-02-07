# Part 1

t = []
with open('input_03.txt') as f:
    for line in f.readlines():
        t.append(line.strip())

# for i in range(len(t)):
    # print(len(t[i]))

x = 0
trees = 0
for i in t[1:]:
    # print(i)
    x += 3
    if x >= 31:
        x -= 31
    if i[x] == '#':
        trees += 1
    

print(trees)

