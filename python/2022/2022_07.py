import decimal
from dataclasses import dataclass, field
from typing import List

from python.base_solution import BaseSolution


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    files: list[File] = field(default_factory=list)
    directories: list['Directory'] = field(default_factory=list)
    parent: 'Directory' = None

    def get_directories_recursively(self) -> List['Directory']:
        directories = [self]
        for directory in self.directories:
            directories.extend(directory.get_directories_recursively())
        return directories

    def get_size(self) -> int:
        return sum(f.size for f in self.files) + sum(d.get_size() for d in self.directories)

    # For debugging purposes
    def get_formatted_string(self):
        formatted_string = f'DIR {self.name} ({self.get_size()})\n'
        for file in self.files:
            formatted_string += f'|-- {file.name} ({file.size})\n'
        for directory in self.directories:
            formatted_string += ''.join(f'|-- {line}\n' for line in directory.get_formatted_string().splitlines())
        return formatted_string


class Solution(BaseSolution):
    def __init__(self, use_test_data=False):
        data_prefix = '2022_07'
        super().__init__(use_test_data, data_prefix)

    def _parse_filesystem(self) -> Directory:
        filesystem = Directory(name='/', parent=None)
        current_dir = filesystem
        processing_ls = False
        for line in self.dataset[1:]:  # skip first line since it is just "$ cd /"
            if line == '$ cd ..':
                processing_ls = False
                current_dir = current_dir.parent
            elif line.startswith('$ cd '):
                processing_ls = False
                dir_name = line[5:]
                current_dir = [d for d in current_dir.directories if d.name == dir_name][0]
            elif line == '$ ls':
                processing_ls = True
            elif processing_ls:
                size_or_type, name = line.split(' ')
                if size_or_type == 'dir':
                    new_dir = Directory(name=name, parent=current_dir)
                    current_dir.directories.append(new_dir)
                else:
                    new_file = File(name=name, size=int(size_or_type))
                    current_dir.files.append(new_file)
        return filesystem

    def part_1(self) -> str:
        filesystem = self._parse_filesystem()
        sum_of_small_dirs = sum(
            [d.get_size() for d in filesystem.get_directories_recursively() if d.get_size() <= 100000])
        return str(sum_of_small_dirs)

    def part_2(self) -> str:
        filesystem = self._parse_filesystem()
        needed_space = filesystem.get_size() - 40000000  # 40000000 is the disk size (70000000) minus the size of the update (30000000)
        large_enough_dirs = [d for d in filesystem.get_directories_recursively() if d.get_size() >= needed_space]
        large_enough_dirs.sort(key=lambda d: d.get_size())
        return str(large_enough_dirs[0].get_size())


def test_part_1():
    test_solution = Solution(True)
    assert test_solution.part_1() == '95437'


def test_part_2():
    test_solution = Solution(True)
    assert test_solution.part_2() == '24933642'


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1 solution: {solution.part_1()}')
    print(f'Part 2 solution: {solution.part_2()}')
