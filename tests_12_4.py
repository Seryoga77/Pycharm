import logging
import unittest

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w', format='%(asctime)s | %(levelname)s | %(message)s')


class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if speed < 0:
            raise ValueError("speed не может быть отрицательным")
        self.name = name
        self.speed = speed


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner(name="Тестовый бегун", speed=-10)  # Передаем отрицательное значение
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(name=123, speed=5)  # Передаем неправильный тип
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == "__main__":
    unittest.main()