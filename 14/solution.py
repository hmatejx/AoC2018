#!/usr/bin/python3

input = 290431
inputl = [c for c in str(input)]
recipes = None
elves = None


def iteration():
    global recipes
    r0, r1 = int(recipes[elves[0]]), int(recipes[elves[1]])
    recipes.extend([c for c in str(r0 + r1)])
    elves[0] = (elves[0] + r0 + 1) % len(recipes)
    elves[1] = (elves[1] + r1 + 1) % len(recipes)


def init():
    global recipes, elves
    recipes = ['3', '7']
    elves = [0, 1]


if __name__ == '__main__':
    # part 1
    init()
    while len(recipes) < input + 10:
        iteration()
    print(''.join(map(str, recipes[input:(input + 10)])))

    # part 2
    init()
    n = len(inputl)
    while recipes[-n:] != inputl and recipes[-(n + 1):-1] != inputl:
        iteration()
    if recipes[-n:] == inputl:
        print(len(recipes) - n)
    else:
        print(len(recipes) - n - 1)
