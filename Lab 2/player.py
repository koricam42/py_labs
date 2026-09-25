"""
Program Name: Match Coins (Players)
Author: Jordan Mensah
Purpose: Represents the player with a name, wallet of coins, and a coin object
Starter Code: N/A
Date: 9/21/26
"""

from coin import Coin

class Player():
    """Class that represents a player in the game
    """
    def __init__(self, name: str) -> None:
        """Initializes the player with a name, 20-coin wallet, and Coin object

        Args:
            name (str): Name of player
        """
        self.__name = name
        self.__wallet = 20
        self.__coin= Coin()

    def toss_coin(self) -> None:
        """Tosses the players coin
        """
        self.__coin.toss()
    def get_coin_side(self) ->  str:
        """Returns the facing up side of the players coin

        Returns:
            str: Side of the coin facing up
        """
        return self.__coin.get_sideup()
    def win_coin(self) -> None:
        """Adds a coin to the players wallet
        """
        self.__wallet += 1
    def lose_coin(self) -> None:
        """Removes a coin from the players wallet
        """
        self.__wallet -= 1
    def get_wallet(self) -> int:
        """Returns the current number of coins in the players wallet

        Returns:
            int: The current number of coins
        """
        return self.__wallet
    def get_name(self) -> str:
        """Returns the player name

        Returns:
            str: Player name
        """
        return self.__name