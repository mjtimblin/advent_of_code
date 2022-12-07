import os.path
from typing import List

import pytest


class BaseSolution:
    def __init__(self, use_test_data=False, data_prefix='base'):
        self.data_prefix = data_prefix
        if use_test_data:
            self._load_test_dataset()
        else:
            self._load_dataset()

    def _load_dataset(self) -> List[str]:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input', f'{self.data_prefix}.txt'), 'r') as f:
            self.dataset = [line.replace('\n', '') for line in f.readlines()]

    def _load_test_dataset(self) -> List[str]:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test_input', f'{self.data_prefix}.txt'), 'r') as f:
            self.dataset = [line.replace('\n', '') for line in f.readlines()]

    def part_1(self) -> str:
        raise NotImplementedError

    def part_2(self) -> str:
        raise NotImplementedError


def test_part_1():
    with pytest.raises(NotImplementedError) as e_info:
        solution = BaseSolution(True)
        assert solution.part_1() == ''


def test_part_2():
    with pytest.raises(NotImplementedError) as e_info:
        solution = BaseSolution(True)
        assert solution.part_2() == ''
