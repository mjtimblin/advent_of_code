#!/usr/bin/env python3

import os
import re
import sys
import itertools as it


def _group_consecutive(iterable, length=2):
    iterable_copies = it.tee(iterable, length)
    for i in range(length):
        for _ in range(i):
            next(iterable_copies[i], None)
    return zip(*iterable_copies)


def part_1(dataset=[]):
    return len([group for group in _group_consecutive(dataset) if group[1] > group[0]])


def part_2(dataset=[]):
    return len([group for group in _group_consecutive(_group_consecutive(dataset, 3)) if sum(group[1]) > sum(group[0])])


def test():
    test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected_part_1 = 7
    expected_part_2 = 5

    assert expected_part_1 == part_1(test_data)
    assert expected_part_2 == part_2(test_data)
    print('Tests passed!')


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test()
        exit(0)

    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print('solution.py {path_to_input_file}')
        exit(1)

    dataset = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            dataset.append(int(line))

    print(f'Part 1 solution: {part_1(dataset)}')
    print(f'Part 2 solution: {part_2(dataset)}')
