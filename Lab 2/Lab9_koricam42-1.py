"""
Program Name: Match Coins (Main)
Author: Jordan Mensah
Purpose: Runs main game loop, creates the objects, and manages the rules/winners
Starter Code: N/A
Date: 9/21/26
"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while True:
        player_choice = input("Do you want to play? Press 'Y' or 'y' to continue")
        
        if player_choice == 'Y' or player_choice == 'y':
            pass
        else:
            print("Incorrect option.")




main()