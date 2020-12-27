from typing import Dict, Tuple

info_th = Dict[str, Dict[str, int]]
loc_th = Tuple[int, int]

X, Y = 'x', 'y'
LOC, SPEED = 'location', 'speed'


class Asteroid:
    """ An object which will represent an asteroid in the game"""
    def __init__(self, x: int = 0, y: int = 0, size: int = 1):
        """
        Creates a new space asteroid.
        :param x: location at x axis
        :param y: location at y axis
        """
        self.info: info_th = {X: {LOC: x, SPEED: 0},
                              Y: {LOC: y, SPEED: 0}}
        self.__size: int = size

    def set_location(self, x: int, y: int):
        """ sets asteroid's location by x and y """
        self.info[X][LOC] = x
        self.info[Y][LOC] = y

    def get_location(self) -> loc_th:
        """ :return asteroid's location (x, y) """
        return self.info[X][LOC], self.info[Y][LOC]

    def set_speed(self, x_spd: int, y_spd: int):
        """ sets asteroid's speed """
        self.info[X][SPEED] = x_spd
        self.info[Y][SPEED] = y_spd

    def get_speed(self) -> Tuple[int, int]:
        """ :return  (speed at x, speed at y) """
        return self.info[X][SPEED], self.info[Y][SPEED]

    def set_size(self, size: int):
        """ sets asteroid's size """
        self.__size = size

    def get_size(self) -> int:
        """ :return ship's heading """
        return self.__size
