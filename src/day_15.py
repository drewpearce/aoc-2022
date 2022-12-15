import re

from helpers import load_day_data


def distance(one, two):
    return sum((abs(one[0] - two[0]), abs(one[1] - two[1])))


def parse_data(data):
    grid = {}

    for line in data.strip().splitlines():
        ints = re.findall(r'-?\d+', line)
        s = (int(ints[0]), int(ints[1]))
        b = (int(ints[2]), int(ints[3]))
        grid[s] = {
            'value': 'S',
            'closest': b,
            'distance': distance(s, b)
        }
        grid[b] = {
            'value': 'B'
        }

    return grid


def solution_1(grid, target_y):
    affected_sensors = {}

    for k, v in grid.items():
        if v['value'] == 'S':
            wiggle_room = v['distance'] - distance(k, (k[0], target_y))

            if wiggle_room >= 0:
                affected_sensors[k] = wiggle_room

    beacons = [k for k in grid.keys() if grid[k]['value'] == 'B']
    no_beacons = set()

    for k, v in affected_sensors.items():
        for x in range(k[0] - v, k[0] + v + 1):
            no_beacons.add((x, target_y))

    sol_1 = len([n for n in no_beacons if n not in beacons])
    print(sol_1)

    return sol_1


def get_untouched_edges(pos, dist, _max):
    untouched = set()

    for i in range(dist + 2):
        x = pos[0] + (dist - i) + 1
        y = pos[1] + i

        if 0 <= x <= _max and 0 <= y <= _max:
            untouched.add((x, y))

        y = pos[1] - i

        if 0 <= x <= _max and 0 <= y <= _max:
            untouched.add((x, y))

        x = pos[0] - (dist - i) - 1

        if 0 <= x <= _max and 0 <= y <= _max:
            untouched.add((x, y))

        y = pos[1] + i

        if 0 <= x <= _max and 0 <= y <= _max:
            untouched.add((x, y))

    return untouched


def solution_2(grid, _max):
    sensors = {k: v['distance'] for k, v in grid.items() if v['value'] == 'S'}
    # iterate through sensors
    for key, dist in sensors.items():
        # generate untouched egdes
        untouched = get_untouched_edges(key, dist, _max)

        # Check if untouched are in the range of other sensors
        for pos in untouched:
            covered = False

            for s, _dist in sensors.items():
                if s == key:
                    continue

                if distance(pos, s) <= _dist:
                    covered = True
                    break

            if covered is False:
                sol_2 = (pos[0] * 4000000) + pos[1]
                print(sol_2)

                return sol_2


def solution(data, sample=False):
    target_y = 10 if sample is True else 2000000
    _max = 20 if sample is True else 4000000
    grid = parse_data(data)
    sol_1 = solution_1(grid, target_y)
    sol_2 = solution_2(grid, _max)

    return sol_1, sol_2


if __name__ == '__main__':
    data = load_day_data('15')
    solution(data)
