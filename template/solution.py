import os.path
from typing import List


def part_1(dataset: List[str]) -> str:
    return ''


def part_2(dataset: List[str]) -> str:
    return ''


# noinspection DuplicatedCode
def run_tests():
    test_data = [line.strip() for line in '''
'''.strip().splitlines()]
    expected_part_1 = ''
    expected_part_2 = ''
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

    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    f = open(filepath, 'r')
    input_lines = [line.strip() for line in f.readlines()]
    f.close()

    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: {part_2(input_lines)}')


if __name__ == '__main__':
    main()
