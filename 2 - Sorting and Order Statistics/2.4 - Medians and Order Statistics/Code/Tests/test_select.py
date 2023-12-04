"""
test_select.py

"""


from ..select import Select


# Example from the book

array = [6, 19, 4, 12, 14, 9, 15, 7, 8, 11, 3, 13, 2, 5]
order_statistic = Select(array)
P = 0
R = len(array) - 1
I = 9  # Picks the 8th order statistic for the test


def test_select():
    """Method select obtains the correct order statistic"""
    expected_result = 12
    result = order_statistic.select(P, R, I)

    assert result == expected_result
