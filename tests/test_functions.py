import pytest

from coding_challenge.functions import (
    Substring,
    find_alphanumeric_substrings,
    find_largest_substrings,
    replace_substrings_with_underscores,
    compute_area,
    compute_perimeter,
    NotEnoughSubstringsError,
)


@pytest.mark.parametrize(
    "test_substring,expected",
    [
        (Substring("abcde", 1, 3), 7),
        (Substring("HelloWorld", 8, 10), 19),
    ],
)
def test_substring_end_index(test_substring, expected):
    assert test_substring.end_index == expected


@pytest.mark.parametrize(
    "test_substring,expected",
    [
        (Substring("abcde", 1, 3), (1, 3)),
        (Substring("HelloWorld", 8, 10), (8, 10)),
    ],
)
def test_substring_location(test_substring, expected):
    assert test_substring.location == expected


@pytest.mark.parametrize(
    "test_substring1,test_substring2,expected",
    [
        (Substring("abcde", 1, 3), Substring("abcde", 1, 3), False),
        (Substring("abcde", 1, 3), Substring("efghi", 1, 7), False),
        (Substring("efghi", 1, 7), Substring("HelloWorld", 8, 10), True),
    ],
)
def test_substring_no_overlap(test_substring1, test_substring2, expected):
    assert test_substring1.no_overlap(test_substring2) == expected


@pytest.mark.parametrize(
    "test_lines,substring_len,expected",
    [
        (["Hello, World!\n"], 5, [Substring("Hello", 0, 0), Substring("World", 0, 7)]),
        (
            ["   \n", "--aA1234.@#$(\n"],
            4,
            [Substring("aA12", 1, 2), Substring("A123", 1, 3), Substring("1234", 1, 4)],
        ),
    ],
)
def test_find_alphanumeric_substrings(test_lines, substring_len, expected):
    assert find_alphanumeric_substrings(test_lines, substring_len) == expected


@pytest.mark.parametrize(
    "substrings,num_largest_substrings,expected",
    [
        (
            [Substring("Hello", 0, 0), Substring("World", 0, 7)],
            2,
            [Substring("World", 0, 7), Substring("Hello", 0, 0)],
        ),
        (
            [Substring("aA12", 1, 0), Substring("A123", 1, 1), Substring("1234", 1, 2)],
            1,
            [Substring("aA12", 1, 0)],
        ),
    ],
)
def test_find_largest_substrings(substrings, num_largest_substrings, expected):
    assert find_largest_substrings(substrings, num_largest_substrings) == expected


@pytest.mark.parametrize(
    "substrings,num_largest_substrings",
    [([Substring("aA12", 1, 0), Substring("A123", 1, 1), Substring("1234", 1, 2)], 2)],
)
def test_find_largest_substrings_not_enough(substrings, num_largest_substrings):
    with pytest.raises(NotEnoughSubstringsError) as err:
        find_largest_substrings(substrings, num_largest_substrings)

    assert f"Cannot find {num_largest_substrings} non-overlapping substrings. " in str(
        err.value
    )


@pytest.mark.parametrize(
    "test_lines,test_substrings,expected",
    [
        (
            ["Hello, World!\n"],
            [Substring("World", 0, 7), Substring("Hello", 0, 0)],
            ["_____, _____!\n"],
        ),
        (
            ["   \n", "--aA1234.@#$(\n"],
            [Substring("aA12", 1, 2)],
            ["   \n", "--____34.@#$(\n"],
        ),
    ],
)
def test_replace_substrings_with_underscores(test_lines, test_substrings, expected):
    assert replace_substrings_with_underscores(test_lines, test_substrings) == expected


@pytest.mark.parametrize(
    "points,expected",
    [
        ([(0, 0), (3, 0), (3, 5), (0, 5)], 15),
        ([(0, 0), (3, 0), (3, 4)], 6),
        ([(0, 0), (3, 4), (3, 0), (0, 4)], 0),
        ([(0, 0), (0, 1), (0, 3)], 0),
        ([(0, -2), (6, -2), (9, -0.5), (6, 2), (9, 4.5), (4, 7), (-1, 6), (-3, 3)], 77),
    ],
)
def test_compute_area(points, expected):
    assert compute_area(points) == expected


@pytest.mark.parametrize(
    "points,expected",
    [
        ([(0, 0), (3, 0), (3, 5), (0, 5)], 16.0),
        ([(0, 0), (3, 0), (3, 4)], 12.0),
        ([(0, 0), (3, 4), (3, 0), (0, 4)], 18.0),
        ([(0, 0), (0, 1), (0, 3)], 6),
    ],
)
def test_compute_perimeter(points, expected):
    assert compute_perimeter(points) == expected
