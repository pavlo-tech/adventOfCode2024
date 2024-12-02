def get_data():
    with open('inputs/day1.txt') as f:
        lines = f.readlines()
        values = [tuple([int(val) for val in l.split("   ")]) for l in lines]

        return map(list, zip(*values))


def dist(lv, rv):
    return abs(lv - rv)

[l, r] = get_data()

l.sort()
r.sort()


zip_list = [*zip(l, r)]
print(zip_list)
sum_dist = sum([dist(lv, rv) for (lv, rv) in zip_list])
print(sum_dist)


