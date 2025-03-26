from task import reverse_even_elements
import pytest

@pytest.mark.parametrize("array, expected",
                         [
                             ([1,2,3,4,5], [1, 4, 3, 2, 5]),
                             ([5,6,7,8,9,10], [5, 10, 7, 8, 9, 6]),
                             ([0,5,10,15,20,25], [20, 5, 10, 15, 0, 25])
                         ])
def test_reverse_even_elements_positive(array, expected):

    assert reverse_even_elements(array) == expected


@pytest.mark.parametrize("array, expected",
                         [
                             ("fsdfs", TypeError),
                             ("1,2,3,4,5", TypeError),
                             ([0,5,"10",15,"20",25], TypeError)
                         ])
def test_reverse_even_elements_negative(array, expected):
    with pytest.raises(expected):
        reverse_even_elements(array)


@pytest.mark.parametrize("array, expected",
                         [
                             ([0], [0]),
                             ([2,4], [4, 2]),
                             ([1,3,5], [1, 3, 5])
                         ])
def test_reverse_even_elements_bound(array, expected):

    assert reverse_even_elements(array) == expected