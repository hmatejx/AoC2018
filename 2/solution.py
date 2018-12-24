#!/usr/bin/python3
import collections

# read instructions
ids = [line.rstrip('\n') for line in open('input.txt')]


def main():
    # part 1
    twos = 0
    threes = 0
    for id in ids:
        d = collections.defaultdict(int)
        for c in id:
            d[c] += 1
        twos += 2 in list(d.values())
        threes += 3 in list(d.values())
    print(twos * threes)

    # part 2
    for i1 in range(0, len(ids)):
        id1 = ids[i1]
        for i2 in range(i1 + 1, len(ids)):
            id2 = ids[i2]
            i = 0
            while i < len(id1) and id1[i] == id2[i]:
                i += 1
            j = i + 1
            while j < len(id1) and id1[j] == id2[j]:
                j += 1
            if j == len(id1):
                print('id1 = \t {}\nid2 = \t {}\ncommon = {}{}'.format(id1, id2, id1[0:i], id1[(i + 1):len(id1)]))
                return


if __name__ == '__main__':
    main()