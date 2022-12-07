import math

from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_07'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        positions = [int(n) for n in self.dataset[0].split(',')]
        return str(min([sum([abs(n - i) for n in positions]) for i in range(min(positions), max(positions) + 1)]))

    def part_2(self) -> str:
        positions = [int(n) for n in self.dataset[0].split(',')]
        return str(min([sum([math.comb(abs(n - i), 2) + abs(n - i) for n in positions]) for i in range(min(positions), max(positions) + 1)]))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '37'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '168'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
