from helpers import load_day_data


def solution(data):
    for i in range(0, len(data) - 4):
        sub = data[i:i + 4]

        if all([
            sub.count(c) == 1
            for c in sub
        ]):
            print(sub)
            start = i + 4
            print(start)
            break

    for i in range(0, len(data) - 14):
        sub = data[i:i + 14]

        if all([
            sub.count(c) == 1
            for c in sub
        ]):
            print(sub)
            second = i + 14
            print(second)
            break

    return start, second


if __name__ == '__main__':
    data = load_day_data('06')
    solution(data)
