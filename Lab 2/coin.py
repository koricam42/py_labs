"""
Program Name: Match Coins (Coin)
Author: Jordan Mensah
Purpose: Represents a single coin with a private state of either "Heads" or "Tails"
Starter Code: N/A
Date: 9/21/26
"""
from random import randint

class Coin():
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        toss = randint(0, 1)

        if toss == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup