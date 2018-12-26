#!/usr/bin/python3
import string
import re


# read input
input = open('input.txt').readline().rstrip('\n')


def react(input):
    # create regular expressions for all letter pairs
    res = []
    for c in string.ascii_lowercase:
        res.append(c + c.upper() + '|' + c.upper() + c)

    # iteratively remove pairs
    poly = input
    while True:
        reaction = False
        for r in res:
            poly, nrep = re.subn(r, '', poly)
            reaction = reaction or nrep > 0
        if not reaction:
            break

    return poly


def main():
    # part 1
    res1 = react(input)
    print(len(res1))

    # part 2
    res2 = {}
    for c in string.ascii_lowercase:
        test = re.sub(c + '|' + c.upper(), '', input)
        res2[c] = len(react(test))
    print(res2)


if __name__ == '__main__':
    main()