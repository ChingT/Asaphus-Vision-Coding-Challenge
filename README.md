# Solution To Asaphus Vision Coding Challenge

## Motivation

This repository tries to solve the following Asaphus Vision Coding Challenge problems:

- Write a Python script that reads a text file, and finds the 4 lexicographically largest non-overlapping substrings satisfying the conditions:
    1. the substring is contained in a single line, and
    2. the substring is strictly alphanumeric, and
    3. the substring is of length 5.

- Compute the pair (line_number, start_index) for each of the 4 substrings. Take the 4 pairs as 4 points in the x-y plane that are corners of a quadrilateral,
and print its area and its perimeter.

- Create an output text file in which these 4 locations only are replaced with '_____'.

- Write test cases.

- It should be possible to run the script from the `__main__` section or from command 
  line.


## Installation

```bash
pip install .
```

## Usage

```bash
coding-challenge tests/data/input_1.txt
```
or
```bash
python src/coding_challenge/main.py tests/data/input_1.txt
```
To get help:
```bash
coding-challenge --help
``` 



## Test

```bash
pytest .
```


## Author
- Ching-Ting Huang