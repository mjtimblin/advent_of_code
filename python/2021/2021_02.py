from python.base_solution import BaseSolution


def _parse_movement(direction_str):
    direction, distance = direction_str.split()
    distance = int(distance)
    return {
        'x': distance if direction == 'forward' else 0,
        'y': distance if direction == 'down' else (distance * -1) if direction == 'up' else 0
    }


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_02'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        movements = [_parse_movement(x) for x in self.dataset]
        horizontal_change = sum([m['x'] for m in movements])
        depth_change = sum([m['y'] for m in movements])
        return str(abs(horizontal_change * depth_change))

    def part_2(self) -> str:
        movements = [_parse_movement(x) for x in self.dataset]
        aim = 0
        horizontal_change = 0
        depth_change = 0
        for m in movements:
            aim += m['y']
            horizontal_change += m['x']
            depth_change += (aim * m['x'])
        return str(abs(horizontal_change * depth_change))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '150'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '900'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
