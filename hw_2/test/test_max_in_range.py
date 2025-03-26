from task import max_in_range
import pytest

@pytest.mark.parametrize("array, start, end, expected",
                         [
                             ([1,2,3,4,5], 1, 3, (4, 3, 2)),
                             ([5,6,7,8,9,10], 2, 4, (9, 4, 2)),
                             ([0,5,10,15,20,25], 0, 4, (20, 4, 4))
                         ])
def test_max_in_range_positive(array, start, end, expected):

    assert max_in_range(array, start, end) == expected


@pytest.mark.parametrize("array, start, end, expected",
                         [
                             ([1,2,3,4,5], 1, 7, ValueError),
                             ([5,6,7,8,9,10], -1, 4, ValueError),
                             ([0,5,10,15,20,25], 0, 10, ValueError)
                         ])
def test_max_in_range_negative(array, start, end, expected):
    with pytest.raises(expected):
        max_in_range(array, start, end)


@pytest.mark.parametrize("array, start, end, expected",
                         [
                             ([0,2,3,4,5], 0, 0, (0, 0, 0)),
                             ([0,2,3,4,5], 1, 1, (2, 1, 0))
                         ])
def test_max_in_range_bound(array, start, end, expected):

    assert max_in_range(array, start, end) == expected