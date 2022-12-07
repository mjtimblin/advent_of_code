from typing import List

from python.base_solution import BaseSolution


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.start = start_point
        self.end = end_point


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_05'
        super().__init__(use_test_data, data_prefix)

    def _get_lines_from_dataset(self) -> List[Line]:
        lines = []
        for line in self.dataset:
            start, end = [Point(int(p[0]), int(p[1])) for p in [raw_point.split(',') for raw_point in line.split(' -> ')]]
            lines.append(Line(start, end))
        return lines

    def part_1(self) -> str:
        lines = self._get_lines_from_dataset()
        point_counts_map = {}

        for line in [l for l in lines if l.start.x == l.end.x or l.start.y == l.end.y]:
            if line.start.x == line.end.x:
                points = [Point(line.start.x, y) for y in range(min(line.start.y, line.end.y), max(line.start.y, line.end.y) + 1)]
            else:
                points = [Point(x, line.start.y) for x in range(min(line.start.x, line.end.x), max(line.start.x, line.end.x) + 1)]

            for p in points:
                key = f'{p.x}_{p.y}'
                if key not in point_counts_map.keys():
                    point_counts_map[key] = 1
                else:
                    point_counts_map[key] += 1

        return str(len([p for p in point_counts_map.values() if p > 1]))

    def part_2(self) -> str:
        lines = self._get_lines_from_dataset()
        point_counts_map = {}

        for line in lines:
            if line.start.x == line.end.x:
                points = [Point(line.start.x, y) for y in range(min(line.start.y, line.end.y), max(line.start.y, line.end.y) + 1)]
            elif line.start.y == line.end.y:
                points = [Point(x, line.start.y) for x in range(min(line.start.x, line.end.x), max(line.start.x, line.end.x) + 1)]
            else:
                xs = [x for x in range(min(line.start.x, line.end.x), max(line.start.x, line.end.x) + 1)]
                ys = [y for y in range(min(line.start.y, line.end.y), max(line.start.y, line.end.y) + 1)]

                if line.start.x != xs[0]:
                    xs.reverse()

                if line.start.y != ys[0]:
                    ys.reverse()

                points = [Point(p[0], p[1]) for p in zip(xs, ys)]

            for p in points:
                key = f'{p.x}_{p.y}'
                if key not in point_counts_map.keys():
                    point_counts_map[key] = 1
                else:
                    point_counts_map[key] += 1

        return str(len([p for p in point_counts_map.values() if p > 1]))

def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '5'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '12'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
