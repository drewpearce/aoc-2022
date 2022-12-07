from collections import deque
import re

from helpers import load_day_data


def generate_file_tree(data):
    tree = {}
    path = deque()

    for line in data:
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '/':
                path.clear()
                path.append('/')
            elif line[2] == '..' and path[-1] != '/':
                path.pop()
            else:
                path.append(line[2])

        elif re.match(r'^\d', line[0]):
            _tree = tree

            for i, p in enumerate(path):
                if p not in _tree:
                    _tree[p] = {'dirs': {}, 'sizes': [0], 'files': ['']}

                if i == len(path) - 1:
                    _tree = _tree[p]
                else:
                    _tree = _tree[p]['dirs']

            _tree['sizes'].append(int(line[0]))
            _tree['files'].append(line[1])

    return tree


def crawl(_tree, path, sizes, _max):
    size = sum(_tree['sizes'])

    if not _tree['dirs']:
        sizes['/'.join(path)] = size

        return size, size if size <= _max else 0, sizes

    cumulative = 0

    for name, _dir in _tree['dirs'].items():
        path.append(name)
        _size, _cumulative, _ = crawl(_dir, path, sizes, _max)
        path.pop()
        size += _size
        cumulative += _cumulative

    sizes['/'.join(path)] = size

    return size, cumulative + size if size <= _max else cumulative, sizes


def solution(data):
    data = [d.split(' ') for d in data.splitlines()]
    tree = generate_file_tree(data)
    path = deque(['/'])
    sizes = {}
    dir_size, cumulative_size, sizes = crawl(tree['/'], path, {}, 100000)
    print(cumulative_size)

    total_space = 70000000
    target_free = 30000000
    current_free = total_space - dir_size
    diff = target_free - current_free
    smallest = min([v for v in sizes.values() if v >= diff])
    print(smallest)

    return cumulative_size, smallest


if __name__ == '__main__':
    data = load_day_data('07')
    solution(data)
