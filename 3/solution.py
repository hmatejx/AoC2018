#!/usr/bin/python3
import collections

# read instructions
claims = [line.rstrip('\n') for line in open('input.txt')]


def main():

    d = collections.defaultdict(int)
    # part 1
    for c in claims:
        cut = c.split(' @ ')[1].split(': ')
        off = [int(s) for s in cut[0].split(',')]
        siz = [int(s) for s in cut[1].split('x')]
        for i in range(0, siz[0]):
            for j in range(0, siz[1]):
                d[off[0] + i + 1000*(off[1] + j)] += 1
    x = [f for f in d.values() if f > 1]
    print(len(x))


if __name__ == '__main__':
    main()