import pytest


@pytest.fixture
def error_case_2():
    assert 1 == 2

# we can call another ficture in fixture function
@pytest.fixture
def error_case(error_case_2):
    assert 0


def test_abc():
    x = "abcd"
    assert "a" in x


def test_error(error_case):
    pass