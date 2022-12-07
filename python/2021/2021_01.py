import itertools as it

from python.base_solution import BaseSolution


def group_consecutive(iterable, length=2):
    iterable_copies = it.tee(iterable, length)
    for i in range(length):
        for _ in range(i):
            next(iterable_copies[i], None)
    return zip(*iterable_copies)


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_01'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        number_dataset = [int(n) for n in self.dataset]
        return str(len([group for group in group_consecutive(number_dataset) if group[1] > group[0]]))

    def part_2(self) -> str:
        number_dataset = [int(n) for n in self.dataset]
        return str(len([group for group in group_consecutive(group_consecutive(number_dataset, 3)) if
                        sum(group[1]) > sum(group[0])]))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '7'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '5'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
