from python.base_solution import BaseSolution


def score_round(opponent_index: int, personal_index: int) -> int:
    score = 1 if personal_index == 0 else 2 if personal_index == 1 else 3  # initial points for chosen move
    if opponent_index == personal_index:
        return score + 3  # 3 points for tie
    elif (personal_index - 1) % 3 == opponent_index:
        return score + 6  # 6 points for win
    else:
        return score  # 0 points for loss


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_02'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        total_score = 0
        for line in self.dataset:
            opponent_choice, personal_choice = line.split(' ')
            opponent_index = ['A', 'B', 'C'].index(opponent_choice)
            personal_index = ['X', 'Y', 'Z'].index(personal_choice)
            total_score += score_round(opponent_index, personal_index)
        return str(total_score)

    def part_2(self) -> str:
        total_score = 0
        for line in self.dataset:
            opponent_choice, outcome = line.split(' ')

            opponent_index = ['A', 'B', 'C'].index(opponent_choice)
            if outcome == 'X':  # loss
                personal_index = (opponent_index - 1) % 3
            elif outcome == 'Y':  # tie
                personal_index = opponent_index
            else:  # win
                personal_index = (opponent_index + 1) % 3

            total_score += score_round(opponent_index, personal_index)
        return str(total_score)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '15'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '12'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
