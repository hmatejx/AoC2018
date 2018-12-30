#!/usr/bin/python3

input = [452, 71250]


def game(np, nm):
    players = [[] for i in range(np)]
    circle = [0]
    pos = 0
    for m in range(1, nm + 1):
        if m % 23 == 0:
            pos = (pos - 7) % len(circle)
            t = circle[pos]
            del circle[pos]
            players[(m - 1) % np] += [m, t]
        else:
            pos = (pos + 2) % len(circle)
            if pos == 0:
                pos = len(circle)
            circle.insert(pos, m)
    print(max(list(map(sum, players))))


if __name__ == '__main__':
    # part 1
    game(*input)
    # part 2 (I am sure this can be done faster by explicitly calculating the taken values)
    game(np=input[0], nm=100*input[1])
