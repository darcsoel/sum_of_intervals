import sys


def sum_of_intervals(intervals):
    min_, max_ = sys.maxsize, 0

    for (start, end) in intervals:
        min_, max_ = min(min_, start), max(max_, end)

    elements = ["" for _ in range(max_ - min_)]

    for (start, end) in intervals:
        elements[start - 1 : end - 1] = ["0" for _ in range(end - start)]

    return elements.count("0")
