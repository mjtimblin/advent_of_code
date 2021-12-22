import argparse
import re
from dataclasses import dataclass
from typing import List


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


def part_1(dataset=[]):
    points = []
    instructions = []

    for l in dataset:
        if ',' in l:
            x, y = l.split(',')
            points.append(Coordinate(int(x), int(y)))
        elif 'fold' in l:
            for match in re.findall('([a-z])=([0-9]+)', l):
                instructions.append(FoldInstruction(int(match[1]), match[0]))

    return len(fold_points(points, instructions[0]))


def part_2(dataset=[]):
    points = []
    instructions = []

    for l in dataset:
        if ',' in l:
            x, y = l.split(',')
            points.append(Coordinate(int(x), int(y)))
        elif 'fold' in l:
            for match in re.findall('([a-z])=([0-9]+)', l):
                instructions.append(FoldInstruction(int(match[1]), match[0]))

    for instruction in instructions:
        points = fold_points(points, instruction)

    grid = [[' ' for _ in range(max(p.x for p in points) + 1)] for _ in range(max(p.y for p in points) + 1)]
    for p in points:
        grid[p.y][p.x] = '█'

    return '\n'.join([''.join(l) for l in grid])

def run_tests():
    test_data = [
        '6,10',
        '0,14',
        '9,10',
        '0,3',
        '10,4',
        '4,11',
        '6,0',
        '6,12',
        '4,1',
        '0,13',
        '10,12',
        '3,4',
        '3,0',
        '8,4',
        '1,10',
        '2,14',
        '8,10',
        '9,0',
        '',
        'fold along y=7',
        'fold along x=5',
    ]
    expected_part_1 = 17

    assert expected_part_1 == part_1(test_data)
    print('Tests passed!')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=argparse.FileType('r'), help='Filepath for the input data file')
    args = parser.parse_args()

    run_tests()

    input_lines = [l.strip() for l in args.filepath.readlines()]
    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: \n{part_2(input_lines)}')


if __name__ == '__main__':
    main()
