#!/usr/bin/python3
from datetime import datetime as dt, timedelta as td
import numpy as np


def parse_input(logline):
    return [dt.strptime(logline[1:17], '%Y-%m-%d %H:%M'), logline[19:]]


# read log and sort by time
log = list(map(parse_input, [line.rstrip('\n') for line in open('input.txt')]))
log.sort(key = lambda x: x[0])


# format log
def format_log(log):
    elog = []

    for ts, info in log:
        if info.find('#') > -1:
            g = int(info[7:(7 + info[7:].find(' '))])
            event = 'b'
        else:
            event = info[0]
        ts0 = dt(ts.year, ts.month, ts.day) if ts.hour == 0 else ts + td(minutes = 60 - ts.minute)
        elog.append([g, ts.minute if ts.hour == 0 else 0, event, '{}-{}-{}'.format(ts0.year, ts0.month, ts0.day), info])

    return elog


def main():
    # preprocess log
    elog = format_log(log)

    # get all guard IDs
    guards = list(set([e[0] for e in elog]))

    # construct schedule density matrix
    schedule = np.zeros((len(guards), 60))
    for i in range(0, len(guards)):
        g = guards[i]
        entries = [e for e in elog if e[0] == g and e[2] != 'b']
        for j in range(0, len(entries), 2):
            schedule[i, entries[j][1]:entries[j+1][1]] += 1

    # part 1
    i = schedule.sum(axis = 1).argmax()
    guard = guards[i]
    minute = schedule[i, ].argmax()
    print(guard * minute)

    # part 2
    i = np.unravel_index(schedule.argmax(), schedule.shape)
    print(guards[i[0]] * i[1])


if __name__ == '__main__':
    main()