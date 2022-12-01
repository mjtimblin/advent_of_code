import os
import re


def traverse_slope(slope, num_right, num_down):
    num_trees = 0
    x = num_right
    y = num_down

    while y < len(slope):
        if slope[y][x] == '#':
            num_trees += 1
        x = (x + num_right) % len(slope[y])
        y = y + num_down

    return num_trees


def main():
    layout = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'r') as f:
        for line in f.readlines():
            sanitized_line = re.sub('[^#.]', '', line)
            layout.append(list(sanitized_line))

    part_1_num_trees = traverse_slope(layout, 3, 1)
    part_2_product_of_num_trees = traverse_slope(layout, 1, 1) * traverse_slope(layout, 3, 1) * traverse_slope(layout, 5, 1) * traverse_slope(layout, 7, 1) * traverse_slope(layout, 1, 2)

    print(f'Part 1 solution: {part_1_num_trees}')
    print(f'Part 2 solution: {part_2_product_of_num_trees}')


if __name__ == '__main__':
    main()
