from collections import defaultdict

from python.base_solution import BaseSolution


def is_big_cave(node_id: str):
    return node_id.upper() == node_id


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_12'
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        neighbors = defaultdict(list)
        for l in self.dataset:
            n1, n2 = l.split('-')
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        completed_paths = []
        partial_paths = [['start']]

        while len(partial_paths) > 0:
            for path in list(partial_paths):
                partial_paths.remove(path)

                for neighbor_node in neighbors[path[-1]]:
                    if neighbor_node == 'end':
                        completed_paths.append([*path, neighbor_node])
                    elif neighbor_node not in path or is_big_cave(neighbor_node):
                        partial_paths.append([*path, neighbor_node])

        return str(len(completed_paths))

    def part_2(self) -> str:
        neighbors = defaultdict(list)
        for l in self.dataset:
            n1, n2 = l.split('-')
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        completed_paths = []
        partial_paths = [['start']]

        while len(partial_paths) > 0:
            for path in list(partial_paths):
                partial_paths.remove(path)

                for neighbor_node in neighbors[path[-1]]:
                    if neighbor_node == 'end':
                        completed_paths.append([*path, neighbor_node])
                    elif neighbor_node not in path or is_big_cave(neighbor_node) or (neighbor_node != 'start' and len([n for n in path if path.count(n) > 1 and not is_big_cave(n)]) == 0):
                        partial_paths.append([*path, neighbor_node])

        return str(len(completed_paths))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '226'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '3509'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
