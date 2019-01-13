#!/usr/bin/python3

area = [[c for c in line.rstrip('\n')] for line in open('input.txt')]
nx = len(area[0])
ny = len(area)


def neighbors(x, y):
    #    .  |  #
    n = [0, 0, 0]
    for j in range(max(y - 1, 0), min(y + 2, ny)):
        for i in range(max(x - 1, 0), min(x + 2, nx)):
            if j == y and i == x:
                continue
            if area[j][i] == '.':
                n[0] += 1
            elif area[j][i] == '|':
                n[1] += 1
            else:
                n[2] += 1
    return n


def evolve():
    global area
    newarea = [l[:] for l in area]
    for y in range(ny):
        for x in range(nx):
            n = neighbors(x, y)
            if area[y][x] =='.' and n[1] >= 3:
                newarea[y][x] = '|'
            elif area[y][x] == '|' and n[2] >= 3:
                newarea[y][x] = '#'
            elif area[y][x] == '#' and (n[1] < 1 or n[2] < 1):
                newarea[y][x] = '.'
    area = newarea


def resources():
    w = sum([len([l for l in line if l == '|']) for line in area])
    l = sum([len([l for l in line if l == '#']) for line in area])
    return w * l


if __name__ == '__main__':
    m = start = 0
    seen = {}
    resource = {}
    while True:
        m += 1
        evolve()
        key = ''.join([''.join(line) for line in area])
        if key in seen:
            start = seen[key]
            break
        seen[key] = m
        resource[m] = resources()
    period = m - start
    # part 1
    print(resource[10])
    # part 2
    print(resource[((1000000000 - start) % period) + start])
