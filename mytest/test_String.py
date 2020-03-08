import pytest


class TestForString:
    @pytest.mark.parametrize("x,y", [('245', True), ('{9,6},{9,6,7}', False)])
    def test_isdigit(self, x, y):
        # Состоит ли строка из цифр
        assert x.isdigit() == y

    @pytest.mark.parametrize("x,y", [('24d5', True), ('{9,6},{9,6,7}', False)])
    def test_isalnum(self, x, y):
        # Состоит ли строка из цифр или букв
        assert x.isalnum() == y

    @pytest.mark.parametrize("x,y", [('adsh', True), ('{9,6},{9,6,7}', False)])
    def test_isalpha(self, x, y):
        # Состоит ли строка из букв
        assert x.isalpha() == y

    @pytest.mark.parametrize("x,y", [('245df', True), ('A{9,6},{9,6,7}', False)])
    def test_islower(self, x, y):
        # Состоит ли строка из символов в нижнем регистре
        assert x.islower() == y

    @pytest.mark.parametrize("x,y", [('FGHJ', True), ('{9,6hh},{9,6,7}', False)])
    def test_isupper(self, x, y):
        # Состоит ли строка из символов в верхнем регистре
        assert x.isupper() == y
