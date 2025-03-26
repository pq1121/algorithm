from task import inc_number
import pytest

@pytest.mark.parametrize("array, expected",
                         [
                             ([1,2,3,4,5], [1,2,3,4,6]),
                             ([5,6,7,8,9,1], [5,6,7,8,9,2]),
                             ([9,5,1,1,2,2], [9,5,1,1,2,3])
                         ])
def test_inc_number_positive(array, expected):

    assert inc_number(array) == expected


@pytest.mark.parametrize("array, expected",
                         [
                             ("fsdfs", TypeError),
                             ("1,2,3,4,5", TypeError),
                             ([1,5,2,1,5,25], ValueError),
                             ([0], ValueError),
                         ])
def test_inc_number_negative(array, expected):
    with pytest.raises(expected):
        inc_number(array)


@pytest.mark.parametrize("array, expected",
                         [
                             ([9], [1, 0])
                         ])
def test_inc_number_bound(array, expected):

    assert inc_number(array) == expected