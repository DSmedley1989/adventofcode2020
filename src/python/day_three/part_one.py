test_input_raw = """
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
"""

test_input = [ row.strip() for row in test_input_raw.split('\n') if row != '' ]

problem_input = None

with open('./data/day_three_part_one.txt', 'r') as file:
    problem_input = [r.strip() for r in file.read().split('\n') if r != '']


class Slope:
    def __init__(self, map_as_rows):
        self.height = len(map_as_rows)
        self.width = len(map_as_rows[0])

        self.trees = []

        for row_index in range(0, self.height):
            row = map_as_rows[row_index]

            for column_index in range(0, self.width):
                cell = row[column_index]

                if cell == "#":
                    self.trees.append(self._to_coords(column_index, row_index))

    def _to_coords(self, x, y):
        return '%d,%d' % (x, y)

    def has_tree(self, x, y):
        if y >= self.height:
            return None

        x_wrapped = x % self.width

        return self._to_coords(x_wrapped, y) in self.trees

def count_trees_on_slope(slope, x_change, y_change):
    trees = 0
    x = 0
    y = 0
    has_tree = slope.has_tree(x, y)

    while has_tree is not None:
        if has_tree:
            trees += 1

        x += x_change
        y += y_change

        has_tree = slope.has_tree(x, y)

    return trees

if __name__ == '__main__':
    test_slope = Slope(test_input)
    test_trees = count_trees_on_slope(test_slope, 3, 1)

    if test_trees != 7:
        print('TEST FAILURE!')
        print(test_trees)
        print(test_slope.trees)
        exit()

    problem_slope = Slope(problem_input)

    print(count_trees_on_slope(problem_slope, 3, 1))
