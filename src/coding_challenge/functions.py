import math
from collections.abc import Iterable
from dataclasses import dataclass


class NotEnoughSubstringsError(Exception):
    """Exception raised when not enough non-overlapping substrings can be found."""


@dataclass
class Substring:
    text: str
    line_number: int  # line number in file
    start_index: int  # start index in line

    @property
    def end_index(self) -> int:
        """end index of the substring in line"""

        return self.start_index + len(self) - 1

    @property
    def location(self):
        return self.line_number, self.start_index

    def no_overlap(self, other):
        """Verifies if the substring do not have overlap with another substring
        in terms of their locations in the file."""

        return (
            self.line_number != other.line_number
            or self.start_index > other.end_index
            or other.start_index > self.end_index
        )

    def __len__(self):
        return len(self.text)

    def __repr__(self):
        return f"Substring('{self.text}', {self.line_number}, {self.start_index})"


def find_alphanumeric_substrings(
    lines: list[str], substring_len: int
) -> list[Substring]:
    """Finds all alphanumeric substrings from the input lines."""

    substrings = []
    for line_number, line in enumerate(lines):
        for start_index in range(len(line) - substring_len + 1):
            text = line[start_index : start_index + substring_len]
            if text.isalnum():
                substrings.append(Substring(text, line_number, start_index))

    return substrings


def find_largest_substrings(
    substrings: list[Substring], num_largest_substrings: int
) -> list[Substring]:
    """Finds n lexicographically largest non-overlapping substrings from the input
    substrings."""

    substrings.sort(key=lambda s: s.text, reverse=True)

    largest_substrings = []
    for substring in substrings:
        if all(
            substring.no_overlap(largest_substring)
            for largest_substring in largest_substrings
        ):
            largest_substrings.append(substring)

        if len(largest_substrings) >= num_largest_substrings:
            return largest_substrings

    raise NotEnoughSubstringsError(
        f"Cannot find {num_largest_substrings} non-overlapping substrings. "
        f"Only found {len(largest_substrings)} non-overlapping substrings."
    )


def replace_substrings_with_underscores(
    lines: list[str], substrings: list[Substring]
) -> list[str]:
    """Replaces substrings in the lines with underscores."""

    for substring in substrings:
        line = lines[substring.line_number]
        assert (
            line[substring.start_index : substring.end_index + 1] == substring.text
        ), "The substring in the line  does not match the input substring text."

        replaced_line = (
            line[: substring.start_index]
            + "_" * len(substring)
            + line[substring.end_index + 1 :]
        )
        lines[substring.line_number] = replaced_line
    return lines


def compute_area(points: Iterable[tuple[float, float]]) -> float:
    """Computes the area of a 2D simple polygon (i.e., without self-intersections)
    using Shoelace formula.

    @param points: Cartesian coordinates of the vertices of the polygon.
    @return: The area of the polygon.
    """

    return 0.5 * abs(
        sum(
            x0 * y1 - x1 * y0
            for ((x0, y0), (x1, y1)) in zip(points, [*points[1:], points[0]])
        )
    )


def compute_perimeter(points: Iterable[tuple[float, float]]) -> float:
    """Computes the perimeter of a 2D polygon.

    @param points: Cartesian coordinates of the vertices of the polygon.
    @return: The perimeter of the polygon.
    """

    return sum(
        math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        for ((x0, y0), (x1, y1)) in zip(points, [*points[1:], points[0]])
    )


def read_file(file_path: str) -> list[str]:
    """Returns all lines of a file ."""

    print(f"Reading text from {file_path}")
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def write_file(file_path: str, lines: Iterable[str]):
    """Writes a sequence of strings to the file."""

    with open(file_path, "w") as file:
        file.writelines(lines)

    print(f"The replaced text is output to {file_path}")


def run(
    input_file_path: str,
    output_file_path: str,
    substring_len: int,
    num_largest_substrings: int,
):
    if substring_len < 1:
        raise RuntimeError("The length of a substring should be at least 1.")
    if num_largest_substrings < 1:
        raise RuntimeError("The number of largest substrings should be at least 1.")

    lines = read_file(input_file_path)
    substrings = find_alphanumeric_substrings(lines, substring_len)
    largest_substrings = find_largest_substrings(substrings, num_largest_substrings)
    replaced_lines = replace_substrings_with_underscores(lines, largest_substrings)
    write_file(output_file_path, replaced_lines)

    points = [substring.location for substring in largest_substrings]
    area = compute_area(points)
    perimeter = compute_perimeter(points)

    print(f"largest substrings: {largest_substrings}")
    print(f"{len(points)} points in the x-y plane: {points}")
    print(f"Area of the polygon: {area}")
    print(f"Perimeter of the polygon: {perimeter}")
