#!/usr/bin/python3

# read input
tracks = [[c for c in line.rstrip('\n')] for line in open('input.txt')]
nx, ny = len(tracks[0]), len(tracks)
carts = None


def tick_order():
    l = [[c, carts[c][0], carts[c][1]] for c in carts]
    l.sort(key=lambda x: x[2]*nx + x[1])
    return list(map(lambda x: x[0], l))


def tick():
    global carts
    coll = False
    # check for any mid-tick collisions and remove colliding carts
    for c in tick_order():
        if carts.get(c) == None:
            continue
        #colliding = None
        x, y, d = carts[c][0:3]
        if d == '>':
            colliding = [t for t in carts if t != c and carts[t][0] == x + 1 and carts[t][1] == y and carts[t][2] == '<']
        elif d == '<':
            colliding = [t for t in carts if t != c and carts[t][0] == x - 1 and carts[t][1] == y and carts[t][2] == '>']
        elif d == '^':
            colliding = [t for t in carts if t != c and carts[t][0] == x and carts[t][1] == y - 1 and carts[t][2] == 'v']
        else:
            colliding = [t for t in carts if t != c and carts[t][0] == x and carts[t][1] == y + 1 and carts[t][2] == '^']
        if len(colliding) > 0:
            coll = True
            k = colliding[0]
            print('Mid-tick collision at {},{} of cart {} and {}, removing...'.format(x, y, c, k))
            del carts[c]
            del carts[k]
    # move
    for c in tick_order():
        if carts.get(c) == None:
            continue
        x, y, d, o = carts[c]
        if d == '>' or d == '<':
            m = -1 if d == '<' else 1
            carts[c][0] += m
            nexttrack = tracks[y][x + m]
            if nexttrack == '\\':
                carts[c][2] = '^' if d == '<' else 'v'
            elif nexttrack == '/':
                carts[c][2] = 'v' if d == '<' else '^'
            elif nexttrack == '+':
                if o == 0:
                    carts[c][2] = 'v' if d == '<' else '^'
                elif o == 2:
                    carts[c][2] = '^' if d == '<' else 'v'
                carts[c][3] = (o + 1) % 3
        elif d == '^' or d == 'v':
            m = -1 if d == '^' else 1
            carts[c][1] += m
            nexttrack = tracks[y + m][x]
            if nexttrack == '\\':
                carts[c][2] = '<' if d == '^' else '>'
            elif nexttrack == '/':
                carts[c][2] = '>' if d == '^' else '<'
            elif nexttrack == '+':
                if o == 0:
                    carts[c][2] = '<' if d == '^' else '>'
                elif o == 2:
                    carts[c][2] = '>' if d == '^' else '<'
                carts[c][3] = (o + 1) % 3
        # remove any colliding carts
        colliding = [t for t in carts if t != c and carts[t][0] == carts[c][0] and carts[t][1] == carts[c][1]]
        if len(colliding) > 0:
            coll = True
            k = colliding[0]
            print('After-tick collision at {},{} of cart {} and {}, removing...'.format(x, y, c, k))
            del carts[c]
            del carts[k]

    return coll


if __name__ == '__main__':
    # find carts and replace carts with tracks
    carts = {}
    k = 0
    for j in range(ny):
        for i in range(nx):
            t = tracks[j][i]
            if t in ['^', '>', 'v', '<']:
                carts[k] = [i, j, t, 0]
                k += 1
                if t == 'v' or t ==  '^':
                    tracks[j][i] = '|'
                else:
                    tracks[j][i] = '-'

    # run
    print('Starting with {} carts...'.format(len(carts)))
    while len(carts) > 1:
        tick() # part 1 (will print the collision coordinates)
    for k, v in carts.items():
        print('Last cart located at {},{}...'.format(v[0], v[1])) # part 2 (position of the last cart)
