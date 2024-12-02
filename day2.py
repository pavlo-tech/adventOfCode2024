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


data = get_data()

print(sum(filter(lambda x: x, map(is_safe, data))))



