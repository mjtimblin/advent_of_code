from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2020_01'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)
        self.dataset = [int(line) for line in self.dataset]

    def part_1(self) -> str:
        for i in range(0, len(self.dataset)):
            for j in range(0, len(self.dataset)):
                if i != j and self.dataset[i] + self.dataset[j] == 2020:
                    return str(self.dataset[i] * self.dataset[j])

    def part_2(self) -> str:
        for i in range(0, len(self.dataset)):
            for j in range(0, len(self.dataset)):
                for k in range(0, len(self.dataset)):
                    if i != j and i != k and self.dataset[i] + self.dataset[j] + self.dataset[k] == 2020:
                        return str(self.dataset[i] * self.dataset[j] * self.dataset[k])


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '514579'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '241861950'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
