# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_1():
    assert all_division(40, 2, 2, 2) == 5, "Не верное значение"


@pytest.mark.smoke
def test_2():
    assert all_division(777) == 777, "Не верное значение"


def test_3():
    assert all_division(0, 999, 99, 9) == 0, "Не верное значение"

@pytest.mark.acceptance
def test_4():
    assert all_division(-112, 4, 4) == -7, "Не верное значение"


def test_negative():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)
