"""
test_randomized_select.py

"""


from ..randomized_select import RandomizedSelect


# Example from book

array = [6, 19, 4, 12, 14, 9, 15, 7, 8, 11, 3, 13, 2, 5]
order_statistic = RandomizedSelect(array)
P = 0
R = len(array) - 1
I = 5  # Picks the 5th order statistic for the test


def test_randomized_select():
    """Method randomized_select picks the correct i-th order statistic"""
    expected_result = 6
    result = order_statistic.randomized_select(P, R, I)

    assert result == expected_result
