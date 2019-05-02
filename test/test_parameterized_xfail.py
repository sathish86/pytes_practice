import pytest


@pytest.mark.parametrize("n", ['abcf', 'abc', 'abc'])
def test_param(n):
    assert n == "abc"

@pytest.mark.xfail
def test_expected_failure():
    assert 10 == 11