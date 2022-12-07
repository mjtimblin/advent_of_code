from collections import defaultdict

from python.base_solution import BaseSolution


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


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_14'
        super().__init__(use_test_data, data_prefix)

    def _get_polymer_pair_and_element_counts(self) -> dict:
        polymer = self.dataset[0]
        polymer_pair_and_element_counts = defaultdict(int)
        for i in range(len(polymer) - 1):
            polymer_pair_and_element_counts[polymer[i:i+2]] += 1

        for c in list(polymer):
            polymer_pair_and_element_counts[c] += 1
        return polymer_pair_and_element_counts

    def _get_insertion_lookup(self) -> dict:
        insertion_lookup = dict()
        for line in self.dataset[2:]:
            a, b = line.split(' -> ')
            insertion_lookup[a] = b
        return insertion_lookup

    def part_1(self) -> str:
        polymer_pair_and_element_counts = self._get_polymer_pair_and_element_counts()
        insertion_lookup = self._get_insertion_lookup()

        for _ in range(10):
            polymer_pair_and_element_counts = run_insertion_step(polymer_pair_and_element_counts, insertion_lookup)

        counts = [polymer_pair_and_element_counts[e] for e in polymer_pair_and_element_counts.keys() if len(e) == 1]
        return str(max(counts) - min(counts))

    def part_2(self) -> str:
        polymer_pair_and_element_counts = self._get_polymer_pair_and_element_counts()
        insertion_lookup = self._get_insertion_lookup()

        for _ in range(40):
            polymer_pair_and_element_counts = run_insertion_step(polymer_pair_and_element_counts, insertion_lookup)

        counts = [polymer_pair_and_element_counts[e] for e in polymer_pair_and_element_counts.keys() if len(e) == 1]
        return str(max(counts) - min(counts))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '1588'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '2188189693529'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
