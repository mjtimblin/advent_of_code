import os.path
from typing import List


def score_round(opponent_index: int, personal_index: int) -> int:
    score = 1 if personal_index == 0 else 2 if personal_index == 1 else 3  # initial points for chosen move
    if opponent_index == personal_index:
        return score + 3  # 3 points for tie
    elif (personal_index - 1) % 3 == opponent_index:
        return score + 6  # 6 points for win
    else:
        return score  # 0 points for loss


def part_1(dataset: List[str]) -> str:
    total_score = 0
    for line in dataset:
        opponent_choice, personal_choice = line.split(' ')
        opponent_index = ['A', 'B', 'C'].index(opponent_choice)
        personal_index = ['X', 'Y', 'Z'].index(personal_choice)
        total_score += score_round(opponent_index, personal_index)
    return str(total_score)


def part_2(dataset: List[str]) -> str:
    total_score = 0
    for line in dataset:
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


# noinspection DuplicatedCode
def run_tests():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test-input.txt'), 'r') as f:
        test_data = [line.strip() for line in f.readlines()]
    expected_part_1 = '15'
    expected_part_2 = '12'
    actual_part_1 = part_1(test_data)
    actual_part_2 = part_2(test_data)

    test_num = 1
    try:
        assert expected_part_1 == actual_part_1
        test_num = 2
        assert expected_part_2 == actual_part_2
    except AssertionError:
        print(f'Part {test_num} test failed. Expected {expected_part_1 if test_num == 1 else expected_part_2}, got {actual_part_1 if test_num == 1 else actual_part_2}')
        exit(1)

    print('Tests passed!')


# noinspection DuplicatedCode
def main():
    run_tests()

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'r') as f:
        input_lines = [line.strip() for line in f.readlines()]

    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: {part_2(input_lines)}')


if __name__ == '__main__':
    main()