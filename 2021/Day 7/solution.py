import argparse
import math

def part_1(dataset=[]):
    positions = [int(n) for n in dataset[0].split(',')]
    return min([sum([abs(n - i) for n in positions]) for i in range(min(positions), max(positions) + 1)])


def part_2(dataset=[]):
    positions = [int(n) for n in dataset[0].split(',')]
    return min([sum([math.comb(abs(n - i), 2) + abs(n - i) for n in positions]) for i in range(min(positions), max(positions) + 1)])


def run_tests():
    test_data = ['16,1,2,0,4,2,7,1,2,14']
    expected_part_1 = 37
    expected_part_2 = 168

    assert expected_part_1 == part_1(test_data)
    assert expected_part_2 == part_2(test_data)
    print('Tests passed!')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=argparse.FileType('r'), help='Filepath for the input data file')
    args = parser.parse_args()

    run_tests()

    input_lines = [l.strip() for l in args.filepath.readlines()]
    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: {part_2(input_lines)}')


if __name__ == '__main__':
    main()
