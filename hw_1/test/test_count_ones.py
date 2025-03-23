from tasks import count_ones
import pytest

@pytest.mark.parametrize("num, expected",
                         [
                             (1,"1"),
                             (5,"101"),
                             (15,"1111")
                         ])
def test_count_ones_positive(num, expected):

    assert count_ones(num) == expected


@pytest.mark.parametrize("num, expected",
                         [
                             (-3,ValueError),
                             ("2",TypeError),
                             (2.5,TypeError)
                         ])
def test_count_ones_negative(num, expected):
    with pytest.raises(expected):
        count_ones(num)

@pytest.mark.parametrize("num, expected",
                         [
                             (0,"0")
                         ])
def test_count_ones_bound(num, expected):

    assert count_ones(num) == expected