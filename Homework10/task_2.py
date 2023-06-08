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
# print(all_division(-20, 2, -5))

@pytest.mark.smoke
def test_division_positive():
    assert all_division(12, 2, 3) == 2


@pytest.mark.smoke
def test_division_negative():
    assert all_division(-20, 2, -5) == 2


@pytest.mark.parametrize("a, b, c, expected", [(10, 2, 5, 1), (100, 5, 2, 10), (15, 3, 1, 5)])
def test_division_parametrize(a, b, c, expected):
    assert all_division(a, b, c) == expected


@pytest.mark.smoke
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0, 5)


def test_division_float():
    assert all_division(10.0, 2.0, 5.0) == 1.0

# 1) pytest -v
# 2) pytest -v -m smoke
# 3) pytest -v -k "zero or float"


