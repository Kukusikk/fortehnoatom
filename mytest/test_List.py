import pytest
class TestForList:
    @pytest.mark.parametrize("x,y", [([],[7,]), ([9,9,6],[9,9,6,7])])
    def test_append(self,x,y):
        # Добавляет элемент в конец списка
        x.append(7)
        assert x==y
    @pytest.mark.parametrize("x,y", [([],[]), ([9,9,6,7],[7,6,9,9])])
    def test_reverse(self,x,y):
        # Разворачивает список
        x.reverse()
        assert x == y
    @pytest.mark.parametrize("x,y", [([],[]), ([9,9,6],[])])
    def test_clear(self,x,y):
        # Очищает список
        x.clear()
        assert x==y
    @pytest.mark.parametrize("x,y", [([1,],0), ([9,9,6],2)])
    def test_count(self,x,y):
        # Возвращает количество элементов со значением x
        assert x.count(9)==y
    @pytest.mark.parametrize("x,y", [([],[4,]), ([9,9,6],[9,9,4,6])])
    def test_insert(self,x,y):
        # Вставляет на i-ый элемент значение x
        x.insert(2,4)
        assert x==y

