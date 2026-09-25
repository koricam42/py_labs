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
        print("\nMatch Coin Game")
        player_choice = input("Do you want to play the Match Coins Game? Input 'Y' or 'y' to continue")
        
        if player_choice == 'Y' or player_choice == 'y':
            print(f"Player 1 has {player1.get_wallet()} coins")
            print(f"Player 2 has {player2.get_wallet()} coins")
            print()

            player1.toss_coin()
            player2.toss_coin()

            p1_side = player1.get_coin_side()
            p2_side = player2.get_coin_side()


            print(f'Player 1 tossed {p1_side}')
            print(f'Player 2 tossed {p2_side}')

            if p1_side == p2_side:
                pass
            else:
                pass
                
        elif player_choice == "N" or player_choice == "n":
            print("See you later.")
            break
        else:  
            print("Invalid input.")




main()