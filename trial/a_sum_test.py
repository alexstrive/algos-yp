from a_sum import get_sum


def test_get_sum_case1():
    assert get_sum(12, 90) == 102


def test_get_sum_case2():
    assert get_sum(200, -200) == 0


def test_get_sum_case3():
    assert get_sum(1000000000, 1000000000) == 2000000000
