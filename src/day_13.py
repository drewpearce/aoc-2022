from helpers import load_day_data


def parse_data_1(data):
    return [
        tuple(eval(s) for s in pair.split('\n'))
        for pair in data.split('\n\n')
    ]


def parse_data_2(data):
    return [
        eval(ln) for ln in data.replace('\n\n', '\n').splitlines()
    ] + [[[2]], [[6]]]


def is_ordered(left, right):
    ordered = False

    if isinstance(left, list) or isinstance(right, list):
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
        len_left = len(left)
        len_right = len(right)
        _ordered = None

        for i in range(len_left if len_left < len_right else len_right):
            _ordered = is_ordered(left[i], right[i])

            if _ordered is not None:
                break

        if _ordered is not None:
            ordered = _ordered
        elif len_left < len_right:
            ordered = True
        elif len_left > len_right:
            ordered = False
        else:
            ordered = None

    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            ordered = True
        elif left == right:
            ordered = None
        else:
            ordered = False

    return ordered


def solution_1(data):
    data = parse_data_1(data.strip())
    ordered = []

    for i, pair in enumerate(data):
        if is_ordered(pair[0], pair[1]):
            ordered.append(i + 1)

    sol_1 = sum(ordered)
    print(sol_1)

    return sol_1


def solution_2(data):
    data = parse_data_2(data.strip())
    ordered = []

    for d in data:
        for i in range(len(ordered)):
            if is_ordered(d, ordered[i]):
                ordered.insert(i, d)
                break

        if d not in ordered:
            ordered.append(d)

    sol_2 = (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)
    print(sol_2)

    return sol_2


def solution(data):
    sol_1 = solution_1(data)
    sol_2 = solution_2(data)

    return sol_1, sol_2


if __name__ == '__main__':
    data = load_day_data('13')
    solution(data)
