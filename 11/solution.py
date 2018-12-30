#!/usr/bin/python3

# input
size = 300
serial = 9445


def power(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y + serial
    power_level *= rack_id
    hdigit = (power_level % 1000) // 100
    return hdigit - 5


def scan(grid, window):
    square = [[sum([sum(line[i:(i + window)]) for line in grid[j:(j + window)]]) for i in range(size - window + 1)] for j in range(size - window - 1)]
    maximum = max([max(line) for line in square])
    res = [[i + 1, j + 1] for j, v1 in enumerate(square) for i, v2 in enumerate(v1) if v2 == maximum][0]
    return [maximum, res]


if __name__ == '__main__':
    grid = [[power(i + 1, j + 1, serial=serial) for i in range(size)] for j in range(size)]

    # part 1
    scan(grid, 3)

    # part 2
    goal = -1
    for window in range(1, size+1):
        res = scan(grid, window)
        print('{}: {},{},{}'.format(res[0], res[1][0], res[1][1], window))
        # total grid sum is negative, there is a maximum for intermediate window size
        if res[0] > goal - 9:
            goal = res[0]
        else:
            break
