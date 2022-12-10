from helpers import load_day_data


def solution_1(data):
    cycles = [1]

    for line in data.splitlines():
        if line.startswith('n'):
            cycles.append(cycles[-1])
        else:
            cycles.append(cycles[-1])
            cycles.append(cycles[-1] + int(line.split(' ')[1]))

    power = sum([cycles[i] * (i + 1) for i in range(19, 220, 40)])
    print(power)
    return power, cycles


def solution_2(cycles):
    crt = ''

    for x, sprite in enumerate(cycles):
        if x % 40 in (sprite - 1, sprite, sprite + 1):
            crt += '#'
        else:
            crt += '.'

        if x % 40 == 39:
            crt += '\n'

    print(crt)


def solution(data):
    power, cycles = solution_1(data)
    with open('temp1.txt', 'w') as f:
        f.write('\n'.join([str(c) for c in cycles]))
    solution_2(cycles)
    return power, None


if __name__ == '__main__':
    data = load_day_data('10')
    solution(data)
