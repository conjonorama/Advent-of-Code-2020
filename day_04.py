# Part 1 
import re

# data = open('input_04.txt').read()
        
# t = data.split('\n\n')

def parse_passport(txt):
    """
    >>> data = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    ... byr:1937 iyr:2017 cid:147 hgt:183cm'''
    >>> parse_passport(data)
    {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
    """
    pp = {kv.split(':')[0]:kv.split(':')[1]
    for kv in txt.split()}
    return pp
    
    # pp = {}
    # for kv in txt.split():
    #     k, v = kv.split(":")
    #     pp[k] = v
    # return pp

def parse_passports(txt):
    pps_txt = txt.split('\n\n')
    pps = [parse_passport(pp_txt) for pp_txt in pps_txt]
    return pps


def valid_passport(passport):
    '''
    Passports must have 7 keys, CID is optional
    '''
    keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return set(passport) >= keys

def valid_height(val):
    try:
        num, unit = re.match(r'(\d{2,3})(cm|in)$', val).groups()
    except AttributeError:
        return False
    if unit == 'cm':
        return 150 <= int(num) <= 193
    elif unit == 'in':
        return 59 <= int(num) <= 76



def valid_values(passport):
    keys = {'byr':lambda val: 1920 <= int(val) <= 2002,
    'iyr':lambda val: 2010 <= int(val) <= 2020,
    'eyr':lambda val: 2020 <= int(val) <= 2030,
    'hgt':valid_height,
    'hcl':lambda val: re.match(r'\#[a-f0-9]{6}$', val),
    'ecl':lambda val: val in set('amb blu brn gry grn hzl oth'.split()),
    'pid':lambda val: re.match(r'[0-9]{9}$', val)}
    for key, val in passport.items():
        if key not in keys:
                continue
        if not keys[key](val):            
            return False
    return True
    return set(passport) >= keys



'''
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
        return line 
    else:
        return False

fin_t = []

for i in range(len(t)):
    if evalLine(t[i]):
        fin_t.append(t[i])

print(len(fin_t))
# print(fin_t[0])

# Part 2
'''
