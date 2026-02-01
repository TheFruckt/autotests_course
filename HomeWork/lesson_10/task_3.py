# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize(
    'test_set,expected',
    [
        pytest.param((40, 2, 2, 2), 5, marks=pytest.mark.smoke),
        pytest.param((777,), 777, marks=pytest.mark.smoke),
        ((0, 999, 99, 9), 0),
        pytest.param((-112, 4, 4), -7, marks=pytest.mark.skip),
        ((10, 0), None)
    ], ids=[
        'smoke',
        'yourself',
        'zero by',
        'below zero',
        'by zero'
    ]
)
def test_division(test_set, expected):
    if expected is None:
        with pytest.raises(ZeroDivisionError):
            all_division(*test_set)
    else:
        assert all_division(*test_set) == expected



