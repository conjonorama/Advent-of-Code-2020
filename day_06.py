# def count_entry(txt):
#     """
#     return sum entries in one group
#     >>> count_entry('abac')
#     3
#     """
#     d = {}
#     for c in txt:
#         d[c] = d.get(c, 0) + 1
    
#     return(len(d.keys()))


def group_count(txt):
    """
    >>> data = '''a
    ... b
    ... c'''
    >>> group_count(data)
    3
    """
    answers = set() # no empty set literal
    for line in txt.split('\n'):
        answers.update(set(line))
    return len(answers)

def group_count2(txt):
    """
    >>> data = '''ab
    ... ac
    ... ad'''
    >>> group_count2(data)
    1
    """
    d = {}
    for line in txt.split():
        for c in line:
            d[c] = d.get(c, 0) + 1
    tot = 0
    t = []
    for k, v in d.items():
        if v == len(txt.split()):
            t.append((k,v))
            tot += 1
    return tot

def part1():
    data = open('input_06.txt', encoding='utf8').read()
    total = 0
    for group in data.split('\n\n'):
        total += group_count(group)
    print(total)

def part2():
    data = open('input_06.txt', encoding='utf8').read()
    total = 0
    for group in data.split('\n\n'):
        total += group_count2(group)
    print(total)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # part1()
    part2()