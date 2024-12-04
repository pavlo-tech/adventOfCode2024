import re


def get_data():
    with open('inputs/day3.txt') as f:
        lines = f.readlines()
        return '\n'.join(lines)


def mul(vals):
    l, r = vals
    return int(l) * int(r)


to_mul = re.findall(r'mul\((\d+),(\d+)\)', get_data())
muls = map(mul, to_mul)

print(sum(muls))
