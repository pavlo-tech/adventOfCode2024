def get_data():
    with open('inputs/day1.txt') as f:
        lines = f.readlines()
        values = [tuple([int(val) for val in l.split("   ")]) for l in lines]

        return map(list, zip(*values))




def count_occurrences(lv, r):
    return len(list(filter(lambda rv: rv == lv, r)))

[l, r] = get_data()

sim_score = sum([lv * count_occurrences(lv, r) for lv in l])

print(sim_score)


