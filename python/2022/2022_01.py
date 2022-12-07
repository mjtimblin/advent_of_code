from typing import List

from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_01'
        super().__init__(use_test_data, data_prefix)

    def _get_inventories(self) -> List[List[int]]:
        inventories = []
        data = list(self.dataset)

        while '' in data:
            inventories.append([int(item) for item in data[:data.index('')]])
            data = data[data.index('') + 1:]

        # Add final inventory (after last blank line)
        inventories.append([int(item) for item in data])

        return inventories

    def part_1(self) -> str:
        inventories = self._get_inventories()
        sorted_inventory_sums = sorted([sum(i) for i in inventories])
        return str(max(sorted_inventory_sums))

    def part_2(self) -> str:
        inventories = self._get_inventories()
        sorted_inventory_sums = sorted([sum(i) for i in inventories])
        return str(sum(sorted_inventory_sums[-3:]))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '24000'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '45000'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
