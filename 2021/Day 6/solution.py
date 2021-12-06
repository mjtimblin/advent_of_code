import argparse
from typing import List


def _get_fish_population_after_days(initial_fish_ages: List[int], num_days: int):
    fish_at_ages = [0 for _ in range(9)]
    for n in initial_fish_ages:
        fish_at_ages[n] += 1

    for _ in range(num_days):
        left_over_fish = fish_at_ages[0]
        fish_at_ages = fish_at_ages[1:] + fish_at_ages[:1]
        fish_at_ages[6] += left_over_fish

    return sum(fish_at_ages)


def part_1(dataset=[]):
    return _get_fish_population_after_days([int(n) for n in dataset[0].split(',')], 80)


def part_2(dataset=[]):
    return _get_fish_population_after_days([int(n) for n in dataset[0].split(',')], 256)


def run_tests():
    test_data = ['3,4,3,1,2']
    expected_part_1 = 5934
    expected_part_2 = 26984457539

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
