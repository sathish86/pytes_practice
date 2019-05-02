# content of test_strings.py
# pytest -q --stringinput="hello" --stringinput="world" --stringinput="#$"  test/conftest_practice/test_string.py


def test_valid_string(stringinput):
    assert stringinput.isalpha()