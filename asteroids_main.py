from screen import Screen
import sys
import ship
from typing import Dict, Tuple
import random

DEFAULT_ASTEROIDS_NUM = 5
X, Y = 'x', 'y'
LOC, SPEED = 'location', 'speed'

info_th = Dict[str, Dict[str, int]]
loc_th = Tuple[int, int]


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        self.ship = ship.Ship(*self.get_random_location())

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        x, y = self.ship.get_location()
        self.__screen.draw_ship(x, y, self.ship.get_heading())

    def get_random_location(self) -> loc_th:
        """ :return: random location inside screen's borders """
        x = random.randint(self.__screen_min_x, self.__screen_max_x)
        y = random.randint(self.__screen_min_y, self.__screen_max_y)
        return x, y

    def calculate_move(self, obj) -> loc_th:
        """ gets object. calculates and returns it's new location after
        moving by formula """
        old_x, old_y = obj.get_location()
        spd_x, spd_y = obj.get_speed()
        delta_x = self.__screen_max_x - self.__screen_min_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        new_x = self.__screen_min_x + (old_x + spd_x -
                                       self.__screen_min_x) % delta_x
        new_y = self.__screen_min_y + (old_y + spd_y -
                                       self.__screen_min_y) % delta_y
        return new_x, new_y

    def blah(self):
        pass


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
