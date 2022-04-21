from main import sum_of_intervals


def test1():
    assert sum_of_intervals([(1, 5)]) == 4


def test2():
    assert sum_of_intervals([(1, 5), (6, 10)]) == 8


def test3():
    assert sum_of_intervals([(1, 5), (1, 5)]) == 4


def test4():
    assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7


def test5():
    assert sum_of_intervals([[1, 2], [6, 10], [11, 15]]) == 9


def test6():
    intervals = [
        (-195, 99),
        (68, 406),
        (292, 497),
        (-213, 429),
        (278, 493),
        (119, 337),
        (414, 444),
        (-13, 22),
        (287, 301),
        (-192, 136),
    ]

    assert sum_of_intervals(intervals) == 710
