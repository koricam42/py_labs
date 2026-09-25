"""
Program Name: Match Coins (Coin)
Author: Jordan Mensah
Purpose: Represents a single coin with a private state of either "Heads" or "Tails"
Starter Code: N/A
Date: 9/21/26
"""
from random import randint

class Coin():
    """Class that represents a single tossable coin
    """
    def __init__(self) -> None:
        """Initalizes coin with default value of heads
        """
        self.__sideup = "Heads"

    def toss(self) -> None:
        """Generates random number to flip coin to either heads or tails
        """
        toss = randint(0, 1)

        if toss == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self) -> str:
        """Returns the current face up side of the coin

        Returns:
            str: _description_
        """
        return self.__sideup