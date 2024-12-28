"""
The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""


def read_input(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append([int(x) for x in line.strip().split()])

    return data


def check_if_safe(report):
    safe = True
    if len(report) <= 1:
        return safe

    is_increasing = report[1] > report[0]

    prev = report[0]
    for a in report[1:]:
        diff = abs(a - prev)
        if (
            diff > 3
            or diff == 0
            or (is_increasing and (a <= prev))
            or (not is_increasing and (a >= prev))
        ):
            safe = False
            break
        prev = a

    return safe


if __name__ == "__main__":
    data = read_input("02_input.txt")
    safe_reports = 0
    for report in data:
        if check_if_safe(report):
            # print(report)
            safe_reports += 1

    print(safe_reports)
