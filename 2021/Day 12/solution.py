import argparse
from collections import defaultdict


def is_big_cave(node_id: str):
    return node_id.upper() == node_id


def part_1(dataset=[]):
    neighbors = defaultdict(list)
    for l in dataset:
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

    return len(completed_paths)


def part_2(dataset=[]):
    neighbors = defaultdict(list)
    for l in dataset:
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

    return len(completed_paths)


def run_tests():
    test_data = [
        'fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW'
    ]
    expected_part_1 = 226
    expected_part_2 = 3509

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
