#!/usr/bin/python3
from operations import op

# read input
prog = [line.rstrip('\n') for line in open('input.txt')]

# global state
reg = ipr = ip = None

def init(ipar=[0]*8):
    global reg, ipr, ip
    reg = ipar[0:6]
    ipr, ip = ipar[6:]


def exec(line, debug=False):
    global reg, ipr, ip
    if line[0] == '#':
        ipr = int(line[3:])
        if debug: print('ipr={}'.format(ipr))
    else:
        reg[ipr] = ip
        if debug: print('ip={} {} {}'.format(ip, str(reg), line), end='')
        o, i = line[0:4], [0] + list(map(int, line[5:].split(' ')))
        reg = op[o](reg, i)
        if debug: print(' {}'.format(str(reg)))
        ip = reg[ipr]
        ip += 1


if __name__ == '__main__':
    # part 1
    init()
    exec(prog[0])
    while ip >= 0 and ip < len(prog) - 1:
        exec(prog[ip + 1])
    print(reg[0])

    # part 2
    init([1] + [0]*7)
    exec(prog[0])
    i = 1
    while ip >= 0 and ip < len(prog) - 1 and i < 30:
        exec(prog[ip + 1], True)
        i += 1
    # part 2 calculates the sum of all factors of the number 10551282,
    # calculated by the program while reg[0] == 1.
    # afterwards reg[0] is changed to 0 and a double for loop is made with
    # incrementing the result if both loop parameters multiply into the
    # target number (basically a quadratic algorithm, which would take
    # O(10551282^2) of time).
    #
    # so the result below is obtained symbolically :)
    print('24117312')