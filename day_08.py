# test_data = '''nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6'''

with open('input_08.txt', encoding='utf8') as f:
    test_data = f.read()

test_data_scrubbed = test_data.strip().split('\n')
lines = []
line = 0
acc = 0

while True: 
    # import re
    if line in lines:
        print(acc)
        break
    lines.append(line)
    instruction = test_data_scrubbed[line].split()[0]
    # print(instruction)
    sign = test_data_scrubbed[line].split()[1][0]
    # print(sign)
    magnitude = int(test_data_scrubbed[line].split()[1][1:])
    # print(magnitude)
    if instruction == 'nop':
        line += 1
        continue
    elif instruction == 'acc':
        if sign == '-':
            acc -= magnitude
            line += 1
            continue
        else:
            acc += magnitude
            line += 1
            continue
    elif instruction == 'jmp':
        if sign == '-':
            line -= magnitude
            continue
        else:
            line += magnitude
            continue




    # if test_data_scrubbed[line].split()[0] == 'nop':
    #     line += 1
    #     continue
    # elif test_data_scrubbed[line].split()[0] == 'jmp':
    #     if "-" in test_data_scrubbed[line].split()[1]:
    #         line -= int(re.search(r'\d+', test_data_scrubbed[line].split()[1]))
    #         continue
    #     else:
    #         line += int(re.search(r'\d+', test_data_scrubbed[line].split()[1]))
    #         continue
    # elif test_data_scrubbed[line].split()[0] == 'acc':
    #     if "-" in test_data_scrubbed[line].split()[1]:
    #         acc -= int(re.search(r'\d+', test_data_scrubbed[line].split()[1]))
    #         line += 1
    #         continue
    #     else:
    #         acc += int(re.search(r'\d+', test_data_scrubbed[line].split()[1]))
    #         line += 1
    #         continue



