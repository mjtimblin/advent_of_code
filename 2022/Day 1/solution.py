import os.path


def get_inventories(dataset=[]):
    inventories = []
    while '' in dataset:
        inventories.append([int(l) for l in dataset[:dataset.index('')]])
        dataset = dataset[dataset.index('') + 1:]
    inventories.append([int(l) for l in dataset])
    return inventories


def part_1(dataset=[]):
    inventories = get_inventories(dataset)
    return max([sum(i) for i in inventories])


def part_2(dataset=[]):
    inventories = get_inventories(dataset)
    return sum(sorted([sum(i) for i in inventories])[-3:])


def run_tests():
    test_data = [l.strip() for l in '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''.strip().splitlines()]
    expected_part_1 = 24000
    expected_part_2 = 45000

    assert expected_part_1 == part_1(test_data)
    assert expected_part_2 == part_2(test_data)
    print('Tests passed!')


def main():
    run_tests()

    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    f = open(filepath, 'r')
    input_lines = [l.strip() for l in f.readlines()]
    f.close()

    print(f'Part 1 solution: {part_1(input_lines)}')
    print(f'Part 2 solution: {part_2(input_lines)}')


if __name__ == '__main__':
    main()
