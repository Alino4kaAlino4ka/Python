# запуск теста из командной строки:
# python -m pytest -v test_my_funcs.py


import pytest
from task002 import prime_fact as pf


list_for_test_1 = [(5, [5]), (10, [2, 5.0]), (100, [2, 2, 5, 5])]
@pytest.mark.parametrize('x, expected_result', list_for_test_1)
def test_my_pf_good(x, expected_result):
    assert pf(x) == expected_result


list_for_test_0 = [('2', TypeError), ('num', TypeError)]    # надо погуглить и вспомнить ошибки
@pytest.mark.parametrize('x, expected_exception', list_for_test_0)
def test_my_pf_bad(x, expected_exception):
    with pytest.raises(expected_exception):
        pf(x)

