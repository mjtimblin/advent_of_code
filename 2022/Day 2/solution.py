import os.path
from typing import List


def score_round(opponent_choice: str, personal_choice: str) -> int:
    opponent_index = ['A', 'B', 'C'].index(opponent_choice)
    personal_index = ['X', 'Y', 'Z'].index(personal_choice)

    score = 1 if personal_choice == 'X' else 2 if personal_choice == 'Y' else 3
    win_points = 6
    tie_points = 3
    lose_points = 0

    if opponent_index == personal_index:
        return score + tie_points
    elif (personal_index - 1) % 3 == opponent_index:
        return score + win_points
    else:
        return score + lose_points


def part_1(dataset: List[str]) -> str:
    total_score = 0
    for line in dataset:
        opponent_choice, personal_choice = line.split(' ')
        total_score += score_round(opponent_choice, personal_choice)
    return str(total_score)


def part_2(dataset: List[str]) -> str:
    total_score = 0
    for line in dataset:
        opponent_choice, outcome = line.split(' ')

        opponent_index = ['A', 'B', 'C'].index(opponent_choice)
        winning_choice = ['X', 'Y', 'Z'][(opponent_index + 1) % 3]
        losing_choice = ['X', 'Y', 'Z'][(opponent_index - 1) % 3]
        tie_choice = ['X', 'Y', 'Z'][opponent_index]
        personal_choice = winning_choice if outcome == 'Z' else losing_choice if outcome == 'X' else tie_choice

        total_score += score_round(opponent_choice, personal_choice)
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
