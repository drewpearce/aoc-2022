from string import ascii_letters

from helpers import load_day_data


def solution(data):
    data = data.splitlines()
    priority = sum([
        ascii_letters.index([
            c for c in sack[:len(sack) // 2]
            if c in sack[len(sack) // 2:]
        ][0]) + 1
        for sack in data
    ])
    print(priority)

    badge_priority = sum([
        ascii_letters.index([
            c for c in data[i]
            if c in data[i - 1]
            and c in data[i - 2]
        ][0]) + 1
        for i in range(2, len(data), 3)
    ])
    print(badge_priority)

    return priority, badge_priority


if __name__ == '__main__':
    data = load_day_data('03')
    solution(data)
