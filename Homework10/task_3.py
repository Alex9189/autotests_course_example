# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("input, expected_output", [
    ((12, 2, 3), 2),
    ((-20, 2, -5), 2),
    pytest.param((100, 0, 5), None, marks=pytest.mark.skip(reason="Division by zero")),
    ((30, 3, 2), 5),
    pytest.param((10, 0, 5), None, marks=pytest.mark.skip(reason="Division by zero")),
])
def test_all_division_parametrized(input, expected_output):
    if expected_output is None:
        with pytest.raises(ZeroDivisionError):
            all_division(*input)
    else:
        assert all_division(*input) == expected_output

    if input == ((12, 2, 3), 2):
        pytest.mark.smoke(test_all_division_parametrized)


