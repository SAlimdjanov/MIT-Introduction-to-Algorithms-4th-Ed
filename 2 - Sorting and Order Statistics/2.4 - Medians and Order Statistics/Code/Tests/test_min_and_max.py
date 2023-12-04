"""
test_min_and_max.py

"""


from ..min_and_max import MinAndMax


array = [1, 8, 3, 4, 6, 5, 2, 7]
comparison = MinAndMax(array)


def test_minimum():
    """Method 'minimum' returns the correct minimum"""
    expected_result = min(array)
    result = comparison.minimum()

    assert result == expected_result


def test_maximum():
    """Method 'maximum' returns the correct maximum"""
    expected_result = max(array)
    result = comparison.maximum()

    assert result == expected_result
