def get_data():
    with open('inputs/day2.txt') as f:
        lines = f.readlines()
        values = [[int(val) for val in l.split(" ")] for l in lines]

        return values


def is_safe(levels):
    prev = None
    isIncreasing = None
    for curr in levels:
        if prev is not None:
            if isIncreasing is None:
                isIncreasing = curr - prev > 0

            currentlyIncreasing = prev < curr
            if currentlyIncreasing != isIncreasing:
                return False
            diff = abs(curr - prev)
            if diff < 1 or diff > 3:
                return False
        prev = curr
    return True

def is_safe_with_level_removed(levels):
    if is_safe(levels):
        return True
    else:
        for idx, curr in enumerate(levels):
            removed_list = levels[0:idx] + levels[idx+1:]
            if is_safe(removed_list):
                return True
        return False


data = get_data()

print(sum(filter(lambda x: x, map(is_safe_with_level_removed, data))))



