import argparse


def _get_most_common_bit_by_index(list_of_nums=[], i=0):
    ones = [True for n in list_of_nums if list(n)[i] == '1']
    if len(ones) == (len(list_of_nums) / 2):
        return None
    return '1' if len(ones) > (len(list_of_nums) / 2) else '0'


def part_1(dataset=[]):
    gamma_rate = '0b'
    epsilon_rate = '0b'

    for i in range(len(dataset[0])):
        if _get_most_common_bit_by_index(dataset, i) == '1':
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_2(dataset=[]):
    oxygen_options = list(dataset)
    co2_options = list(dataset)

    for i in range(len(dataset[0])):
        if len(oxygen_options) > 1:
            new_list = []
            most_common_bit = _get_most_common_bit_by_index(oxygen_options, i)
            for n in oxygen_options:
                desired_bit = list(n)[i]
                if (most_common_bit is not None and desired_bit == most_common_bit) or (most_common_bit is None and desired_bit == '1'):
                    new_list.append(n)
            oxygen_options = new_list

    for i in range(len(dataset[0])):
        if len(co2_options) > 1:
            new_list = []
            most_common_bit = _get_most_common_bit_by_index(co2_options, i)
            for n in co2_options:
                desired_bit = list(n)[i]
                if (most_common_bit is not None and desired_bit != most_common_bit) or (most_common_bit is None and desired_bit == '0'):
                    new_list.append(n)
            co2_options = new_list

    return int('0b' + oxygen_options[0], 2) * int('0b' + co2_options[0], 2)


def run_tests():
    test_data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    expected_part_1 = 198
    expected_part_2 = 230

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
