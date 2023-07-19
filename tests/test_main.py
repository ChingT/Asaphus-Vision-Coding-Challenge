import filecmp
import os

import pytest

from coding_challenge.functions import run


@pytest.mark.parametrize(
    "input_file_path,substring_len,num_largest_substrings,expected",
    [
        ("tests/data/input_1.txt", 5, 4, "tests/data/expected_output_1.txt"),
        ("tests/data/input_2.txt", 3, 5, "tests/data/expected_output_2.txt"),
    ],
)
def test_run(input_file_path, substring_len, num_largest_substrings, expected):
    output_file_path = "temp.txt"
    run(input_file_path, output_file_path, substring_len, num_largest_substrings)
    assert filecmp.cmp(output_file_path, expected)
    os.remove(output_file_path)
