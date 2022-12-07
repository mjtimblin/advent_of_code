from typing import List

from python.base_solution import BaseSolution


def get_segment_digit_mapping(sample_encoded_digits: List[str]):
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


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_08'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        second_halves = [line.split(' | ')[1].split(' ') for line in self.dataset]
        count = 0
        for line in second_halves:
            for n in line:
                if len(n) == 2 or len(n) == 4 or len(n) == 3 or len(n) == 7:
                    count += 1
        return str(count)

    def part_2(self) -> str:
        total = 0
        for line in self.dataset:
            segment_digit_mapping = get_segment_digit_mapping(line.split(' | ')[0].split(' '))
            total += int(''.join([str(segment_digit_mapping.index(set(n))) for n in line.split(' | ')[1].split(' ')]))
        return str(total)

def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '26'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '61229'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
