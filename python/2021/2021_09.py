from typing import List

from python.base_solution import BaseSolution


def get_low_points(grid: List[List]) -> List[tuple]:
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y == 0 or grid[y - 1][x] > grid[y][x]) and \
                    (y == (len(grid) - 1) or grid[y + 1][x] > grid[y][x]) and \
                    (x == 0 or grid[y][x - 1] > grid[y][x]) and \
                    (x == (len(grid[0]) - 1) or grid[y][x + 1] > grid[y][x]):
                low_points.append((x, y,))
    return low_points


def get_higher_by_one_adjacent_points(grid, point) -> List[tuple]:
    higher_points = []
    p_x, p_y = point

    # left
    if p_x > 0 and grid[p_y][p_x - 1] > grid[p_y][p_x] and grid[p_y][p_x - 1] != 9:
        higher_points.append((p_x - 1, p_y))
    # right
    if p_x < (len(grid[0]) - 1) and grid[p_y][p_x + 1] > grid[p_y][p_x] and grid[p_y][p_x + 1] != 9:
        higher_points.append((p_x + 1, p_y))
    # up
    if p_y > 0 and grid[p_y - 1][p_x] > grid[p_y][p_x] and grid[p_y - 1][p_x] != 9:
        higher_points.append((p_x, p_y - 1))
    # down
    if p_y < (len(grid) - 1) and grid[p_y + 1][p_x] > grid[p_y][p_x] and grid[p_y + 1][p_x] != 9:
        higher_points.append((p_x, p_y + 1))

    if higher_points == []:
        return []
    else:
        new_higher_points = [*higher_points]
        for p in higher_points:
            new_higher_points.extend(get_higher_by_one_adjacent_points(grid, p))
        return new_higher_points


def get_basin_size_from_point(grid: List[List], low_point: tuple) -> int:
    adjacent_points = sorted(set(get_higher_by_one_adjacent_points(grid, low_point)))
    return len(adjacent_points) + 1


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_09'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        grid: List[List[str]] = [list(line) for line in self.dataset]
        return str(sum(int(grid[y][x]) + 1 for x, y in get_low_points(grid)))

    def part_2(self) -> str:
        grid: List[List[str]] = [list(line) for line in self.dataset]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x] = int(grid[y][x])

        low_points = get_low_points(grid)
        basin_sizes = sorted([get_basin_size_from_point(grid, p) for p in low_points])
        return str(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '15'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '1134'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
