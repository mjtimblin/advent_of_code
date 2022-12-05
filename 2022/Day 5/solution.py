import os.path
import re
from typing import List


def get_stacks_from_input(dataset: List[str]) -> List[List[str]]:
    stacks = []
    lines_to_process = []

    for line in dataset:
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


def part_1(dataset: List[str]) -> str:
    stacks = get_stacks_from_input(dataset)
    for line in dataset:
        if re.match(r'move [0-9]+ from [0-9]+ to [0-9]+', line):
            amount, move_from, move_to = re.search(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', line).groups()
            for _ in range(int(amount)):
                stacks[int(move_to) - 1].append(stacks[int(move_from) - 1].pop())
    return ''.join([stack[-1] for stack in stacks])


def part_2(dataset: List[str]) -> str:
    stacks = get_stacks_from_input(dataset)
    for line in dataset:
        if re.match(r'move [0-9]+ from [0-9]+ to [0-9]+', line):
            amount, move_from, move_to = re.search(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', line).groups()
            intermediate_stack = []
            for _ in range(int(amount)):
                intermediate_stack.append(stacks[int(move_from) - 1].pop())
            for crate in reversed(intermediate_stack):
                stacks[int(move_to) - 1].append(crate)
    return ''.join([stack[-1] for stack in stacks])


# noinspection DuplicatedCode
def run_tests():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test-input.txt'), 'r') as f:
        test_data = [line.replace('\n', '') for line in f.readlines()]
    expected_part_1 = 'CMZ'
    expected_part_2 = 'MCD'
    actual_part_1 = part_1(test_data)
    actual_part_2 = part_2(test_data)

    test_num = 1
    try:
        assert expected_part_1 == actual_part_1
        test_num = 2
        assert expected_part_2 == actual_part_2
    except AssertionError:
        print(
            f'Part {test_num} test failed. Expected {expected_part_1 if test_num == 1 else expected_part_2}, got {actual_part_1 if test_num == 1 else actual_part_2}')
        exit(1)

    print('Tests passed!')


# noinspection DuplicatedCode
def main():
    run_tests()

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'r') as f:
        input_lines = [line.replace('\n', '') for line in f.readlines()]

    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: {part_2(input_lines)}')


if __name__ == '__main__':
    main()
