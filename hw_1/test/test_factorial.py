from task1 import factorial
import pytest

@pytest.mark.parametrize("num, expected",
                         [
                             (3,6),
                             (5,120),
                             (20,2432902008176640000)
                         ])
def test_factorial_positive(num, expected):

    assert factorial(num) == expected


@pytest.mark.parametrize("num, expected",
                         [
                             (-3,ValueError),
                             ("2",TypeError),
                             (22,ValueError)
                         ])
def test_factorial_negative(num, expected):
    with pytest.raises(expected):
        factorial(num)

@pytest.mark.parametrize("num, expected",
                         [
                             (0,1),
                             (1,1)
                         ])
def test_factorial_negative(num, expected):

    assert factorial(num) == expected