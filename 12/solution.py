#!/usr/bin/python3

# read input
inFile = open('input.txt')
dots = '.....'
state = dots + inFile.readline().replace('initial state: ', '').rstrip('\n')
rules = [rule.rstrip('\n') for rule in inFile if rule is not '\n']
bignum = 50000000000


def generation(state, rules):
    if state[-5:] != dots:
        state = state + dots
    res = ''.join(state) # difficult to clone a string in python...
    for p in range(2, len(state) - 2):
        neigh = state[(p - 2):(p + 3)]
        match = False
        for r in rules:
            if neigh == r[0:5]:
                res = res[:p] + r[9] + res[(p + 1):]
                match = True
                break
    return res


def value(state):
    return sum([i - 5 for i in range(len(state)) if state[i] == '#'])


if __name__ == '__main__':
    # part 1
    for i in range(1, 21):
        state = generation(state, rules)
    res = value(state)
    print('Value after 20 generations: {}'.format(res))

    # part 2
    # find when gliders start appearing
    dold = 0
    old = res
    gen = 20
    while True:
        gen += 1
        state = generation(state, rules)
        new = value(state)
        dnew = new - old
        if dnew == dold:
            break
        old = new
        dold = dnew
print('\'Gliders\' appear at generation: {}'.format(gen))
print('Value after {} generations: {}'.format(bignum, new + (bignum - gen)*dnew))
