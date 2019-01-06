#!/usr/bin/python3
import pprint
from operations import op

def process(trace):
    ip = 0
    cases = []
    while ip < len(trace):
        if len(trace[ip]) == 0:
            ip += 1
            continue
        reg = list(map(int, trace[ip][9:-1].split(',')))
        instr = list(map(int, trace[ip + 1].split(' ')))
        res = list(map(int, trace[ip + 2][9:-1].split(',')))
        cases.append([reg, instr, res])
        ip += 3
    return cases


if __name__ == '__main__':
    trace = [line.rstrip('\n') for line in open('input1.txt')]
    cases = process(trace)

    # part 1
    counts = {}
    for o in range(16):
        counts[o] = {}
    res1 = 0
    for case in cases:
        match = 0
        for oname in [oname for oname in op.keys() if case[2] == op[oname](case[0], case[1])]:
            match +=1
            counts[case[1][0]][oname] = counts[case[1][0]][oname] + 1 if counts[case[1][0]].get(oname) else 1
        if match >= 3:
            res1 += 1
    print(res1)

    # part 2
    # identify ops
    identified = {}
    while True:
        for o, c in {o:c for (o, c) in counts.items() if len(c) == 1 and not identified.get(o)}.items():
            identified[o] = list(c.keys())[0]
        for o, c in counts.items():
            counts[o] = {key:value for (key, value) in c.items() if key not in identified.values() and value == max(c.values())}
        if len(identified.keys()) == 16:
            break
    # run program
    program = [list(map(int, line.split())) for line in open('input2.txt')]
    regs = [0, 0, 0, 0]
    for line in program:
        regs = op[identified[line[0]]](regs, line)
    print(regs[0])
