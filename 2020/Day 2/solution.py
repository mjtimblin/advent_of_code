#!/usr/bin/env python3

import os
import re
import sys


def main():
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print('solution.py {path_to_input_file}')
        exit(1)

    password_candidates = []

    with open(sys.argv[1]) as f:
        for line in f.readlines():
            match = re.search('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
            password_candidates.append({
                'num_1': int(match.group(1)),
                'num_2': int(match.group(2)),
                'character': match.group(3),
                'password': match.group(4)
            })

    part_1_num_valid_passwords = 0
    part_2_num_valid_passwords = 0

    for candidate in password_candidates:
        num_occurances = candidate['password'].count(candidate['character'])
        if num_occurances >= candidate['num_1'] and num_occurances <= candidate['num_2']:
            part_1_num_valid_passwords += 1

    for candidate in password_candidates:
        if (candidate['password'][candidate['num_1'] - 1] == candidate['character']) != (candidate['password'][candidate['num_2'] - 1] == candidate['character']):
            part_2_num_valid_passwords += 1

    print(f'Part 1 solution: {part_1_num_valid_passwords}')
    print(f'Part 2 solution: {part_2_num_valid_passwords}')


if __name__ == '__main__':
    main()
