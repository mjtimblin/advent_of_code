from typing import Tuple, List

from python.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_09'
        super().__init__(use_test_data, data_prefix)

    def _get_tail_location_for_movement(self, head_location: Tuple[int, int], tail_location: Tuple[int, int]) -> Tuple[int, int]:
        new_tail = (tail_location[0], tail_location[1])
        # Tail needs to move down
        if head_location[0] > tail_location[0] + 1:
            new_tail = (tail_location[0] + 1, tail_location[1])

            # Check to see if tail needs to move diagonally either right or left
            if new_tail[1] < head_location[1]:
                new_tail = (new_tail[0], new_tail[1] + 1)
            elif new_tail[1] > head_location[1]:
                new_tail = (new_tail[0], new_tail[1] - 1)

        # Tail needs to move up
        elif head_location[0] + 1 < tail_location[0]:
            new_tail = (tail_location[0] - 1, tail_location[1])

            # Check to see if tail needs to move diagonally either right or left
            if new_tail[1] < head_location[1]:
                new_tail = (new_tail[0], new_tail[1] + 1)
            elif new_tail[1] > head_location[1]:
                new_tail = (new_tail[0], new_tail[1] - 1)

        # Tail needs to move right
        if head_location[1] > tail_location[1] + 1:
            new_tail = (tail_location[0], tail_location[1] + 1)

            # Check to see if tail needs to move diagonally either up or down
            if new_tail[0] < head_location[0]:
                new_tail = (new_tail[0] + 1, new_tail[1])
            elif new_tail[0] > head_location[0]:
                new_tail = (new_tail[0] - 1, new_tail[1])

        # Tail needs to move left
        elif head_location[1] + 1 < tail_location[1]:
            new_tail = (tail_location[0], tail_location[1] - 1)

            # Check to see if tail needs to move diagonally either up or down
            if new_tail[0] < head_location[0]:
                new_tail = (new_tail[0] + 1, new_tail[1])
            elif new_tail[0] > head_location[0]:
                new_tail = (new_tail[0] - 1, new_tail[1])

        return new_tail

    def part_1(self) -> str:
        tail_locations = {(0, 0)}
        current_head = (0, 0)
        current_tail = (0, 0)
        for line in self.dataset:
            direction, distance = line.split(' ')
            distance = int(distance)
            for _ in range(distance):
                if direction == 'U':
                    current_head = (current_head[0], current_head[1] + 1)
                elif direction == 'D':
                    current_head = (current_head[0], current_head[1] - 1)
                elif direction == 'L':
                    current_head = (current_head[0] - 1, current_head[1])
                else:
                    current_head = (current_head[0] + 1, current_head[1])
                current_tail = self._get_tail_location_for_movement(current_head, current_tail)
                tail_locations.add(current_tail)

        return str(len(tail_locations))

    def part_2(self) -> str:
        tail_locations = {(0, 0)}
        knots = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        for line in self.dataset:
            direction, distance = line.split(' ')
            distance = int(distance)
            for _ in range(distance):
                if direction == 'U':
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                elif direction == 'D':
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                elif direction == 'L':
                    knots[0] = (knots[0][0] - 1, knots[0][1])
                else:
                    knots[0] = (knots[0][0] + 1, knots[0][1])

                for i in range(1, len(knots)):
                    knots[i] = self._get_tail_location_for_movement(knots[i - 1], knots[i])
                    if i == 9:
                        tail_locations.add(knots[i])

        return str(len(tail_locations))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '88'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '36'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
