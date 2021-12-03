import argparse


def _parse_movement(direction_str):
    direction, distance = direction_str.split()
    distance = int(distance)
    return {
        'x': distance if direction == 'forward' else 0,
        'y': distance if direction == 'down' else (distance * -1) if direction == 'up' else 0
    }


def part_1(dataset=[]):
    movements = [_parse_movement(x) for x in dataset]
    horizontal_change = sum([m['x'] for m in movements])
    depth_change = sum([m['y'] for m in movements])
    return abs(horizontal_change * depth_change)


def part_2(dataset=[]):
    movements = [_parse_movement(x) for x in dataset]
    aim = 0
    horizontal_change = 0
    depth_change = 0
    for m in movements:
        aim += m['y']
        horizontal_change += m['x']
        depth_change += (aim * m['x'])
    return abs(horizontal_change * depth_change)


def run_tests():
    test_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    expected_part_1 = 150
    expected_part_2 = 900

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
