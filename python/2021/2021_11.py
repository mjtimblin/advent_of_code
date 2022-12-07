from dataclasses import dataclass
from typing import List

from python.base_solution import BaseSolution


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
            Coordinate(c.x, c.y - 1),  # up
            Coordinate(c.x, c.y + 1),  # down
            Coordinate(c.x - 1, c.y),  # left
            Coordinate(c.x + 1, c.y),  # right
            Coordinate(c.x - 1, c.y - 1),  # up-left
            Coordinate(c.x + 1, c.y - 1),  # up-right
            Coordinate(c.x - 1, c.y + 1),  # down-left
            Coordinate(c.x + 1, c.y + 1),  # down-right
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
            newly_flashed_coords: List[Coordinate] = [c for c in self._get_flashed_coordinates() if
                                                      c not in flashed_coords]

        for c in flashed_coords:
            self.grid[c.y][c.x] = 0

        return len(flashed_coords)


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_11'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        grid = OctopusGrid([[int(n) for n in list(line)] for line in self.dataset])
        return str(sum([grid.tick() for _ in range(100)]))

    def part_2(self) -> str:
        grid = OctopusGrid([[int(n) for n in list(line)] for line in self.dataset])
        i = 1
        while grid.tick() != 100:
            i += 1
        return str(i)


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '1656'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '195'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
