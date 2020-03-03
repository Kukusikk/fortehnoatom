import pytest


class TestForInt:
    @pytest.mark.parametrize("x,y", [(3, 7), (0, 9), (-1, 2)])
    def test_big(self, x, y):
        # >
        assert (y > x) == True

    @pytest.mark.parametrize("x,y", [(3, 7), (0, 9), (-1, 2)])
    def test_little(self, x, y):
        # <
        assert (x < y) == True

    @pytest.fixture()
    def some_data(self):
        a = 7
        return a

    def test_is(self, x=some_data, y=some_data):
        # one object
        assert (x is y) == True

    @pytest.mark.parametrize("x,y", [(3, 3), (0, 0), (-1, -1)])
    def test_equial(self, x, y):
        # ==
        assert (x == y) == True

    @pytest.mark.parametrize("x,y", [(3, 7), (0, 9), (-1, 2)])
    def test_not_equial(self, x, y):
        # !=
        assert (x != y) == True
