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

# Part 2

def slope(inp, down, right):
    x = 0
    y = 0
    trees = 0
    while True:
        x += right
        y += down
        if y >= len(t):
            break
        if x >= 31:
            x -= 31
        if inp[y][x] == '#':
            trees += 1
    return trees

# x = 0
# y = 0

# while True:
#     if y > len(t): break
#     print(t[y])
#     y += 1

slope_1 = slope(t, 1, 1)
slope_2 = slope(t, 1, 3)
slope_3 = slope(t, 1, 5)
slope_4 = slope(t, 1, 7)
slope_5 = slope(t, 2, 1)

print(slope_1 * slope_2 * slope_3 * slope_4 * slope_5)
    
downs = [1, 1, 1, 1, 2]
rights = [1, 3, 5, 7, 1]

ans2 = []
for i in range(len(downs)):
    ans2.append(slope(t, downs[i], rights[i]))

import math
print((math.prod(ans2)))