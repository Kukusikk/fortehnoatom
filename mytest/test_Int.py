import pytest


class TestForInt:
    @pytest.mark.parametrize("x,y", [(3, 7), (0, 9), (-1, 2)])
    def test_big(self, x, y):
        # >
        assert y > x

    @pytest.mark.parametrize("x,y", [(3, 7), (0, 9), (-1, 2)])
    def test_little(self, x, y):
        # <
        assert x < y

    def test_is(self):
        # one object
        x=[]
        y=x
        assert x is y

    @pytest.mark.parametrize("x,y", [(3, 3), (0, 0), (-1, -1)])
    def test_equial(self, x, y):
        # ==
        assert x == y

    @pytest.mark.parametrize("x,y", [(3, 7), (0, 9), (-1, 2)])
    def test_not_equial(self, x, y):
        # !=
        assert x != y
