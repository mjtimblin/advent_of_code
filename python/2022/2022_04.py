import re

from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_04'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        num_fully_contained = 0
        for line in self.dataset:
            e1_min, e1_max, e2_min, e2_max = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups()
            e1_min, e1_max, e2_min, e2_max = int(e1_min), int(e1_max), int(e2_min), int(e2_max)
            if (e1_min <= e2_min and e1_max >= e2_max) or (e2_min <= e1_min and e2_max >= e1_max):
                num_fully_contained += 1
        return str(num_fully_contained)

    def part_2(self) -> str:
        num_overlap = 0
        for line in self.dataset:
            e1_min, e1_max, e2_min, e2_max = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups()
            e1_min, e1_max, e2_min, e2_max = int(e1_min), int(e1_max), int(e2_min), int(e2_max)
            if (e1_min <= e2_min <= e1_max) or (e2_min <= e1_min <= e2_max):
                num_overlap += 1
        return str(num_overlap)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '2'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '4'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')

