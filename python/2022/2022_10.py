from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_10'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        vals_at_cycle = {20: -1, 60: -1, 100: -1, 140: -1, 180: -1, 220: -1}
        cycle = 1
        x_reg = 1
        for line in self.dataset:
            duration = 1 if line == 'noop' else 2
            for _ in range(duration):
                if cycle in vals_at_cycle:
                    vals_at_cycle[cycle] = x_reg
                cycle += 1
            # Register gets set after the cycle has finished
            if line.startswith('addx'):
                x_reg += int(line.split(' ')[1])

        signal_strength = 0
        for k, val in vals_at_cycle.items():
            signal_strength += val * k
        return str(signal_strength)

    def part_2(self) -> str:
        display_rows = ['', '', '', '', '', '']
        row_end_indices = [40, 80, 120, 160, 200, 240]
        cycle = 1
        x_reg = 1
        for line in self.dataset:
            duration = 1 if line == 'noop' else 2
            for _ in range(duration):
                row_index = row_end_indices.index([i for i in row_end_indices if cycle > i - 40][-1])
                if cycle - 1 - (row_index * 40) in [x_reg - 1, x_reg, x_reg + 1]:
                    display_rows[row_index] += '█'
                else:
                    display_rows[row_index] += '.'
                cycle += 1
            # Register gets set after the cycle has finished
            if line.startswith('addx'):
                x_reg += int(line.split(' ')[1])

        return str('\n'.join(display_rows))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '13140'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '''██..██..██..██..██..██..██..██..██..██..
███...███...███...███...███...███...███.
████....████....████....████....████....
█████.....█████.....█████.....█████.....
██████......██████......██████......████
███████.......███████.......███████.....'''.strip()


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: \n{solution.part_2()}')
