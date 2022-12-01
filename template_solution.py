import os


def part_1(dataset=[]):
    pass


def part_2(dataset=[]):
    pass


def run_tests():
    test_data = [l.strip() for l in '''
'''.strip().splitlines()]
    expected_part_1 = None
    expected_part_2 = None

    assert expected_part_1 == part_1(test_data)
    assert expected_part_2 == part_2(test_data)
    print('Tests passed!')


def main():
    run_tests()

    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    f = open(filepath, 'r')
    input_lines = [l.strip() for l in f.readlines()]
    f.close()

    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: {part_2(input_lines)}')


if __name__ == '__main__':
    main()
