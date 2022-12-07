from python.base_solution import BaseSolution


def get_most_common_bit_by_index(list_of_nums=[], i=0):
    ones = [True for n in list_of_nums if list(n)[i] == '1']
    if len(ones) == (len(list_of_nums) / 2):
        return None
    return '1' if len(ones) > (len(list_of_nums) / 2) else '0'


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2021_03'
        if data_prefix == '20xx_xx':
            raise ValueError('You must set the data prefix for the year and day')
        super().__init__(use_test_data, data_prefix)

    def part_1(self) -> str:
        gamma_rate = '0b'
        epsilon_rate = '0b'

        for i in range(len(self.dataset[0])):
            if get_most_common_bit_by_index(self.dataset, i) == '1':
                gamma_rate += '1'
                epsilon_rate += '0'
            else:
                gamma_rate += '0'
                epsilon_rate += '1'

        return str(int(gamma_rate, 2) * int(epsilon_rate, 2))

    def part_2(self) -> str:
        oxygen_options = list(self.dataset)
        co2_options = list(self.dataset)

        for i in range(len(self.dataset[0])):
            if len(oxygen_options) > 1:
                new_list = []
                most_common_bit = get_most_common_bit_by_index(oxygen_options, i)
                for n in oxygen_options:
                    desired_bit = list(n)[i]
                    if (most_common_bit is not None and desired_bit == most_common_bit) or (
                            most_common_bit is None and desired_bit == '1'):
                        new_list.append(n)
                oxygen_options = new_list

        for i in range(len(self.dataset[0])):
            if len(co2_options) > 1:
                new_list = []
                most_common_bit = get_most_common_bit_by_index(co2_options, i)
                for n in co2_options:
                    desired_bit = list(n)[i]
                    if (most_common_bit is not None and desired_bit != most_common_bit) or (
                            most_common_bit is None and desired_bit == '0'):
                        new_list.append(n)
                co2_options = new_list

        return str(int('0b' + oxygen_options[0], 2) * int('0b' + co2_options[0], 2))


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '198'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '230'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
