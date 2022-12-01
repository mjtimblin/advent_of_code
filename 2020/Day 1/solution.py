import os
import re


def main():
    entries = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'r') as f:
        for line in f.readlines():
            line_only_nums = re.sub('[^0-9]', '', line)
            entries.append(int(line_only_nums))

    found = False

    for i in range(0, len(entries)):
        for j in range(0, len(entries)):
            if i != j and entries[i] + entries[j] == 2020:
                found = True
                print(f'Part 1 solution: {entries[i] * entries[j]}')
                break
        if found:
            break

    for i in range(0, len(entries)):
        for j in range(0, len(entries)):
            for k in range(0, len(entries)):
                if i != j and i != k and entries[i] + entries[j] + entries[k] == 2020:
                    print(f'Part 2 solution: {entries[i] * entries[j] * entries[k]}')
                    exit()


if __name__ == '__main__':
    main()
