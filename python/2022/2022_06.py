from python.base_solution import BaseSolution


def get_index_of_sequential_non_repeating_chars(text: str, length: int):
    current_str = ''
    for i in range(0, len(text)):
        if len(current_str) < length:
            current_str += text[i]
        else:
            current_str = current_str[1:] + text[i]
            if len(set(current_str)) == length:
                return i
    return -1


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_06'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        code = self.dataset[0]
        return str(get_index_of_sequential_non_repeating_chars(code, 4) + 1)

    def part_2(self) -> str:
        code = self.dataset[0]
        return str(get_index_of_sequential_non_repeating_chars(code, 14) + 1)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '11'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '26'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
