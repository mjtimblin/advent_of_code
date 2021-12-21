import argparse
from typing import List


def _get_segment_digit_mapping(sample_encoded_digits: List[str]):
    encoded_digit_sets = [set(s) for s in sample_encoded_digits]
    key = [set()] * 10

    key[1] = set(*[s for s in encoded_digit_sets if len(s) == 2])
    key[4] = set(*[s for s in encoded_digit_sets if len(s) == 4])
    key[7] = set(*[s for s in encoded_digit_sets if len(s) == 3])
    key[8] = set(*[s for s in encoded_digit_sets if len(s) == 7])

    segments_b_and_d = list(key[4] - key[1])
    key[5] = set(*[l for l in encoded_digit_sets if len(l) == 5 and segments_b_and_d[0] in l and segments_b_and_d[1] in l])

    segment_a = list(key[7] - key[1])[0]
    segment_g = list(key[5] - key[4] - set(segment_a))[0]
    segment_e = list(key[8] - key[4] - set(segment_a) - set(segment_g))[0]
    key[9] = set(*[s for s in encoded_digit_sets if len(s) == 6 and s.union(set(segment_e)) == key[8]])

    remaining_encoded_digits = [set(n) for n in encoded_digit_sets if set(n) not in key]
    key[2] = set(*[s for s in remaining_encoded_digits if len(s) == 5 and segment_e in s])
    key[3] = set(*[s for s in remaining_encoded_digits if len(s) == 5 and segment_e not in s])

    key[0] = set(*[s for s in remaining_encoded_digits if len(s) == 6 and len(s - key[1]) == 4])
    key[6] = set(*[s for s in remaining_encoded_digits if len(s) == 6 and len(s - key[1]) == 5])

    return key


def part_1(dataset=[]):
    second_halves = [line.split(' | ')[1].split(' ') for line in dataset]
    count = 0
    for line in second_halves:
        for n in line:
            if len(n) == 2 or len(n) == 4 or len(n) == 3 or len(n) == 7:
                count += 1
    return count


def part_2(dataset=[]):
    total = 0
    for line in dataset:
        segment_digit_mapping = _get_segment_digit_mapping(line.split(' | ')[0].split(' '))
        total += int(''.join([str(segment_digit_mapping.index(set(n))) for n in line.split(' | ')[1].split(' ')]))
    return total


def run_tests():
    test_data = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe', 'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc', 'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg', 'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb', 'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea', 'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb', 'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe', 'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef', 'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb', 'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
    expected_part_1 = 26
    expected_part_2 = 61229

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
