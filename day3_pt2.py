import re


def get_data():
    with open('inputs/day3.txt') as f:
        lines = f.readlines()
        return '\n'.join(lines)



pattern = r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))'
instructions = re.findall(pattern, get_data())

mul_sum = 0
should_do = True
for instruction in instructions:
    (l, r, dontVal, doVal) = instruction
    if dontVal == 'don\'t()':
        should_do = False
    elif doVal == 'do()':
        should_do = True
    elif should_do:
        mul_sum += int(l) * int(r)

print(mul_sum)
