import pytest


def raise_abc():
    raise SystemExit(1)


def test_raise_abc():
    with pytest.raises(SystemExit):
        raise_abc()
