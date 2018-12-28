#!/usr/bin/python3


# read input
input = [[line[5], line[36]] for line in open('input.txt')]


def main1(deps, tasks):
    res = ''
    remaining = tasks[:]

    for i in range(len(tasks)):
        waiting = set(map(lambda x: x[1], deps))
        started = sorted([task for task in remaining if task not in waiting])[0]
        res += started
        remaining.remove(started)
        deps = list(filter(lambda x: x[0] is not started, deps))

    print(res)


def main2(deps, tasks, nworkers=2, delay=1):
    # set up workers
    workers = [['.', 0] for i in range(nworkers)]

    pending = tasks[:]
    done = []
    clock = 0
    while len(done) < len(tasks):
        # find tasks that can be started
        deps = list(filter(lambda x: x[0] not in done, deps))
        triggered = sorted([task for task in pending if task not in [d[1] for d in deps]])
        # find idle workers
        idle = [i for i in range(nworkers) if workers[i][1] == 0]
        # run tasks within limitations
        for i in range(min([nworkers, len(triggered), len(idle)])):
            workers[idle[i]] = [triggered[i], ord(triggered[i]) - ord('A') + delay + 1]
            pending.remove(triggered[i])
        # clock tick: do the work and check if job is finished
        clock += 1
        for w in [w for w in workers if w[1] > 0]:
            w[1] -= 1
            if w[1] == 0:
                done.append(w[0])
                w[0] = '.'

    print(clock)


if __name__ == '__main__':
    tasks = list(sorted(set([val for subset in input for val in subset])))
    main1(input, tasks)
    main2(input, tasks, nworkers = 5, delay = 60)