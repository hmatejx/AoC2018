#!/usr/bin/python3
import sys

# read instructions
instructions = [int(line) for line in open('input.txt')]

def main():
    # part 1
    f = 0
    frequency = {}
    for i in instructions:
        f += i
        frequency[f] = 1
    print('Final frequency = {}'.format(f))

    # part 2
    while True:
        for i in instructions:
            f += i
            if f in frequency:
                print('Frequency {} is repeated'.format(f))
                return
            frequency[f] = 1

if __name__ == '__main__':
    main()