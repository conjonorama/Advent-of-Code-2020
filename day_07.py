def parse_lines(lines):
    res = {}
    for line in lines:
        res.update(parse_line(line))
    return res

def parse_line(txt):
    """
    >>> data = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    >>> parse_line(data)
    {'light red': ['bright white', 'muted yellow', 'muted yellow']}
    >>> data2 = 'dotted black bags contain no other bags'
    >>> parse_line(data2)
    {'dotted black': []}
    """
    color, other, = txt.strip().split(' bags contain ')
    others = other.split(', ')
    result = {}
    for bag_info in others:
        if 'no other' in txt:
            result[color] = []
            continue
        count = int(bag_info.split()[0])
        other_color = ' '.join(bag_info.split()[1:-1])
        if color not in result:
            result[color] = [other_color] * count   
        else:
            result[color].extend([other_color] * count)
    return result

def bfs(mapping, root, needle):
    if root == needle:
        return True
    q = []
    discovered = {root}
    q.append(root)
    while q:
        v = q.pop(0)
        if v == needle:
            return True
        for child in mapping.get(v, []):
            if child not in discovered:
                discovered.add(child)
                q.append(child)


def bft(mapping, root):
    q = []
    q.append(root)
    while q:
        v = q.pop(0)
        yield v
        for child in mapping.get(v, []):
            q.append(child)
                
def traverse_mapping(mapping, needle=None):
    count = 0
    for key in mapping:
        if bfs(mapping, key, needle):
            count += 1
    return count

def part1():
    with open('input_07.txt', encoding='utf8') as fin:
        lines = fin.readlines()
    mapping = parse_lines(lines)
    print(traverse_mapping(mapping, needle = 'shiny gold'))

def part2():
    with open('input_07.txt', encoding='utf8') as fin:
        lines = fin.readlines()
    mapping = parse_lines(lines)
    print(sum(1 for bag in bft(mapping, "shiny gold")))

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    part1()
    part2()


