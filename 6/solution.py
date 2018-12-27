#!/usr/bin/python3
import copy


# read input
input = [list(map(int, line.split(','))) for line in open('input.txt')]


def main():
    # get extreme coordinates
    x0 = min(map(lambda x: x[0], input))
    y0 = min(map(lambda x: x[1], input))
    x1 = max(map(lambda x: x[0], input))
    y1 = max(map(lambda x: x[1], input))
    nx = x1 - x0 + 1
    ny = y1 - y0 + 1
    N = len(input)

    # construct an empty grid
    grid0 = [[0]*nx for i in range(ny)]

    # part 1
    grid = copy.deepcopy(grid0)
    # slow Voronoi tesselation
    for i in range(nx):
        for j in range(ny):
            mindist = nx*ny
            for k in range(N):
                x, y = input[k]
                d = abs(x - x0 - i) + abs(y - y0 - j)
                if d < mindist:
                    mindist = d
                    grid[j][i] = k + 1
                elif d == mindist:
                    grid[j][i] = 0

    # find the largest non-infinite area
    areas = []
    for k in range(N):
        x, y = input[k]
        if x == x0 or x == x1 or y == y0 or y == y1:
            continue
        areas.append([k + 1, len([val for line in grid for val in line if val == k + 1])])
    print(max(areas, key = lambda x: x[1])[1])

    # part 2
    grid = copy.deepcopy(grid0)
    for i in range(nx):
        for j in range(ny):
            d = 0
            for k in range(N):
                x, y = input[k]
                d += abs(x - x0 - i) + abs(y - y0 - j)
            if d < 10000:
                grid[j][i] = 1
    print(sum(map(sum, grid)))


if __name__ == '__main__':
    main()