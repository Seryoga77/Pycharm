import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name



class TestRunner(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Тестовый бегун 1")  # создаем объект Runner
        for _ in range(10):
            runner.walk()  # вызываем метод walk 10 раз
        self.assertEqual(runner.distance, 50)  # проверка, что total distance равен 50

    def test_run(self):
        runner = Runner("Тестовый бегун 2")  # создаем объект Runner
        for _ in range(10):
            runner.run()  # вызываем метод run 10 раз
        self.assertEqual(runner.distance, 100)  # проверка, что total distance равен 100

    def test_challenge(self):
        runner1 = Runner("Тестовый бегун 3")  # создаем первый объект Runner
        runner2 = Runner("Тестовый бегун 4")  # создаем второй объект Runner
        for _ in range(10):
            runner1.run()  # вызываем метод run для первого объекта
            runner2.walk()  # вызываем метод walk для второго объекта
        self.assertNotEqual(runner1.distance, runner2.distance)  # проверка на неравенство дистанций

# Запуск тестов
if __name__ == '__main__':
    unittest.main()