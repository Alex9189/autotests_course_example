# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


@pytest.fixture(scope="class")
def test_class_fixture(request):
    start_time = time.time()
    print(f"\nStarting {request.cls.__name__} class at {start_time}")
    yield
    end_time = time.time()
    print(f"\nEnding {request.cls.__name__} class at {end_time}")
    print(f"Total time taken: {end_time - start_time}")


@pytest.fixture()
def test_fixture():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nTest time {end_time - start_time} seconds")


class TestClass:

    def test_one(self, test_fixture):
        print("Test one")

    def test_two(self, test_fixture):
        print("Test two")

    def test_three(self, test_fixture):
        print("Test three")
