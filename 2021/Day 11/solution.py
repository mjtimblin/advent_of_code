import argparse
from dataclasses import dataclass
from typing import List


@dataclass
class Coordinate:
    x: int
    y: int


class OctopusGrid:
    def __init__(self, values: List[List[int]]):
        self.grid = values


    def _get_flashed_coordinates(self):
        coords = []
        for x in range(10):
            for y in range(10):
                if self.grid[y][x] > 9:
                    coords.append(Coordinate(x, y))
        return coords


    def _increment_surrounding(self, c: Coordinate):
        coords_to_update = [
            Coordinate(c.x, c.y - 1), # up
            Coordinate(c.x, c.y + 1), # down
            Coordinate(c.x - 1, c.y), # left
            Coordinate(c.x + 1, c.y), # right
            Coordinate(c.x - 1, c.y - 1), # up-left
            Coordinate(c.x + 1, c.y - 1), # up-right
            Coordinate(c.x - 1, c.y + 1), # down-left
            Coordinate(c.x + 1, c.y + 1), # down-right
        ]

        for nc in coords_to_update:
            if nc.x >= 0 and nc.x < 10 and nc.y >= 0 and nc.y < 10:
                self.grid[nc.y][nc.x] += 1


    def tick(self):
        flashed_coords: List[Coordinate] = []
        for x in range(10):
            for y in range(10):
                self.grid[y][x] += 1

        newly_flashed_coords: List[Coordinate] = [c for c in self._get_flashed_coordinates() if c not in flashed_coords]
        while len(newly_flashed_coords) > 0:
            for c in newly_flashed_coords:
                self._increment_surrounding(c)
            flashed_coords.extend(newly_flashed_coords)
            newly_flashed_coords: List[Coordinate] = [c for c in self._get_flashed_coordinates() if c not in flashed_coords]

        for c in flashed_coords:
            self.grid[c.y][c.x] = 0

        return len(flashed_coords)



def part_1(dataset=[]):
    grid = OctopusGrid([[int(n) for n in list(l)] for l in dataset])
    return sum([grid.tick() for _ in range(100)])


def part_2(dataset=[]):
    grid = OctopusGrid([[int(n) for n in list(l)] for l in dataset])
    i = 1
    while grid.tick() != 100:
        i += 1
    return i


def run_tests():
    test_data = [
        '5483143223',
        '2745854711',
        '5264556173',
        '6141336146',
        '6357385478',
        '4167524645',
        '2176841721',
        '6882881134',
        '4846848554',
        '5283751526'
    ]
    expected_part_1 = 1656
    expected_part_2 = 195

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
