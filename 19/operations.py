def addr(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] + res[instr[2]]
    return res

def addi(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] + instr[2]
    return res

def mulr(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] * res[instr[2]]
    return res

def muli(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] * instr[2]
    return res

def banr(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] & res[instr[2]]
    return res

def bani(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] & instr[2]
    return res

def borr(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] | res[instr[2]]
    return res

def bori(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]] | instr[2]
    return res

def setr(reg, instr):
    res = reg[:]
    res[instr[3]] = res[instr[1]]
    return res

def seti(reg, instr):
    res = reg[:]
    res[instr[3]] = instr[1]
    return res

def gtir(reg, instr):
    res = reg[:]
    res[instr[3]] = 1 if instr[1] > res[instr[2]] else 0
    return res

def gtri(reg, instr):
    res = reg[:]
    res[instr[3]] = 1 if res[instr[1]] > instr[2] else 0
    return res

def gtrr(reg, instr):
    res = reg[:]
    res[instr[3]] = 1 if res[instr[1]] > res[instr[2]] else 0
    return res

def eqir(reg, instr):
    res = reg[:]
    res[instr[3]] = 1 if instr[1] == res[instr[2]] else 0
    return res

def eqri(reg, instr):
    res = reg[:]
    res[instr[3]] = 1 if res[instr[1]] == instr[2] else 0
    return res

def eqrr(reg, instr):
    res = reg[:]
    res[instr[3]] = 1 if res[instr[1]] == res[instr[2]] else 0
    return res

op = {}
op['addr'] = addr
op['addi'] = addi
op['mulr'] = mulr
op['muli'] = muli
op['bani'] = bani
op['banr'] = banr
op['borr'] = borr
op['bori'] = bori
op['setr'] = setr
op['seti'] = seti
op['gtir'] = gtir
op['gtri'] = gtri
op['gtrr'] = gtrr
op['eqir'] = eqir
op['eqri'] = eqri
op['eqrr'] = eqrr
