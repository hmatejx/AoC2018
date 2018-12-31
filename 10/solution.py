#!/usr/bin/python3
import re


# read input
input = [list(map(int, re.sub('position=<|velocity=<|>|,', '', line.rstrip('\n')).split())) for line in open('input.txt')]


def span(stars):
    x0, y0 = min(stars, key=lambda x: x[0])[0], min(stars, key=lambda x: x[1])[1]
    x1, y1 = max(stars, key=lambda x: x[0])[0], max(stars, key=lambda x: x[1])[1]
    return [x0, y0, x1, y1]


def paint(stars):
    ss = span(stars)
    nx, ny = ss[2] - ss[0] + 1, ss[3] - ss[1] + 1
    grid = [['.'] * nx for i in range(ny)]
    for y in range(ny):
        for star in [star for star in stars if star[1] == ss[1] + y]:
            grid[y][star[0] - ss[0]] = '#'
    for line in grid:
        print(''.join(line))


def main(stars):
    i = 0
    xspan = yspan = 1000000
    while True:
        for star in stars:
            star[0] += star[2]
            star[1] += star[3]
        i += 1
        ss = span(stars)
        xs, ys = ss[2] - ss[0] + 1, ss[3] - ss[1] + 1
        if xs < xspan:
            xspan = xs
        if ys < yspan:
            yspan = ys
        if xs > xspan or ys > yspan:
            for star in stars:
                star[0] -= star[2]
                star[1] -= star[3]
            paint(stars)
            print(i - 1)
            return


if __name__ == '__main__':
    main(input)