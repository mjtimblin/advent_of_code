import os.path
import re
from typing import List


def part_1(dataset: List[str]) -> str:
    num_fully_contained = 0
    for line in dataset:
        e1_min, e1_max, e2_min, e2_max = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups()
        e1_min, e1_max, e2_min, e2_max = int(e1_min), int(e1_max), int(e2_min), int(e2_max)
        if (e1_min <= e2_min and e1_max >= e2_max) or (e2_min <= e1_min and e2_max >= e1_max):
            num_fully_contained += 1
    return str(num_fully_contained)


def part_2(dataset: List[str]) -> str:
    num_overlap = 0
    for line in dataset:
        e1_min, e1_max, e2_min, e2_max = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups()
        e1_min, e1_max, e2_min, e2_max = int(e1_min), int(e1_max), int(e2_min), int(e2_max)
        if (e1_min <= e2_min <= e1_max) or (e2_min <= e1_min <= e2_max):
            num_overlap += 1
    return str(num_overlap)


# noinspection DuplicatedCode
def run_tests():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test-input.txt'), 'r') as f:
        test_data = [line.strip() for line in f.readlines()]
    expected_part_1 = '2'
    expected_part_2 = '4'
    actual_part_1 = part_1(test_data)
    actual_part_2 = part_2(test_data)

    test_num = 1
    try:
        assert expected_part_1 == actual_part_1
        test_num = 2
        assert expected_part_2 == actual_part_2
    except AssertionError:
        print(f'Part {test_num} test failed. Expected {expected_part_1 if test_num == 1 else expected_part_2}, got {actual_part_1 if test_num == 1 else actual_part_2}')
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
