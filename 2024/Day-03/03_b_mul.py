"""
For example, consider the following section of corrupted memory:

    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
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

    DO = "do()"
    DONT = "don't()"
    final_result = 0

    while len(text) > 0:
        if DONT in text:
            idx = text.find(DONT)
            r = process(text[:idx])
            final_result += r
            text = text[idx + len(DONT) :]
            if DO in text:
                idx = text.find(DO)
                text = text[idx + len(DO) :]
            else:
                text = ""
        else:
            r = process(text)
            final_result += r
            text = ""

    print(final_result)
