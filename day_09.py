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


    
