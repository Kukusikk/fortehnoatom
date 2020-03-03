import pytest
class TestForSet:
    @pytest.mark.parametrize("x,y", [(set(),{7,}), ({9,6},{9,6,7})])
    def test_add(self,x,y):
        # добавляет элемент в множество
        x.add(7)
        assert x==y
    @pytest.mark.parametrize("x,y", [(set(),set()), (set([9,9,6]),set([9,9,6,]))])
    def test_copy(self,x,y):
        # копия множества
        assert x.copy()==y
    @pytest.mark.parametrize("x,y", [(set(),set()), (set([9,9,6]),set())])
    def test_clear(self,x,y):
        #   очистка множества
        x.clear()
        assert x==y
    @pytest.mark.parametrize("x,y", [(set(),set([7,])), (set([9,6]),set([1,2,4]))])
    def test_isdisjoint(self,x,y):
        # истина, если set и other не имеют общих элементов
        assert x.isdisjoint(y)

    @pytest.mark.parametrize("x,y", [(set(),set([7,9])), (set([9,6]),set([1,2,9,6,4]))])
    def test_issubset(self,x,y):
        # set <= other - все элементы set принадлежат other
        assert x.issubset(y)