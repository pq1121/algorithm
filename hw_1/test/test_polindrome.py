from tasks import polindrome
import pytest

@pytest.mark.parametrize("num, expected",
                         [
                             (1,True),
                             (55,True),
                             (15,False)
                         ])
def test_polindrome_positive(num, expected):

    assert polindrome(num) == expected


@pytest.mark.parametrize("num, expected",
                         [
                             ("check",TypeError),
                             ("2",TypeError),
                             (2.5,TypeError)
                         ])
def test_polindrome_negative(num, expected):
    with pytest.raises(expected):
        polindrome(num)

@pytest.mark.parametrize("num, expected",
                         [
                             (0,True),
                             (-1,False)
                         ])
def test_polindrome_bound(num, expected):

    assert polindrome(num) == expected