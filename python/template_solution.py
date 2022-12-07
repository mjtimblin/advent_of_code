from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '20xx_xx'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        return ''

    def part_2(self) -> str:
        return ''


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == ''


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == ''


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
