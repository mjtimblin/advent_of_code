import string

from python.base_solution import BaseSolution


def split_line_in_half(rucksack: str) -> (str, str):
    return rucksack[:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):]


def get_priority(char: str) -> int:
    types = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return types.index(char) + 1


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_03'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        priority_sum = 0
        for line in self.dataset:
            left, right = split_line_in_half(line)
            common_item = ''.join(set(left) & set(right))
            priority_sum += get_priority(common_item)
        return str(priority_sum)

    def part_2(self) -> str:
        priority_sum = 0
        for line1, line2, line3 in zip(*(iter(self.dataset),) * 3):
            common_item = ''.join(set(line1) & set(line2) & set(line3))
            priority_sum += get_priority(common_item)
        return str(priority_sum)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '157'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '70'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
