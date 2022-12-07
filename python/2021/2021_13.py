import re
from dataclasses import dataclass
from typing import List

from python.base_solution import BaseSolution


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


@dataclass(frozen=True)
class FoldInstruction:
    value: int
    axis: str


def fold_points(coords: List[Coordinate], instruction: FoldInstruction) -> List[Coordinate]:
    folded_coords = set()
    for c in list(coords):
        if instruction.axis == 'x':
            if c.x > instruction.value:
                folded_coords.add(Coordinate(c.x - (2 * (c.x - instruction.value)), c.y))
            else:
                folded_coords.add(c)
        else:
            if c.y > instruction.value:
                folded_coords.add(Coordinate(c.x, c.y - (2 * (c.y - instruction.value))))
            else:
                folded_coords.add(c)

    return list(folded_coords)


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_13'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def _get_points(self) -> List[Coordinate]:
        points = []
        for line in self.dataset:
            if ',' in line:
                x, y = line.split(',')
                points.append(Coordinate(int(x), int(y)))
        return points


    def _get_instructions(self) -> List[FoldInstruction]:
        instructions = []
        for line in self.dataset:
            if 'fold' in line:
                for match in re.findall('([a-z])=([0-9]+)', line):
                    instructions.append(FoldInstruction(int(match[1]), match[0]))
        return instructions

    def part_1(self) -> str:
        points = self._get_points()
        instructions = self._get_instructions()
        return str(len(fold_points(points, instructions[0])))

    def part_2(self) -> str:
        points = self._get_points()
        instructions = self._get_instructions()

        for instruction in instructions:
            points = fold_points(points, instruction)

        grid = [[' ' for _ in range(max(p.x for p in points) + 1)] for _ in range(max(p.y for p in points) + 1)]
        for p in points:
            grid[p.y][p.x] = '█'

        return '\n'.join([''.join(l) for l in grid])


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '17'


def test_part_2():
    test_solution = Solution(True)
    result = test_solution.part_2()
    assert result != ''
    print('\nManually verify that the following output resembles a letter \'O\'')
    print(result)


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: \n{solution.part_2()}')
