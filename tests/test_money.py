import pytest

from ukr.wfst import apply_fst_text, graph, tMoneyFst


@pytest.mark.parametrize('spoken,expected', [
    ('одна гривня', '₴1'),
    ('одна гривня одна копійка', '₴1.01'),
    ('одна гривня двадцять одна копійка', '₴1.21'),
    ('двадцять одна гривня двадцять одна копійка', '₴21.21'),
    ('сто одинадцять доларів двадцять один цент', '$111.21'),
    ('сто одинадцять доларів і двадцять один цент', '$111.21'),
    ('двадцять один цент', '$0.21'),
    ('двадцять один копійка', '₴0.21'),
    ('сім копійок', '₴0.07'),
])
def test_money(spoken, expected):
    assert apply_fst_text(spoken, graph) == expected
