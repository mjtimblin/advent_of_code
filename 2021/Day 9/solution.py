import argparse
from typing import List, Set


def _get_low_points(grid: List[List]) -> List[tuple]:
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y == 0 or grid[y - 1][x] > grid[y][x]) and \
                (y == (len(grid) - 1) or grid[y + 1][x] > grid[y][x]) and \
                (x == 0 or grid[y][x - 1] > grid[y][x]) and \
                (x == (len(grid[0]) - 1) or grid[y][x + 1] > grid[y][x]):
                    low_points.append((x, y,))
    return low_points


def _get_higher_by_one_adjacent_points(grid, point) -> List[tuple]:
    higher_points = []
    p_x, p_y = point

    if grid[p_y][p_x] == 8:
        return []

    # left
    if p_x > 0 and grid[p_y][p_x - 1] - 1 == grid[p_y][p_x]:
        higher_points.append((p_x - 1, p_y))
    # right
    if p_x < (len(grid[0]) - 1) and grid[p_y][p_x + 1] - 1 == grid[p_y][p_x]:
        higher_points.append((p_x + 1, p_y))
    # up
    if p_y > 0 and grid[p_y - 1][p_x] - 1 == grid[p_y][p_x]:
        higher_points.append((p_x, p_y - 1))
    # down
    if p_y < (len(grid) - 1) and grid[p_y + 1][p_x] - 1 == grid[p_y][p_x]:
        higher_points.append((p_x, p_y + 1))

    if higher_points == []:
        return []
    else:
        new_higher_points = [*higher_points]
        for p in higher_points:
            new_higher_points.extend(_get_higher_by_one_adjacent_points(grid, p))
        return new_higher_points    


def _get_basin_size_from_point(grid: List[List], low_point: tuple) -> int:
    adjacent_points = sorted(set(_get_higher_by_one_adjacent_points(grid, low_point)))
    # print('low_point', low_point)
    # print('adjacent_points', adjacent_points)
    # print('basin_size', len(adjacent_points) + 1)
    # print('---------------------')
    return len(adjacent_points) + 1


def part_1(dataset=[]):
    grid = [list(line) for line in dataset]
    return sum(int(grid[y][x]) + 1 for x, y in _get_low_points(grid))


def part_2(dataset=[]):
    grid = [list(line) for line in dataset]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = int(grid[y][x])

    low_points = _get_low_points(grid)
    top_three_basins = sorted([_get_basin_size_from_point(grid, p) for p in low_points])[-3:]
    return top_three_basins[0] * top_three_basins[1] * top_three_basins[2]


def run_tests():
    test_data = ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']
    expected_part_1 = 15
    expected_part_2 = 1134

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
