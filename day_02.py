# Day 2 Advent of Code Challenge

import re

inp = []
with open('input_02.txt') as f:
    for line in f:
        inp.append(line.strip().split())


def getRange(line):
    line = line[0].split('-')
    return(int(line[0]), int(line[1]))

def getLetter(line):
    line = line[1].split(':')
    return(line[0])

def evalLines(line):
    n1, n2 = getRange(line)
    char = getLetter(line)
    pw = line[-1]
    return n1 <= pw.count(char) <= n2

print(sum(evalLines(line) for line in inp))

def evalLines2(line):
    n1, n2 = getRange(line)
    char = getLetter(line)
    pw = line[-1]
    idx1 = n1-1
    idx2 = n2-1
    if pw[idx1] == char and pw[idx2] == char:
        return(False)
    elif pw[idx1] == char or pw[idx2] == char:
        return(True)
    else:
        return(False)

print(sum(evalLines2(line) for line in inp))
    