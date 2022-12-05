import os.path
import string
from typing import List


def split_line_in_half(rucksack: str) -> (str, str):
    return rucksack[:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):]


def get_priority(char: str) -> int:
    types = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return types.index(char) + 1


def part_1(dataset: List[str]) -> str:
    priority_sum = 0
    for line in dataset:
        left, right = split_line_in_half(line)
        common_item = ''.join(set(left) & set(right))
        priority_sum += get_priority(common_item)
    return str(priority_sum)


def part_2(dataset: List[str]) -> str:
    priority_sum = 0
    for line1, line2, line3 in zip(*(iter(dataset),) * 3):
        common_item = ''.join(set(line1) & set(line2) & set(line3))
        priority_sum += get_priority(common_item)
    return str(priority_sum)


# noinspection DuplicatedCode
def run_tests():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test-input.txt'), 'r') as f:
        test_data = [line.strip() for line in f.readlines()]
    expected_part_1 = '157'
    expected_part_2 = '70'
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
        input_lines = [line.strip() for line in f.readlines()]

    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: {part_2(input_lines)}')


if __name__ == '__main__':
    main()
