from helpers import load_day_data


class Grid(object):
    def __init__(self, data):
        self.grid = {}
        y = 0
        x = 0
        self.width = 0

        for pos in data:
            if pos == '\n':
                y += 1
                x = 0
            else:
                self.grid[(x, y)] = int(pos)
                x += 1

                if x > self.width:
                    self.width = x

        self.height = y + 1

    def check_visible(self, x, y, height):
        left = [self.grid[(_x, y)] for _x in range(0, x)]

        if height > max(left):
            return True

        right = [self.grid[(_x, y)] for _x in range(x + 1, self.width)]

        if height > max(right):
            return True

        up = [self.grid[(x, _y)] for _y in range(0, y)]

        if height > max(up):
            return True

        down = [self.grid[(x, _y)] for _y in range(y + 1, self.height)]

        if height > max(down):
            return True

        return False

    def determine_visible(self):
        self.visible = set(
            k for k in self.grid.keys()
            if k[0] == 0
            or k[1] == 0
            or k[0] == self.width - 1
            or k[1] == self.height - 1
        )

        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                height = self.grid[(x, y)]
                if self.check_visible(x, y, height):
                    self.visible.add((x, y))

    def get_dir_score(self, x, y, height, dir):
        if dir == 'left':
            heights = [self.grid[(_x, y)] for _x in range(x - 1, -1, -1)]
        elif dir == 'right':
            heights = [self.grid[(_x, y)] for _x in range(x + 1, self.width)]
        elif dir == 'up':
            heights = [self.grid[(x, _y)] for _y in range(y - 1, -1, -1)]
        elif dir == 'down':
            heights = [self.grid[(x, _y)] for _y in range(y + 1, self.height)]
        else:
            return 0

        taller = [t for t in heights if t >= height]

        if not taller:
            if dir == 'left':
                return x

            if dir == 'right':
                return self.width - 1 - x

            if dir == 'up':
                return y

            if dir == 'down':
                return self.height - 1 - y

        i = heights.index(taller[0])

        return i + 1

    def get_score(self, x, y):
        if any([x == 0, x == self.width - 1, y == 0, y == self.height - 1]):
            return 0

        height = self.grid[(x, y)]
        left = self.get_dir_score(x, y, height, 'left')
        right = self.get_dir_score(x, y, height, 'right')
        up = self.get_dir_score(x, y, height, 'up')
        down = self.get_dir_score(x, y, height, 'down')

        return left * right * up * down

    def determine_scenic_scores(self):
        self.scenic_scores = {
            k: 0 for k in self.grid.keys()
            if k[0] == 0
            or k[1] == 0
            or k[0] == self.width - 1
            or k[1] == self.height - 1
        }
        self.scenic_scores.update({
            (x, y): self.get_score(x, y)
            for x in range(1, self.width - 1)
            for y in range(1, self.height - 1)
        })


def solution(data):
    grid = Grid(data.strip())
    grid.determine_visible()
    print(len(grid.visible))
    grid.determine_scenic_scores()
    print(max(grid.scenic_scores.values()))
    return len(grid.visible), max(grid.scenic_scores.values())


if __name__ == '__main__':
    data = load_day_data('08')
    solution(data)
