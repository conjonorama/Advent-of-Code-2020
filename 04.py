# Part 1 
import re

data = open('input_04.txt').read()
        
t = data.split('\n\n')


def evalLine(line):
    req_fields = 'byr iyr eyr hgt hcl ecl pid'.split()
    tot = 0
    d = {}
    pairs = line.split()
    for pair in pairs:
        pair = pair.split(':')
        d[pair[0]] = pair[1]
    for i in d.keys():
        if i in req_fields:
            tot += 1
    if tot == len(req_fields):
        return True 
    else:
        return False

pp_sum = 0

for i in range(len(t)):
    if evalLine(t[i]):
        pp_sum += 1

print(pp_sum)

# Part 2

# for i in range(5):
#     print(t[i].split())

# for line in t:
#     if len(line) > 0:
        