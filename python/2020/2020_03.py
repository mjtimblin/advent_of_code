import re
from typing import List

from python.base_solution import BaseSolution


def traverse_slope(slope, num_right, num_down) -> int:
    num_trees = 0
    x = num_right
    y = num_down

    while y < len(slope):
        if slope[y][x] == '#':
            num_trees += 1
        x = (x + num_right) % len(slope[y])
        y = y + num_down

    return num_trees


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2020_03'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def _get_layout(self) -> List[List[str]]:
        layout = []
        for line in self.dataset:
            sanitized_line = re.sub('[^#.]', '', line)
            layout.append(list(sanitized_line))
        return layout

    def part_1(self) -> str:
        layout = self._get_layout()
        num_trees = traverse_slope(layout, 3, 1)
        return str(num_trees)

    def part_2(self) -> str:
        layout = self._get_layout()
        num_trees = traverse_slope(layout, 1, 1) * traverse_slope(layout, 3, 1) * traverse_slope(layout, 5, 1) * traverse_slope(layout, 7, 1) * traverse_slope(layout, 1, 2)
        return str(num_trees)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '7'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '336'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
