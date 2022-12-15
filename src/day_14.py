from helpers import load_day_data


def parse_data(data):
    grid = {}

    for line in data.strip().splitlines():
        line = [
            (int(ln.split(',')[0]), int(ln.split(',')[1]))
            for ln in line.split(' -> ')
        ]

        for i in range(len(line) - 1):
            start_x = line[i][0]
            start_y = line[i][1]
            end_x = line[i + 1][0]
            end_y = line[i + 1][1]
            x_travel = 1 if end_x >= start_x else -1
            y_travel = 1 if end_y >= start_y else -1

            for x in range(start_x, end_x + x_travel, x_travel):
                for y in range(start_y, end_y + y_travel, y_travel):
                    grid[(x, y)] = '#'

    return grid


def down(pos):
    return (pos[0], pos[1] + 1)


def down_left(pos):
    return (pos[0] - 1, pos[1] + 1)


def down_right(pos):
    return (pos[0] + 1, pos[1] + 1)


def solution_1(grid):
    max_y = max([k[1] for k in grid.keys()])
    sand = 0

    while True:
        sand += 1
        pos = (500, 0)

        while True:
            if down(pos) not in grid:
                pos = down(pos)
            elif down_left(pos) not in grid:
                pos = down_left(pos)
            elif down_right(pos) not in grid:
                pos = down_right(pos)
            else:
                grid[pos] = 'o'
                break

            if pos[1] > max_y:
                sand -= 1
                break

        if pos[1] > max_y:
            break

    print(sand)

    return sand


def solution_2(grid):
    max_y = max([k[1] for k in grid.keys()])
    sand = 0

    while True:
        sand += 1
        pos = (500, 0)

        while True:
            if down(pos) not in grid:
                pos = down(pos)
            elif down_left(pos) not in grid:
                pos = down_left(pos)
            elif down_right(pos) not in grid:
                pos = down_right(pos)
            else:
                if pos == (500, 0):
                    print(sand)

                    return sand

                grid[pos] = 'o'
                break

            if pos[1] == 1 + max_y:
                grid[pos] = 'o'
                break


def solution(data):
    grid = parse_data(data)
    sol_1 = solution_1(grid)
    grid = parse_data(data)
    sol_2 = solution_2(grid)

    return sol_1, sol_2


if __name__ == '__main__':
    data = load_day_data('14')
    solution(data)
