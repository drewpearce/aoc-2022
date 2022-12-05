from copy import deepcopy
import re

from helpers import load_day_data


def parse_state(_input):
    _input = _input.splitlines()
    state = {
        int(i): []
        for i in re.findall(r'\d+', _input[-1])
    }

    for line in reversed(_input[:-1]):
        for i, c in enumerate(range(1, len(line), 4)):
            if line[c] != ' ':
                state[i + 1].append(line[c])

    return state


def parse_instructions(_input):
    return [
        tuple(int(i) for i in re.findall(r'\d+', line))
        for line in _input.splitlines()
    ]


def parse_data(data):
    _state, _instructions = data.split('\n\n')
    state = parse_state(_state)
    instructions = parse_instructions(_instructions)

    return state, instructions


def _print(state):
    print('\n')

    for k, v in state.items():
        print(f"{k}: {''.join(v)}")


def run_1(state, instructions):
    # _print(state)
    for inst in instructions:
        for _ in range(inst[0]):
            state[inst[2]].append(state[inst[1]].pop(-1))
            # _print(state)

    return state


def run_2(state, instructions):
    # _print(state)
    for inst in instructions:
        for i in range(-(inst[0]), 0):
            state[inst[2]].append(state[inst[1]].pop(i))
            # _print(state)

    return state


def solution(data):
    state, instructions = parse_data(data)
    state_1 = run_1(deepcopy(state), instructions)
    solution_1 = ''.join([s[-1] for s in state_1.values()])
    print(solution_1)
    state_2 = run_2(deepcopy(state), instructions)
    solution_2 = ''.join([s[-1] for s in state_2.values() if s])
    print(solution_2)

    return solution_1, solution_2


if __name__ == '__main__':
    data = load_day_data('05')
    solution(data)
