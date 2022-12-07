from python.base_solution import BaseSolution


def get_syntax_error_score(input: str):
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


def get_incomplete_stack_score(input: str):
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


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_10'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        return str(sum(get_syntax_error_score(line) for line in self.dataset))

    def part_2(self) -> str:
        scores = [s for s in [get_incomplete_stack_score(line) for line in self.dataset] if s != 0]
        scores.sort()
        return str(scores[int((len(scores) - 1) / 2)])


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '26397'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '288957'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
