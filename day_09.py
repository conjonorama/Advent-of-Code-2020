# test_data = '''
# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# '''
import itertools
with open('input_09.txt', encoding='utf8') as f:
    test_data = f.read()
test_data = test_data.strip().split()
test_data_int = [int(i) for i in test_data]

n = 25
start = 25
magic_num = 0
for i in test_data[start:]:
    combs = itertools.combinations(test_data[(start-n):start], 2)
    combs_sum = []
    for c in combs:        
        combs_sum.append(int(c[0]) + int(c[1]))
    if int(i) not in combs_sum:
        magic_num = i
        break
    else:
        start += 1

print(magic_num)

# Part 2

inv_num = 400480901

for i in range(test_data_int.index(inv_num)):
    for j in range(i+1, test_data_int.index(inv_num)):
        if(sum(test_data_int[i:j])) == inv_num:
            print(test_data_int[i:j], min(test_data_int[i:j]), max(test_data_int[i:j]))

print(len(test_data_int))