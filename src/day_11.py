from copy import deepcopy
import re

from numpy import prod
import yaml

from helpers import load_day_data


class Monkey(object):
    def __init__(self, cfg):
        self.inspected = 0
        self._items = cfg.get('Starting items', '')

        if isinstance(self._items, str):
            self._items = [int(i) for i in self._items.split(', ')]
        elif isinstance(self._items, int):
            self._items = [self._items]

        op = cfg.get('Operation', '').replace('new = ', '')
        self.op = eval(f'lambda old: {op}')

        cond = cfg.get('Test', '')
        div = re.search(r'\d+', cond)
        div = int(div.group(0))
        self.mod = div
        self.cond = lambda val: val % div == 0

        _true = int(cfg.get('If true', '').split(' ')[-1])
        _false = int(cfg.get('If false', '').split(' ')[-1])
        self._next = lambda val: _true if self.cond(val) else _false


def run_rounds(monkeys, rounds, relief, super=None):
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            while monkey._items:
                item = monkey._items.pop(0)
                item = monkey.op(item)
                monkey.inspected += 1

                if relief:
                    item = item // 3
                else:
                    item = item % super if super else item

                _next = monkey._next(item)
                monkeys[_next]._items.append(item)

    return monkeys


def parse_data(data):
    data = data.replace('  If', 'If')
    data = yaml.safe_load(data)
    monkeys = [Monkey(v) for v in data.values()]

    return monkeys


def solution(data):
    monkeys = parse_data(data)

    _monkeys = run_rounds(deepcopy(monkeys), 20, True)
    srt = sorted([m.inspected for m in _monkeys], reverse=True)
    most_active_1 = srt[0] * srt[1]
    print(most_active_1)

    super = prod([m.mod for m in monkeys])
    _monkeys = run_rounds(deepcopy(monkeys), 10000, False, super)
    srt = sorted([m.inspected for m in _monkeys], reverse=True)
    most_active_2 = srt[0] * srt[1]
    print(most_active_2)

    return most_active_1, most_active_2


if __name__ == '__main__':
    data = load_day_data('11')
    solution(data)
