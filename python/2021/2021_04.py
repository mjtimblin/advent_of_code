from typing import List

from python.base_solution import BaseSolution


class Board:
    def __init__(self, numbers) -> None:
        self.layout = [numbers[i:i + 5] for i in range(0, len(numbers), 5)]
        self.marked_nums = [[False for j in range(5)] for i in range(5)]
        self.bingo = False

    def mark_number(self, num) -> bool:
        result = False
        for row_i in range(5):
            for col_i in range(5):
                if self.layout[row_i][col_i] == num:
                    self.marked_nums[row_i][col_i] = True
                    result = True
        return result

    def is_bingo(self):
        if self.bingo:
            return True

        for i in range(5):
            if all(self.marked_nums[i]):
                self.bingo = True
                return True
            if all([row[i] for row in self.marked_nums]):
                self.bingo = True
                return True
        return False

    def get_unmarked_nums(self):
        unmarked = []
        for row_i in range(5):
            for col_i in range(5):
                if not self.marked_nums[row_i][col_i]:
                    unmarked.append(self.layout[row_i][col_i])
        return unmarked


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_04'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def _get_nums_to_call(self) -> List[int]:
        return [int(n) for n in self.dataset[0].split(',')]

    def _get_boards(self) -> List[Board]:
        dataset_without_empty_lines = [line for line in self.dataset if line != '']
        board_raw_nums = [' '.join(dataset_without_empty_lines[i + 1:i + 6]).strip().replace('  ', ' ') for i in
                          range(0, len(dataset_without_empty_lines) - 1, 5)]
        board_nums = [[int(n) for n in b.split(' ')] for b in board_raw_nums]
        return [Board(b) for b in board_nums]

    def part_1(self) -> str:
        boards = self._get_boards()
        nums_to_call = self._get_nums_to_call()

        for num in nums_to_call:
            for board in boards:
                board.mark_number(num)
                if board.is_bingo():
                    return str(sum(board.get_unmarked_nums()) * num)

    def part_2(self) -> str:
        boards = self._get_boards()
        nums_to_call = self._get_nums_to_call()

        for num in nums_to_call:
            for board in [b for b in boards if not b.is_bingo()]:
                board.mark_number(num)
                if board.is_bingo():
                    if [b for b in boards if not b.is_bingo()] == []:
                        return str(sum(board.get_unmarked_nums()) * num)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '4512'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '1924'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
