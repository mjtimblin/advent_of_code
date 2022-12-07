import re

from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2020_02'
        super().__init__(use_test_data, data_prefix)

    def _get_password_candidates(self):
        password_candidates = []
        for line in self.dataset:
            match = re.search('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
            password_candidates.append({
                'num_1': int(match.group(1)),
                'num_2': int(match.group(2)),
                'character': match.group(3),
                'password': match.group(4)
            })
        return password_candidates

    def part_1(self) -> str:
        num_valid_passwords = 0
        for candidate in self._get_password_candidates():
            num_occurrences = candidate['password'].count(candidate['character'])
            if candidate['num_1'] <= num_occurrences <= candidate['num_2']:
                num_valid_passwords += 1
        return str(num_valid_passwords)

    def part_2(self) -> str:
        num_valid_passwords = 0
        for candidate in self._get_password_candidates():
            if (candidate['password'][candidate['num_1'] - 1] == candidate['character']) != (candidate['password'][candidate['num_2'] - 1] == candidate['character']):
                num_valid_passwords += 1
        return str(num_valid_passwords)

def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '2'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '1'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
