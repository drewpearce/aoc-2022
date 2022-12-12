from string import ascii_lowercase

from helpers import load_day_data


class Node(object):
    def __init__(self, x, y, height, width, val):
        self.is_start = False
        self.is_end = False
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.pos = (x, y)

        if val == 'S':
            self.is_start = True
            self.val = 0
        elif val == 'E':
            self.is_end = True
            self.val = 25
        else:
            self.val = ascii_lowercase.index(val)

    def get_neigbors(self):
        out = []

        if self.x != 0:
            out.append((self.x - 1, self.y))

        if self.x != self.width - 1:
            out.append((self.x + 1, self.y))

        if self.y != 0:
            out.append((self.x, self.y - 1))

        if self.y != self.height - 1:
            out.append((self.x, self.y + 1))

        return out


class Map(object):
    def __init__(self, unvisited, visited, start, end, grid):
        self.unvisited = unvisited
        self.visited = visited
        self.start = start
        self.end = end
        self.grid = grid
        self.distances = {
            u: 999 for _ in range(len(grid))
            for u in unvisited
        }
        self.distances[start] = 0

    def visit_1(self, current):
        cur_node = self.grid[current]

        for node in cur_node.get_neigbors():

            node = self.grid[node]

            if node.pos not in self.visited:
                if node.val <= cur_node.val + 1:
                    if self.distances[current] + 1 < self.distances[node.pos]:
                        self.distances[node.pos] = self.distances[current] + 1

        self.unvisited.remove(current)
        self.visited.append(current)

    def run_1(self):
        while self.end not in self.visited:
            current = min(self.unvisited, key=self.distances.get)
            self.visit_1(current)

        return self.distances[self.end]

    def visit_2(self, current):
        end = None
        cur_node = self.grid[current]

        for node in cur_node.get_neigbors():
            node = self.grid[node]

            if node.pos not in self.visited:
                if node.val >= cur_node.val - 1:
                    if self.distances[current] + 1 < self.distances[node.pos]:
                        self.distances[node.pos] = self.distances[current] + 1

                    if node.val == 0:
                        end = self.distances[node.pos]

        self.unvisited.remove(current)
        self.visited.append(current)

        return end

    def run_2(self):
        while True:
            current = min(self.unvisited, key=self.distances.get)
            end = self.visit_2(current)

            if end:
                break

        return end


def parse_grid(data):
    start = None
    end = None
    grid = {}
    data = data.strip().splitlines()
    h = len(data)
    for y, line in enumerate(data):
        w = len(line)
        for x, datum in enumerate(line):
            node = Node(x, y, h, w, datum)
            grid[node.pos] = node

            if node.is_start:
                start = node.pos
            elif node.is_end:
                end = node.pos

    return start, end, grid


def solution_1(start, end, grid):
    _map = Map(list(grid.keys()), [], start, end, grid)
    shortest = _map.run_1()
    print(shortest)

    return shortest


def solution_2(end, grid):
    _map = Map(list(grid.keys()), [], end, end, grid)
    shortest = _map.run_2()
    print(shortest)

    return shortest


def solution(data):
    start, end, grid = parse_grid(data)
    sol_1 = solution_1(start, end, grid)
    sol_2 = solution_2(end, grid)
    return sol_1, sol_2


if __name__ == '__main__':
    data = load_day_data('12')
    solution(data)
