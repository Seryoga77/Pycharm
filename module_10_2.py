import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            self.days += 1
            remaining = max(0, self.enemies)
            print(f"{self.name} сражается {self.days}..., осталось {remaining} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(я)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончены!")