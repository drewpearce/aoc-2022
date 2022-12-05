from helpers import load_day_data


def solution(data):
    data = [
        tuple(
            tuple(int(i) for i in _d.split('-'))
            for _d in d.split(',')
        )
        for d in data.splitlines()
    ]
    contains = sum([
        1 for d in data
        if (d[0][0] in range(d[1][0], d[1][1] + 1)
            and d[0][1] in range(d[1][0], d[1][1] + 1))
        or (d[1][0] in range(d[0][0], d[0][1] + 1)
            and d[1][1] in range(d[0][0], d[0][1] + 1))
    ])
    print(contains)

    overlaps = sum([
        1 for d in data
        if d[0][0] in range(d[1][0], d[1][1] + 1)
        or d[0][1] in range(d[1][0], d[1][1] + 1)
        or d[1][0] in range(d[0][0], d[0][1] + 1)
        or d[1][1] in range(d[0][0], d[0][1] + 1)
    ])
    print(overlaps)

    return contains, overlaps


if __name__ == '__main__':
    data = load_day_data('04')
    solution(data)
