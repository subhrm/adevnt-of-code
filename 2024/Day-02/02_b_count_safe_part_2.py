"""
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report.
It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
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
        else:
            for i in range(len(report)):
                new_report = report[:i] + report[i + 1 :]
                if check_if_safe(new_report):
                    safe_reports += 1
                    break

    print(safe_reports)
