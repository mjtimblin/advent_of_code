import argparse
import itertools as it


def _group_consecutive(iterable, length=2):
    iterable_copies = it.tee(iterable, length)
    for i in range(length):
        for _ in range(i):
            next(iterable_copies[i], None)
    return zip(*iterable_copies)


def part_1(dataset=[]):
    number_dataset = [int(n) for n in dataset]
    return len([group for group in _group_consecutive(number_dataset) if group[1] > group[0]])


def part_2(dataset=[]):
    number_dataset = [int(n) for n in dataset]
    return len([group for group in _group_consecutive(_group_consecutive(number_dataset, 3)) if sum(group[1]) > sum(group[0])])


def run_tests():
    test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected_part_1 = 7
    expected_part_2 = 5

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
