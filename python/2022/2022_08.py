from dataclasses import dataclass

from python.base_solution import BaseSolution


@dataclass
class Tree:
    value: int
    x: int
    y: int
    visible: bool = False
    scenic_score: int = 0


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_08'
        super().__init__(use_test_data, data_prefix)
        self.trees = None

    def _parse_trees(self) -> None:
        trees = []
        for y, line in enumerate(self.dataset):
            trees_in_line = []
            for x, value in enumerate(line):
                trees_in_line.append(Tree(int(value), x, y))
            trees.append(trees_in_line)
        self.trees = trees

    def _is_tallest_in_some_direction(self, tree: Tree) -> bool:
        rows = [row for row in self.trees]
        columns = [list(column) for column in zip(*self.trees)]

        visible = True
        for t in columns[tree.x][tree.y + 1:]:
            if t.value >= tree.value:
                visible = False

        if visible:
            return True
        else:
            visible = True

        for t in columns[tree.x][:tree.y]:
            if t.value >= tree.value:
                visible = False

        if visible:
            return True
        else:
            visible = True

        for t in rows[tree.y][tree.x + 1:]:
            if t.value >= tree.value:
                visible = False

        if visible:
            return True
        else:
            visible = True

        for t in rows[tree.y][:tree.x]:
            if t.value >= tree.value:
                visible = False

        return visible

    def _set_trees_visibility(self):
        rows = [row for row in self.trees]
        columns = [list(column) for column in zip(*self.trees)]
        for tree in rows[0] + rows[-1] + columns[0] + columns[-1]:
            tree.visible = True

        for x in range(1, len(rows) - 1):
            for y in range(1, len(columns) - 1):
                if self._is_tallest_in_some_direction(self.trees[x][y]):
                    self.trees[x][y].visible = True

    def _calculate_scenic_score(self, tree: Tree) -> None:
        rows = [row for row in self.trees]
        columns = [list(column) for column in zip(*self.trees)]

        up_view_trees = 0
        down_view_trees = 0
        left_view_trees = 0
        right_view_trees = 0

        for t in columns[tree.x][tree.y + 1:]:
            left_view_trees += 1
            if t.value >= tree.value:
                break

        for t in reversed(columns[tree.x][:tree.y]):
            right_view_trees += 1
            if t.value >= tree.value:
                break

        for t in rows[tree.y][tree.x + 1:]:
            up_view_trees += 1
            if t.value >= tree.value:
                break

        for t in reversed(rows[tree.y][:tree.x]):
            down_view_trees += 1
            if t.value >= tree.value:
                break

        tree.scenic_score = up_view_trees * down_view_trees * left_view_trees * right_view_trees

    def part_1(self) -> str:
        if not self.trees:
            self._parse_trees()
        self._set_trees_visibility()
        return str(sum([1 for row in self.trees for tree in row if tree.visible]))

    def part_2(self) -> str:
        if not self.trees:
            self._parse_trees()
        for row in self.trees:
            for tree in row:
                self._calculate_scenic_score(tree)
        return str(max([tree.scenic_score for row in self.trees for tree in row]))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '21'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '8'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
