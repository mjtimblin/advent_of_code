import argparse


def _get_syntax_error_score(input: str):
    pairs_and_scores = [('(', ')', 3), ('[', ']', 57), ('{', '}', 1197), ('<', '>', 25137),]
    stack = []
    for c in input:
        for opening, closing, score in pairs_and_scores:
            if opening == c:
                stack.append(c)
            elif closing == c:
                most_recent_added = stack.pop()
                if most_recent_added != opening:
                    return score
    return 0


def _get_incomplete_stack_score(input: str):
    pairs_and_scores = [('(', ')', 1), ('[', ']', 2), ('{', '}', 3), ('<', '>', 4),]
    stack = []
    total = 0
    for c in input:
        for opening, closing, score in pairs_and_scores:
            if opening == c:
                stack.append(c)
                break
            elif closing == c:
                most_recent_added = stack.pop()
                if most_recent_added != opening:
                    return 0
                break

    while len(stack) > 0:
        c = stack.pop()
        for opening, closing, score in pairs_and_scores:
            if c == opening:
                total = (total * 5) + score
                break

    return total


def part_1(dataset=[]):
    return sum(_get_syntax_error_score(l) for l in dataset)


def part_2(dataset=[]):
    scores = [s for s in [_get_incomplete_stack_score(l) for l in dataset] if s != 0]
    scores.sort()
    return scores[int((len(scores) - 1) / 2)]


def run_tests():
    test_data = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]
    expected_part_1 = 26397
    expected_part_2 = 288957

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
