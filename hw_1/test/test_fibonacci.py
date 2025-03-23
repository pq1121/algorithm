from tasks import fibonacci
import pytest

@pytest.mark.parametrize("num, expected",
                         [
                             (3,[0,1,1,2]),
                             (5,[0,1,1,2,3,5]),
                             (10,[0,1,1,2,3,5,8,13,21,34,55])
                         ])
def test_fibonacci_positive(num, expected):

    assert fibonacci(num) == expected


@pytest.mark.parametrize("num, expected",
                         [
                             (-3,ValueError),
                             ("2",TypeError),
                             ("",TypeError)
                         ])
def test_fibonacci_negative(num, expected):
    with pytest.raises(expected):
        fibonacci(num)

@pytest.mark.parametrize("num, expected",
                         [
                             (0,[0]),
                             (1,[0,1])
                         ])
def test_fibonacci_bound(num, expected):

    assert fibonacci(num) == expected