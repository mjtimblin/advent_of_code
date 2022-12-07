from typing import List

from python.base_solution import BaseSolution


def get_fish_population_after_days(initial_fish_ages: List[int], num_days: int) -> int:
    num_fish_at_ages = [0 for _ in range(9)]

    for n in initial_fish_ages:
        num_fish_at_ages[n] += 1

    for _ in range(num_days):
        num_parents = num_fish_at_ages[0]
        num_fish_at_ages = num_fish_at_ages[1:] + num_fish_at_ages[:1]
        num_fish_at_ages[6] += num_parents

    return sum(num_fish_at_ages)


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_06'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        return str(get_fish_population_after_days([int(n) for n in self.dataset[0].split(',')], 80))

    def part_2(self) -> str:
        return str(get_fish_population_after_days([int(n) for n in self.dataset[0].split(',')], 256))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '5934'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '26984457539'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
