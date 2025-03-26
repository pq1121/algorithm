from task import rotate_and_reverse
import pytest

@pytest.mark.parametrize("array, k, expected",
                         [
                             ([1,2,3,4,5], 1, [4, 3, 2, 1, 5]),
                             ([5,6,7,8,9,10], 2, [8, 7, 6, 5, 10, 9]),
                             ([0,5,10,15,20,25], 3, [10, 5, 0, 25, 20, 15])
                         ])
def test_rotate_and_reverse_positive(array, k, expected):

    assert rotate_and_reverse(array, k) == expected


@pytest.mark.parametrize("array, k, expected",
                         [
                             ([1,2,3,4,5], "1", TypeError),
                             ([5,6,7,8,9,10], -1, ValueError),
                             ([0,5,10,15,20,25], "k", TypeError)
                         ])
def test_rotate_and_reverse_negative(array, k, expected):
    with pytest.raises(expected):
        rotate_and_reverse(array, k)


@pytest.mark.parametrize("array, k, expected",
                         [
                             ([0,2,3,4,5], 0, [5, 4, 3, 2, 0]),
                             ([0,2,3,4,5,6,7], 125, [0, 7, 6, 5, 4, 3, 2])
                         ])
def test_rotate_and_reverse_bound(array, k, expected):

    assert rotate_and_reverse(array, k) == expected