from helpers import load_day_data


def solution(data):
    data = data.split('\n\n')
    data = [
        [int(i) for i in d.splitlines()]
        for d in data
    ]
    _max = max([sum(d) for d in data])
    print(_max)
    max_three = sum(sorted([sum(d) for d in data], reverse=True)[:3])
    print(max_three)

    return _max, max_three


if __name__ == '__main__':
    data = load_day_data('01')
    solution(data)
