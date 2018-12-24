#!/usr/bin/python3
import collections


def parse_claim(claim):
    id, cut =  claim.split(' @ ')
    cut = cut.split(': ')
    off = [int(s) for s in cut[0].split(',')]
    siz = [int(s) for s in cut[1].split('x')]
    return [id] + off + siz


# read instructions
cuts = list(map(parse_claim, [line.rstrip('\n') for line in open('input.txt')]))


def main():
    d = collections.defaultdict(int)

    # part 1
    for c in cuts:
        for i in range(0, c[3]):
            for j in range(0, c[4]):
                d[c[1] + i + 1000*(c[2] + j)] += 1
    print(len([f for f in d.values() if f > 1]))

    # part 2
    for c in cuts:
        single = 1
        for i in range(0, c[3]):
            for j in range(0, c[4]):
                if d[c[1] + i + 1000*(c[2] + j)] > 1:
                    single = 0
        if single:
            print(c)
            return


if __name__ == '__main__':
    main()