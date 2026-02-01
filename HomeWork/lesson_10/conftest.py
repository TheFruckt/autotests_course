import pytest
import time


@pytest.fixture(scope="class")
def class_time_logger():
    start_time = time.strftime("%H:%M:%S")
    print(f"\nНачало выполнения класса: {start_time}")
    yield
    end_time = time.strftime("%H:%M:%S")
    print(f"Конец выполнения класса: {end_time}")


@pytest.fixture
def test_time_logger():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nВремя выполнения теста: {end_time - start_time:.3f} сек.")



