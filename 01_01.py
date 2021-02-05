# Starting day 1
# Using itertools to find combinations that sum to desired amount

import sys, itertools

def sumTo(inp, n, tot):
    t = []
    combs = itertools.combinations(inp, n)
    for i in combs:
        if sum(i) == tot:
            t.append(i)
    return(t)

def prod(inp):
    ans = 1
    for i in inp[0]:
        ans *= i
    return(ans)


if __name__ == '__main__':
    inp = []
    with open(sys.argv[1]) as f:
        for line in f:
            inp.append(int(line.strip()))
    arg_n = int(sys.argv[2])
    arg_tot = int(sys.argv[3])
    sols = sumTo(inp, arg_n, arg_tot)
    ans = prod(sols)
    print(ans)

# inp = []
# with open('input_01.txt') as f:
#     for line in f:
#        inp.append(int(line.strip()))


