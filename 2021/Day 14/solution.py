import argparse
from collections import Counter, defaultdict
from typing import List, Tuple


def run_insertion_step(polymer_pair_and_element_counts: dict, insertion_lookup: dict) -> dict:
    new_polymer_pair_and_element_counts = defaultdict(int)
    for pair in polymer_pair_and_element_counts.keys():
        if pair in insertion_lookup.keys():
            new_polymer_pair_and_element_counts[pair[0] + insertion_lookup[pair]] += polymer_pair_and_element_counts[pair]
            new_polymer_pair_and_element_counts[insertion_lookup[pair] + pair[1]] += polymer_pair_and_element_counts[pair]
            new_polymer_pair_and_element_counts[insertion_lookup[pair]] += polymer_pair_and_element_counts[pair]
        else:
            new_polymer_pair_and_element_counts[pair] += polymer_pair_and_element_counts[pair]
    return new_polymer_pair_and_element_counts


def part_1(dataset=[]):
    polymer = dataset[0]
    polymer_pair_and_element_counts = defaultdict(int)
    for i in range(len(polymer) - 1):
        polymer_pair_and_element_counts[polymer[i:i+2]] += 1

    for c in list(polymer):
        polymer_pair_and_element_counts[c] += 1

    insertion_lookup = dict()
    for l in dataset[2:]:
        a, b = l.split(' -> ')
        insertion_lookup[a] = b

    for _ in range(10):
        polymer_pair_and_element_counts = run_insertion_step(polymer_pair_and_element_counts, insertion_lookup)

    counts = [polymer_pair_and_element_counts[e] for e in polymer_pair_and_element_counts.keys() if len(e) == 1]
    return max(counts) - min(counts)


def part_2(dataset=[]):
    polymer = dataset[0]
    polymer_pair_and_element_counts = defaultdict(int)
    for i in range(len(polymer) - 1):
        polymer_pair_and_element_counts[polymer[i:i+2]] += 1

    for c in list(polymer):
        polymer_pair_and_element_counts[c] += 1

    insertion_lookup = dict()
    for l in dataset[2:]:
        a, b = l.split(' -> ')
        insertion_lookup[a] = b

    for _ in range(40):
        polymer_pair_and_element_counts = run_insertion_step(polymer_pair_and_element_counts, insertion_lookup)

    counts = [polymer_pair_and_element_counts[e] for e in polymer_pair_and_element_counts.keys() if len(e) == 1]
    return max(counts) - min(counts)


def run_tests():
    test_data = [
        'NNCB',
        '',
        'CH -> B',
        'HH -> N',
        'CB -> H',
        'NH -> C',
        'HB -> C',
        'HC -> B',
        'HN -> C',
        'NN -> C',
        'BH -> H',
        'NC -> B',
        'NB -> B',
        'BN -> B',
        'BB -> N',
        'BC -> B',
        'CC -> N',
        'CN -> C'
    ]
    expected_part_1 = 1588
    expected_part_2 = 2188189693529

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
