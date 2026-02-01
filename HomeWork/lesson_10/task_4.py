# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


class Calculator:
    @staticmethod
    def addition(a, b):
        time.sleep(0.34)
        return a + b

    @staticmethod
    def subtract(a, b):
        time.sleep(1.17)
        return a - b


@pytest.mark.usefixtures("class_time_logger")
class TestCalculator:

    def test_addition(self, test_time_logger):
        calc = Calculator()
        result = calc.addition(3, 5)
        assert result == 8

    def test_subtract(self, test_time_logger):
        calc = Calculator()
        result = calc.subtract(10, 4)
        assert result == 6
