import sys


def sum_of_intervals(intervals):
    min_, max_ = sys.maxsize, -sys.maxsize - 1

    for (start, end) in intervals:
        min_, max_ = min(min_, start), max(max_, end)

    diff = -1

    if min_ < 0:
        diff = abs(min_)
        max_ += diff
        min_ = 0

    elements = ["" for _ in range(max_ - min_)]

    for (start, end) in intervals:
        elements[start + diff : end + diff] = ["0" for _ in range((end + diff) - (diff + start))]

    return elements.count("0")
