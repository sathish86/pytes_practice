def abc():
    return "ABC"


class TestMultipleCases():
    def test_abc(self):
        assert abc() == "ABC"

    def test_abc_fail(self):
        assert abc() == "XYZ"

    def test_abc_fail_2(self):
        assert abc() == "XYZ@#$"