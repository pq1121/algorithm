from task import three_sum_unique
import pytest

@pytest.mark.parametrize("array, expected",
                         [
                             ([-1,0,1,2,-1,4,-4], [[-1, 0, 1], [-1, 2, -1], [0, 1, -1], [0, 4, -4]]),
                             ([-1,0,1,2], [[-1, 0, 1]]),
                             ([-1,0,1,2,-2], [[-1, 0, 1], [0, 2, -2]])
                         ])
def test_three_sum_unique_positive(array, expected):

    assert three_sum_unique(array) == expected


@pytest.mark.parametrize("array, expected",
                         [
                             ("fsdfs", TypeError),
                             ("1,2,3,4,5", TypeError),
                             ([1,5,2,1,5,"25"], TypeError),
                             ([1], ValueError)
                         ])
def test_three_sum_unique_negative(array, expected):
    with pytest.raises(expected):
        three_sum_unique(array)


@pytest.mark.parametrize("array, expected",
                         [
                             ([0,1,0], None),
                             ([-1,1,0], [[-1, 1, 0]])
                         ])
def test_three_sum_unique_bound(array, expected):

    assert three_sum_unique(array) == expected