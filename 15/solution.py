#!/usr/bin/python3

world = None
nx = ny = None
units = None
state = None
DEBUG = 0


def paint(h=None, grid=None):
    if h:
        print(h)
    for j in range(ny):
        for i in range(nx):
            if state[j][i] == '.' and grid and grid[j][i] > 0:
                print('{}'.format(grid[j][i]), end='')
            else:
                print('{}'.format(state[j][i]), end='')
        print('\t   ' + ', '.join(map(str, [u for u in units if u.y == j and u.hp > 0])))
    print()


def flood_fill(x0, y0):
    grid = [[0 if c == '.' else -1 for c in line] for line in state]
    grid[y0][x0] = -1
    neigh = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    frontier = [[x0, y0, 0]]
    while frontier:
        f = min(frontier, key=lambda f: f[2])
        frontier.remove(f)
        for n in neigh:
            newx, newy = f[0] + n[0], f[1] + n[1]
            if grid[newy][newx] == 0:
                frontier.append([newx, newy, f[2] + 1])
                grid[newy][newx] = f[2] + 1
    return grid


class Unit():

    def __init__(self, id, kind, x, y, ap):
        self.id = id
        self.kind = kind
        self.hp = 200
        self.ap = ap
        self.x = x
        self.y = y

    def is_adjacent(self, x, y):
        return abs(self.x - x) + abs(self.y - y) == 1

    def closest_adjacent(self, dist):
        dmin, xmin, ymin = 1000, -1, -1
        neigh = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        for n in neigh:
            newx, newy = self.x + n[0], self.y + n[1]
            d = dist[newy][newx]
            if d <= 0:
                continue
            if d < dmin:
                dmin, xmin, ymin = d, newx, newy
        if dmin == 1000:
            return
        return [dmin, xmin, ymin]

    def enemies(self):
        return [t for t in units if t.kind != self.kind and t.hp > 0]

    def attack(self, targets):
        attackable = [t for t in targets if self.is_adjacent(t.x, t.y)]
        if attackable:
            a = min(attackable, key=lambda a: nx*ny*a.hp + a.y*nx + a.x)
            a.hp -= self.ap
            return 1
        return 0

    def move_and_attack(self):
        targets = self.enemies()
        if not targets:
            return 0
        if self.attack(targets):
            return 1
        dist = flood_fill(self.x, self.y)
        reachable = [r for r in [t.closest_adjacent(dist) for t in targets] if r]
        if not reachable:
            return 0
        dmin = min(reachable, key=lambda x: x[0])[0]
        closest = sorted([c[1:3] for c in reachable if c[0] == dmin], key=lambda t: t[1]*nx + t[0])[0]
        if self.is_adjacent(*closest):
            m = closest
        else:
            dist = flood_fill(*closest)
            m = self.closest_adjacent(dist)[1:3]
        if m:
            self.x, self.y = m
            self.attack(targets)
            return 1
        return 0

    def check_skip(self):
        if self.hp <= 0:
            return 0
        if self.enemies():
            return 1
        return -1

    def __str__(self):
        return '{}[{:>2}]'.format(self.kind, self.id) + '{' + '{:>2},{:>2}'.format(self.x, self.y) + '}' + '({:>3})'.format(self.hp)


def update_state():
    global state, units
    state = [[c for c in line] for line in world]
    for u in units:
        if u.hp > 0:
            state[u.y][u.x] = u.kind


def initialize(input, elves_ap=3):
    global world, nx, ny, units, state
    state = [[c for c in line.rstrip('\n')] for line in open(input)]
    world = [[c for c in line] for line in state]
    nx, ny = len(state[0]), len(state)
    units = []
    for j in range(ny):
        for i in range(nx):
            if state[j][i] == 'E' or state[j][i] == 'G':
                units.append(Unit(len(units), state[j][i], i, j, 3 if state[j][i] == 'G' else elves_ap))
                world[j][i] = '.'


def game(input='input.txt', elves_ap=3):
    initialize(input, elves_ap)
    paint(h='Initially:')
    rounds = 0
    victory = False
    while not victory:
        remaining = [u for u in units if u.hp > 0]
        remaining.sort(key=lambda u: nx*u.y + u.x)
        actions = [-1 if u.hp > 0 else 0 for u in remaining]
        for i in range(len(remaining)):
            u = remaining[i]
            actions[i] = u.check_skip()
            if actions[i] <= 0:
                continue
            actions[i] = u.move_and_attack()
            update_state()
        victory = not [u for u in remaining if u.hp > 0 and u.kind == 'E'] or not [u for u in remaining if u.hp > 0 or u.kind == 'G']
        if -1 in actions:
            break
        rounds += 1
    paint(h='Finally:')
    tothp = sum([u.hp for u in units if u.hp > 0])
    print('Part 1: {} ({}x{})'.format(rounds*tothp, rounds, tothp))


if __name__ == '__main__':
    # part 1
    game()

    # part 2
    totelves = len([u for u in units if u.kind == 'E'])
    ap = 4
    while True:
        game(elves_ap=ap)
        if len([u for u in units if u.kind == 'E' and u.hp > 0]) == totelves:
            break
        ap += 1
