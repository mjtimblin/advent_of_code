import argparse


class Board:
    def __init__(self, numbers) -> None:
        self.layout = [numbers[i:i+5] for i in range(0, len(numbers), 5)]
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


def part_1(dataset=[]):
    dataset_without_empty_lines = [l for l in dataset if l != '']
    nums_to_call = [int(n) for n in dataset_without_empty_lines[0].split(',')]
    board_raw_nums = [' '.join(dataset_without_empty_lines[i+1:i+6]).strip().replace('  ', ' ') for i in range(0, len(dataset_without_empty_lines) - 1, 5)]
    board_nums = [[int(n) for n in b.split(' ')] for b in board_raw_nums]
    boards = [Board(b) for b in board_nums]

    for num in nums_to_call:
        for board in boards:
            board.mark_number(num)
            if board.is_bingo():
                return sum(board.get_unmarked_nums()) * num


def part_2(dataset=[]):
    dataset_without_empty_lines = [l for l in dataset if l != '']
    nums_to_call = [int(n) for n in dataset_without_empty_lines[0].split(',')]
    board_raw_nums = [' '.join(dataset_without_empty_lines[i+1:i+6]).strip().replace('  ', ' ') for i in range(0, len(dataset_without_empty_lines) - 1, 5)]
    board_nums = [[int(n) for n in b.split(' ')] for b in board_raw_nums]
    boards = [Board(b) for b in board_nums]

    for num in nums_to_call:
        for board in [b for b in boards if not b.is_bingo()]:
            board.mark_number(num)
            if board.is_bingo():
                if [b for b in boards if not b.is_bingo()] == []:
                    return sum(board.get_unmarked_nums()) * num


def run_tests():
    test_data = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1', '', '22 13 17 11  0', ' 8  2 23  4 24', '21  9 14 16  7', ' 6 10  3 18  5', ' 1 12 20 15 19', '', ' 3 15  0  2 22', ' 9 18 13 17  5', '19  8  7 25 23', '20 11 10 24  4', '14 21 16 12  6', '', '14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5', ' 2  0 12  3  7',]
    expected_part_1 = 4512
    expected_part_2 = 1924

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
