from typing import Dict, Tuple

info_th = Dict[str, Dict[str, int]]
loc_th = Tuple[int, int]

X, Y = 'x', 'y'
LOC, SPEED = 'location', 'speed'


class Ship:
    """ Object 'Ship', represents the space ship in the game """
    def __init__(self, x: int = 0, y: int = 0):
        """
        Creates a new space ship.
        :param x: location at x axis
        :param y: location at y axis
        """
        self.info: info_th = {X: {LOC: x, SPEED: 0},
                              Y: {LOC: y, SPEED: 0}}
        self.__heading: float = 0

    def set_location(self, x: int, y: int):
        """ sets ship's location by x and y """
        self.info[X][LOC] = x
        self.info[Y][LOC] = y

    def get_location(self) -> loc_th:
        """ :return ship's location (x, y) """
        return self.info[X][LOC], self.info[Y][LOC]

    def set_speed(self, x_spd: int, y_spd: int):
        """ sets ship's speed """
        self.info[X][SPEED] = x_spd
        self.info[Y][SPEED] = y_spd

    def get_speed(self) -> Tuple[int, int]:
        """ :return  speed at x, speed at y """
        return self.info[X][SPEED], self.info[Y][SPEED]

    def set_heading(self, heading: float):
        """ sets ship's heading """
        self.__heading = heading

    def get_heading(self) -> float:
        """ :return ship's heading """
        return self.__heading
