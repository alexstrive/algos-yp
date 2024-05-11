from c_sliding_sum import sliding


def test_case_1():
    assert sliding([1, 2, 3, 4, 5, 6, 7], 4) == [2.5, 3.5, 4.5, 5.5]


def test_case_2():
    assert sliding([9, 3, 2, 0, 1, 5, 1, 0, 0], 3) == [4.6666666667, 1.666666667, 1, 2, 2.333333335, 2, 0.3333333]


def test_case_3():
    assert sliding([1, 2, 3, 4, 5], 5) == [3]
