import unittest
from suit_12_3 import Runner
from suit_12_3 import Tournament


def skip_if_frozen(test_func):
    def wrapper(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_func(self)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Изменяем на True, чтобы заморозить тесты

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Runner1", speed=10)
        runner.run()
        self.assertEqual(runner.distance, 20)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Runner2", speed=5)
        runner.walk()
        self.assertEqual(runner.distance, 5)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1", speed=10)
        runner2 = Runner("Runner2", speed=5)
        self.assertNotEqual(runner1, runner2)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Замораживаем тесты класса TournamentTest

    @skip_if_frozen
    def test_first_tournament(self):
        runner1 = Runner("Runner1", speed=10)
        runner2 = Runner("Runner2", speed=5)
        tournament = Tournament(100, runner1, runner2)
        results = tournament.start()
        self.assertIn(1, results)

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner("Runner1", speed=10)
        runner2 = Runner("Runner2", speed=15)
        tournament = Tournament(100, runner1, runner2)
        results = tournament.start()
        self.assertIn(1, results)

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner("Runner1", speed=5)
        runner2 = Runner("Runner2", speed=5)
        tournament = Tournament(100, runner1, runner2)
        results = tournament.start()
        self.assertIn(1, results)

if __name__ == "__main__":
    unittest.main()