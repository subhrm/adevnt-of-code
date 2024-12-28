"""
For example, consider the following section of corrupted memory:

    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

import re


def process(text):
    # find all substrings with the pattern mul(x, y)
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(text)

    # convert the substrings to integers and multiply them
    result = sum([int(x) * int(y) for x, y in matches])

    return result


if __name__ == "__main__":
    file_name = "03_input.txt"
    with open(file_name, "r") as file:
        text = file.read().strip()

    print(process(text))
