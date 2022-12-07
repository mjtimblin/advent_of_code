import re
from typing import List

from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_05'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def _get_stacks_from_input(self) -> List[List[str]]:
        stacks = []
        lines_to_process = []

        for line in self.dataset:
            if line.lstrip().startswith('1   2   '):
                for _ in range(int(len(line) / 4) + 1):
                    stacks.append([])
                break
            else:
                lines_to_process.append(line)

        for line in reversed(lines_to_process):
            line = line + ' ' * (4 - len(line) % 4)
            for i, val in enumerate(zip(*(iter(line),) * 4)):
                val = ''.join(val)
                if '[' in val:
                    val = val.replace('[', '').replace(']', '').replace(' ', '')
                    stacks[i].append(val)

        return stacks

    def part_1(self) -> str:
        stacks = self._get_stacks_from_input()
        for line in self.dataset:
            if re.match(r'move [0-9]+ from [0-9]+ to [0-9]+', line):
                amount, move_from, move_to = re.search(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', line).groups()
                for _ in range(int(amount)):
                    stacks[int(move_to) - 1].append(stacks[int(move_from) - 1].pop())
        return ''.join([stack[-1] for stack in stacks])

    def part_2(self) -> str:
        stacks = self._get_stacks_from_input()
        for line in self.dataset:
            if re.match(r'move [0-9]+ from [0-9]+ to [0-9]+', line):
                amount, move_from, move_to = re.search(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', line).groups()
                intermediate_stack = []
                for _ in range(int(amount)):
                    intermediate_stack.append(stacks[int(move_from) - 1].pop())
                for crate in reversed(intermediate_stack):
                    stacks[int(move_to) - 1].append(crate)
        return ''.join([stack[-1] for stack in stacks])


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == 'CMZ'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == 'MCD'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
