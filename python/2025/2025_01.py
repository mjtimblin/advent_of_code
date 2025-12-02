from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2025_01'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        count = 0
        num = 50
        for line in self.dataset:
            adding = True if line[0] == 'R' else False
            increment = int(line[1:])

            if adding:
                num += increment
                num %= 100
            else:
                num -= increment
                num += 100
                num %= 100

            if num == 0:
                count += 1

        return str(count)

    def part_2(self) -> str:
        count = 0
        num = 50
        for line in self.dataset:
            adding = True if line[0] == 'R' else False
            increment = int(line[1:])

            if adding:
                for _ in range(increment):
                    num += 1
                    if num == 100:
                        num = 0
                        count += 1
            else:
                for _ in range(increment):
                    num -= 1
                    if num == -1:
                        num = 99
                    elif num == 0:
                        count += 1


        return str(count)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '3'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '6'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
