import argparse
from typing import List


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.start = start_point
        self.end = end_point


def _get_lines_from_dataset(dataset=[]) -> List[Line]:
    lines = []
    for l in dataset:
        start, end = [Point(int(p[0]), int(p[1])) for p in [raw_point.split(',') for raw_point in l.split(' -> ')]]
        lines.append(Line(start, end))
    return lines


def part_1(dataset=[]):
    lines = _get_lines_from_dataset(dataset)
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

    return len([p for p in point_counts_map.values() if p > 1])


def part_2(dataset=[]):
    lines = _get_lines_from_dataset(dataset)
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

    return len([p for p in point_counts_map.values() if p > 1])


def run_tests():
    test_data = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']
    expected_part_1 = 5
    expected_part_2 = 12

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
