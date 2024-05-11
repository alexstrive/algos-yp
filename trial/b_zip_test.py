from b_zip import make_zip


def test_case_1():
    assert make_zip([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]


def test_case_2():
    assert make_zip([1], [2]) == [1, 2]


def test_case_3():
    assert make_zip([1, 8, 9], [2, 3, 1]) == [1, 2, 8, 3, 9, 1]
