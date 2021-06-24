import day_08

def test_small_input():
    data = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')
    assert day_08.process_instructions(data)[0] == 5

def test_input():
    data = open('input_08.txt', encoding='utf8').read().strip().split('\n')
    assert day_08.process_instructions(data)[0] == 1337

def test_part2():
    data = open('input_08.txt', encoding='utf8').read().strip().split('\n')
    assert day_08.part2(data) == 1358