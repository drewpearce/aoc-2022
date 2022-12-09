from helpers import load_day_data


def parse_instructions(data):
    return [
        (d.split(' ')[0], int(d.split(' ')[1]))
        for d in data.splitlines()
    ]


class Rope(object):
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.visited = set([pos])

    def move(self, direction):
        if 'L' in direction:
            self.x -= 1

        if 'R' in direction:
            self.x += 1

        if 'U' in direction:
            self.y += 1

        if 'D' in direction:
            self.y -= 1

        self.visited.add((self.x, self.y))


def move(knots, i, direction):
    knots[i].move(direction)
    t_move = ''

    if i == len(knots) - 1:
        return knots

    if (
        abs(knots[i].x - knots[i + 1].x) <= 1
        and abs(knots[i].y - knots[i + 1].y) <= 1
    ):
        return knots

    if knots[i].x != knots[i + 1].x and knots[i].y != knots[i + 1].y:
        if knots[i].x > knots[i + 1].x:
            t_move += 'R'
        else:
            t_move += 'L'

        if knots[i].y > knots[i + 1].y:
            t_move += 'U'
        else:
            t_move += 'D'

    else:
        if knots[i].x - knots[i + 1].x > 1:
            t_move += 'R'
        elif knots[i].x - knots[i + 1].x < -1:
            t_move += 'L'

        if knots[i].y - knots[i + 1].y > 1:
            t_move += 'U'
        elif knots[i].y - knots[i + 1].y < -1:
            t_move += 'D'

    knots = move(knots, i + 1, t_move)

    return knots


def solution_1(instructions):
    head = Rope((0, 0))
    tail = Rope((0, 0))
    knots = [head, tail]

    for inst in instructions:
        for _ in range(inst[1]):
            knots = move(knots, 0, inst)

    visited = len(knots[-1].visited)
    print(visited)
    return visited


def solution_2(instructions):
    knots = [Rope((0, 0)) for _ in range(10)]

    for inst in instructions:
        for _ in range(inst[1]):
            knots = move(knots, 0, inst)

    visited = len(knots[-1].visited)
    print(visited)
    return visited


def solution(data):
    instructions = parse_instructions(data)
    sol_1 = solution_1(instructions)
    sol_2 = solution_2(instructions)
    return sol_1, sol_2


if __name__ == '__main__':
    data = load_day_data('09')
    solution(data)
