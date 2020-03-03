import pytest


class TestForDictionary:

    # @pytest.mark.parametrize(
    #     "test_input,expected",
    #     [[{8:'kk'},{'aa':8,'ss':7}], pytest.param([{8:'kk'},{'aa':8,'ss':7}])],
    # )
    # @pytest.mark.parametrize("x", [{8:'kk'},{'aa':8,'ss':7}])
    # @pytest.mark.parametrize("y", [{8:'kk'},{'aa':8,'ss':7}])
    @pytest.mark.parametrize("x,y", [({8: 'kk'}, {8: 'kk'}), ({'aa': 8, 'ss': 7}, {'aa': 8, 'ss': 7})])
    def test_copy(self, x, y):
        # возвращает копию словаря
        assert x == y.copy()

    @pytest.mark.parametrize("x,y", [({}, []), ({'aa': 8, 'ss': 7}, ['aa', 'ss'])])
    def test_keys(self, x, y):
        # возвращает объект ключей в словаре который должен переводиться в список
        assert list(x.keys()) == y

    @pytest.mark.parametrize("x,y", [({}, None), ({'aa': 8, 'ss': 7}, None)])
    def test_clean(self, x, y):
        # очищает словарь
        assert x.clear() == y

    @pytest.mark.parametrize("x,y", [({}, []), ({'aa': 8, 'ss': 7}, [8, 7])])
    def test_values(self, x, y):
        # возвращает значения в словаре  который должен переводиться в список
        assert list(x.values()) == y

    @pytest.mark.parametrize("x,y", [({}, []), ({'aa': 8, 'ss': 7}, [('aa', 8), ('ss', 7)])])
    def test_items(self, x, y):
        # возвращает пары (ключ, значение)
        assert list(x.items()) == y
        pass
